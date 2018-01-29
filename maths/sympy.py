"""
Intro
"""
import sympy as smp

smp.init_printing()  # Init pretty print as default
x = smp.symbols('x')


"""
Equations
"""
smp.solve([x + 5*y - 2, -3*x + 6*y - 15], [x, y])

"""
Integration
"""
smp.integrate(x ** 2 + x + 1, x)  # Give the primitive
smp.integrate(x ** 2 + x + 1, (x, 0, 1))  # Give the value of the integral

"""
Matrix
Ref: http://docs.sympy.org/latest/modules/matrices/matrices.html
"""

n = 3
print("Identity matrix")
I3 = smp.eye(n)  # Identity
I3 = I3.inv()  # Inverse: I3^-1
smp.pprint(I3)
print(I3.det())  # Determinant
print()
print()

print("Zeros matrix")
M = smp.zeros(2, 3)  # Matrix of all zeros
smp.pprint(M)
M = smp.zeros(n)
print()
print()

print("Ones matrix")
M = smp.ones(1, 2)  # Matrix of all zeros
smp.pprint(M)
M = smp.ones(n)
print(M[1, 2])
print()
print()

print("Reduction ")
M = smp.Matrix([[1, 1], [1, 1]])
P, D = M.diagonalize()
print(M == P * D * P.inv())
smp.pprint(M)
p = M.charpoly(x)  # Characteristic polynomials using variable x
print()
print()

"""
Polynomials
"""
smp.pprint(p.factor())
