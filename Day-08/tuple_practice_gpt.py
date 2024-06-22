"""
# 1 Create a tuple containing the numbers 1, 2, and 3.
my_tuple = (1,2,3)
print(my_tuple)
"""
"""
#2 Print the second element of the tuple.
my_tuple = (1,2,3)
print(my_tuple[1])
"""
"""
# 3 Unpack the tuple into three variables and print them.
my_tuple = (1,2,3)
a,b,c = my_tuple
print(a,b,c)
"""
"""
# 4 Create a nested tuple containing two tuples: (1, 2, 3) and (4, 5, 6).
my_tuple = (1,2,3)
nested_tuple = ((1,2,3),(4,5,6))
print(nested_tuple)
"""
"""
# 5 Concatenate two tuples (1, 2) and (3, 4).
tuple1 = (1,2)
tuple2 = (3,4)
new_tuple = tuple1 + tuple2
print(new_tuple)
"""
"""
# 6 Try to change the first element of a tuple and observe what happens.
try:
    my_tuple = (1,2)
    my_tuple[0] = 10
except TypeError as e:
    print(e)
"""
"""
# 7 Create a tuple (1, 2, 2, 3, 4, 2) and find the count of the number 2 and the index of the first occurrence of the number 3.
my_tuple = (1, 2, 2, 3, 4, 2)
print(my_tuple.count(2))
print(my_tuple.index(3))
"""
"""
# 8 Convert the list [1, 2, 3, 4, 5] to a tuple.
my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
print(my_tuple)
"""
# 9 Create a tuple containing an integer, a string, and a list. Access and print each element.

my_tuple = (1,"home",[2,3,4])
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[2])
