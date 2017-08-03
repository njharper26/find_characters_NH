lst1 = ['hello','boo', 'world','my','name','is','Anna']
str1 = 'o'
lst2 = []

# for i in range(0, (len(lst1) -1)):
for x in lst1:
    for y in x:
        if y == str1:
            lst2.append(x)

for i in range(0, (len(lst2) - 1)):
    if lst2[i] == lst2[i - 1]:
        lst2.pop(i)

print lst2
 