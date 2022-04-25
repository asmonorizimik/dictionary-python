# 14.sort

# dict1={'bijender':45,'deepak':60,'param':20,'anjali':30,'roshini':50}
# sorted_values = sorted(dict1.values())
# sorted_dict = {}
# for i in sorted_values:
#     for k in dict1.keys():
#         if dict1[k] == i:
#             sorted_dict[k] = dict1[k]
#             break
# print("ascending: ",sorted_dict)






import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_d = sorted(d.items(), key=operator.itemgetter(1))
print('ascending : ',sorted_d)
sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
print('Descending: ',sorted_d)


