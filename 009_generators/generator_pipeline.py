# Data flows: source -> filter -> transform -> loop (consumer)

def data_source():
    for i in range(1, 11):
        yield i

def filter_even(iterable):
    for i in iterable:
        if i % 2 == 0:
            yield i

def transform_square(iterable):
    for i in iterable:
        yield i * i

source = data_source()
evens = filter_even(source)
squares = transform_square(evens)

print("Pipeline Output:", list(squares)) 