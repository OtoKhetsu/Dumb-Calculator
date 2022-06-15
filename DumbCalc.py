from colorama import init
init()
from colorama import Fore,Back
print(Back.YELLOW)
print(Fore.BLACK)
#Dumb Calc By Khetsuriani Otari
a = float(input("First Num : "))
b = float(input("Second Num : "))
#Which operator
print("+  -  plus ") 
print("-  -  minus")
print("*  -  multiply")
print("/  -  divide")
oper = input("What operator want you to use?")
if oper == "+":
    print(a + b)
elif oper == "-":
    print(a - b)
elif oper == "*":
    print(a * b)
elif oper == "/":
    print(a / b)
else :
    print(f"What the hell is this ? {oper} You dont know? Im DUMB i know only this four options !")
    print("+  -  plus ") 
    print("-  -  minus")
    print("*  -  multiply")
    print("/  -  divide")