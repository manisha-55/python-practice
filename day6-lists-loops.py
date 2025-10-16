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

# Problem 2 — Find the Maximum and Minimum Element
a = [12, 45, 7, 89, 23]
min=a[0]
max=a[0]
for i in a:
    if(i>max):
        max=i
    if(i<min):
        min=i
print(max, min)

# Problem 3 — Count Even and Odd Numbers in a List
a = [12, 45, 7, 89, 23]
even=0
odd=0
for i in a:
    if i%2==0:
        even+=1
    else:
        odd+=1
print(even, odd)

# Problem 4 — Reverse a List Without Using reverse()
numbers = [1, 2, 3, 4, 5]
print(numbers[::-1])