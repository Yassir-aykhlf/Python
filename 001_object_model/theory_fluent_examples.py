class TwilightBus:
    """
    Example from Ch 6: The danger of Aliasing.
    If you use a mutable default argument or assign a list directly,
    variables become aliases for the same object.
    """
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            # This creates an alias, not a copy
            self.passengers = passengers 

    def drop(self, name):
        self.passengers.remove(name)

class Vector:
    """
    Example from Ch 1: The Python Data Model.
    Demonstrates correct use of __repr__ (for devs) vs __str__ (for users).
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        # !r forces the standard representation
        return f'Vector({self.x!r}, {self.y!r})'

    def __str__(self):
        return f'({self.x}, {self.y})'

if __name__ == "__main__":
    # Test Aliasing
    team = ['Sue', 'Tina', 'Maya']
    bus = TwilightBus(team)
    bus.drop('Tina')
    print(f"Bus passengers: {bus.passengers}")
    print(f"Original list:  {team} <--- 'Tina' vanished from here too")
    
    # Test Repr
    v = Vector(3, 4)
    print(f"User view (str): {v}")      # (3, 4)
    print(f"Dev view (repr): {v!r}")    # Vector(3, 4)