# First Principle Way: Reverse a string manually
text="hello"
reversed_text=""
for i in range (len(text) -1,-1,-1):
    reversed_text+=text[i]

print(reversed_text)

"""
Breaking it down

len(text) → gives the length of the string.

Example: "hello" → len("hello") = 5

len(text) - 1 → gives the last index.

"hello" → last index = 5 - 1 = 4 (because Python indexes start at 0).

range(start, stop, step) → generates a sequence of numbers.

start = len(text) - 1 → start from last index (4)

stop = -1 → go until just before -1 (so it includes 0)

step = -1 → move backwards
"""