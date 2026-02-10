class Range:
    def __init__(self, start, stop=None, step=1):
        if step == 0:
            raise ValueError("Range() arg 3 must not be zero")
        if stop is None:
            self.start = 0
            self.stop = start
        else:
            self.start = start
            self.stop = stop
        self.step = step
        self.current = self.start

    def __iter__(self):
        return self
    
    def __next__(self):
        if (self.step > 0 and self.current >= self.stop) or \
           (self.step < 0 and self.current <= self.stop):
           raise StopIteration
        result = self.current
        self.current += self.step
        return result

for n in Range(1, 10, 2):
    print(n, end=" ")
print("\n")