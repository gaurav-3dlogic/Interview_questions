a = [1,2,4,5,6,7]
b = [7,5,4,6,4,5]
c = []

for i in a:
    if i in b:
        c.append(i)
print(c)

# c = []
# for i in a:
#     if i not in b:
#         c.append(i)
# print(c)

