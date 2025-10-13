# Day 5 — Patterns & Loops
# Problem 1 — Right-Angled Triangle of Stars, Task: Print a right-angled triangle pattern using *.
n=5
for i in range(1,n+1):
    for j in range(0,i):
        print('*',end=' ')
    print()

