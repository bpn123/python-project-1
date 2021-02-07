#Python program which accepts the radius of a circle from the user and computs area.

import math
r = float(input("Input the radius of the circle: "))
ar = math.pi* r * r
print("The area of the circle with radius %.2f"%r)
print("is: %f"%ar)
