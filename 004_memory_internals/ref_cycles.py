import sys
import gc

a = object()
print(f"After count: {sys.getrefcount(a)}") # 2, observer effect

b = a
print(f"After alias: {sys.getrefcount(a)}") # 3

del b
print(f"After delete: {sys.getrefcount(a)}") # 2


""" Reference Cycles """

gc.disable()
class Node:
    pass

n1 = Node()
n2 = Node()
n1.partner = n2
n2.partner = n1

del n1
del n2

print(gc.collect()) # 2