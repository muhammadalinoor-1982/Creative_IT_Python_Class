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

# "List" if need to access of list index then it's start from "0"
# "List" if need to access of list index from revers direction then it's start from "-1"
list = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 96, 93]
list [0] = 200
print(list [0])
print(list [-2])

MixList = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 96, 93, 'hello', 2.5]
print(MixList)

# Multidimentional List
NestedList = [100, 99, 98, 97, 96, 95, 94, [79, 89, [11, 22, 33], 45], 93, 92, 91, 90, 96, 93, 'hello', 2.5]
print(NestedList[7][2][1])

#Need to Add new value in the last index of the list
AppendList = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 96, 93]
AppendList.append(212)
print(AppendList)

#How to Insert value in the specific index of the List
SpecificList = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 96, 93]
SpecificList.insert(3, 212)
print(SpecificList)

#How to Extend the List
ExtendList = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 96, 93]
#ExtendList = ExtendList + [1, 11, 111]
ExtendList.extend([1, 11, 111])
print(ExtendList)

#How to Remove List Element
RemoveELEList = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 96, 93]
RemoveELEList.remove(93)
print(RemoveELEList)

#How to Remove List Index Element
IndexELEList = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 96, 93]
IndexELEList.remove(list[3])
print(IndexELEList)

#How to Remove Last Element of the List
LastELEList = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 96, 93]
LastELEList.pop()
print(LastELEList)

#How to Sort Element by assending order of the List
SortELEList = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 96, 93]
SortELEList.sort()
print(SortELEList)

#How to Sort Element by Alphabetic order of the List
Alphabetic = ['N', 'B', 'H', 'P', 'C', 'K', 'W', 'D', 'Y', 'D', 'Z', 'Q', 'M']
Alphabetic.sort()
print(Alphabetic)

#How to Find Element of List Index
IndexELEofList = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 96, 93]
print(IndexELEofList.index(94))

#How Many Specific Element of List
CountELEofList = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 96, 93]
print(CountELEofList.count(93))



