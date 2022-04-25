# 8Take input of name and marks of 10 students and store to a dictionary.

# student=int(input("how many students"))
# a=[]
# b=[]
# for i in range(student):
#     user=input('enter name')
#     user2=int(input("enter marks"))
#     a.append(user)
#     b.append(user2)
# x=zip(a,b)
# print(dict(x))



d={}
i=0
a=[]
while i<=3:
    n=input("enter key")
    value=int(input("enter values"))
    a.append(value)
    d[n]=a
    i+=1
print(d)
