#list commands
print("list commands:")

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
print()

#tuple commands
print ("tuple commands:")

my_tuple = ("apple", "banana", "cherry", "apple")

print(my_tuple.count("apple")) #counts the amount of times element is in tuple

print(my_tuple.index("cherry")) #finds the index of the first occurence of an element
print()

#set commands: sets store multiple elements in a single object but do not allow duplicate elements, sets are unordered and unindexed
#   if you print a set, all elements are printed in a random order
print ("set commands:")
vegetables = {"tomato", "potato", "carrot"}

vegetables.add("brocolli") #add a new element in the set
print(vegetables)

vegetables.discard("tomato") #remove the specified element from the set
print(vegetables)

vegetables.remove("potato") #removes specified element from the set but diff from discard where will return error if specified element is not there
print(vegetables)

vegetables.clear() #removes all elements in the set
print(vegetables)
