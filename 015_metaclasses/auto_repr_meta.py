"""Metaclass that automatically generates a __repr__ method for classes."""


class AutoReprMeta(type):
    def __new__(mcs, name: str, bases: tuple[type, ...], namespace: dict):
        def __repr__(self):
            return f"{name}({', '.join(f'{k}={v!r}' for k, v in self.__dict__.items())})"
        namespace['__repr__'] = __repr__
        return super().__new__(mcs, name, bases, namespace)


if __name__ == "__main__":
    class Point(metaclass=AutoReprMeta):
        def __init__(self, x: int, y: int):
            self.x = x
            self.y = y

    p = Point(1, 2)
    print(p)
