# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# d = dict.fromkeys(keys)
# for i, k in enumerate(d.keys()):
# 	d[k] = values[i]
# print(d)





# sampleDict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }
# minV = min(sampleDict.values())
# for v,k in sampleDict.items():
#   if  minV== k:
#     print(v)
#     break


# details={'Name': 'RAM','Age': 17, 'student': {'id': 22,'place': 'dharamsala'}} 
# details['student']['id']=35
# print(details)











# print("Enter the String: ", end="")
# s = input()
# s = bytes(s, "utf-8")
# print(list(s))





# str = "codescracker dot com"
# x = bytearray(str, "utf-8")
# print(x)
# del x[12:]
# print(x)
# x[12:] = b".com"
# print(x)



# y={'carl':40,'alan':2,'bob':1,'danny':3}                                      
# l=list(y.items())   
# l.sort()            
# print('Ascending order is',l) 
# l=list(y.items())
# l.sort(reverse=True) 
# print('Descending order is',l)
# dict=dict(l)
# print("Dictionary",dict)





# squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# # remove a particular item, returns its value
# # Output: 16
# print(squares.pop(4))
# # Output: {1: 1, 2: 4, 3: 9, 5: 25}
# print(squares)
# # remove an arbitrary item, return (key,value)
# # Output: (5, 25)
# print(squares.popitem())
# # Output: {1: 1, 2: 4, 3: 9}
# print(squares)
# # remove all items
# squares.clear()
# # Output: {}
# print(squares)
# # delete the dictionary itself
# del squares
# # Throws Error
# print(squares)



# odd_squares = {x: x*x for x in range(11) if x % 2 != 0}
# print(odd_squares)


# list=["a","b","a","a","c","d","e","b","c"]
# i=0
# s=""
# while i<len(list):
#     if list[i]!=list[i-1]:
#         s+=list[i]
#     i+=1
# print(s)





# list=["1","1","2","1","5","0","5","2","7"] 
# i=0
# a=[ ]
# while i<len(list):
#     j=0
#     count=0
#     b=[ ]
#     while j<len(list):
#         if list[i]==list[j]:
#             count=count+1
#         j=j+1
#     b.append(list[i])
#     b.append(count)
#     if b not in a:
#         a.append(b)
#     i=i+1
# print(dict(a))




list=input("enter:")
x={}
for i in list:
    x[i]=list.count(i)
print(x)


# for i in list:
#     if i in x:
#         x[i]+=1
#     else:
#         x[i]=1
# print(x)
    