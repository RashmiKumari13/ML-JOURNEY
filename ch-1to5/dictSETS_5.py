"""

1. Write a program to create a dictionary of Hindi words with values as their English 
translation. Provide user with an option to look it up! 
2. Write a program to input eight numbers from the user and display all the unique 
numbers (once). 
3. Can we have a set with 18 (int) and '18' (str) as a value in it? 
4. What will be the length of following set s: 
s = set() 
s.add(20) 
s.add(20.0) 
s.add('20') # length of s after these operations? 
5. s = {} 
What is the type of 's'? 
6. Create an empty dictionary. Allow 4 friends to enter their favorite language as 
value and use key as their names. Assume that the names are unique. 
7. If the names of 2 friends are same; what will happen to the program in problem 
6? 
8. If languages of two friends are same; what will happen to the program in problem 
6? 
9. Can you change the values inside a list which is contained in set S? 
s = {8, 7, 12, "Harry", [1,2]}
"""
"""
lang={
    "मित्र":"friend",
    "करुणा":"compassion",
    "प्रेम":"love",
    "परिवार":"family",
    "शांति":"Peace"
}
print("available words: ",list(lang.keys()))
print(lang.items())
word = input("Enter word: ")
check=lang.get(word)
if check:
    print("English translation of{word} is: ",{check})
else:
    print("does not exists.")



for num in range(0,8):
    number=int(input("eneter the number:"))
    num+=1
for num in range(0,8):
    print(number)
    num+=1


setsvalue={18,"18",95.059}
print(setsvalue)


s = set() 
s.add(20) 
s.add(20.0) 
s.add('20')
print(s)
print(type(s))

s={}
print(type(s))
"""
emptydict={ }

for i in range(0,4):
    print("name of friends:",input("i"))
    i+=1
for j in range(0,4):
    print("name of lang:",input("j"))
    j+=1

print("dictionary:",emptydict.add({"i":"j"}))