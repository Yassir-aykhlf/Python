class MyDefaultDict(dict):
    def __init__(self, default_factory):
        super().__init__()
        self.default_factory = default_factory

    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key)
        value = self.default_factory()
        self[key] = value
        return value

counter = MyDefaultDict(int)
counter['apple'] += 1
print(counter)

groups = MyDefaultDict(list)
groups['fruits'].append('apple')
print(groups)