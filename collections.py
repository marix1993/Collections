# Collections

# List

# Array - list
# First list - shopping list
# [] = list

# shopping_list = ["eggs", "bread", "milk", "chocolate", "jam"]
#
# print(shopping_list)
# print(type(shopping_list))
#
# # Accessing a particular part of the list
# print(shopping_list[0])  # Indexing starts at 0
#
# # change element in the list
# shopping_list[2] = "butter"  # changing second index
# print(shopping_list)
#
# # Using list methods
# # Append - adding at the end of the list
# shopping_list.append("fish")
# print(shopping_list)
# # Removing
# shopping_list.remove("butter")
# print(shopping_list)
# # Removing last item from the list
# shopping_list.pop()
# print(shopping_list)

# # Can I have a list with mix data types?
# mixture = [1, 2, 3, 4.5, "five", "six"]
# print(mixture)
#
# # Slicing
# print(mixture[1:3])
#
# # Reverse the order of the slice
# print(mixture[-2::])  # The last two index till end "five", "six"

# Step over
# print(mixture[::2])  # It's gonna step over every other second character

# Tuples ()()()() !!!
# Tuples are immutable (cannot be changed)

# tuple_example = ("bread", "eggs", "milk")
# print(tuple_example)
# tuple_example(0) = "cheese" # not doable
# print(tuple_example)

## Dictionaries - another way to manage data, but little bit more dynamic and complex {}{}{}{}
# Key values pairs
# Key as a reference to the object (name)
# Value as a data mechanism you wish to store data in (string, int, list)

student_1 = {
    "name": "luke",
    "stream": "DevOps",
    "completed_lessons": 4,
    "completed_lesson_names": ["variables", "data types", "set up"]
}

# # Access to dictionary
# print(student_1["stream"])
# # Access a part of the list in the dictionary
# print(student_1["completed_lesson_names"][0])
#
# # Change a value in dictionary
# student_1["completed_lessons"] = 3
# print(student_1)

# Changing an element of a list within a dictionary
student_1["completed_lesson_names"].remove("data types")
print(student_1["completed_lesson_names"])

# Dictionary methods
print(student_1.keys())
print(student_1.values())

## Sets and frozen sets
# set is python is a list that has no order
car_parks = {"wheels", "doors", "exhaust"}
print(car_parks)

car_parks.add("windows")
print(car_parks)

car_parks.discard("doors")
print(car_parks)

# # Frozen sets (immutable set) - we cannot change anything
# x = frozenset([1, 2, 3, 4, 5, 6])
# x.add(4)
# print(x)
