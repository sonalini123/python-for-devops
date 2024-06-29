
n = int(input("enter any number: "))
number_list = list(range(n))
for i in range(0,n):
  print(i*i)  # Output: [0, 1, 2]
  
# Given a year, determine whether it is a leap year

def is_leap_year(year):
  if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0 ):
    return True
  else:
        return False
year = int(input("enter year: "))
print(is_leap_year(year))       

#Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
#Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

student_marks = []
n = int(input("enter the number of students: "))

for _ in range(n):
  name = input()
  marks = int(input())
  student_marks.append([name, marks])
  sorted_student_marks = sorted(student_marks, key=lambda x: x[1], reverse=True)
  lowest_marks_student = sorted_student_marks[-1]
  print(student_marks[0])
  
