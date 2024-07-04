from collections import namedtuple
N = int(input("enter total number of students: "))
Student = namedtuple('Student',['ID','Marks','Name','Class'])
students = []
for i in range(N):
    print(f"enter the student info {i+1}:")
    ID = int(input())
    Marks = int(input())
    Name = input()
    Class = int(input())
student = Student(ID,Marks,Name,Class)
students.append(student)
total_marks = sum(student.Marks for student in students)
average = (total_marks)/N
print(f"average is {average}")

