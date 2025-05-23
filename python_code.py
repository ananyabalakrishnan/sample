
#print command:
print('Hello World') 


a = 10
print(a) 

# print array:
c = [1, 2, 3, 4, 5]
print(c) 

#print type command:
print(type(10)) 

# print range command: range(start, stop, step)
# start: optional, at 0 for default; stop: mandatory; step: optional, 1 by default
for i in range(10): 
    print(i)

print(round(23.5678,2))

#input commands
x = input("Enter value: ")
print(x)
print(type(x))

stringword = input("Enter sentence: ")
print(stringword)
print(len(stringword))

# round command
print(round(23.5678,2))

#loop commands:
y = 1
while y < 10:
    print(y)
    y = y + 1
names = ["A", "B", "C", "D"]
for z in names:
    print(z)


#string commands:
str = "123%Hello"
print(str.isalnum()) #isalnum command checks whether given string is in alphanumeric order or not
str1 = "hello"
print(str1.capitalize()) #capitalize command capitalizes given string
print(str1.find("h")) #string.find(substring); string: string in which you want to search; substring: value that you want to search
print(str1.count("l", 1, 5)) #count function returns the count of occurences of a substring in a string object
#syntax: stringname.count(substring, start, end)

str2 = "InterviewBit"
newstr = str2.center(18, "*")
print(newstr)
