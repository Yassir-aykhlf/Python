from __future__ import annotations
from typing import Any, Iterator, Union
import sys

if sys.version_info >= (3, 10):
    from types import NotImplementedType
else:
    NotImplementedType = Any

class Vector:
    _components: tuple[float, ...]

    def __init__(self, *components: int | float) -> None:
        self._components = tuple(float(x) for x in components)

    def __repr__(self) -> str:
        return f"Vector({self._components})"
    
    def __add__(self, other: object) -> Vector | NotImplementedType:
        if isinstance(other, Vector):
            if len(self._components) != len(other._components):
                raise ValueError("Vectors must be same dimension")
            added = (a + b for a, b in zip(self._components, other._components))
            return Vector(*added)
        return NotImplemented
    
    def __mul__(self, other: object) -> Vector | NotImplementedType:
        if isinstance(other, (int, float)):
            scaled = (x * other for x in self._components)
            return Vector(*scaled)
        return NotImplemented

    def __len__(self) -> int:
        return len(self._components)
    
    def __getitem__(self, index: int) -> float:
        return self._components[index]

    def __iter__(self) -> Iterator[float]:
        return iter(self._components)