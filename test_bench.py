class TestBench:
    def __init__(self, devices: list[DevicesUnderTest], test_plan: TestPlan, tools: dict[str, "Tool"] = None):
        self.devices = devices
        self.test_plan = test_plan
        self.tools = tools or {}

    def run_all_tests(self):
        """Run the defined test plan on all devices"""
        pass

    def get_tool(self, name: str) -> "Tool":
        return self.tools[name]
