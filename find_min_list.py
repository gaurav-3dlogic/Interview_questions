nums = [4,5,1,2,3,45,7,8]

#For maximum element in list 
max1 = nums[0]

for ele in nums:
    if ele > max1:
        max1 = ele
print("The Maximum element is: ",max1)


#For minimum element in list 
min1 = nums[0]

for ele in nums:
    if ele < min1:
        min1 = ele
print("The Minimum element is: ",min1)






#Time complexity of this program is O(n^2)

#Space complexity of this program is O(1)