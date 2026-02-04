class Vector:
    def __init__(self, *components):
        self._components = tuple(components)

    def __repr__(self):
        return f"Vector({self._components})"
    
    def __add__(self, other):
        if isinstance(other, self.__class__):
            if len(self._components) != len(other._components):
                raise ValueError("Vectors must be same dimension")
            added = (a + b for a, b in zip(self._components, other._components))
            return Vector(*added)
        return NotImplemented
    
    def __mul__(self, other):
        elif isinstance(other, (int, float)):
            scaled = (x * other for x in self._components)
            return Vector(*scaled)
        return NotImplemented

    def __len__(self):
        return len(self._components)
    
    def __getitem__(self, index):
        return self._components[index]

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = v1 + v2
v4 = v1 * 3
