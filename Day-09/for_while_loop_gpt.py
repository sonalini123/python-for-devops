"""
fruits = ["apple","banana","cherry"]
for a in fruits:
    print(a)
"""
"""
#while loop
count = 0
while count <= 5:
  print(count)
  count += 1   
"""
"""
# Break example
numbers = [1,2,3,4,5]
for i in numbers:
    if i == 3:
         break
    print(i)
    """
"""
# continue 
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number == 3:
        continue
    print(number)
    """

# Log file analysis
log_file = [
   "INFO: Operation successful",
   "ERROR: File not found",
   "DEBUG: Connection established",
   "ERROR: Database connection failed",
]
for i in log_file:
        # Check if the line starts with "ERROR"
        if i.startswith("ERROR"):
            print(i, end='')  # Print the line if it starts with "ERROR"
