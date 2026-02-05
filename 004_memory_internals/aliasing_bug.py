import sys
import gc

""" Mutable Default Bug """

# Wrong
def _add_passenger(passenger, manifest=[]):
    manifest.append(passenger)
    return manifest

# Correct
def add_passenger(passenger, manifest=None):
    if manifest is None:
        manifest = []
    manifest.append(passenger)
    return manifest

print(add_passenger("Alice"))
print(add_passenger("Bob"))

# in Python functions are objects
# when the interepter reads def _add_passenger...
# it creates the function object
# it evaluates [], and stores an empty list object in __defaults__
# evaluated one time, one list persists for all calls
# since list is a mutable type, the changes persist