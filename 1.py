from math import *
x = float(input('Введите значение x=')) 
if x >= -10 and x < -6: y= -2 + sqrt(4-(x+8)**2)
elif x >= -6 and x < 2: y = 0.5*x + 1
elif x >= 2 and x < 6: y = 0
elif x >= 6 and x <= 8: y=(x-6)**2
print("X={0:.2f} Y={1:.2f}".format(x, y))
