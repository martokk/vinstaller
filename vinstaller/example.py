"""Example of code."""
from loguru import logger


class ExampleClass:
    @staticmethod
    def print_name(name: str) -> str:
        return f"Hello {name} from click! See __main__.py"

    @logger.catch
    def example_divide_by_zero(self) -> float:
        return 100 / 0
