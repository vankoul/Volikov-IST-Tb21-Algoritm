import math
from colorama import Fore
from colorama import Back
from colorama import Style
from colorama import init

init(autoreset=True)

flag = 1

shoot = 1

R = float (input("Enter radius: " ))

print("У вас есть десять выстрелов!")

while shoot <= 10:

    flag = 1

    print("Выстрел " + str(shoot))
  
    x = float (input("Enter variable X: "))
    y = float (input("Enter variable Y: "))
  
    if (x >= -2 and x <= 2 and y >= -2 and y <= 2):
      if ((x+R)**2 + (y-R)**2 > R  and (x-R)**2 + (y+R)**2 > R):
        print (Fore.GREEN + "Попадание!")
        flag = 3
      else:
        flag = 2
        print (Fore.RED + "Вы промахнулись!")
    if flag < 3:
      print (Fore.RED + "Вы промахнулись!")

    shoot = shoot + 1

print("Патроны кончились")

input()