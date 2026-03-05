from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional
del Dict, Optional


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if not data:
            return False
        elif type(data).__name__ == "list":
            for element in data:
                if (type(element).__name__ != "int" and
                        type(element).__name__ != "float"):
                    return False
            return True
        elif type(data).__name__ == "int" or type(data).__name__ == "float":
            return True
        return False

    def process(self, data: Any) -> str:
        if type(data).__name__ == "list":
            try:
                numeric_value: int = len(data)
                total: int = sum(data)
                avg: float = total / numeric_value
                return (f"Processed {numeric_value} numeric values,"
                        f" sum={total}, avg={avg:.1f}")
            except (TypeError, ZeroDivisionError):
                return "Error: Data contains non numeric values or is empty"
        else:
            try:
                return (f"Processed 1 numeric value, sum={data}, "
                        f"avg={data:.1f}")
            except TypeError:
                return "Error: Data is not a valid numeric value"


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if type(data).__name__ != "str" or not data:
            return False
        return True

    def process(self, data: Any) -> str:
        try:
            chars: int = len(data)
            count: int = len(data.split())
            return f"Processed text: {chars} characters, {count} words"
        except (TypeError, AttributeError):
            return "Error: Data is not a valid string"


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if type(data).__name__ != "str" or not data:
            return False

        try:
            check: list[str] = data.split(":")
            if len(check) > 1:
                logs: List[str] = ["ERROR", "INFO"]
                if check[0] in logs:
                    return True
        except (IndexError, AttributeError):
            return False
        return False

    def process(self, data: Any) -> str:
        try:
            check: list = data.split(":", 1)
            if check[0] == "ERROR":
                return f"[ALERT] ERROR level detected: {check[1].strip()}"
            elif check[0] == "INFO":
                return f"[INFO] INFO level detected: {check[1].strip()}"
            else:
                return "Error: Unrecognized log level"
        except (AttributeError, IndexError):
            return "Error: Data is not a valid log entry"

    def format_output(self, result: str) -> str:
        return super().format_output(result)


def stream_processor() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    try:
        num_process: NumericProcessor = NumericProcessor()
        print("Initializing Numeric Processor...")
        data_1: list[int] = [1, 2, 3, 4, 5]
        print(f"Processing data: {data_1}")
        if num_process.validate(data_1):
            print("Validation: Numeric data verified")
            print(num_process.format_output(num_process.process(data_1)))
        else:
            print("Validation: Could not verify numeric data")
    except Exception as e:
        print(e)

    try:
        print("\nInitializing Text Processor...")
        text_processor: TextProcessor = TextProcessor()
        data_2: str = "Hello Nexus World"
        print(f'Processing data: "{data_2}"')
        if text_processor.validate(data_2):
            print("Validation: Text data verified")
            txt_pr: str = text_processor.process(data_2)
            print(f"{text_processor.format_output(txt_pr)}")
        else:
            print("Validation:: Could not verify text data")
    except Exception as e:
        print(e)

    try:
        print("\nInitializing Log Processor...")
        log_processor: LogProcessor = LogProcessor()
        data_3: str = "ERROR: Connection timeout"
        print(f'Processing data: "{data_3}"')
        if log_processor.validate(data_3):
            print("Validation: Log entry verified")
            output = log_processor.process(data_3)
            print(f"{log_processor.format_output(output)}")
        else:
            print("Validation: Could not verify log entry")
    except Exception as e:
        print(e)

    try:
        print("\n=== Polymorphic Processing Demo ===")
        print("Processing multiple data types through same interface...")
        data_list: List[Union[List[int], str]] = [
            [1, 2, 3],
            "Hello, world",
            "INFO: System ready"
        ]
        processors: List[DataProcessor] = [
            num_process, text_processor, log_processor
        ]
        result: int = 1
        for processor, data in zip(processors, data_list):
            if processor.validate(data):
                print(f"Result {result}: {processor.process(data)}")
                result += 1
            else:
                print("error: skiped invalid data")
        print("\nFoundation systems online. Nexus ready for advanced streams.")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    stream_processor()
