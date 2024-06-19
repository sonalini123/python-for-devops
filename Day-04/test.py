import sys
def addition(num1,num2):
  x = num1+num2
  return x

def sub(num1,num2):
  y = num1+num2
  return y

num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation =="addition":
  output = addition(num1,num2)
  print(output)

