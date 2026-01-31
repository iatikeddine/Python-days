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
        if criteria == "sensor":
            error_list_1 = []
            critical = 0
            for data in data_batch:
                splited = data.split(":")
                try:
                    if int(splited[1]) > 50:
                        critical += 1
                except ValueError:
                    return "None digit value"
            error_list_1.append(critical)
            return error_list_1
        
        elif criteria == "transaction":
            error_list_2 = []
            large = 0
            for data in data_batch:
                splited = data.split(":")
                try:
                    if int(splited[1]) > 100:
                        large += 1
                except ValueError:
                    return "None digit value"
            error_list_2.append(large)
            return error_list_2

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return f"Stream ID: {self.stream_id}, Type: {self.type}"


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.type = "Environmental Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        data_len = len(data_batch)
        temp = data_batch[0].split(":")
        return (f"Sensor analysis: {data_len} readings processed, "
                f"avg temp: {temp[1]}°C")


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.type = "Financial Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        data_len = len(data_batch)
        buy = sell = 0
        for data in data_batch:
            check = data.split(":")
            try:
                transaction = int(check[1])
                if check[0] == "buy":
                    buy += transaction
                elif check[0] == "sell":
                    sell += transaction
            except ValueError:
                return "None digit value"
        return (f"Transaction analysis: {data_len} operations, "
                f"net flow: +{buy - sell} units")


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.type = "System Events"

    def process_batch(self, data_batch: List[Any]) -> str:
        data_len = len(data_batch)
        count = 0
        for data in data_batch:
            if data == "error":
                count += 1
        return f"Event analysis: {data_len} events, {count} error detected"


class StreamProcessor:
    def __init__(self, process: Any, data: List[Any]):
        self.process = process
        self.data = data

    def process_stream(self):
        if isinstance(self.process, SensorStream):
            return (f"Processing sensor batch: "
                    f"[{self.data[0]}, {self.data[1]}, {self.data[2]}]")
        elif isinstance(self.process, TransactionStream):
            return (f"Processing transaction batch: "
                    f"[{self.data[0]}, {self.data[1]}, {self.data[2]}]")                    
        elif isinstance(self.process, EventStream):
            return (f"Processing event batch: "
                    f"[{self.data[0]}, {self.data[1]}, {self.data[2]}]")
    
    def process_data(self):
        return len(self.data)


def data_stream():
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    print("Initializing Sensor Stream...")
    sensor_1 = SensorStream("SENSOR_001")
    print(sensor_1.get_stats())
    data_1 = ["temp:22.5", "humidity:65", "pressure:1013"]
    process_1 = StreamProcessor(sensor_1, data_1)
    print(process_1.process_stream())
    print(sensor_1.process_batch(data_1))

    print()

    print("Initializing Transaction Stream...")
    transaction_1 = TransactionStream(" TRANS_001")
    print(transaction_1.get_stats())
    data_2 = ["buy:100", "sell:150", "buy:75"]
    process_2 = StreamProcessor(transaction_1, data_2)
    print(process_2.process_stream())
    print(transaction_1.process_batch(data_2))

    print()
    print("Initializing Event Stream...")
    event_1 = EventStream("EVENT_001")
    print(event_1.get_stats())
    data_3 = ["login", "error", "logout"]
    process_3 = StreamProcessor(event_1, data_3)
    print(process_3.process_stream())
    print(event_1.process_batch(data_3))

    print()

    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    data_4 = ["humidity:65", "pressure:1013"]
    data_5 = ["buy:100", "buy:70", "sell:125", "sell:25"]
    data_6 = ["error", "error", "logout"]

    sensor_2 = SensorStream("SENSOR_002")
    transaction_2 = TransactionStream(" TRANS_002")
    event_2 = EventStream("EVENT_002")

    process_3 = StreamProcessor(sensor_2, data_4)
    process_4 = StreamProcessor(transaction_2, data_5)
    process_5 = StreamProcessor(event_2, data_6)

    processes = [process_3, process_4, process_5]

    print("Batch 1 Results:")
    for process in processes:
        if isinstance(process.process, SensorStream):
            print(f"- Sensor data: {process.process_data()} "
                  f"readings processed")
        elif isinstance(process.process, TransactionStream):
            print(f"- Transaction data: {process.process_data()} "
                  f"operations processed")
        elif isinstance(process.process, EventStream):
            print(f"- Event data: {process.process_data()} events processed")

    print()
    print("Stream filtering active: High-priority data only")
    sensor_filtered = sensor_2.filter_data(data_4, 'sensor')
    transaction_filtered = transaction_2.filter_data(data_5, 'transaction')
    print(f"Filtered results: {sensor_filtered[0]} critical sensor alerts, "
          f"{transaction_filtered[0]} large transaction")

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    data_stream()
