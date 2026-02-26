"""Metaclass that converts method names to uppercase."""

class UpperCaseMeta(type):
    def __new__(mcs, name: str, bases: tuple[type, ...], namespace: dict):
        upper_namespace: dict = {}
        for key, val in namespace.items():
            if callable(val) and not key.startswith('__'):
                upper_namespace[key.upper()] = val
            else:
                upper_namespace[key] = val
        return super().__new__(mcs, name, bases, upper_namespace)



if __name__ == "__main__":
    class APIClient(metaclass=UpperCaseMeta):
        def fetch_data(self):
            return "Data fetched"

    client = APIClient()
    print(client.FETCH_DATA())
