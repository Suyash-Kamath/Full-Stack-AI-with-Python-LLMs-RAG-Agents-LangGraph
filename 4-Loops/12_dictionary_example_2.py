def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

operations={
    "add":add,
    "subtract":subtract,
    "multiply":multiply
}

choice=input("Enter your choice")
result = operations.get(choice, lambda a,b:"Invalid")(5,6)
print(result)