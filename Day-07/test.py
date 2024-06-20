imp sys

instance_type = srv.argv[1]
if instance_type == 't2.micro':
  print("done")
elseif instance_type == 't3.large':
  print("4 dollars charge")
elseif instance_type == 't3.medium':
  print("10 dollar charge")
else:
  print("unknown instance")
