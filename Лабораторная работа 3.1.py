import math as np

x = float(input("Введите начальное значение Х: "))
x2 = float(input("Введите конечное значение Х: "))
step = float(input("Шаг: " ))
 
if x > x2:
	x, x2 = x2, x
 
print("Таблица значений")
print("   x        y")
while x <= x2:
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
	print('%5.2f | %7.2f' % (x, y))
	x += step


input()