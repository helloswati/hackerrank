Polar coordinates are an alternative way of representing Cartesian coordinates or Complex Numbers.
A complex number z [Capture.PNG] 
    z = x + yj
is completely determined by its real part x and imaginary part y.
Here, j is the imaginary unit.
A polar coordinate (r,p) 

# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath
n = input()
print(abs(complex(n)))
print(cmath.phase(complex(n)))

