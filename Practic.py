# 1.python is a CASE sensitive language we have to take care of using lowwer case & upper case 
# name ="rada since"
# age = "20"
# is_adult= True
# print("hello ")
# print(name)
# print(age)

# sname =input("what is your supper hero name=")
# print( sname)

# old_body = input("Enter your old body weight=\n")
# new_body = int(old_body) + 5
# print(new_body)

# sum of two numbers
# ===================================================================================================================
import tkinter
window = tkinter.Tk()
window.title("Rada")
window.mainloop()

# fst = input("Enter the first no.=\n")
# scd = input("Enter the second no.=\n")

# sum = int(fst) + int(scd)
# print(f"the sum of two no. is {str(sum)}")

# ======================================================================================================================
# strings
# name =  "spidder man"
# print(name.upper())
# print(name.find('man'))
# print(name.replace("spidder man","pitter parker"))
# print('m'in name)

# ===========================================================================================================================

# Arithmatic operaters
# print(5+2)
# print(5-2)
# print(5*2)
# print(5/2)
# # to remove the decimal
# print(5//2)
# print(5%2)
# # /power
# print(5**2)
# # same conditional operators
# print(5>2)
# # same logical operators
# print(5>2 or 2>5)
# print(5>2 and 5>4)
# print(not 5>4)

# if - else statements
first = input("Enter the first no. :")
operater = input("Enter the operator (+,-,*,/)::")
second = input("Enter the second no. :")

first =int(first)
second =int(second)
if operater=='+':
     print(first+second)

elif operater=='-':
     print(first - second)

elif operater=='*':
     print(first * second) 
     
elif operater=='/':
     print(first / second)

else:
     print("Enter the valide no.")