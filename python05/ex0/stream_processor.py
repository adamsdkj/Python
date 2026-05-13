#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        ...

    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...

    def format_output(self, result: str) -> str:
        return result


class NumericProcessor(DataProcessor):

    def process(self, data: List[int]) -> str:
        self.data: List[int] = data
        if self.validate(data):
            number_count: int = len(self.data)
            numbers_sum: int = sum(self.data)
            avg: float = numbers_sum / number_count if number_count else 0.0
            return (
                f"Processed {number_count} numeric values, "
                f"sum={numbers_sum}, avg={avg}"
            )
        return "Validation: Invalid numeric data"

    def format_output(self, result: str) -> str:
        return (
            "Initializing Numeric Processor...\n"
            f"Processing data: {self.data}\n"
            "Validation: Numeric data verified\n"
            f"Output: {result}\n"
        )

    def validate(self, data: List[int]) -> bool:
        try:
            for number in data:
                if not isinstance(number, int):
                    raise Exception
        except Exception:
            return False
        return True


class TextProcessor(DataProcessor):

    def process(self, data: str) -> str:
        self.data: str = data
        if self.validate(data):
            char_count: int = len(self.data)
            words_count: int = len(data.split())
            return (
                f"Processed text: {char_count} characters, "
                f"{words_count} words"
            )
        return "Validation: Invalid text data"

    def format_output(self, result: str) -> str:
        return (
            "Initializing Text Processor...\n"
            f'Processing data: "{self.data}"\n'
            "Validation: Text data verified\n"
            f"Output: {result}\n"
        )

    def validate(self, data: str) -> bool:
        try:
            for character in data:
                if not isinstance(character, str):
                    raise Exception
        except Exception:
            return False
        return True


class LogProcessor(DataProcessor):

    def process(self, data: str) -> str:
        self.data: str = data
        if self.validate(data):
            split_data = data.split(":", 1)
            level = split_data[0].strip().lower()
            message = split_data[1].strip() if len(split_data) > 1 else ""
            if level == "error":
                return f"[ALERT] ERROR level detected: {message}"
            if level == "info":
                return f"[INFO] INFO level detected: {message}"
            return f"[LOG] Unknown log level: {data}"
        return "Validation: Invalid log data"

    def format_output(self, result: str) -> str:
        split_data = self.data.split(":", 1)
        level = split_data[0].strip().lower()
        message = split_data[1].strip() if len(split_data) > 1 else ""
        if level == "error":
            output_line = f"Output: [ALERT] ERROR level detected: {message}\n"
            validation_line = "Validation: Log entry verified\n"
        elif level == "info":
            output_line = f"Output: [INFO] INFO level detected: {message}\n"
            validation_line = "Validation: Log entry verified\n"
        else:
            output_line = f"Output: [LOG] Unknown log level: {self.data}\n"
            validation_line = "Validation: Log entry verified\n"
        return (
            "Initializing Log Processor...\n"
            f'Processing data: "{self.data}"\n'
            f"{validation_line}"
            f"{output_line}"
        )

    def validate(self, data: str) -> bool:
        try:
            split_data = data.split(":", 1)
            level = split_data[0].strip().lower()
            if level not in ["info", "error"]:
                raise Exception
        except Exception:
            return False
        return True


def run(processor: DataProcessor, data: Any) -> None:
    print(processor.process(data))


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    numeric_proc = NumericProcessor()
    text_proc = TextProcessor()
    log_proc = LogProcessor()

    print(numeric_proc.format_output(numeric_proc.process([1, 2, 3, 4, 5])))
    print(text_proc.format_output(text_proc.process("Hello Nexus World")))
    print(log_proc.format_output(
        log_proc.process("ERROR: Connection timeout")))
    print(
        "=== Polymorphic Processing Demo ===\n"
        "Processing multiple data types through same interface..."
    )
    processors = {
        NumericProcessor: [2, 2, 2],
        TextProcessor: "adadadadad aa",
        LogProcessor: "INFO: System ready"
    }
    i = 1
    for key, data in processors.items():
        print(f"Result {i}: ", end="")
        run(key(), data)
        i += 1
    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
