import cmath

signal = complex(2, 5)
print(signal + 3)
print(signal * 1j)
print(signal.conjugate())
print(cmath.sqrt(-16))
try:
    print(signal < 3)
except TypeError:
    print("complex numbers have no ordering")
