import numpy as np
plain = np.arange(6)
print(np.shares_memory(plain, plain.reshape(2, 3)))
transposed = np.arange(6).reshape(3, 2).T
print(np.shares_memory(transposed, transposed.reshape(6)))
