#Day 3 — Python Strings & String Operations
text = "hello world"
print(text.upper())     # HELLO WORLD
print(text.lower())     # hello world
print(text.title())     # Hello World
print(text.replace("world", "Manisha"))  # hello Manisha
print(len(text))        # 11

# Mini Task: Greeting Formatter
# first_name = input("enter 1st name: ")
# last_name = input("enter last name: ")
# fullname =first_name.capitalize()+ " "+last_name.capitalize()
# print("Hello",fullname+" !, Welcome to Python.")

# Q1: Reverse a String
str = "Welcome to Python"
print(str[::-1])

# Q2: Check Palindrome String
str = "madam"
rev_Str = str[::-1]
if(str==rev_Str):
    print("palindrome ")
else:
    print("not palindrome")

# Q3: Count Vowels in a String
str = "Welcome to Python"
str= str.lower()
count=0
for i in str:
    if (i=='a' or i=='e'or i=='i' or i=='o'or i=='u'):
        count=count+1
print(count)


