flag = 1
while flag == 1:
    a=input ("Enter variable A: ")
    import math
    z_1 = (math.sin(2 * a) + math.sin(5 * a) - math.sin(3 * a))/(math.cos(a) + 1 - 2 * (math.sin(2 * a)) * (math.sin(2 * a)))
    z_2 = 2*math.sin(a)
    print (z_1)
    print (z_2)