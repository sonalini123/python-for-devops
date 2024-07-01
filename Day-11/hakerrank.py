#The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.Example
#The query_name is 'beta'. beta's average score is .
my_dict = {}
n = int(input("enter the number of entries: "))
for _ in range (n):
    name, *line = input().split()
    scores = list(map(float, line))
    my_dict [name] = scores
    print(my_dict)
key_to_print = input("enter the key you want to print the average for: ")
if key_to_print in my_dict:
    average_marks = sum(scores) / len(scores)
    print(f"average of marks for '{key_to_print}' is: ", average_marks)
else:
        print("key value not present in my_dict")

#Students of District College have a subscription to English and French newspapers. Some students have subscribed to only the English newspaper, some have subscribed to only the French newspaper, and some have subscribed to both newspapers.

#You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to only English newspapers.

Eng_no = int(input("enter the number of students who have subscribed to Eng newspaper: "))
Eng_sub = set(map(int,input().split()))

Frn_no = int(input("enter the number of students who have subscribed to Frn newspaper: "))
Frn_sub = set(map(int,input().split()))

difference_EngFrn = Eng_sub.difference(Frn_sub)
#difference_FrnEng_operator = set_Frn - set_Eng

print("no of students subscribed for Eng newspaper: ", (len(difference_EngFrn)))
#print("Difference (set_Frn - set_Eng) using - operator:", difference_FrnEng_operator)

#You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to either the English or the French newspaper but not both.
Eng_sub = int(input("enter the number of students subscribed to English newspaper: "))
Eng_sub_roll_nos = set(map(int,input().split()))

Frn_sub = int(input("enter the number of students subscribed to Frn newspaper: "))
Frn_sub_roll_nos = set(map(int,input().split()))

symm_diff = Eng_sub_roll_nos ^ Frn_sub_roll_nos
print(len(symm_diff))


#You are given a set A  and N number of other sets. These N number of sets have to perform some specific mutation operations on set A.

#Your task is to execute those operations and print the sum of elements from set A.
N = int(input("enter the number of elements you want to have: "))
A = set(list(map(int,input().split())))
no_of_operations = int(input("enter the number of operations you want to perform: "))
for _ in range(no_of_operations):
    operation, No_of_elements_in_B = input().split()
    B = set(list(map(int,input().split())))
    if operation == 'intersection_update':
        A.intersection_update(B)
    elif operation == 'update':
        A.update(B)
    elif operation == 'symmetric_difference_update':
        A.symmetric_difference_update(B)
    elif operation == 'difference_update':
        A.difference_update(B) 
    A = list(A)      
    total = sum(A)
    print(total)    
