'''
9 Advanced Lists in Python
- Accessing and manipulating list elements using indexing and slicing
- Understand and apply advanced list slicing techniques
- Differentiate between shallow and deep copies of lists
=======
- Access and manipulating list elements using indexing and slicing
- Understnand and apply advanced list slicing techniques
- differentiate between shallow and deep copies of list
- Multi-dimensional arrays
'''


'''
9.1 Index and Negative Indexing
- Lists in Python can be accessed using index numbers. Negative indexing allows access to elements from
the end of the list
=======
9.1 Index and Negative indexing
- Lists in python can be accessed using index numbers. Negative indexing allows access to elements from
    the end of the list
'''
# Example 9.1
# Create a list containing the first ten squares
squares = [1,4,9,16,25,36,49,64,81,100]

'''
9.2 Advanced List Slicing
- List slicing allows you to use syntax 'list[start:end]'
'''
# Example 9.2.1
# Extract elements from a list that have been indexes using the stride size argument
print(squares[::2])
# Example 9.2.2
# Use negative indexing stride size argument
=======
9.2 Advanced LIst Slicing
- LIst slicing allows you to use sytanx 'list[start:end]'
'''
# Example 9.2 
# Extract elements from a list that have been indexes using the stride size argument
print(squares[::2])
# Example 9.2.2
# use negative incexing stride size argument
print(squares[::-2])
# Example 9.2.3
# Extract elements at a defined set or known as a subset
print(squares[4:8:2])
=======

# Example 9.2.4
# Extract elements with even indexes from the 5th element
print(squares[4::2])

'''
9.3 Advanced List Assignment
- List can be modified by assigning values to slices of the list
'''
# Example 9.3.1
my_numbers = [1,3,6,10,15,21,28,36,45,55]
print(f"My list of number (first 10 triangle numbers): {my_numbers}")

# Substituing a subset of the list with new elements
my_numbers[1:3] = [4,9]
print(f"My list of numbers (substitutions): {my_numbers}")

# Example 9.3.2
# Replace every nth element with a new value where N = 3
my_numbers[::3] = [1,16,49,100]
print(f"My list of numbers (n-th replacements): {my_numbers}")

# Example 9.3.3
# Replace and resize a subset of the list
my_numbers[4:] = [25,36,49,64]
print(f"My list of numbers (first 8 squares numbers): {my_numbers}")

# Example 9.3.4
# Delete every nth number starting from the 2nd element
del my_numbers[1::2]
print(f"My list of numbers (every other sqaure number): {my_numbers}")
=======
#Example 9.3.1
my_numbers = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
print(f'My list of numbers (first 10 triangle numbers): {my_numbers}')

# Substituting a subset of the list with new elements
my_numbers[1:3] = [4, 9]
print(f'My list of numbers (substitutions): {my_numbers}')

# Example 9.3.2
# Replace every nth element with a new value where N = 3
my_numbers[::3] = [1, 16, 49, 100]
print(f'My list of numbers (n-th replacements): {my_numbers}')

# Example 9.3.3
# Replace and resize a subset of the list
my_numbers[4:] = [25, 36, 49, 64]
print(f'My list of numbers (first 8 square numbers): {my_numbers}')

# Example 9.3.4
# delete every nth number starting frmo the 2nd element
del my_numbers[1::2]
print(f'My list of numbers (every other square number): {my_numbers}')

'''
9.4 Shallow and Deep List Copies
- Shallow copies duplicate the structure of a list but not the elements of the list
- Deep copies duplicate both the structure and list elements
'''
# 9.4.1 Create a shallow copy of the original list using slicing notation
my_phrases = [['a','b','c'], ['d','e','f'], ['g','h','i']]
print(f'Original list of phrases: {my_phrases}')

my_shallow_phrases = my_phrases[:2] + [['j','k','l']]
print(f"Shallow copy of my phrases: {my_shallow_phrases}")

# Example 9.4.2 Create a shallow copy using the list() function
my_other_shallow_phrases = list(my_phrases) + [['j','k','l']]
print(f"Another shallow copy of my phrases: {my_other_shallow_phrases}")

# Example 9.4.3 Make a change to the original list of phrases
my_phrases[0][0] = "ALPHA"
my_phrases[0][1] = "BETA"
my_phrases[0][2] = "GAMMA"
print(f"\nUpdated original list of phrases: {my_phrases}")
print(f"Shallow copy of my phrases: {my_shallow_phrases}")
print(f"Another shallow copy of my phrases {my_other_shallow_phrases}")

# Example 9.4.4 Create a deep copy of the original list
import copy

my_phrases = [['a','b','c'], ['d','e','f'], ['g','h','i']]
my_deep_phrases = copy.deepcopy(my_phrases)
print(f"Original list of phrases: {my_phrases}")
print(f"Deep copy of my phrases: {my_deep_phrases}")

my_phrases[0][0] = "ALPHA"
my_phrases[0][1] = "BETA"
my_phrases[0][2] = "GAMMA"
print(f"\nUpdated original list of phrases: {my_phrases}")
print(f"Deep copy of my phrases: {my_deep_phrases}")

'''
9.5 Iterating List
- Lists can be iterated through using while loops, for loops and enumarate function.
'''
# Example 9.5.1
my_diatomic_list = [0,1,1,2,1,3,2,3,1,4,3,5,2,5,3,4]
i = 0
while i < len(my_diatomic_list):
    print(f"Diatomic Sequence - Element #{i+1}: {my_diatomic_list[i]}")
    i+=1

# Example 9.5.2 Iterate the list using a for loop
for x in range(len(my_diatomic_list)):
    print(f"Diatomic Sequence - Element #{x+1}: {my_diatomic_list[x]}")

# Example 9.5.3 Iterate the list using a for loop with the 'in' operator
=======
- Deep copies duplcate both the structure and list elements.
'''
# 9.4.1 Create a shallow copy of  the original list using slicing notation
my_phrases = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
print(f'Original list of phrases: {my_phrases}')

my_shallow_phrases = my_phrases[:2] + [['j', 'k', 'l']]
print(f'Shallow copy of my phrases: {my_shallow_phrases}')

# Example 9.4.2 Create a shallow copyt using the list() function
my_other_shallow_phrases = list(my_phrases) + [['j', 'k', 'l']]
print(f'Another shallow copy of my phrases: {my_other_shallow_phrases}')

# Example 9.4.3 Make a change to the originla list of phrases
my_phrases[0][0] = 'ALPHA'
my_phrases[0][1] = 'BETA'
my_phrases[0][2] = 'GAMMA'
print(f'\nUpdated original list of phrases: {my_phrases}')

print(f'Shallow copy of my phrases: {my_shallow_phrases}')
print(f'Another shallow copy of my phrases: {my_other_shallow_phrases}')

# Example 9.4.4 Create a deep copy of the orginal list
import copy

my_phrases = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
my_deep_phrases = copy.deepcopy(my_phrases)
print(f'Original list of phrases: {my_phrases}')
print(f'Deep copy of my phrases: {my_deep_phrases}')

my_phrases[0][0] = 'ALPHA'
my_phrases[0][1] = 'BETA'
my_phrases[0][2] = 'GAMMA'
print(f'\nUpdated original list of phrases: {my_phrases}')

print(f'Deep copy of my phrases: {my_deep_phrases}')

'''
9.5 Iterating List
- Lists can be iterated through using while loops, forr loops and the enumarate function.
'''
# Example 9.5.1
my_diatomic_list = [0, 1, 1, 2, 1, 3, 2, 3, 1, 4, 3, 5, 2, 5, 3, 4]
i = 0
while i < len(my_diatomic_list):
    print(f'Diatomic Sequence - Element #{i + 1}: {my_diatomic_list[i]}')
    i += 1

# Example 9.5.2 Iterate the list using a for loop
for x in range(len(my_diatomic_list)):
    print(f'Diatomic Sequence - Element #{x + 1}: {my_diatomic_list[x]}')

# Example 9.5.3  Iterate the list using a for loop with the 'in' operator
for elem in my_diatomic_list:
    print(elem)
# Example 9.5.4 Iterate the list using the enumerate function
for idx, elem in enumerate(my_diatomic_list):
    print(f"Diatomic Sequence - Element #{idx + 1}: {elem}")


'''
9.6 List Membership
- List membership can be tested using the 'in' and 'not in' operators.
'''
# 9.6.1 Test whether an element exists in a list
squares = [1,4,9,16,25]
=======
# 9.6.1 Test wheter an element exists in a list
squares = [1, 4, 9, 16, 25]
x = 16
if x in squares:
    print(f"{x} exists in our list of square numbers")
else:
    print(f"{x} does not exist in our list of square numbers")

# Example 9.6.2 Test whether an element is not in the list
=======
# Example 9.6.2 Test wheter an element is not in the list
y = 169
if y not in squares:
    print(f"{y} does not exist in our list of square numbers")
else:
    print(f"{y} exists in our list of square numbers")

'''
9.7 List Comprehension
- Create comprehension provides a concise way of creating lists
=======
- List comprehension provides a conscise way of creating lists
'''
# Example 9.7.1
squares = [num * num for num in range(1,9)]
print(squares)

# Example 9.7.2 Create a list formed of characters from a string
letters_in_abibliophobia = [character for character in "abibliophobia"]
=======
letters_in_abibliophobia = [character for character in 'abibliophobia']
print(letters_in_abibliophobia)

# Example 9.7.3
def isPrime(num):
    if num <= 1 or num%1 > 0:
        return False
    for i in range(2,num//2):
        if num%i == 0:
            return False
    return True

prime_numbers = [i for i in range(1,101) if isPrime(i)]
print(prime_numbers)

# Example 9.7.4
even_number_zeroed_odd = [i if i%2 == 0 else 0 for i in range(1,101)]
print(even_number_zeroed_odd)

'''
9.8 Multi-Dimensional Arrays
- List that contains other lists
'''
# Example 9.8.1 Create a two dimensional array
my_2d_array = [[1,2,3],[4,5,6],[7,8,9]]
=======
    if num <= 1 or num % 1 > 0:
        return False
    for i in range(2, num//2):
        if num % i == 0:
            return False
    return True

prime_numbers = [i for i in range(1, 101) if isPrime(i)]
print(prime_numbers)

# Example 9.7.4
even_numbers_zeroed_odd = [i if i % 2 == 0 else 0 for i in range(1, 101)]
print(even_numbers_zeroed_odd)

'''
9.8 Multi-Dimensonal Arrays
- LIst that contains other lists
'''
# Example 9.8.1 Create a two dimensional array
my_2d_array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in my_2d_array:
    for elem in row:
        print(elem, end=' ')
    print()
# Example 9.8.2 Create a two dimensional array with list comprehension
number_cols = 3
number_rows = 3
my_2d_array = [[0 for i in range(number_cols)] for j in range(number_rows)]
for row in my_2d_array:
    for elem in row:
        print(elem, end=" ")
    print()

# Example 9.8.3 Access elements using square brackets and indexes 
my_2d_array = [[1,2,3],[4,5,6],[7,8,9]]
=======
        print(elem, end=' ')
    print()

# Example 9.8.3 Access elements using square brackets and indices
my_2d_array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(my_2d_array[0][0])
print(my_2d_array[1][1])
print(my_2d_array[2][2])

# Example 9.8.4 Manipulate a two-dimensional array
my_2d_array = [[1,2,3],[4,5,6],[7,8,9]]

my_2d_array[1][1] = 0
my_2d_array.insert(2,[9,9,9])
my_2d_array.append([7,4,7])
my_2d_array[0].extend([0,0])
=======
my_2d_array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

my_2d_array[1][1] = 0
my_2d_array.insert(2, [9, 9, 9])
my_2d_array.append([7, 4, 7])
my_2d_array[0].extend([0, 0])
my_2d_array[2].reverse()
del my_2d_array[3]

for row in my_2d_array:
    for elem in row:
        print(elem, end= ' ')
    print()

=======
        print(elem, end=' ')
    print()
