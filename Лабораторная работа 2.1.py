flag = 1
while flag == 1:
  x = float (input("Enter variable X: "))
  import math as np
  if (x >= -9 and x < -5 ):
    y = 2 - np.sqrt(4 - ((x + 7)**2))
  elif (x >= -5 and x < -4 ):
    y = x*0 + 2
  elif (x >= -4 and x < 0 ):
    y = -0.5*x
  elif (x >= 0 and x < np.pi ):
    y = np.sin(x)
  elif (x >= np.pi ):
    y = x - np.pi
  print (y)