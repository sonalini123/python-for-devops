my_dict = {}
n = int(input("enter the number of entries: "))
for _ in range (n):
    name = input("enter the name: ")
    marks = int(input("enter the marks: "))
    my_dict [name] = marks
    print(my_dict)
key_to_print = input("enter the key you want to print: ")

if key_to_print in my_dict:
    print(key_to_print)
else:
        print("key value not present in my_dict")
