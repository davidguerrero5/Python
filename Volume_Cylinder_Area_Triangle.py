#David Guerrero
#Volume of a cylinder and area of a triangle at the same time
import math
def cylinarea(p,r2,h1):
    return p * r2 * h1
def triarea(b, h2):
    return (b * h2)/2
r = float(raw_input("Enter radius of cylinder: ")) 
h1 = float(raw_input("Enter height of cylinder: ")) 
h2 = float(raw_input("Enter height of triangle: ")) 
b = float(raw_input("Enter base of triangle: "))
pi = math.pi 
rad = math.pow(r, 2)
areacyn = cylinarea(pi, rad, h1)
areatri = triarea(b,h2)
print "The volume of the cylinder is",areacyn, "and the area of the triangle is",areatri