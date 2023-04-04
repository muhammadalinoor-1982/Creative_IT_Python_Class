""" Python Collections (Arrays)
There are four collection data types in the Python programming language:

*>> tuple is a collection which is ordered and changeable. Allows duplicate members.
*>> Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
*>> Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
*>> Dictionary is a collection which is ordered** and changeable. No duplicate members. """

# Tuples in Python
# *>> Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Simple_tuple = ("a", "b", "c")
print(Simple_tuple)

# Duplicate values of Tuples
Duplicate_tuple = ("a", "b", "c", "a", "c")
print(Duplicate_tuple)

# Length of Tuple 
Duplicate_tuple = ("a", "b", "c", "a", "c")
print(len(Duplicate_tuple))

# Data Type of Tuple 
Duplicate_tuple = ("a", "b", "c", "a", "c")
print(type(Duplicate_tuple))

# Different Data Type of Tuple
# String, int and boolean data types
str_tuple = ["a", "b", "c"]
int_tuple = [1, 5, 7, 9, 3]
bool_tuple = [True, False, False]
print(str_tuple, int_tuple, bool_tuple)

# A tuple can contain different data types
# A tuple with strings, integers and boolean values
Complex_tuple = ["abc", 34, True, 40, "male"]
print(Complex_tuple)

# Define The tuple() Constructor
Constructor_tuple = tuple(("a", "b", "c")) 
print(Constructor_tuple)

# Access Tuple Items
# Print the second item in the tuple
Access_tuple = ("a", "b", "c")
print(Access_tuple[1])

# Negative Indexing
# -1 refers to the last item
# Print the last item of the tuple
Ngt_index_tuple = ("a", "b", "c")
print(Ngt_index_tuple[-1])

# Range of Indexes
# Return the third, fourth, and fifth item
Range_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(Range_tuple[2:5])

# This tuple returns the items from the beginning to, but NOT included, "kiwi"
Beginning_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(Beginning_tuple[:4])

# This tuple returns the items from "cherry" and to the end
End_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(End_tuple[2:])

# Range of Negative Indexes
# Specify negative indexes if you want to start the search from the end of the tuple
# This tuple returns the items from index -4 (included) to index -1 (excluded)
Negative_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(Negative_tuple[-4:-1])

# Check if Item Exists
# To determine if a specified item is present in a tuple use the in keyword
# Check if "apple" is present in the tuple
Exists_tuple = ("apple", "banana", "cherry")
if "apple" in Exists_tuple:
  print("Yes, 'apple' is in the fruits tuple")

# Update:Change Tuple Values
# Convert the tuple into a list to be able to change it
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# Add Items in a Tuple
# Convert the tuple into a list, add "orange", and convert it back into a tuple
Add_Item_tuple = ("apple", "banana", "cherry")
z = list(Add_Item_tuple)
z.append("orange")
Add_Item_tuple = tuple(z)
print(Add_Item_tuple)

# Create a new tuple with the value "orange", and add that tuple
Tuple_in_tuple = ("apple", "banana", "cherry")
A = ("orange",)
Tuple_in_tuple += A
print(Tuple_in_tuple)

# Remove Items
# Convert the tuple into a list, remove "apple", and convert it back into a tuple
Remove_Items_tuple = ("apple", "banana", "cherry")
B = list(Remove_Items_tuple)
B.remove("apple")
Remove_Items_tuple = tuple(B)
print(Remove_Items_tuple)

# Delete Items of Tuple
# The del keyword can delete the tuple completely
Delete_tuple = ("apple", "banana", "cherry")
del Delete_tuple
# print(Delete_tuple) #this will raise an error because the tuple no longer exists





