# Q1. Write a program that removes all vowels (a, e, i, o, u) from a given string.
s="programming"
s1=''
v='aeiou'
for i in s.lower():
    if i not in v:
        s1+=i
print(s1)

# Problem 2 — Reverse a String Without Slicing
s="programming"
rev=''
for i in s:
    rev=i+rev
print(rev)

# Problem 3 — Check If Two Strings Are Anagrams, Check if two strings contain the same letters in a different order.
a='listen'
b='silent'
if sorted(a) == sorted(b):
    print("anagrams")
else:
    print("not")
