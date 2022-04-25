# 7.list and unique values
# a=[
# {"first":"1"}, 
# {"second": "2"}, 
# {"third": "1"}, 
# {"four": "5"}, 
# {"five":"5"}, 
# {"six":"9"},
# {"seven":"7"}
# ]
# a=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# b=[]
# for i in a:
#     for j in i.values():
#         if j not in b:
#             b.append(j)
# print(b)




dict = {1:'manory',2:'onring',3:'ningthemla',4:'onring',5:'manory'}
list =[]
for val in dict.values(): 
  if val  not in list: 
#     continue 
#   else:
    list.append(val)

print (list)