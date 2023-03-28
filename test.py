
b = [2,3,4,6,8,9,10]
n = 5

lower = 0
for i in b:
    if i < n:
        lower = i
        
upper = 0
for j in b:
    if j > n:
        upper = j
        break
    
        
        
        
print(lower)
print(upper)