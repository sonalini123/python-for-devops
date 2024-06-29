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

