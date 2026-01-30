from abc import ABC, abstractmethod
from typing import Any


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
        if type(data).__name__ != "list":
            return False
        else:
            count = 0
            for element in data:
                if type(element).__name__ == "int" or\
                        type(element).__name__ == "float":
                    count += 1
            if count == len(data):
                return True
            else:
                return False

    def process(self, data: Any) -> str:
        numeric_value = len(data)
        total = sum(data)
        avg = total / numeric_value
        return (f"Processed {numeric_value} numeric values,"
                f" sum={total}, avg={avg:.1f}")


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if type(data).__name__ != "str":
            return False
        return True

    def process(self, data: Any) -> str:
        chars = len(data)
        count = len(data.split())
        return f"Processed text: {chars} characters, {count} words"


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if type(data).__name__ != "str":
            return False

        check = data.split(":")
        if len(check) > 1:
            logs = ["ERROR", "INFO"]
            if check[0] in logs:
                return True
        return False

    def process(self, data: Any) -> str:
        check = data.split(":")
        if check[0] == "ERROR":
            return f"[ALERT] ERROR level detected: {check[1]}"
        elif check[0] == "INFO":
            return f"[INFO] INFO level detected: {check[1]}"


def stream_processor() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    num_process = NumericProcessor()
    print("Initializing Numeric Processor...")
    data_1 = [1, 2, 3, 4, 5]
    print(f"Processing data: {data_1}")
    if num_process.validate(data_1):
        print("Validation: Numeric data verified")
        print(num_process.format_output(num_process.process(data_1)))
    else:
        print("Validation: Could not validate Numeric data")

    print()

    print("Initializing Text Processor...")
    text_processor = TextProcessor()
    data_2 = "Hello Nexus World"
    print(f'Processing data: "{data_2}"')
    if text_processor.validate(data_2):
        print("Validation: Text data verified")
        txt_pr = text_processor.process(data_2)
        print(f"{text_processor.format_output(txt_pr)}")
    else:
        print("Validation:: Coud not verify Text data")

    print()

    print("Initializing Log Processor...")
    log_processor = LogProcessor()
    data_3 = "ERROR: Connection timeout"
    print(f"Processing data: {data_3}")
    if log_processor.validate(data_3):
        print("Validation: Log entry verified")
        print(f"{log_processor.format_output(log_processor.process(data_3))}")
    else:
        print("Validation: Could not validate log entry")

    print()

    print("=== Polymorphic Processing Demo ===")
    data_1 = [1, 2, 3]
    data_2 = "Hello, world"
    data_3 = "INFO: System ready"
    processors = [num_process, text_processor, log_processor]
    print(f"Result 1: {processors[0].process(data_1)}")
    print(f"Result 2: {processors[1].process(data_2)}")
    print(f"Result 3: {processors[2].process(data_3)}")


if __name__ == "__main__":
    stream_processor()
