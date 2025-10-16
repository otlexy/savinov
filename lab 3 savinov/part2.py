from math import * 
from random import * 
flag = 0
print("Введите радиус: ")
r=float(input())
print(" X       Y      Res") 
print("-------------------") 
for n in range(10): 
    x = uniform(-1, 4) 
    y = uniform(-1, 10) 
    if (r**2 - y**2 >= 0 and x <= sqrt(r**2 - y**2) and abs(y) <= r and x>=0
        or x < 0 and y <= r and y >= -x
        or x < 0 and abs(y) <= r and y <= x): 
        flag = 1 	
    else: 
        flag = 0
    print("{0: 7.2f} {1: 7.2f}".format(x, y), end=" ") 
    if flag: 
        print("Yes") 
    else: 
        print("No")
