import numpy as np
from scipy.optimize import leastsq
import matplotlib.pyplot as plt
import random

filename = input("Please input your points' file name: ");
print ("File name is: ", filename)
file = open(filename, "r");
xcoords = []
ycoords = []
for line in file:
    print(line, end='')
    lst = line.split()
    xcoords.append(float(lst[0]))
    ycoords.append(float(lst[1]))
file.close();

print("\n\nData preparing...");
print(len(xcoords), 'points listed:\n')

i=0
while i < len(xcoords):
    print(xcoords[i], " ", ycoords[i])
    i = i+1
    
#X=np.linspace(0,10,50)
#k0=random.random()
#b0=random.random()
#Y=k0*X+b0+np.random.randn(50)

XCoords = np.array(xcoords)
YCoords = np.array(ycoords)

#%% Optimize
 
def residuals(p,x,y, infor):
    print(infor);
    a,b=p
    return y-(a*x+b)
    
infor = "Iteration..."   
initAB = [1,0] 
r=leastsq(residuals,initAB,args=(XCoords, YCoords, infor))
#%% Test
a,b=r[0]

XMinMax = []
XMinMax.append(min(XCoords))
XMinMax.append(max(XCoords));
XMinMax[0] = XMinMax[0] - 0.2;
XMinMax[1] = XMinMax[1] + 0.2;
YMinMax = a*np.array(XMinMax) + b

#plt.plot(X,Y,X,Yy)
plt.title("Least Square Method: Fit 2D Line");
plt.plot(XCoords, YCoords, 'ro', XMinMax, YMinMax)
plt.axis([-1, 1, -1, 1])
str = "y = a*x+b,  a= {0}, b={1}".format(a,b);
plt.xlabel(str);
plt.show()
