from numpy import *

a = random.rand(4,4)
print(a)
print(type(a))
randmat = mat(random.randint(4,4))
randmat_I = randmat.I
print(randmat)
print(randmat_I)
print(randmat * randmat_I)