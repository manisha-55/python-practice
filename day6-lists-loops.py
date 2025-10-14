# Day 6 — Lists & Loops in Python

# 1. Create and Access a List
fruits = ["apple", "banana", "cherry"]
print(fruits[0])     # apple
print(fruits[-1])    # cherry

# 2. Modify Elements
fruits[1] = "mango"
print(fruits)        # ['apple', 'mango', 'cherry']

# 3. Add Elements
fruits.append("orange")
fruits.insert(1, "grapes")
print(fruits)        # ['apple', 'grapes', 'mango', 'cherry', 'orange']

# 4. Remove Elements
fruits.remove("mango")
fruits.pop()         # removes last element

# 5. Loop Through a List
for f in fruits:
    print(f)
