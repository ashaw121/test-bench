class TestPlan:
    def __init__(self, tests: list["Test"]):
        self.tests = tests

    def get_test_plan(self) -> list["Test"]:
        return self.tests

    def get_required_tools(self) -> set[str]:
        required = set()
        for test in self.tests:
            if hasattr(test, "tool_name"):
                required.add(test.tool_name)
        return required
