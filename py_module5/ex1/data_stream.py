from abc import ABC, abstractmethod
from typing import Any, List, Optional, Dict, Union


class DataStream(ABC):

    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
                    = None) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "id": self.stream_id
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.type = "Environmental Data"
        print("Initializing Sensor Stream...")

    def process_batch(self, data_batch: List[Any]) -> str:
        if not data_batch:
            return "Error: None Valid Data"
        if isinstance(data_batch, list):
            try:
                data_len = len(data_batch)
                temp = 0
                count = 0
                for data in data_batch:
                    if data.split(":", 1)[0] == "temp":
                        temp += float(data.split(":", 1)[1])
                        count += 1
                return (
                        f"Sensor analysis: {data_len} readings "
                        f"processed, avg temp: "
                        f"{temp / count if count > 0 else 0}°C")
            except (ValueError, IndexError, AttributeError, TypeError):
                return "Error: None Valid Data"
        else:
            return "Error: Invalid Data"

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
                    = None) -> List[Any]:
        if not isinstance(data_batch, list):
            return []
        if isinstance(criteria, str):
            criteria = criteria.lower()
        if criteria == "temp":
            return [
                data
                for data in data_batch
                if isinstance(data, str)
                and ":" in data
                and data.split(":", 1)[0] == "temp"]
        elif criteria == "humidity":
            return [
                data
                for data in data_batch
                if isinstance(data, str)
                and ":" in data
                and data.split(":", 1)[0] == "humidity"]
        elif criteria == "pressure":
            return [
                data
                for data in data_batch
                if isinstance(data, str)
                and ":" in data
                and data.split(":", 1)[0] == "pressure"]
        else:
            return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = self.type
        return stats


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.type = "Financial Data"
        print("Initializing Transaction Stream...")

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
                    = None) -> List[Any]:
        if not isinstance(data_batch, list):
            return []
        if isinstance(criteria, str):
            criteria = criteria.lower()
        if criteria == "buy":
            return [
                data for data in data_batch
                if isinstance(data, str) and ":" in data
                and data.split(":", 1)[0].lower() == "buy"]

        elif criteria == "sell":
            return [
                data for data in data_batch
                if isinstance(data, str) and ":" in data
                and data.split(":", 1)[0].lower() == "sell"]
        else:
            return data_batch

    def process_batch(self, data_batch: List[Any]) -> str:
        if not data_batch:
            return "Error: None Valid data"
        if isinstance(data_batch, list):
            data_len = len(data_batch)
            buy = sell = 0
            for data in data_batch:
                try:
                    check = data.split(":")
                    transaction = int(check[1])
                    if check[0].lower() == "buy":
                        buy += transaction
                    elif check[0].lower() == "sell":
                        sell += transaction
                    else:
                        return "Error: Invalid Transaction"
                except (ValueError, AttributeError, IndexError):
                    return "Error: None digit value"
            return (f"Transaction analysis: {data_len} operations, "
                    f"net flow: +{buy - sell} units")
        else:
            return "Error: Invalid Data"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = self.type
        return stats


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.type = "System Events"
        print("Initializing Event Stream...")

    def process_batch(self, data_batch: List[Any]) -> str:
        if not data_batch:
            return "Error: Non Valid Data"
        if isinstance(data_batch, list):
            data_len = len(data_batch)
            count = 0
            for data in data_batch:
                try:
                    if data.lower() == "error":
                        count += 1
                except AttributeError:
                    return "Error: Invalid Data"
            return f"Event analysis: {data_len} events, {count} error detected"
        else:
            return "Error: Invalid Data"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = self.type
        return stats


class StreamProcessor:
    def __init__(self, process: DataStream) -> None:
        self.process = process

    def process_stream(self, data: List[Any]) -> str:
        if isinstance(data, list):
            return self.process.process_batch(data)
        else:
            return "Error: Invalid Data"

    def process_data(self, data: List[Any]) -> int:
        return len(data)


def data_stream() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    sensor_1 = SensorStream("SENSOR_001")
    stats = sensor_1.get_stats()
    print(f"Stream ID: {stats['id']}, Type: {stats['type']}")
    data_1 = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Processing sensor batch: {data_1}")
    process_1 = StreamProcessor(sensor_1)
    print(process_1.process_stream(data_1))

    print()
    transaction_1 = TransactionStream("TRANS_001")
    stats = transaction_1.get_stats()
    print(f"Stream ID: {stats['id']}, Type: {stats['type']}")
    data_2 = ["buy:100", "sell:150", "buy:75"]
    print(f'Processing transaction batch: {data_2}')
    process_2 = StreamProcessor(transaction_1)
    print(process_2.process_stream(data_2))

    print()
    event_1 = EventStream("EVENT_001")
    stats = event_1.get_stats()
    print(f"Stream ID: {stats['id']}, Type: {stats['type']}")
    data_3 = ["login", "error", "logout"]
    print(f'Processing event batch: {data_3}')
    process_3 = StreamProcessor(event_1)
    print(process_3.process_stream(data_3))

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    data_list = [
        ["humidity:65", "pressure:1013"],
        ["buy:100", "buy:70", "sell:125", "sell:25"],
        ["error", "error", "logout"]
    ]

    streams_list = [
        sensor_1,
        transaction_1,
        event_1
    ]

    processes = [
        StreamProcessor(streams_list[0]),
        StreamProcessor(streams_list[1]),
        StreamProcessor(streams_list[2])
    ]

    print("Batch 1 Results:")
    for data, process in zip(data_list, processes):
        result = process.process_data(data)
        if isinstance(process.process, SensorStream):
            print(f"- Sensor data: {result} readings processed")
        elif isinstance(process.process, TransactionStream):
            print(f"- Transaction data: {result} operations processed")
        elif isinstance(process.process, EventStream):
            print(f"- Event data: {result} events processed")

    print("\nStream filtering active: High-priority data only")
    sensor_filtered = streams_list[0].filter_data(data_list[0], "humidity")
    transaction_filtered = streams_list[1].filter_data(data_list[1], "buy")

    print(f"Filtered results: {len(sensor_filtered)} humidity readings, "
          f"{len(transaction_filtered)} buy transactions")

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    data_stream()
