from typing import TypeVar, Generic

T = TypeVar("T")

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._stack: list[T] = []

    def push(self, item: T) -> None:
        self._stack.append(item)
        
    def pop(self) -> T:
        if not self._stack:
            raise IndexError("Stack is empty")
        return self._stack.pop()

s_int = Stack[int]()
s_int.push(1)
s_int.push("typeError")