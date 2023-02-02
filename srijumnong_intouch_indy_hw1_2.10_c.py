#worked with JT and Emma
import numpy as np
Z=int(input("Z = "))
a1=15.67
a2=17.23
a3=0.75
a4=93.2
Alist=np.arange(Z,3*Z,1)
maxA=0 #A for the highest energy
bestA=0 #best_suitable_A
x=0
for x in range(len(Alist)):
  A=Alist[x]
  if A%2!=0:
    a5=0
  elif A%2==0 and Z%2==0:
    a5=12.0
  elif A%2==0 and Z%2!=0:
    a5=-12.0
  B=(a1*A)-(a2*((A)**(2/3)))-(a3*((Z**2)/(A**(1/3))))-(a4*(((A-(2*Z))**2)/A))+(a5/(A)**(1/2))
  if((B/A)>maxA):
    maxA=B/A
    bestA=A
  x=x+1
print("The most stable nucleus with the given atomic number of",Z,"is",bestA,
      "and the value of the binding energy per nucleon is",maxA)


