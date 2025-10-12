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

# Q4: Count Consonants and Vowels Separately
str = "Python Programming"
str= str.lower()
vov=0
con=0
vowels='aeiou'
for i in str:
    if i.isalpha():
        if i in vowels:
            vov+=1
        else:
            con+=1
print("count of vowels:",vov,"\ncount of consonants: ", con)

# Q5: Count Frequency of Each Character
# Write a program that takes a string and prints the frequency of each character.
str1 ='banana'
freq_count = {}
for i in str1:
    if i in freq_count:
        freq_count[i]+=1
    else:
        freq_count[i]=1
print(freq_count)

for i in set(str1):
    print(i, ":",str1.count(i))

#Q6: Find the Most Frequent Character
# Write a program to find the character that appears most frequently in a string.
s= "sucess"
dict={}
for i in s:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)
max_key=""
max_value=0
for k,v in dict.items():
    if v>max_value:
        max_value=v
        max_key=k
print(max_key)




