from math import * 
print('Введите Xbeg, Xend и Dx')
Xbeg = float(input('Xbeg=')) 
Xend = float(input('Xend=')) 
dx = float(input('Dx=')) 
print("Xbeg={0: 7.2f} Xend={1: 7.2f}".format(Xbeg, Xend)) 
print(" Dx={0: 7.2f}".format(dx)) 
Xt = Xbeg 
print("+--------+--------+") 
print("I    X   I   Y    I") 
print("+--------+--------+") 
while Xt <= Xend:
    if Xt >= -10 and Xt < -6: y= -2 + sqrt(4-(Xt+8)**2)
    elif Xt >= -6 and Xt < 2: y = 0.5*Xt + 1
    elif Xt >= 2 and Xt < 6: y = 0
    elif Xt >= 6 and Xt <= 8: y=(Xt-6)**2
    print("I{0: 7.2f} I{1: 7.2f} I".format(Xt, y)) 
    Xt += dx 
print("+--------+--------+")
