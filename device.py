class DeviceUnderTest:
    def __init__(self, serial_number: str, device_id: str, sub_assembly: str, metadata: dict = None):
        self.serial_number = serial_number  # Specific ID for this DUT
        self.device_id = device_id  # ID for all DUTs of the same type
        self.metadata = metadata or {}

    def perform_test(self):
        """Perform a specific test and return the result"""
        pass
