# Day 5 — Patterns & Loops
# Problem 1 — Right-Angled Triangle of Stars, Task: Print a right-angled triangle pattern using *.
n=5
for i in range(1,n+1):
    for j in range(0,i):
        print('*',end=' ')
    print()
print()

#Pattern 2 — Inverted Triangle
for i in range(0,n):
    for j in range(0,n-i):
        print('*',end=' ')
    print()
print()

# Pattern 3 — Right-Aligned Triangle
for i in range(0,n):
    for j in range(0,n-i-1):
        print(' ',end='')
    for j in range(0,i+1):
        print('* ',end='')
    print()
print()

for i in range(1,n+1):
    for j in range(n-i):
        print("  ",end='')
    for j in range(i):
        print("* ",end='')
    print()