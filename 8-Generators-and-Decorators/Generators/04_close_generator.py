def local_chai():
    yield "Masala Chai"
    yield "Ginger Chai"

def imported_chai():
    yield "Matcha"
    yield "Oolong"

def full_menu():
    yield from local_chai()
    yield from imported_chai()

for chai in full_menu():
    print(chai)


def chai_stall():
    try:
        while True:
            order = yield "Waiting for chai order"
    except:
        print("Stall closed, No more chai")


stall = chai_stall()
print(next(stall))
stall.close() #cleanup

"""

def local_chai():
    yield "Masala"
    yield "Ginger"

def full_menu():
    yield from local_chai   # ❌ notice: no ()
What happens here?
local_chai without parentheses is just a function object, not a generator.

yield from expects an iterable (like a list, tuple, or generator).

Since a function is not iterable, Python will throw a TypeError:

php
Copy code
TypeError: 'function' object is not iterable
Correct usage ✅
python
Copy code
def full_menu():
    yield from local_chai()   # () calls the function → gives a generator
Now it works, because local_chai() returns a generator (which is iterable).

⚡ Rule of thumb:

local_chai → function object (not iterable)

local_chai() → generator object (iterable)



"""