# Python Data Types Roadmap

# We'll cover these topics:

# Variables
# Numeric types (int, float, complex)
# Strings (str)
# Boolean (bool)
# Lists (list)
# Tuples (tuple)
# Sets (set)
# Dictionaries (dict)
# NoneType
# Type conversion
# Mutable vs immutable
# Practice exercises


# Variables
print("variables")
name = "Saikat"
age = 25
height = 5.8

print(name)
print(age)
print(height)

# Numeric types (int, float, complex)
print("Numeric types (int, float, complex)")
x = 10          # int
y = 3.14        # float
z = 2 + 3j      # complex
print(x)
print(y)
print(z)
print(type(z))
# Strings (str)
#sliceing
print("sliceing")
word = "Hello"

print(word[0])   # H
print(word[1])   # e
print(word[-1])  # o

text = "Programming"

print(text[0:6])
print(text[3:8])
print(text[:5])
print(text[5:])

print("Concatenation")
first = "Hello"
second = "World"

print(first + " " + second)

print("Repetition")
print("hi " * 3)


print("Useful methods")
name = "python programming"

print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())
print(name.replace("python", "Java"))
print(name.replace("p", "k"))

# Boolean (bool)
print("Boolean (bool)")

is_logged_in = True
is_admin = False

print(type(is_logged_in))


# Lists (list)

fruits = ["Apple", "Banana", "Orange"]

print(fruits)
print(fruits[0])
print(fruits[2])
fruits[2] = "saikat"
print(fruits[2])
fruits.append("Grapes")
print(fruits)
# Tuples (tuple)
numbers = (1, 2, 3, 4)

print(numbers[0])
# Sets (set)
nums = {1, 2, 3, 4, 4, 5}

print(nums)
nums.add(10)
nums.remove(3)
names = ["A", "A", "B", "C", "C"]

unique = set(names)

print(unique)

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union: Items in either set
print(set_a | set_b)  # Output: {1, 2, 3, 4, 5, 6}

# Intersection: Items in both sets
print(set_a & set_b)  # Output: {3, 4}

# Difference: Items in set_a but not in set_b
print(set_a - set_b)  # Output: {1, 2}

# Symmetric Difference: Items in one set or the other, but not both
print(set_a ^ set_b)  # Output: {1, 2, 5, 6}
# Dictionaries (dict)
student = {
    "name": "Saikat",
    "age": 25,
    "cgpa": 3.75
}

print(student)
print(student["name"])
print(student["age"])
student["age"] = 26
student["department"] = "CSE"
for key, value in student.items():
    print(key, value)
# NoneType

result = None

print(result)
print(type(result))
# Type conversion
# Mutable vs immutable
# Practice exercises
