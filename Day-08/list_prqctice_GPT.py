"""
my_list = [1,2,3,4,5,6,7,8,9,10]
print(my_list)
"""
"""
# print first and last element 
my_list = [1,2,3,4,5,6,7,8,9,10]
print(my_list[-1])
print(my_list[0])
"""
"""
#Print the first and last elements of the list.
my_list = [10,20,3,4,5,6,7,8,9,10]
sublist = my_list[0:2]
print(sublist)
"""
"""
#Append the number 11 to the list.
my_list = [1,2,3,4,5,6,7,8,9,10]
my_list.append(11)
print(my_list)
"""
"""
#4 Extend the list with another list [12, 13, 14]

my_list = [1,2,3,4,5,6,7,8,9,10]
my_list.append(11)
my_list.extend([12,13,14])
print(my_list)
"""
"""
# 5 Create a list of squares of numbers from 1 to 10 using list comprehension.
my_list = list(range(1,11))
squares = [x**2 for x in range(1,11)]
print(squares)
"""
"""
# 6 Remove the element 5 from the list.
my_list = list(range(1,11))
my_list.remove(5)
print(my_list)
"""
"""
# 7 Sort the list in descending order.
my_list = list(range(1,11))
my_list.sort(reverse=True)
print(my_list)
"""
"""
# 8 Print the length of the list.
my_list = list(range(1,11))
length = len(my_list)
print(length)
"""
"""
# 9 Calculate and print the sum of all elements in the list.
my_list = list(range(1,11))
print(sum(my_list))
"""
"""
# 10 Find and print the maximum value in the list.
my_list = list(range(1,11))
print(max(my_list))
"""
