
import random
for i in range(5):
    value=random.randint(1,6)
    print(value)

#if you only need certain functions from a module.
from math import pi
print(pi)

#You can import a module or object under a different name using the as keyword.
from math import sqrt as sqareroot
print(sqareroot(4))