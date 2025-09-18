menu = ["Green", "Lemon", "Spiced", "Mint"]

# one of the way to number each item 

numbered_menu=list(enumerate(menu))
print(numbered_menu)

# second way to use enumerate in loop
for idx, item in enumerate(menu, start=1):
    print(f"{idx} : {item} chai")