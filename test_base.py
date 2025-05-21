from abc import ABC, abstractmethod


class Test(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def run(self, dut: DeviceUnderTest) -> "TestResult":
        """Perform the test"""
        pass
