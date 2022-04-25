# 6remove duplicate keys
dic={
"ball":"red",
"bat":4,
"wickets":8,
"ball":"green",
"bat":3,
"bat":7
}
print(dic)

result = {}
for key,value in dic.items():
    if value not in result.values():
        result[key] = value
print(result)
