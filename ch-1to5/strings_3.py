a=input("name=")
print("Good Afternoon,",a)

''' 
Dear <|Name|>, 
You are selected! 
<|Date|> 
'''
name="Ram"
date="20jan 2026"
print("Dear ",name,"\nYou are selected!\n",date)


string="I  am Rashmi KUMARI. I am  in Final Year."
if "  " in string:
    print("string has double spaces")
    print(string.count("  "))
else:
    print("string does not conatin spaces.")

print(string)
string=string.replace("  ", " ") # Store krega replaced string
print(string)

letter = "Dear Harry, this python course is nice. Thanks!"
print("Dear Harry,\n","this python course is nice.\n", "Thanks!")