# Investigative Way: Try built-in features and experiment
text = "hello"

# Try slicing
print(text[::-1])  # "olleh"

# Investigate: what if I change the step?
print(text[::2])   # "hlo" (every 2nd character)
print(text[::-2])  # "olh" (reverse every 2nd character)

# Try with different strings
print("Python"[::-1])   # "nohtyP"
print("12345"[::-1])    # "54321"

"""
The syntax is:

text[start:stop:step]


start → where to begin (default = 0)

stop → where to end (default = end of string)

step → how much to jump each time (default = 1)


Perfect question ⚡ You're now comparing **positive step (`::2`)** vs **negative step (`::-1`)**.
Let’s break it **exactly how Python interprets them internally**.

---

## 🔹 General rule for slicing

```python
text[start:stop:step]
```

1. If `step > 0` → move **left → right**

   * default `start = 0`
   * default `stop = len(text)`

2. If `step < 0` → move **right → left**

   * default `start = len(text) - 1`
   * default `stop = -1`

---

## 🔹 Example text

```python
text = "hello"   # indexes: h=0, e=1, l=2, l=3, o=4
```

---

### Case 1: `text[::2]`

* `step = 2` (positive → left → right)
* `start = 0`
* `stop = len(text) = 5`
* So internally → `range(0, 5, 2) → [0, 2, 4]`

👉 Collect chars: `"hlo"`

---

### Case 2: `text[::-1]`

* `step = -1` (negative → right → left)
* `start = len(text)-1 = 4`
* `stop = -1`
* So internally → `range(4, -1, -1) → [4, 3, 2, 1, 0]`

👉 Collect chars: `"olleh"`

---

### 🚀 Key difference in interpretation

* `::2` → “Walk forward, skipping every 2nd character.”
* `::-1` → “Walk backward, one step at a time.”

Both are just **different ranges under the hood**.

---

✅ Think like this:

* If **step > 0** → start from **left side (0)**.
* If **step < 0** → start from **right side (len-1)**.

---

Would you like me to **draw both index ranges visually on `"hello"`**, so you can see how Python is literally walking through the string?


"""