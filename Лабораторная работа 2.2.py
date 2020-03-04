flag = 1
import math
while flag > 0:
  flag = 1
  R = float (input("Enter radius: " ))
  x = float (input("Enter variable X: "))
  y = float (input("Enter variable Y: "))
  if (x >= -2 and x <= 2 and y >= -2 and y <= 2):
    if ((x+R)**2 + (y-R)**2 > R  and (x-R)**2 + (y+R)**2 > R):
      print ("Congratulations!!!")
      flag = 3
    else:
      print ("You lose!")
      flag = 2
  if flag < 3:
    print ("You lose!")