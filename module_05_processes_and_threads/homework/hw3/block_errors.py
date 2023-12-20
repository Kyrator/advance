"""
Реализуйте контекстный менеджер, который будет игнорировать переданные типы исключений, возникающие внутри блока with.
Если выкидывается неожидаемый тип исключения, то он прокидывается выше.
"""
import sys
from typing import Collection, Type, Literal
from types import TracebackType


class BlockErrors:
    def __init__(self, errors: Collection) -> None:
        self.errors = errors

    def __enter__(self) -> None:
        self.stdout = sys.stderr
        self.stderr = sys.stderr
        # print("self.stdout", self.stdout)
        # print("self.stderr", self.stderr)

    def __exit__(
            self,
            exc_type: Type[BaseException] | None,
            exc_val: BaseException | None,
            exc_tb: TracebackType | None
            ) -> Literal[True] | None:
        # print("start end")
        if issubclass(exc_type, tuple(self.errors)) or exc_type in self.errors:
            return True
        else:
            print(exc_type.__name__, exc_val)
            return None



