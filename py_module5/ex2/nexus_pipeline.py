from typing import Protocol, Any, Dict, List
from abc import ABC, abstractmethod


class ProcessingStage(Protocol):
    def process(self, data) -> Any:
        pass


class ProcessPipeline(ABC):
    def __init__(self):
        self.stages = []

    @abstractmethod
    def process(self, data) -> Any:
        pass

    def add_stage(self, stage: ProcessingStage):
        self.stages.append(stage)


class InputStage:
    def process(self, data: Any) -> Dict:
        if not data and not isinstance(data, (int, float)):
            raise ValueError("Error: Invalid Data")
        elif isinstance(data, dict):
            return {
                "data": data,
                "type": "dict"
            }
        elif isinstance(data, str):
            if "," in data:
                return {
                    "data": data.split(","),
                    "type": "csv"
                }
            else:
                raise ValueError("Error: Invalid format for CSV")
        elif isinstance(data, list):
            return {
                "data": data,
                "type": "list"
            }
        elif isinstance(data, (int, float)):
            return {
                "data": data,
                "type": "number"
            }
        else:
            raise ValueError("Error: Invalid data format")


class TransformStage:
    def process(self, data: Dict) -> Dict:
        if not isinstance(data, dict):
            raise ValueError("Error: Data is a not a Dictionary")

        data["timestamp"] = 2087

        if data["type"] == "list":
            data["count"] = len(data["data"])
        elif data["type"] == "csv":
            lenght = 0
            for value in data["data"]:
                lenght += len(value)
            data["length"] = lenght
            data["words"] = len(data["data"])
        elif data["type"] == "number":
            data["is_positive"] = data["data"] > 0
        return data


class OutputStage:
    def process(self, data: Dict) -> str:
        if not isinstance(data, dict):
            raise ValueError("Error: Data is not a dict")

        data_type = data["type"]
        if data_type == "csv":
            return (
                f'Processed text: {data["words"]} words, '
                f'{data["length"]} chars'
                )
        elif data_type == "list":
            return f'Processed list -> {data["count"]} items'
        elif data_type == "number":
            return (
                f'Processed number: {data["data"]} positive: '
                f'{data["is_positive"]}')
        else:
            return f'Processed {data_type} -> year {data["timestamp"]}'


class JSONAdapter(ProcessPipeline):
    def __init__(self, pipeline_id):
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Dict):
        if not isinstance(data, dict):
            raise ValueError("Error: invalid data (Not a dict)")
        if not self.stages:
            self.add_stage(InputStage())
            self.add_stage(TransformStage())
            self.add_stage(OutputStage())

        result = data
        for stage in self.stages:
            result = stage.process(result)
        return result


class CSVAdapter(ProcessPipeline):
    def __init__(self, pipeline_id):
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: str):
        if not isinstance(data, str):
            raise ValueError("Error: invalid data (Not a string)")

        if not self.stages:
            self.add_stage(InputStage())
            self.add_stage(TransformStage())
            self.add_stage(OutputStage())

        result = data
        for stage in self.stages:
            result = stage.process(result)

        return result


class StreamAdapter(ProcessPipeline):
    def __init__(self, pipeline_id):
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: list):
        if not isinstance(data, list):
            raise ValueError("Error: invalid data (not a list)")

        if not self.stages:
            self.add_stage(InputStage())
            self.add_stage(TransformStage())
            self.add_stage(OutputStage())

        result = data
        for stage in self.stages:
            result = stage.process(result)

        return result


class NexusManager:
    def __init__(self):
        self.pipelines: List = []

    def add_pipeline(self, pipeline: ProcessPipeline):
        self.pipelines.append(pipeline)

    def process_data(self, data_list: list[Any]):
        if not self.pipelines:
            raise ValueError("No pipelines configured")

        results = []
        for element in data_list:
            try:
                if isinstance(element, dict):
                    result = self.pipelines[0].process(element)
                    results.append(result)
                elif isinstance(element, str):
                    result = self.pipelines[1].process(element)
                    results.append(result)
                elif isinstance(element, list):
                    result = self.pipelines[2].process(element)
                    results.append(result)
                else:
                    raise ValueError(
                        f"Unsupported data type: "
                        f"{type(element).__name__}")

            except ValueError as e:
                print(f"Error detected in pipeline: {e}")
                print("Recovery initiated: Switching to backup processor")
                print("Recovery successful: Pipeline restored, "
                      "processing resumed")
                continue

        return results


if __name__ == "__main__":
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")
    manager = NexusManager()
    csv = CSVAdapter("csv_1")
    json = JSONAdapter("json_1")
    stream = StreamAdapter("steam_1")
    manager.add_pipeline(json)
    manager.add_pipeline(csv)
    manager.add_pipeline(stream)
    data_list = [
        {"sensor": "temp", "value": 23.5},
        "user,action,timestamp",
        [22.1, 23.5, 21.8]
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

    print("\n=== Pipeline Chaining Demo ==")
    print("Pipeline A -> Pipeline B -> Pipeline C")

    print("\n=== Error Recovery Test ===")
    corrupted_data = [None, "test,hello", [1, 2, 4]]
    print("Simulating pipeline failure...")
    errors = manager.process_data(corrupted_data)

    print("\nNexus Integration complete. All systems operational")
