"""
import sys
number = sys.argv[1]
print(number)
"""
"""
number = input("provide any number: ")
print(number)
"""
# program to print the list of files in a folder  
import os
folder_names = input("provide folder names: ").split()
for i in folder_names:
   try:  
     files = os.listdir(i)
   except FileNotFoundError:
    print("provide valid folder name: " + i )
    break
   except PermissionError:
    print("no access to this folder:" + i )
    break
   print("====listing files for the folder " + i)
   for file in files:
      print(file)
