""" Python Collections (Arrays)
There are four collection data types in the Python programming language:

*>> List is a collection which is ordered and changeable. Allows duplicate members.
*>> Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
*>> Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
*>> Dictionary is a collection which is ordered** and changeable. No duplicate members. """

# List in Python
# *>> List is a collection which is ordered and changeable. Allows duplicate members.
Simple_list = ["a", "b", "c"]
print(Simple_list)

# Allow Duplicates in List
Duplicates_list = ["a", "b", "c", "a", "c"]
print(Duplicates_list)

# List Items - Data Types
# String, int and boolean data types
str_list = ["a", "b", "c"]
int_list = [1, 5, 7, 9, 3]
bool_list = [True, False, False]
print(str_list, int_list, bool_list)

# A list can contain different data types
# A list with strings, integers and boolean values
Complex_list = ["abc", 34, True, 40, "male"]
print(Complex_list)

# Python's perspective, lists are defined as objects with the data type 'list':type()
# What is the data type of a list?
List_Data_Type = ["a", "b", "c"]
print(type(List_Data_Type))

# List Length
Lenth_list = ["a", "b", "c"]
print(len(Lenth_list))

# Define The list() Constructor
Constructor_list = list(("a", "b", "c")) 
print(Constructor_list)

# Access List Items
# List items are indexed and you can access them by referring to the index number
# Print the second item of the list
indexed_list = ["a", "b", "c"]
print(indexed_list[1])

# Negative Indexing
# Negative indexing means start from the end
# -1 refers to the last item, -2 refers to the second last item etc
Negative_list = ["a", "b", "c"]
print(Negative_list[-1])

# Range of Indexes
# Return the third, fourth, and fifth item
# The search will start at index 2 (included) and end at index 5 (not included).
Range_list = ["a", "b", "c", "o", "k", "m", "m"]
print(Range_list[2:5])

# Change Item Value
# To change the value of a specific item, refer to the index number
# Change the second item
change_list = ["a", "b", "c"]
change_list[1] = "z"
print(change_list)

# Change a Range of Item Values
# Change the values "b" and "c" with the values "blackcurrant" and "watermelon"
Val_item_list = ["a", "b", "c", "o", "k", "m"]
Val_item_list[1:3] = ["x", "w"]
print(Val_item_list)

# Change the second and third value by replacing it with one value
Custom_list = ["a", "b", "c"]
Custom_list[1:3] = ["w"]
print(Custom_list)

# Insert Items
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.
# The insert() method inserts an item at the specified index
# Insert "watermelon" as the third item
insert_list = ["a", "b", "c"]
insert_list.insert(2, "w")
print(insert_list)

# Append Items
# To add an item to the end of the list, use the append() method
Append_list = ["a", "b", "c"]
Append_list.append("o")
print(Append_list)

# The insert() method inserts an item at the specified index
# Insert an item as the second position
insert_list = ["a", "b", "c"]
insert_list.insert(1, "o")
print(insert_list)

# Extend List
# To append elements from another list to the current list, use the extend() method
# Add the elements of 'elements_list' to 'Extend_list'
Extend_list = ["a", "b", "c"]
elements_list = ["m", "p", "q"]
Extend_list.extend(elements_list)
print(Extend_list)

# Add Any Iterable
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.
# Add elements of a tuple to a list
Ex_Tupl_list = ["a", "b", "c"]
thistuple = ("k", "o")
Ex_Tupl_list.extend(thistuple)
print(Ex_Tupl_list)

# Remove Specified Item
# The remove() method removes the specified item
# Remove "b"
Remove_list = ["a", "b", "c"]
Remove_list.remove("b")
print(Remove_list)

# Remove Specified Index
# The pop() method removes the specified index
# If you do not specify the index, the pop() method removes the last item
# Remove the second item:
Specified_list = ["a", "b", "c"]
Specified_list.pop(1)
print(Specified_list)

# The del keyword also removes the specified index
removes_list = ["a", "b", "c"]
del removes_list[0]
print(removes_list)

# The del keyword can also delete the list completely
delete_list = ["a", "b", "c"]
del delete_list

# Clear the List
# The clear() method empties the list.
# The list still remains, but it has no content

clear_list = ["a", "b", "c"]
clear_list.clear()
print(clear_list)

# Loop Through a List
# You can loop through the list items by using a for loop
loop_list = ["a", "b", "c"]
for x in loop_list:
  print(x)

# Loop Through the Index Numbers
# You can also loop through the list items by referring to their index number.
# Use the range() and len() functions to create a suitable iterable.
# Print all items by referring to their index number:
Through_list = ["a", "b", "c"]
for i in range(len(Through_list)):
  print(Through_list[i])

# Print all items, using a while loop to go through all the index numbers
while_list = ["a", "b", "c"]
i = 0
while i < len(while_list):
  print(while_list[i])
  i +=  1
#   i = i + 1

# A short hand for loop that will print all items in a list
Short_list = ["a", "b", "c"]
[print(x) for x in Short_list]

# List Comprehension
# Based on a list of later, you want a new list, containing only the later with the letter "a" in the name.
# Without list comprehension you will have to write a for statement with a conditional test inside
later = ["a", "b", "c", "k", "m"]
new_list = []
for x in later:
  if "a" in x:
    new_list.append(x)
print('Result of List Comprehension: ', (new_list))

# With list comprehension you can do all that with only one line of code
later_list = ["a", "b", "c", "k", "m"]
new__list = [x for x in later_list if "a" in x]
print('Result of List Comprehension is one line : ', (new__list))

# The condition is like a filter that only accepts the items that valuate to True
# Only accept items that are not "apple"
later__list = ["a", "b", "c", "k", "m"]
neww_list = [x for x in later__list if x != "a"]
print('Result of List Comprehension is True : ', (neww_list))

# The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all fruits except "apple".
# With no if statement
condition_list = ["a", "b", "c", "k", "m"]
condition_new_list = [x for x in condition_list]
print('Result of Conditional List of Comprehension : ', (condition_new_list))

# You can use the range() function to create an iterable
new_range_list = [x for x in range(10)]
print('Result of range function : ', (new_range_list))

# Same example, but with a condition
# Accept only numbers lower than 5
new_condition_list = [x for x in range(10) if x < 5]
print('Result of list with condition : ', (new_condition_list))

# Set the values in the new list to upper case
upper_case_list = ["a", "b", "c", "k", "m"]
new_upper_case_list = [x.upper() for x in upper_case_list]
print('Result of list with upper case : ', (new_upper_case_list))

# You can set the outcome to whatever you like
# Set all values in the new list to 'hello'
val__list = ["a", "b", "c", "k", "m"]
n_list = ['hello' for x in val__list]
print('Set all values in the new list : ', (n_list))

# Return "o" instead of "b"
instead_list = ["a", "b", "c", "k", "m"]
new_instead_list = [x if x != "b" else "o" for x in instead_list]
print('Return "o" instead of "b" : ', (new_instead_list))

# Sort List Alphanumerically
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default
# Sort the list alphabetically
ascending_list = ["orange", "mango", "kiwi", "pineapple", "banana"]
ascending_list.sort()
print('Alphanumerically sorted by Ascending : ', (ascending_list))

# Sort the list numerically
numeric_list = [100, 50, 65, 82, 23]
numeric_list.sort()
print('Result of numerically sorted List : ', (numeric_list))

# To sort descending, use the keyword argument reverse = True
# Sort the list descending alphabetically
descending_list = ["orange", "mango", "kiwi", "pineapple", "banana"]
descending_list.sort(reverse = True)
print('Result of descending orderd List : ', (descending_list))

# Sort the list descending numerically
descending_numerically_list = [100, 50, 65, 82, 23]
descending_numerically_list.sort(reverse = True)
print('Result of numerically descending orderd List : ', (descending_numerically_list))

""" Customize Sort Function
You can also customize your own function by using the keyword argument key = function.
The function will return a number that will be used to sort the list (the lowest number first) """
# Sort the list based on how close the number is to 50
def myfunc(n):
  return abs(n - 50)
close_number_list = [100, 50, 65, 82, 23]
close_number_list.sort(key = myfunc)
print('Result of based on how close the number is to 50 : ', (close_number_list))

# Case Insensitive Sort
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters
# Case sensitive sorting can give an unexpected result
Case_Insensitive_list = ["banana", "Orange", "Kiwi", "cherry"]
Case_Insensitive_list.sort()
print('Result of Case Insensitive Sort : ', (Case_Insensitive_list))

# if you want a case-insensitive sort function, use str.lower as a key function
# Perform a case-insensitive sort of the list
ins_list = ["banana", "Orange", "Kiwi", "cherry"]
ins_list.sort(key = str.lower)
print('Result of Case Insensitive Sort using str.lower funtion : ', (ins_list))

# Reverse the order of the list items
Reverse_order_list = ["banana", "Orange", "Kiwi", "cherry"]
Reverse_order_list.reverse()
print('Reverse the order of the list items : ', (Reverse_order_list))

# Make a copy of a list with the copy() method
copy_method_list = ["apple", "banana", "cherry"]
my__list = copy_method_list.copy()
print('Result of List using copy() method : ', (my__list))

# Another way to make a copy is to use the built-in method list()
# Make a copy of a list with the list() method
Another_list = ["apple", "banana", "cherry"]
list_my_list = list(Another_list)
print('Result of List using list() method : ', (list_my_list))

# Join Two Lists
# There are several ways to join, or concatenate, two or more lists in Python.
# One of the easiest ways are by using the + operator.
list011 = ["a", "b", "c"]
list022 = [1, 2, 3]

list033 = list011 + list022
print('Result of Join Two Lists : ', (list033))

# Another way to join two lists is by appending all the items from list2 into list1, one by one
# Append list2 into list1
list100 = ["a", "b" , "c"]
list200 = [1, 2, 3]
for x in list200:
  list100.append(x)
print('Result of Another way to Join Two Lists : ', (list100))

# you can use the extend() method, which purpose is to add elements from one list to another list
# Use the extend() method to add list2 at the end of list1
extend_method_list1 = ["a", "b" , "c"]
extend_method_list2 = [1, 2, 3]

extend_method_list1.extend(extend_method_list2)
print('Result of Join Two Lists using extend() method : ', (extend_method_list1))
