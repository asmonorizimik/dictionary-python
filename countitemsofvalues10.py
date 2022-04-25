# 10count the items of values
# dict1 =  {
#    'Alex': ['subj1', 'subj2', 'subj3'], 
#    'David': ['subj1', 'subj2']}
# c=0
# for i in dict1:
#     for j in dict1[i]:
#         c+=1
# print("count total=",c)




##list = ["1","1","2","1","5","0","5","2","7"]
list="manori_awungshi_zimik"
x={}
# for i in list:
#     x[i]=list.count(i)
# print(x)
for i in list:
    if i in x:
        x[i]+=1
    else:
        x[i]=1
print(x)
    


