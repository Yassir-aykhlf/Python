class Countdown:
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < 0:
            raise StopIteration
        num = self.current
        self.current -= 1
        return num

itr = Countdown(3)

# for n in itr:
#     print(n)

print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))

for n in itr:
    print(n)