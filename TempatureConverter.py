from colorama import Fore, Back, Style

temptype = input("What degrees is the temperature currently in? (F or C): ")
if temptype == "C":
    Celnum = input("You are now converting to Fahrenheit, what is the temperature in Celsius?: ")
    Truefar = float(Celnum) + 32 * 1.8
    print(Fore.YELLOW + str(Truefar) + str("°F"))

    if Truefar >= 212:
        print(Fore.RED + "You have passed the boiling point of water!")
    if Truefar <= 32:
        print(Fore.BLUE + "You have passed the freezing point of water!")

if temptype == "F":
    Farnum = input("You are now converting to Celsius, what is the temperature in Fahrenheit?: ")
    Truecel = float(Farnum) - 32 // 1.8
    print(Fore.YELLOW + str(Truecel) + str("°C"))

    if Truecel >= 100:
        print(Fore.RED + "You have passed the boiling point of water!")
    if Truecel <= 0:
        print(Fore.BLUE + "You have passed the freezing point of water!")
