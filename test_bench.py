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

    def check_required_tools(self):
        missing_tools = []
        required_tools = self.test_plan.get_required_tools()
        for tool_name in required_tools:
            if tool_name not in self.tools:
                missing_tools.append(tool_name)
        if missing_tools:
            raise RuntimeError(f"Missing required tools: {missing_tools}")

        return True
