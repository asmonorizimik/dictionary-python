d1 = {}
d2 = {}
for i in range(2):
  key = input("enter key")
  val = input("enter value")
  d1.update({key: val})
for i in range(2):
  key = input("enter 2nd key")
  val = input("enter 2nd value")
  d2.update({key: val})
d1.update(d2)
print("\nThe New Dictionary is:")
print(d1)