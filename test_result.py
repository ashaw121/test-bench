from datetime import datetime


class TestResult:
    def __init__(self, serial_number: str, device_id: str, test_name: str, test_result: bool, test_data: dict, timestamp=None):
        self.serial_number = serial_number
        self.device_id = device_id
        self.test_name = test_name
        self.test_result = test_result
        self.test_data = test_data
        self.timestamp = timestamp or datetime.now().isoformat()

    def to_dict(self) -> dict:
        return {
            "serial_number": self.serial_number,
            "device_id": self.device_id,
            "test_name": self.test_name,
            "test_result": self.test_result,
            "test_data": self.test_data,
            "timestamp": self.timestamp,
        }

    def __repr__(self):
        return (f"TestResult(serial_number={self.serial_number!r}, device_id={self.device_id!r}, "
                f"test_name={self.test_name!r}, test_result={self.test_result!r}, "
                f"test_data={self.test_data!r}, timestamp={self.timestamp!r})")
