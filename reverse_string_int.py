#first apporach
#time - o(n)
#space - o(1)

# string = input("Enter string on int string: ")


# string_1 = ""



# for i in string:
#     string_1 = i + string_1
# print(string_1)

#approch 2
#Time and space same as first
# string = input("Enter string on int string: ")


# string_1 = ""

# a = len(string) - 1

# while(a >= 0):
#     string_1 += string[a] 
#     a -= 1
# print(string_1)



# Apporch third

string = input("Enter string on int string: ")
for i in range(len(string)-1,-1,-1):
    print(string[i],end = "")
  
    
