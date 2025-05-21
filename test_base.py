from abc import ABC, abstractmethod


class Test:
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def run(self, device: DeviceUnderTest) -> "TestResult":
        """Perform the test"""
        pass
