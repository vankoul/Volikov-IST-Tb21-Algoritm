# -*- coding: utf-8 -*-
"""алгоритмы 2,2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/113kHmKTx0B6XRXdaU3LnM7JAnsjbfHu4
"""

flag = 1
import math
while flag > 0:
  flag = 1
  x = float (input("Enter variable X: "))
  y = float (input("Enter variable Y: "))
  if (x >= -2 and x <= 2 and y >= -2 and y <= 2):
    if ((x+2)**2 + (y-2)**2 > 1  and (x-2)**2 + (y+2)**2 > 1):
      print ("Congratulations!!!")
      flag = 3
    else:
      print ("You lose!")
      flag = 2
  if flag < 3:
    print ("You lose!")

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