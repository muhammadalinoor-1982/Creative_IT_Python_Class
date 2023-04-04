""" Python Collections (Arrays)
There are four collection data types in the Python programming language:

*>> List is a collection which is ordered and changeable. Allows duplicate members.
*>> Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
*>> Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
*>> Dictionary is a collection which is ordered** and changeable. No duplicate members. """

# Dictionary in Python
# *>> Dictionary is a collection which is ordered** and changeable. No duplicate members.
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name
Symple_dict = {
  "name": "Aupu",
  "phone": "Samsang",
  "age": 19
}
print(Symple_dict)

# Duplicate values will overwrite existing values
Duplicate_dict = {
  "name": "Aupu",
  "phone": "Samsang",
  "age": 19,
  "age": 22
}
print(Duplicate_dict)

# String, int, boolean, and list data types
Data_type_dict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(Data_type_dict)

# Print the data type of a dictionary
type_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(type_dict))

# The dict() Constructor
# Using the dict() method to make a dictionary
Con_dict = dict(name = "John", age = 36, country = "Norway")
print(Con_dict)

# Access Dictionary Items
# You can access the items of a dictionary by referring to its key name, inside square brackets
Access_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = Access_dict["model"]
print(x)
# There is also a method called get() that will give you the same result
get_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = get_dict.get("model")
print(x)

# Get Keys
# The keys() method will return a list of all the keys in the dictionary
Keys_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = Keys_dict.keys()
print(x)

# Add a new item to the original dictionary, and see that the keys list gets updated as well
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change

# The values() method will return a list of all the values in the dictionary
values_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = values_dict.values()
print(x)

# Make a change in the original dictionary, and see that the values list gets updated as well
bus = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = bus.values()
print(x) #before the change
bus["year"] = 2020
print(x) #after the change

# Add a new item to the original dictionary, and see that the values list gets updated as well
trak = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = trak.values()
print(x) #before the change
trak["color"] = "red"
print(x) #after the change

# The items() method will return each item in a dictionary, as tuples in a list
items_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = items_dict.items()
print(x)

# Make a change in the original dictionary, and see that the items list gets updated as well
jeep = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = jeep.items()
print(x) #before the change
jeep["year"] = 2020
print(x) #after the change

# Add a new item to the original dictionary, and see that the items list gets updated as well
pajero = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = pajero.items()
print(x) #before the change
pajero["color"] = "red"
print(x) #after the change

# To determine if a specified key is present in a dictionary use the in keyword
Check_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in Check_dict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

#  Change Dictionary Items
# You can change the value of a specific item by referring to its key name
Change_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
Change_dict["year"] = 2018
print(Change_dict)

# Update Dictionary
# The update() method will update the dictionary with the items from the given argument.
# The argument must be a dictionary, or an iterable object with key:value pairs.
# Update the "year" of the car by using the update() method
update_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
update_dict.update({"year": 2020})
print(update_dict)

# Add Dictionary Items
# Adding an item to the dictionary is done by using a new index key and assigning a value to it
Add_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
Add_dict["color"] = "red"
print(Add_dict)

# Add a color item to the dictionary by using the update() method
update_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
update_dict.update({"color": "red"})
print(update_dict)

# The pop() method removes the item with the specified key name
Removee_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
Removee_dict.pop("model")
print(Removee_dict)

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead)
popitem_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
popitem_dict.popitem()
print(popitem_dict)

# The del keyword removes the item with the specified key name
Delete_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del Delete_dict["model"]
print(Delete_dict)

# The del keyword can also delete the dictionary completely
Full_Delete_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del Full_Delete_dict
# print(Full_Delete_dict)

# The clear() method empties the dictionary
clear_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
clear_dict.clear()
print(clear_dict)

# Print all key names in the dictionary, one by one
key_dict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in key_dict:
  print(x)

#   Print all values in the dictionary, one by one
values_dict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in values_dict:
  print(values_dict[x])

# You can also use the values() method to return values of a dictionary
method_Val_dict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in method_Val_dict.values():
  print(x)

# You can use the keys() method to return the keys of a dictionary
keys_val_dict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in keys_val_dict.keys():
  print(x)

# Loop through both keys and values, by using the items() method
method_key_val_dict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in method_key_val_dict.items():
  print(x, y)

# Make a copy of a dictionary with the copy() method
Copy_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
my_Copy_dict = Copy_dict.copy()
print(my_Copy_dict)

# Another way to make a copy is to use the built-in function dict()
# Make a copy of a dictionary with the dict() function
built_in_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
my_built_in_dict = dict(built_in_dict)
print(my_built_in_dict)

# Nested Dictionaries
# A dictionary can contain dictionaries, this is called nested dictionaries
# Create a dictionary that contain three dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)

# Create three dictionaries, then create one dictionary that will contain the other three dictionaries
child10 = {
  "name" : "Emil",
  "year" : 2004
}
child20 = {
  "name" : "Tobias",
  "year" : 2007
}
child30 = {
  "name" : "Linus",
  "year" : 2011
}

my_Child_family = {
  "child10" : child10,
  "child20" : child20,
  "child30" : child30
}

print(my_Child_family)

# To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary
my_family = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(my_family["child2"]["name"])

