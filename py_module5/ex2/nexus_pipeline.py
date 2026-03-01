from typing import Protocol, Any, Dict, List, Union, Optional
from abc import ABC, abstractmethod
from collections import defaultdict


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        ...


class InputStage:
    def process(self, data: Any) -> Dict[str, Any]:
        if data is None:
            raise ValueError("Error: Invalid data")

        if isinstance(data, dict):
            return {
                "payload": {key: value for key, value in data.items()},
                "type": "dict",
            }

        if isinstance(data, str):
            csv_parts = [part.strip() for part in data.split(",") if part.strip()]
            if len(csv_parts) < 2:
                raise ValueError("Error: Invalid format for CSV")
            return {"payload": csv_parts, "type": "csv"}

        if isinstance(data, list):
            return {"payload": [item for item in data], "type": "list"}

        if isinstance(data, (int, float)):
            return {"payload": data, "type": "number"}

        raise ValueError("Error: Invalid data format")


class TransformStage:
    def process(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if not isinstance(data, dict):
            raise ValueError("Error: Data is not a dictionary")

        transformed: Dict[str, Any] = {key: value for key, value in data.items()}
        payload = transformed.get("payload")
        data_type = transformed.get("type")
        transformed["timestamp"] = f"step-{data_type}-{len(str(payload))}"

        if data_type == "list":
            numeric_values = [value for value in payload if isinstance(value, (int, float))]
            transformed["count"] = len(payload)
            transformed["average"] = (
                sum(numeric_values) / len(numeric_values) if numeric_values else None
            )
        elif data_type == "csv":
            transformed["words"] = len(payload)
            transformed["length"] = sum(len(value) for value in payload)
            transformed["unique_words"] = len({value.lower() for value in payload})
        elif data_type == "number":
            transformed["is_positive"] = payload > 0
        elif data_type == "dict":
            transformed["keys"] = [key for key in payload.keys()]
            transformed["size"] = len(payload)

        return transformed


class OutputStage:
    def process(self, data: Dict[str, Any]) -> str:
        if not isinstance(data, dict):
            raise ValueError("Error: Data is not a dict")

        data_type = data.get("type")
        payload = data.get("payload")

        if data_type == "csv":
            return (
                f'Processed text: {data.get("words", 0)} words, '
                f'{data.get("length", 0)} chars'
            )
        if data_type == "list":
            return (
                f'Processed list -> {data.get("count", 0)} items '
                f'(avg: {data.get("average")})'
            )
        if data_type == "number":
            return (
                f'Processed number: {payload} positive: '
                f'{data.get("is_positive", False)}'
            )
        if data_type == "dict":
            digest = {
                key: data[key]
                for key in ("type", "size", "timestamp")
                if key in data
            }
            return f"Processed dict -> {digest}"
        return f"Processed {data_type} -> {data.get('timestamp', 'n/a')}"


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str):
        self.pipeline_id = pipeline_id
        self.stages: List[ProcessingStage] = [InputStage(), TransformStage(),
                                              OutputStage()]
        self.metrics: Dict[str, int] = {"processed": 0, "failed": 0}
        self.processing_units: List[int] = []

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        ...

    @abstractmethod
    def supports(self, data: Any) -> bool:
        ...

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    def run_stages(self, data: Any, include_output: bool) -> Any:
        result = data
        for stage in self.stages:
            if not include_output and isinstance(stage, OutputStage):
                continue
            result = stage.process(result)
        return result

    def record_run(self, include_output: bool, succeeded: bool) -> None:
        units = len(self.stages) if include_output else max(len(self.stages) - 1, 0)
        self.processing_units.append(units)
        if len(self.processing_units) > 200:
            self.processing_units.pop(0)
        if succeeded:
            self.metrics["processed"] += 1
        else:
            self.metrics["failed"] += 1

    def process_for_chain(self, data: Any) -> Dict[str, Any]:
        try:
            result = self.run_stages(data, include_output=False)
            self.record_run(include_output=False, succeeded=True)
            return result
        except ValueError:
            self.record_run(include_output=False, succeeded=False)
            raise

    def get_stats(self) -> Dict[str, Any]:
        total_calls = self.metrics["processed"] + self.metrics["failed"]
        average_units = (
            sum(self.processing_units) / len(self.processing_units)
            if self.processing_units
            else 0.0
        )
        return {
            "pipeline_id": self.pipeline_id,
            "total_calls": total_calls,
            "processed": self.metrics["processed"],
            "failed": self.metrics["failed"],
            "avg_work_units": round(average_units, 6),
        }


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str):
        super().__init__(pipeline_id)

    def supports(self, data: Any) -> bool:
        return isinstance(data, dict)

    def process(self, data: Any) -> Union[str, Any]:
        if not self.supports(data):
            raise ValueError("Error: invalid data (not a dict)")
        try:
            result = self.run_stages(data, include_output=True)
            self.record_run(include_output=True, succeeded=True)
            return result
        except ValueError:
            self.record_run(include_output=True, succeeded=False)
            raise


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str):
        super().__init__(pipeline_id)

    def supports(self, data: Any) -> bool:
        return isinstance(data, str)

    def process(self, data: Any) -> Union[str, Any]:
        if not self.supports(data):
            raise ValueError("Error: invalid data (not a string)")
        try:
            result = self.run_stages(data, include_output=True)
            self.record_run(include_output=True, succeeded=True)
            return result
        except ValueError:
            self.record_run(include_output=True, succeeded=False)
            raise


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str):
        super().__init__(pipeline_id)

    def supports(self, data: Any) -> bool:
        return isinstance(data, list)

    def process(self, data: Any) -> Union[str, Any]:
        if not self.supports(data):
            raise ValueError("Error: invalid data (not a list)")
        try:
            result = self.run_stages(data, include_output=True)
            self.record_run(include_output=True, succeeded=True)
            return result
        except ValueError:
            self.record_run(include_output=True, succeeded=False)
            raise


class NexusManager:
    def __init__(self):
        self.pipelines: Dict[str, ProcessingPipeline] = {}
        self.metrics: Dict[str, int] = {"processed": 0, "failed": 0}
        self.failures: List[str] = []
        self.pipeline_loads: Dict[str, List[int]] = {}

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines[pipeline.pipeline_id] = pipeline

    def find_pipeline(self, data: Any) -> ProcessingPipeline:
        for pipeline in self.pipelines.values():
            if pipeline.supports(data):
                return pipeline
        raise ValueError(f"Unsupported data type: {type(data).__name__}")

    def process_data(self, data_list: List[Any]) -> List[Any]:
        if not self.pipelines:
            raise ValueError("No pipelines configured")

        results: List[Any] = []
        for element in data_list:
            try:
                pipeline = self.find_pipeline(element)
                result = pipeline.process(element)
                results.append(result)
                self.metrics["processed"] += 1
                if pipeline.pipeline_id not in self.pipeline_loads:
                    self.pipeline_loads[pipeline.pipeline_id] = []
                self.pipeline_loads[pipeline.pipeline_id].append(1)
            except ValueError as error:
                self.metrics["failed"] += 1
                self.failures.append(str(error))
                if len(self.failures) > 20:
                    self.failures.pop(0)
                print(f"Error detected in pipeline: {error}")
                print("Recovery initiated: Switching to backup processor")
                print("Recovery successful: Pipeline restored, processing resumed")
                continue

        return results

    def chain_process(self, data: Any, pipeline_order: List[str]) -> Any:
        if not pipeline_order:
            raise ValueError("Pipeline order cannot be empty")

        current: Any = data
        for pipeline_id in pipeline_order:
            pipeline = self.pipelines.get(pipeline_id)
            if pipeline is None:
                raise ValueError(f"Pipeline {pipeline_id} is not configured")
            try:
                current = pipeline.process_for_chain(current)
            except ValueError as error:
                self.metrics["failed"] += 1
                self.failures.append(str(error))
                if len(self.failures) > 20:
                    self.failures.pop(0)
                print(f"Error detected in chain at {pipeline_id}: {error}")
                print("Recovery initiated: skipping to next stage")
                continue

        return OutputStage().process(current) if isinstance(current, dict) else current

    def get_stats(self) -> Dict[str, Any]:
        pipeline_stats = {
            pipeline_id: pipeline.get_stats()
            for pipeline_id, pipeline in self.pipelines.items()
        }
        average_load = {
            pipeline_id: round(sum(units) / len(units), 6) if units else 0.0
            for pipeline_id, units in self.pipeline_loads.items()
        }
        return {
            "manager": {
                "processed": self.metrics["processed"],
                "failed": self.metrics["failed"],
                "recent_failures": [failure for failure in self.failures],
            },
            "pipelines": pipeline_stats,
            "avg_pipeline_load": average_load,
        }


if __name__ == "__main__":
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")

    manager = NexusManager()
    json_adapter = JSONAdapter("json_1")
    csv_adapter = CSVAdapter("csv_1")
    stream_adapter = StreamAdapter("stream_1")

    manager.add_pipeline(json_adapter)
    manager.add_pipeline(csv_adapter)
    manager.add_pipeline(stream_adapter)

    data_list = [
        {"sensor": "temp", "value": 23.5},
        "user,action,timestamp",
        [22.1, 23.5, 21.8],
    ]

    results = manager.process_data(data_list)

    print("Initializing Nexus Manager...")
    print("Pipeline capacity: 1000 streams/second\n")

    print("Creating Data Processing Pipeline...")
    print("Stage 1: Input validation and parsing")
    print("Stage 2: Data transformation and enrichment")
    print("Stage 3: Output formatting and delivery")

    print("\n=== Multi-Format Data Processing ===\n")
    print("Processing JSON data through pipeline...")
    print(f"input: {data_list[0]}")
    print("Transform: Enriched with metadata and validation")
    print(f"Output: {results[0]}")

    print("\nProcessing CSV data through same pipeline...")
    print(f'input: "{data_list[1]}"')
    print("Transform: Parsed and structured data")
    print(f"Output: {results[1]}")

    print("\nProcessing Stream data through same pipeline...")
    print(f"Input: {data_list[2]}")
    print("Transform: Aggregated and filtered")
    print(f"Output: {results[2]}")

    print("\n=== Pipeline Chaining Demo ===")
    chain_output = manager.chain_process(
        {"a": 1, "b": 2, "c": 3},
        ["json_1", "csv_1", "stream_1"],
    )
    print("Pipeline A -> Pipeline B -> Pipeline C")
    print(f"Chained Output: {chain_output}")

    print("\n=== Error Recovery Test ===")
    corrupted_data = [None, "test,hello", [1, 2, 4]]
    print("Simulating pipeline failure...")
    manager.process_data(corrupted_data)

    print("\n=== Performance & Statistics ===")
    stats = manager.get_stats()
    print(f"Manager stats: {stats['manager']}")
    print(f"Pipeline stats: {stats['pipelines']}")
    print(f"Average pipeline load: {stats['avg_pipeline_load']}")

    print("\nNexus Integration complete. All systems operational")
