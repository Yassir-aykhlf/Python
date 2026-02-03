def explore_immutability():
    x = 1000
    print(f"Original x: {x} (ID: {id(x)})")
    x = x + 1
    print(f"Modified x: {x} (ID: {id(x)}) <--- ID changed, New object created.")

    s = "hello"
    old_id = id(s)
    s += " world"
    print(f"String changed? {id(s) != old_id} (Old ID: {old_id}, New ID: {id(s)})")

def explore_mutability():
    print("\n--- Mutable Types (list, dict, set) ---")
    # Lists are mutable. Modifying 'l' keeps the same object.
    l = [1, 2, 3]
    print(f"Original list: {l} (ID: {id(l)})")
    
    l.append(4)
    print(f"Modified list: {l} (ID: {id(l)}) <--- ID same, Modified in-place.")

def tuple_paradox():
    print("\n--- The Tuple Paradox (Immutability is Shallow) ---")
    
    t = (1, 2, [30, 40]) 
    print(f"Tuple before: {t}")
    
    # t[2] = [99]      # TypeError: 'tuple' object does not support item assignment
    # t[2] += [50]     # TypeError: but the list inside actually changes.
    t[2].append(50)    # This works.
    print(f"Tuple after:  {t} <--- The tuple's value changed, but its ID is constant.")
    print("Lesson: Tuples are immutable containers, but their contents might not be.")

if __name__ == "__main__":
    explore_immutability()
    explore_mutability()
    tuple_paradox()