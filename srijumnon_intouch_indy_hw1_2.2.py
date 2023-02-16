T=float(input("T in seconds = "))
G=6.67E-11
M=5.97E24
R=6371000
Pi=3.1416
h=((G*M*(T**2)/(4*(Pi**2)))**(1/3))-R
print("Altitude in meters =",h)

