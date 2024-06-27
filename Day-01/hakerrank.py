
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
