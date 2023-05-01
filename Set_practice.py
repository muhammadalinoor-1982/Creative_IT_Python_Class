""" Python Collections (Arrays)
There are four collection data types in the Python programming language:

*>> List is a collection which is ordered and changeable. Allows duplicate members.
*>> Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
*>> Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
*>> Dictionary is a collection which is ordered** and changeable. No duplicate members. """

# Set in Python
# *>> Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Symple_set = {"a", "b", "c"}
print(Symple_set)

# Duplicates Not Allowed
# Sets cannot have two items with the same value
# Duplicate values will be ignored
Duplicates_set = {"a", "b", "c", "a"}
print(Duplicates_set)

# The values True and 1 are considered the same value in sets, and are treated as duplicates
# True and 1 is considered the same value
Bool_set = {"a", "b", "c", True, 1, 2}
print(Bool_set)

# Length of Set 
Length_set = {"a", "b", "c", "d", "e"}
print(len(Length_set))

# Data Type of Set 
Type_set = {"a", "b", "c", "d", "e"}
print(type(Type_set))

# Set Items - Data Types
# String, int and boolean data types
str_set = {"a", "b", "c"}
int_set = {1, 5, 7, 9, 3}
bool_set = {True, False, False}
print(str_set, int_set, bool_set)

# A set can contain different data types
# A set with strings, integers and boolean values
Complex_set = {"abc", 34, True, 40, "male"}
print(Complex_set)

# The set() Constructor
# It is also possible to use the set() constructor to make a set.
Constructor_set = set(("a", "b", "c")) 
print(Constructor_set)

# Access set Items
# Print the second item in the set
Access_set = {"a", "b", "c"}
for x in Access_set:
    print(x)

# Check if "b" is present in the set
Check_set = {"a", "b", "c"}
print("b" in Check_set)

""" Change Items
Once a set is created, you cannot change its items, but you can add new items. """

# Add Set Items
# Once a set is created, you cannot change its items, but you can add new items.
# To add one item to a set use the add() method.
Add_set = {"a", "b", "c"}
Add_set.add("orange")
print(Add_set)

# To add items from another set into the current set, use the update() method.
# Add elements from bijoy into shadhinota
shadhinota = {"a", "b", "c"}
bijoy = {21, "m", "p"}
shadhinota.update(bijoy)
print(shadhinota)

# Add Any Iterable
# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.). 
# Add elements of a list to at set
Iterable_set = {"a", "b", "c"}
Iterable_list = ["k", "o"]
Iterable_set.update(Iterable_list)
print(Iterable_set)

# Remove Set Items
# To remove an item in a set, use the remove(), or the discard() method.
# Remove "dust" by using the remove() method
remove_set = {"a", "dust", "c"}
remove_set.remove("dust")
print(remove_set)
# Remove "dust" by using the discard() method
discard_set = {"a", "dust", "c"}
discard_set.discard("dust")
print(discard_set)

""" You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
The return value of the pop() method is the removed item. """
#Remove a random item by using the pop() method
# Sets are unordered, so when using the pop() method, you do not know which item that gets removed.
pop_set = {"a", "b", "c"}
x = pop_set.pop()
print(x)
print(pop_set)

# The clear() method empties the set
clear_set = {"a", "b", "c"}
clear_set.clear()
print(clear_set)

# The del keyword will delete the set completely
delete_set = {"a", "b", "c"}
del delete_set
# print(delete_set)

# Loop Sets
# You can loop through the set items by using a for loop
# Loop through the set, and print the values
loop_set = {"a", "b", "c"}
for x in loop_set:
  print(x)

# Join Sets
""" You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another """
# Both union() and update() will exclude any duplicate items
#The union() method returns a new set with all items from both sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# The update() method inserts the items in set4 into set5
set4 = {"a", "b" , "c"}
set5 = {1, 2, 3}
set4.update(set5)
print(set4)


