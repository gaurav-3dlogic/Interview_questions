# 0 1 1 2 3 5 8 13 21 34

#Fibonacci series using recursion
#a = int(input("Enter a number: "))


# def fibo(a):
#     if a == 0:
#         return 0
#     elif a == 1:
#         return 1
#     else:
#         return fibo(a-1) + fibo(a-2)
# print(fibo(a))


#Second appropch using for loop
# a = int(input("Enter the Range aber: "))
# x,y = 0,1
# s = 0
# for n in range(0, a):
#     if(n <= 1):
#         s = n
        
#     else:
#         s = x + y
#         x = y
#         y = s
#     print(s)

#Third apporch uisng while loop

n = int(input("Enter the Range aber: "))

a = 0
b = 1
z = 0

while(n >= z):
   
    print(z)
    z = a + b
    a = b
    b = z
     