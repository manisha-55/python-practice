# Day 7 — Advanced List Operations in Python

# 1.Nested Lists (Lists inside Lists):A list can contain another list, Used for representing matrices or tabular data.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][1])  # Output: 2

# List Comprehensions (Shortcut for loops) : A compact way to create lists.
squares = [x*x for x in range(1, 6)]
print(squares)   # [1, 4, 9, 16, 25]

squares = []
for x in range(1, 6):
    squares.append(x*x)

# Built-in List Functions Review
# sum(list) — sum of elements
# max(list) / min(list) — highest or lowest element
# sorted(list) — returns a new sorted list
# list.sort() — sorts the same list
# list.count(x) — counts occurrences
# list.index(x) — finds index of first occurrence

# Problem 1 — Print a 3×3 Matrix Using Nested Loops
a = [[5,6,7],[4,5,6],[8,9,3]]
print(a)