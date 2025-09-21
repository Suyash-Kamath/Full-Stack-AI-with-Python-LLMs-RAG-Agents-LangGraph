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


"""

def chai_stall():
  try:
      while True:
          order = yield "Waiting for chai order"
  except:
      print("Stall closed, No more chai")


stall = chai_stall()
print(next(stall))
Why you got both lines?
print(next(stall))

Starts the generator and runs until the first yield.

That yield gives "Waiting for chai order", so that gets printed. ✅

But then you see:

yaml
Copy code
Stall closed, No more chai
This means your generator exited immediately after yielding once.

Why did it exit?
Because of your bare except:.

When a generator ends, Python internally raises a StopIteration to signal "I’m done".

Since you wrote just except:, it catches all exceptions, including StopIteration.

So instead of staying paused and waiting for input, it fell into your except: and printed "Stall closed, No more chai".

Fix ✅
Catch only the exception you expect (like GeneratorExit when you manually close a generator), not StopIteration.

python
Copy code
def chai_stall():
    try:
        while True:
            order = yield "Waiting for chai order"
    except GeneratorExit:
        print("Stall closed, No more chai")
Now:

python
Copy code
stall = chai_stall()
print(next(stall))     # "Waiting for chai order"
print(next(stall))     # still works, order=None
stall.close()          # triggers the except
👉 The important lesson:

StopIteration is normal — it’s how generators end. Don’t catch it accidentally.

Use GeneratorExit if you want custom cleanup logic when the generator is closed.

"""