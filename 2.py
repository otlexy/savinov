from math import * 
flag = 0 
print('Введите координаты X и Y для точки:') 
x = float(input('X=')) 
y = float(input('Y='))
r = float(input('R=')) 
if (abs(x) < r) or (abs(x) > r): 
    flag = 0
if (x <= sqrt(r**2 - y**2) and abs(y) <= r and x>=0
    or y>=x and abs(x)<=r and x<0 and y<=r and y>0 and y>=abs(x)
    or y<=-x and abs(x)<=r and x<0 and abs(y)<=r and y<0 and y<=x): 
    flag = 1 	
else: 
    flag = 0 
print("Точка X={0: 6.2f} Y={1: 6.2f}" .format(x, y), end=" ") 
if flag==1: 
    print("попадает", end=" ") 
else: 
    print("не попадает", end=" ") 
print("в область.")
