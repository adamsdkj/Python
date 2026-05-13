#!/usr/bin/env python3

from typing import Any, List, Optional, Dict, Union
from abc import ABC, abstractmethod


class DataStream(ABC):
    """Abstract base class for core streaming functionality."""

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data."""
        pass

    @abstractmethod
    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter data based on criteria."""
        pass

    @abstractmethod
    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream statistics."""
        pass


class SensorStream(DataStream):

    def __init__(self, stream_id: str):
        self.stream_id = stream_id
        self.stream_type = "Environmental Data"
        self.last_stats = {}

    def process_batch(self, data_batch: List[Any]) -> str:
        readings = len(data_batch)
        temps = [
            float(item.split(":")[1])
            for item in data_batch
            if item[:4] == "temp"
        ]
        avg_temp = sum(temps) / len(temps) if temps else 0
        self.last_stats = {"readings": readings, "avg_temp": avg_temp}
        return (
            f"Processing sensor batch: {data_batch}"
        )

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "high-priority":
            return [
                item for item in data_batch
                if "alert" in item or "critical" in item
            ]
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "analysis": (
                f"{self.last_stats.get('readings', 0)} readings processed, "
                f"avg temp: {self.last_stats.get('avg_temp', 0):.1f}\u00b0C"
            )
        }


class TransactionStream(DataStream):

    def __init__(self, stream_id: str):
        self.stream_id = stream_id
        self.stream_type = "Financial Data"
        self.last_stats = {}

    def process_batch(self, data_batch: List[Any]) -> str:
        operations = len(data_batch)
        net_flow = 0
        try:
            for item in data_batch:
                if len(item) >= 4 and item[:4] == "buy:":
                    net_flow += int(item.split(":")[1])
                elif len(item) >= 5 and item[:5] == "sell:":
                    net_flow -= int(item.split(":")[1])
        except Exception as e:
            return (
                f"{e.__class__.__name__} Please enter valid data"
            )
        self.last_stats = {"operations": operations, "net_flow": net_flow}
        return (
            f"Processing transaction batch: {data_batch}"
        )

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "high-priority":
            return [
                item for item in data_batch
                if (
                    (len(item) >= 4 and item[:4] == "buy:") or
                    (len(item) >= 5 and item[:5] == "sell:")
                ) and int(item.split(":")[1]) > 100
            ]
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "analysis": (
                f"{self.last_stats.get('operations', 0)} operations, "
                f"net flow: {self.last_stats.get('net_flow', 0)} units"
            )
        }


class EventStream(DataStream):

    def __init__(self, stream_id: str):
        self.stream_id = stream_id
        self.stream_type = "System Events"
        self.last_stats = {}

    def process_batch(self, data_batch: List[Any]) -> str:
        events = len(data_batch)
        errors = sum(
            1 for item in data_batch if "error" in item.lower()
        )
        self.last_stats = {"events": events, "errors": errors}
        return (
            f"Processing event batch: {data_batch}"
        )

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "high-priority":
            return [
                item for item in data_batch
                if "critical" in item or "error" in item.lower()
            ]
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "analysis": (
                f"{self.last_stats.get('events', 0)} events, "
                f"{self.last_stats.get('errors', 0)} error detected"
            )
        }


class StreamProcessor:

    def process_streams(self, streams: List[DataStream],
                        batches: List[List[Any]]) -> List[str]:
        results = []
        min_len = min(len(streams), len(batches))
        for i in range(min_len):
            stream = streams[i]
            batch = batches[i]
            result = stream.process_batch(batch)
            stats = stream.get_stats()["analysis"]
            results.append((result, stats))
        return results

    def filter_streams(self, streams: List[DataStream],
                       batches: List[List[Any]],
                       criteria: str) -> List[List[Any]]:
        filtered = []
        min_len = min(len(streams), len(batches))
        for i in range(min_len):
            stream = streams[i]
            batch = batches[i]
            filtered.append(stream.filter_data(batch, criteria))
        return filtered


def processor() -> None:
    streams = [
        SensorStream("SENSOR_001"),
        TransactionStream("SENSOR_001"),
        EventStream("SENSOR_001")
    ]
    batches = [
        ["temp:22.5", "humidity:65", "pressure:1013", "critical sensor alert"],
        ["buy:100", "sell:150", "buy:75", "buy:200"],
        ["login", "error", "logout", "critical event"]
    ]
    streamprocessor = StreamProcessor()
    data = streamprocessor.process_streams(streams, batches)
    print(data)


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    print("Initializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")
    print(f"Stream ID: {sensor.stream_id}, Type: {sensor.stream_type}")
    sensor_batch = [
        "temp:22.5", "humidity:65", "pressure:1013", "critical sensor alert"
    ]
    print(sensor.process_batch(sensor_batch))
    print(f"Sensor analysis: {sensor.get_stats()['analysis']}")

    print("\nInitializing Transaction Stream...")
    transaction = TransactionStream("TRANS_001")
    print(f"Stream ID: {transaction.stream_id}, Type:"
          f"{transaction.stream_type}")
    transaction_batch = [
        "buy:100", "sell:150", "buy:75", "buy:200"
    ]
    print(transaction.process_batch(transaction_batch))
    print(f"Transaction analysis: {transaction.get_stats()['analysis']}")

    print("\nInitializing Event Stream...")
    event = EventStream("EVENT_001")
    print(f"Stream ID: {event.stream_id}, Type: {event.stream_type}")
    event_batch = [
        "login", "error", "logout", "critical event"
    ]
    print(event.process_batch(event_batch))
    print(f"Event analysis: {event.get_stats()['analysis']}")

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")
    batches = [
        ["temp:21.0", "temp:23.0"],
        ["buy:50", "sell:120", "buy:80", "sell:60"],
        ["login", "error", "logout"]
    ]
    print("\nBatch 1 Results:")
    print(f"- Sensor data: {len(batches[0])} readings processed")
    print(f"- Transaction data: {len(batches[1])} operations processed")
    print(f"- Event data: {len(batches[2])} events processed")

    print("\nStream filtering active: High-priority data only")
    filtered_sensor = sensor.filter_data(sensor_batch, "high-priority")
    filtered_transaction = transaction.filter_data(transaction_batch,
                                                   "high-priority")
    print(
        f"Filtered results: {len(filtered_sensor)} critical sensor alerts, "
        f"{len(filtered_transaction)} large transactions"
    )
    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
