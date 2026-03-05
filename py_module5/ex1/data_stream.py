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
            raise ValueError("Error: None Valid Data")
        if not isinstance(data_batch, list):
            raise ValueError("error: invalid data")
        try:
            data_len = len(data_batch)
            temp = 0
            count = 0
            for data in data_batch:
                parts = data.split(":", 1)
                if parts[0] == "temp":
                    temp += float(parts[1])
                    count += 1
            avg_temp = temp / count if count > 0 else 0
            alert = ""
            if avg_temp > 30:
                alert = " [ALERT: HIGH TEMPERATURE!]"
            elif avg_temp < 0:
                alert = " [ALERT: LOW TEMPERATURE!]"
            return (
                    f"Sensor analysis: {data_len} readings "
                    f"processed, avg temp: "
                    f"{avg_temp}°C{alert}")
        except Exception:
            raise ValueError("error: invalid data")

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
                    = None) -> List[Any]:
        if not isinstance(data_batch, list):
            raise ValueError("error: invalid data (not a list)")
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
            raise ValueError("error: invalid data (not a list)")
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
            raise ValueError("error: invalid data")
        if not isinstance(data_batch, list):
            raise ValueError("error: invalid data")
        data_len = len(data_batch)
        buy = sell = 0
        for data in data_batch:
            try:
                check = data.split(":", 1)
                transaction = int(check[1])
                if check[0].lower() == "buy":
                    buy += transaction
                elif check[0].lower() == "sell":
                    sell += transaction
                else:
                    continue
            except Exception:
                raise ValueError("error: none digit value")
        return (f"Transaction analysis: {data_len} operations, "
                f"net flow: +{buy - sell} units")

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
            raise ValueError("Error: Non Valid Data")
        if not isinstance(data_batch, list):
            raise ValueError("error: invalid data")
        data_len = len(data_batch)
        count = 0
        for data in data_batch:
            try:
                if data.lower() == "error":
                    count += 1
            except Exception:
                raise ValueError("Error: Invalid Data")
        return f"Event analysis: {data_len} events, {count} error detected"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = self.type
        return stats


class StreamProcessor:
    def __init__(self, process: DataStream) -> None:
        if not isinstance(process, DataStream):
            raise ValueError("error: invalid processor")
        self.process = process

    def process_stream(self, data: List[Any]) -> str:
        if not isinstance(data, list):
            raise ValueError("Error: Invalid Data")
        if isinstance(self.process, SensorStream):
            print(f"Processing sensor batch: {data}")
        elif isinstance(self.process, TransactionStream):
            print(f"Processing transaction batch: {data}")
        elif isinstance(self.process, EventStream):
            print(f"Processing event batch: {data}")
        return self.process.process_batch(data)

    def process_data(self, data: List[Any]) -> int:
        if not isinstance(data, list):
            raise ValueError("error: data is not a list")
        return len(data)


def data_stream() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    try:
        sensor_1 = SensorStream("SENSOR_001")
        stats = sensor_1.get_stats()
        print(f"Stream ID: {stats['id']}, Type: {stats['type']}")
        data_1 = ["temp:22.5", "humidity:65", "pressure:1013"]
        process_1 = StreamProcessor(sensor_1)
        print(process_1.process_stream(data_1))
    except Exception as e:
        print(e)

    try:
        print()
        transaction_1 = TransactionStream("TRANS_001")
        stats = transaction_1.get_stats()
        print(f"Stream ID: {stats['id']}, Type: {stats['type']}")
        data_2 = ["buy:100", "sell:150", "buy:75"]
        process_2 = StreamProcessor(transaction_1)
        print(process_2.process_stream(data_2))
    except Exception as e:
        print(e)

    try:
        print()
        event_1 = EventStream("EVENT_001")
        stats = event_1.get_stats()
        print(f"Stream ID: {stats['id']}, Type: {stats['type']}")
        data_3 = ["login", "error", "logout"]
        process_3 = StreamProcessor(event_1)
        print(process_3.process_stream(data_3))
    except Exception as e:
        print(e)

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    try:
        data_list = [
            ["humidity:65", "pressure:1013"],
            ["buy:100", "buy:70", "sell:125", "sell:25"],
            ["error", "error", "logout"]
        ]

        processes = [
            StreamProcessor(sensor_1),
            StreamProcessor(transaction_1),
            StreamProcessor(event_1)
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
    except Exception as e:
        print(e)

    print("\nStream filtering active: High-priority data only")
    try:
        crt_1 = "humidity"
        crt_2 = "buy"
        sensor_filtered = sensor_1.filter_data(data_list[0], crt_1)
        transaction_filtered = transaction_1.filter_data(data_list[1], crt_2)

        print(
            f"Filtered results: {len(sensor_filtered)} {crt_1}, "
            f"{len(transaction_filtered)} {crt_2}")
    except Exception as e:
        print(e)

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    try:
        data_stream()
    except Exception as e:
        print(e)
