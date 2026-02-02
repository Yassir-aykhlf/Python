# Python Object Model

## Key Concepts
1. **Everything is an Object**: Variables are labels (references), not boxes.
2. **Identity (`is`) vs Equality (`==`)**: 
   - `is` checks memory address (`id()`).
   - `==` checks value content.
3. **Memory Optimization**:
   - Standard classes use `__dict__` (hash table) to store attributes.
   - `__slots__` replaces `__dict__` with a fixed-size array, saving massive memory on millions of objects.

## Files
- `memory_and_slots.py`: Proof of concept for memory savings.
- `theory_fluent_examples.py`: Examples from *Fluent Python* (Aliasing & Magic Methods).