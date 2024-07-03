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
    
#The tourists consist of:
#→ A Captain.
#→ An unknown group of families consisting of  members per group where  ≠ .

#The Captain was given a separate room, and the rest were given one room per group.

#Mr. Anant has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of the tourists. The room numbers will appear  times per group except for the Captain's room.

#Mr. Anant needs you to help him find the Captain's room number.
#The total number of tourists or the total number of groups of families is not known to you.
#You only know the value of  and the room number list.

#Input Format

#The first line consists of an integer, , the size of each group.
#The second line contains the unordered elements of the room number list.
room_number_list = list(map(int,input().split()))
count = Counter(room_number_list)
for key in count.keys():
  if count[key] == 1:
   print(key)


# You are given a set  and  other sets.
#Your job is to find whether set  is a strict superset of each of the  sets.
#Print True, if  is a strict superset of each of the  sets. Otherwise, print False.
#A strict superset has at least one element that does not exist in its subset.
A = set(map(int,input("enter the elements: ").split()))
n = int(input("enter the number of subsets: "))
is_strict_superset = True
for _ in range(n):
   subsets = set(map(int,input().split()))

   if not (A > subsets):
      is_strict_superset = False
      break
print(is_strict_superset)



