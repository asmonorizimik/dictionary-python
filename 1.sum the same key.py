# output=>{1: 10, 2: 60, 3: 30, 5: 50, 6: 60}

# dic1={1:10, 2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}
# for key in dic2:
#     if key in dic1:
#         dic2[key]=dic2[key]+dic1[key]

# d={**dic1,**dic2,**dic3}
# print(d)





# my_dict = {
#   'data1':100,
#   'data2': -54,
#   'data3': 247
#  }
# sum=0
# for i in my_dict:
#     sum=sum+my_dict[i]
# print(sum)



# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# ## Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
# for key in d2:
#     if key in d1:
#         d2[key] = d2[key] + d1[key]
# print(d2)




# d1 = {'a': 100, 'b': 200, 'c': 300}
# d2 = {'a': 300, 'b': 200, 'd': 400}
# for key, value in d1.items():
#     if key in d2:
#         d1[key] = value + d2[key]
#         del d2[key]
# # z={**d1,**d2}
# z=dict(d1,d2)
# print(z)


# import collections
# # print (collections.Counter("banana"))
# dict_1 = {'a': 100, 'b': 200, 'c': 300}
# dict_2 = {'a': 300, 'b': 200, 'd': 400}

# a_counter = collections.Counter(dict_1)
# b_counter = collections.Counter(dict_2)

# add_dict = a_counter + b_counter
# dict_3 = dict(add_dict)

# print(dict_3)