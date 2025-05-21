#list commands
'''
list = [1, 2, 3, 4]
x = list.append(5) #returns none when trying to print

print(list.copy()) #copy command creates a new copy of the list object

list.insert(4, 3) #listname.insert(position, element) inserts element in position in list
print(list.copy())

list.pop(5) #listname.pop(position) position from which you want to remove the element
print(list.copy())

list.reverse() #reverses order of all elements in the list
print(list.copy())

list.sort() #sort the elements of the list in ascending order by default
print(list.copy())
'''

#tuple commands
my_tuple = ("apple", "banana", "cherry", "apple")
print(my_tuple.count("apple"))
