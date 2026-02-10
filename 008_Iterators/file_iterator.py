import itertools
import os
import time

class FileLineIterator:
    def __init__(self, filename):
        self.file = open(filename, 'r')

    def __iter__(self):
        return self
    
    def __next__(self):
        line = self.file.readline()
        if line == '':
            self.file.close()
            raise StopIteration
        return line.strip()

test_file_name = f"test_{os.getpid()}.txt"

with open(test_file_name, 'w') as f:
    for i in range(100):
        f.write(f"Line {i}\n")

file_itr = FileLineIterator(test_file_name)

first_five = itertools.islice(file_itr, 5)

for line in first_five:
    time.sleep(2)
    print(line)

os.remove(test_file_name)