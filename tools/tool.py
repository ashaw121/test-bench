from abc import ABC, abstractmethod


class Tool(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def initialize(self):
        """Connect to and initialize tool"""
        pass

    @abstractmethod
    def shutdown(self):
        """Safely disconnect or power down the tool"""
        pass
