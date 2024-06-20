import sys

instance_type = sys.argv[1]
if instance_type == 't2.micro':
  print("done")
elif instance_type == 't3.large':
  print("4 dollars charge")
elif instance_type == 't3.medium':
  print("10 dollar charge")
else:
  print("unknown instance")
