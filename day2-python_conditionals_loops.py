# Day 2 — Python: Conditionals & Loops

#age = int(input("Enter your age: "))
age=18
if age >= 18:
    print("You are an adult")
elif age >= 13:
    print("You are a teenager")
else:
    print("You are a child")

for i in range(1,6):
    print(i,end=' ')
print()

count=1
while count<=5:
    print(count,end=' ')
    count+=1
print()

for i in range(1,6):
    if i==3:
        continue
    if i==5:
        break
    print(i)

#Number Guessing Game
# secret_no = 7
# no=1
# while True:
#     no=int(input("enter a num bet 1-10: "))
#     if no<secret_no:
#         print("Too low")
#     elif no>secret_no:
#         print("Too high")
#     else:
#         print("you guessed it right!")
#         break

# Q1: Even or Odd
# Task: Take a number input and print whether it is even or odd.
a=9
if a%2==0:
    print(a,"even no")
else:
    print(a,"odd no")

# Q2: Print Numbers 1–10
# Task: Print numbers from 1 to 10 using a for loop.
for i in range(1,11):
    print(i,end=' ')
print()

# Q3: Factorial of a Number
# Task: Take a number input and print its factorial.
a1=5
fact=1
for i in range(1, a1+1):
    fact = fact*i
print(fact)
