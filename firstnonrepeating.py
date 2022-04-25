# Input: s = "loveleetcode"
# Output: 2




def nonreapeating(string):
    x={}
    for i in string:
        if i not in x:
            x[i]=1
        else:
            x[i]+=1
    for j in range(len(string)):
        if x[string[j]]==1:
            return string[j],":",j
    return -1
print(nonreapeating(input("enter: ")))
     


















# def first(s):
#       d = {}
#       for i in s:
#          if i not in d:
#             d[i] = 1
#          else:
#             d[i] +=1
#       for i in range(len(s)):
#          if d[s[i]] == 1:
#             return s[i],":",i
#       return -1
# print(first(input("enter:")))


