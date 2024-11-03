import os
from colorama import Fore, Back, Style, init

init()

os.system("clear")
os.system("pkg install figlet")
os.system("figlet Xtool")

print(Fore.BLUE +"enjoy using! \n")
print(Fore.YELLOW +"Choices: \n")

print(Fore.RED +"[1]: ", Fore.BLUE +"Calculator")
print(Fore.RED +"[2]: ", Fore.BLUE +"Install Cmatrix")
print(Fore.RED +"[3]: ", Fore.BLUE +"Cctv IP's")

choice = input(Fore.YELLOW +"Choice: ")

if choice == '1':
	cal = input(Fore.CYAN +"Chooce Operation ,+,: ")
	if cal == '+':
		a = int(input("Enter num1: "))
		b = int(input("enter num2: "))
		c = a+b
		print (Fore.GREEN + f"{a} + {b} is {c}"+ Style.BRIGHT)

elif choice == '2':
	os.system("pkg install cmatrix")
	
	ask = input("do you wanna run cmatrix? y/n: ")
	if ask == 'y':
		os.system("cmatrix")
	if ask == 'n':
		print ("okay, thank you for using!")
		
elif choice =='3':
	print(Fore.WHITE +"Paste the ip below in google: \n")
	print(Fore.RED +"http://198.244.125.230:8083\n")
	
else:
	print("EROR: invalid or no input")