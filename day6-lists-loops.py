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

# Problem 1 — Find Sum and Average of List Elements
n = [10, 20, 30, 40, 50]
sum=0
for i in n:
    sum+=i
print(sum)
len= len(n)
avg= sum/len
print(avg)

