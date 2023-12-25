"""
Иногда возникает необходимость перенаправить вывод в нужное нам место внутри программы по ходу её выполнения.
Реализуйте контекстный менеджер, который принимает два IO-объекта (например, открытые файлы)
и перенаправляет туда стандартные потоки stdout и stderr.

Аргументы контекстного менеджера должны быть непозиционными,
чтобы можно было ещё перенаправить только stdout или только stderr.
"""
import sys
import traceback
from types import TracebackType
from typing import Type, Literal, IO


class Redirect:
    def __init__(self, stdout: IO = None, stderr: IO = None) -> None:
        """Перенаправляем поток вывода в файл"""
        self.new_stdout = stdout if stdout else sys.stdout
        self.new_stderr = stderr if stderr else sys.stderr

    def __enter__(self) -> None:
        """Сохраняем старый поток вывода"""
        self.old_stdout = sys.stdout
        self.old_stderr = sys.stderr

        sys.stdout = self.new_stdout
        sys.stderr = self.old_stderr

    def __exit__(
            self,
            exc_type: Type[BaseException] | None,
            exc_val: BaseException | None,
            exc_tb: TracebackType | None
    ) -> Literal[True] | None:
        """Закрываем файл и возвращаем старый поток вывода"""
        if exc_type is not None:
            sys.stdout = self.old_stdout
            sys.stderr = self.new_stderr.write(traceback.format_exc())
            sys.stderr = self.old_stderr
            self.new_stdout.close()
            self.new_stderr.close()
            return True
        else:
            sys.stdout = self.old_stdout
            sys.stderr = self.old_stderr
            self.old_stdout.close()
            self.old_stderr.close()
            return None


if __name__ == '__main__':
    print("Hello stdout")
    stdout_file = open('stdout.txt', 'w')
    stderr_file = open('stderr.txt', 'w')

    with Redirect(stdout=stdout_file, stderr=stderr_file):
        print("Hello stdout.txt")
        raise Exception('Hello stderr.txt')

    print('Hello stdout again')
    raise Exception('Hello stderr')
