# Python Lists

# mylist = ['apple', 'banana', 'cherry']

# print(type(mylist))

# List items are ordered, changeable and allow duplicate values

# List items are indexed, the first term has index [0], the second term has index [1] etc.



# Ordered

# When we say that lists are ordered, it means that the items have defined order, and that order will not change

# If you add new lists to a list, the new items will be placed at the end of the list.

# Data types of list

# Srting

# list = ["Python", "is", "easy"]

# Int

# list = [1, 2, 3]

# Boolean

# list = [True, False, False]

# A list can contain different data types

# list = ['a', 1, 44, 'python', True]



# Access list items

# List items are indexed and you can access them by referring to the index number

# Example

# Print the second item of the list:

# thislist = ['apple', 'banana', 'cherry']
#print(thislist[1])

# The first item has index 0

#Negative indexing

#Negative indexing means starts from the end

# -1 refers to the last one and -2 refers to the second last item etc

# Example

# Print the last item of the list

# thislist = ["apple", "banana", "cherry"]
# print(thislist[-1])


# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.

# When specifying a range, the return value will be a new list with the specified items.

# Example
# Return the third, fourth, and fifth item:

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])

# Example
# This example returns the items from the beginning to, but NOT including, "kiwi":

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:4])

# Example
# This example returns the items from "cherry" to the end:

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:])

# Range of Negative Indexes
# Specify negative indexes if you want to start the search from the end of the list:

# Example
# This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])



# Check if item exists

# To determine if a specified item is present in a list use the 'in' keyword

# Example

# Check if "apple" is present in the list

# thislist = ["apple", "banana", "cherry"]

# if "apple" in thislist:
#     print("Yes, 'apple' is in the list") 


# Change the list items

# thislist = ['apple', 'cherry', 'banana']
# thislist[1] = 'Jhingalala_hurhur'
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)

# Add list item

# thislist.append(whatever)

# Insert

# thislist.insert(position)

# Extend list

a = [1,2,3,4,5]
b = [6,7,8,9]

a.extend(b)
print(a)