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

    def process_batch(self, data_batch: List[Any]) -> str:
        if not data_batch:
            return "Error: Invalid Data"
        if isinstance(data_batch, list):
            try:
                data_len = len(data_batch)
                temp = data_batch[0].split(":")
                return (f"Sensor analysis: {data_len} readings processed, "
                        f"avg temp: {temp[1]}°C")
            except (ValueError, IndexError, AttributeError):
                return "Error: None Valid Data"
        else:
            return "Error: Invalid Data"

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
                    = None) -> List[Any]:
        if criteria == "sensor":
            error_list = []
            critical = 0
            for data in data_batch:
                try:
                    splited = data.split(":")
                    if int(splited[1]) > 50:
                        critical += 1
                except (ValueError, IndexError, AttributeError):
                    return "Error: None Valid Data"
            error_list.append(critical)
            return error_list
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

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
                    = None) -> List[Any]:
        if criteria == "transaction":
            error_list = []
            large = 0
            for data in data_batch:
                try:
                    splited = data.split(":")
                    if int(splited[1]) > 100:
                        large += 1
                except (ValueError, IndexError, AttributeError):
                    return "Error: None Valid Data"
            error_list.append(large)
            return error_list
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
                    if check[0] == "buy":
                        buy += transaction
                    elif check[0] == "sell":
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

    def process_batch(self, data_batch: List[Any]) -> str:
        if not data_batch:
            return "Error: Non Valid Data"
        if isinstance(data_batch, list):
            data_len = len(data_batch)
            count = 0
            for data in data_batch:
                if data == "error":
                    count += 1
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

    def process_stream(self, data: List[Any]):
        if isinstance(data, list):
            return self.process.process_batch(data)
        else:
            return "Error: Invalid Data"

    def process_data(self, data: List[Any]) -> int:
        return len(data)


def data_stream():
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    print("Initializing Sensor Stream...")
    sensor_1 = SensorStream("SENSOR_001")
    stats = sensor_1.get_stats()
    print(f"Stream ID: {stats['id']}, Type: {stats['type']}")
    data_1 = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Processing sensor batch: {data_1}")
    process_1 = StreamProcessor(sensor_1)
    print(process_1.process_stream(data_1))

    print()

    print("Initializing Transaction Stream...")
    transaction_1 = TransactionStream("TRANS_001")
    stats = transaction_1.get_stats()
    print(f"Stream ID: {stats['id']}, Type: {stats['type']}")
    data_2 = ["buy:100", "sell:150", "buy:75"]
    print(f'Processing transaction batch: {data_2}')
    process_2 = StreamProcessor(transaction_1)
    print(process_2.process_stream(data_2))

    print()
    print("Initializing Event Stream...")
    event_1 = EventStream("EVENT_001")
    stats = event_1.get_stats()
    print(f"Stream ID: {stats['id']}, Type: {stats['type']}")
    data_3 = ["login", "error", "logout"]
    print(f'Processing transaction batch: {data_3}')
    process_3 = StreamProcessor(event_1)
    print(process_3.process_stream(data_3))

    print()

    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    data_4 = ["humidity:65", "pressure:1013"]
    data_5 = ["buy:100", "buy:70", "sell:125", "sell:25"]
    data_6 = ["error", "error", "logout"]

    sensor_2 = SensorStream("SENSOR_002")
    transaction_2 = TransactionStream(" TRANS_002")
    event_2 = EventStream("EVENT_002")

    process_3 = StreamProcessor(sensor_2)
    process_4 = StreamProcessor(transaction_2)
    process_5 = StreamProcessor(event_2)

    processes = [process_3, process_4, process_5]

    print("Batch 1 Results:")
    for process in processes:
        if isinstance(process.process, SensorStream):
            print(f"- Sensor data: {process.process_data(data_4)} "
                  f"readings processed")
        elif isinstance(process.process, TransactionStream):
            print(f"- Transaction data: {process.process_data(data_5)} "
                  f"operations processed")
        elif isinstance(process.process, EventStream):
            print(
                f"- Event data: {process.process_data(data_6)} "
                f"events processed")

    print()
    print("Stream filtering active: High-priority data only")
    sensor_filtered = sensor_2.filter_data(data_4, 'sensor')
    transaction_filtered = transaction_2.filter_data(data_5, 'transaction')
    print(f"Filtered results: {sensor_filtered[0]} critical sensor alerts, "
          f"{transaction_filtered[0]} large transaction")

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    data_stream()
