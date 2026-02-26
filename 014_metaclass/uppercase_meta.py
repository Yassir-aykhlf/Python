"""Metaclass that converts method names to uppercase."""


class UpperCaseMeta(type):
    """Metaclass that method names to uppercase in the class namespace."""

    def __new__(mcs, name: str, bases: tuple[type, ...], namespace: dict):
        upper_namespace: dict = {}
        for key, val in namespace.items():
            if callable(val) and not key.startswith('__'):
                upper_namespace[key.upper()] = val
            else:
                upper_namespace[key] = val
        return super().__new__(mcs, name, bases, upper_namespace)



if __name__ == "__main__":

    class Dummy(metaclass=UpperCaseMeta):
        def method_one(self):
            print("Method One")

        def method_two(self):
            print("Method Two")

    d = Dummy()
    print(d)
    d.METHOD_ONE()
    d.METHOD_TWO()

    try:
        d.method_one()
    except AttributeError as e:
        print(e)
