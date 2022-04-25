a={'one':1,'two':2,'three':3,'four':4,'five':5}
for i in a:
    x=a.get(i)
    print(i,x)


# D = {'name': 'Bob', 'age': 25, 'job': 'Manager'}
# print(D.get('job', 'Developer'))##output==>manager..coz second arg is default

# get():Return the value for key if key is in the dictionary, else default.
