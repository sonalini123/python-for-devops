import sys
def add(num1,num2):
  add = num1+num2
  return add

def sub(num1,num2):
  y = num1+num2
  return y

num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation == "add":
  output = add(num1,num2)
  print(output)

