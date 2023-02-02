#worked with JT and Emma
import numpy as np
a1=15.67
a2=17.23
a3=0.75
a4=93.2
Zlist=np.arange(1,100,1)
#Alist=np.arange(Z, 3 * Z, 1)
maxA=0  # A for the highest energy
bestA=0  # best_suitable_A
bestZ=0
x=0
y=0
while (y<len(Zlist)):
    Z=Zlist[y]
    print(Z)
    Alist = np.arange(Z, 3 * Z, 1)
    for x in range(len(Alist)):
        A0=0 #reset every value of A to 0 for each loop
        A=Alist[x]
        if A % 2 != 0:
            a5 = 0
        elif A % 2 == 0 and Z % 2 == 0:
            a5 = 12.0
        elif A % 2 == 0 and Z % 2 != 0:
            a5 = -12.0
        B=(a1*A)-(a2*((A)**(2/3)))-(a3*((Z**2)/(A**(1/3))))-(a4*(((A-(2*Z))**2)/A))+(a5/(A)**(1/2))
        if ((B / A) > A0): #checking if B/A > A0, find the highest Z
            A0 = (B/A)
        if ((B/A) > maxA):
            maxA = (B/A)
            bestA = A
            bestZ = Z
        print("The most suitable A value is",A,",",A0)
        if (Z==28):
            print(" Z=28!, A=", A, "B/A=", (B/A))
        x = x + 1
    y = y + 1
print("The most stable nucleus is",bestA,"for the given Z value of",bestZ,
      "and the value of the binding energy per nucleon of", maxA)


