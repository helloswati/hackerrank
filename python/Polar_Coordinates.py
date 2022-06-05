Polar coordinates are an alternative way of representing Cartesian coordinates or Complex Numbers.
A complex number z [Capture.PNG] 
    z = x + yj

# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath
n = input()
print(abs(complex(n)))
print(cmath.phase(complex(n)))
