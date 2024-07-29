###-----------------------------------------------------------loops
# 1. for (Starting , stop (+ 1), jump)
# 2. while 
#Task can be achived by 'for' loop can also be achived by 'while'loop but Vice versa not possible (cases can be different)
# Note "do while " loop is not used in python

# for var in range(10):
#      print(var)

# company = "RADA enter price"
# name = ['sumit','sorab','ronak','rada']
# marks = (99,98,97,96,95)

# for char in company:
#     print(char)
# for nam in name:
#     print(char)
# for num in marks:
#     print(char)

# dtr = {'a':10,'b':20,'c':30}

# for key in dtr:
#     print(key)
# for value in dtr.values():
#     print(value)

#to find the position 
# items = [2,4,6,8,10,12,14,16,18,20]
# count = 0
# for i in items:
#     if i == 10:
#         print(count)
#     count =count+1

# for item in range(11):
#     if item==5:
#         break            #Break ignore all the occure conditions
#     print(item)

# for item in range(11):
#     if item==5:
#         continue             #continue only ignore the current condition
#     print(item)

# count = 0
# for i in range(10):
   
#     count+=1
#     break
# print(count)

# count = 0
# for i in range(10):
   
#     count+=1
#     continue
# print(count)

## 2.--------------------------------------------------while loop-

# inl = 0
# while inl <=100:
#     print('Oniii chhannn..',inl)
#     inl+=1


###-------------------------------------------------Functions ()-
# # 1.define (one time)
# 2.calling (multiple times)

# functions are following types
# 1. >> pre-define (in-built , built-in)
# Eg. print()/input()/append()/length()/type()...etc

# 2. >> user define 

# num = int(input("Enter any number USER !! : "))

# def div(nu):
#     if num%2==0 :
#         print("EVEN")
#     else:
#         print("ODD")
    
# div(num)

##-------print "*" by using loop 

# def pyramid(n):
#     for i in range(1,n + 1):
#         for j in range(1, i + 1):
#             print("* ", end="")
#         print("")

# n= int(input("Enter a number : "))
# pyramid(n)

##--------print "123.." by using loop 
# total_rows = int (input("Enter any num : "))

# for row in range(1,total_rows +1):
#     for symbol in range(1, row +1):
#         print("{0} ".format(symbol), end="")
#     print(" ")