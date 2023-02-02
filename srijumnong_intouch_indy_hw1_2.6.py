#worked with JT
from math import pi

l1=float(input("Enter the distance l1 of the closest approach that to the Sun (perihelion) in meters"))
v1=float(input("Enter velocity at perihelion v1 in meters/seconds"))
G=6.6738E-11
M=1.9891E30

#solve for b, c in ax^2+bx+c
a=1
b=-2*G*M/(v1*l1)
c=-(v1**2-2*G*M/l1)
d=b*b-4*a*c
root1=(-b-d**(1/2))/2
root2=(-b+d**(1/2))/2

#Kepler's Law
v2=min([root1,root2])
l2=l1*v1/v2
a=(l1+l2)/2
b=(l1*l2)**(1/2)
T=(2*pi*a*b)/(l1*v1)
e=(l2-l1)/(l2+l1)

print("l2 in m = ", l2)
print("v2 in m/s = ", v2)
print("T in s = ", T)
print("e = ", e)

print("Semi major axis is", a/149597870700, "AU")
print("Semi minor axis is", b/149597870700, "AU")
print("Orbital period is ", T/(24*60*60)/365, "years")
print("Orbital eccentricity is", e)