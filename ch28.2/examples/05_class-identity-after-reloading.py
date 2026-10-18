import shape
c = shape.Circle()

import importlib
importlib.reload(shape)

print(isinstance(c, shape.Circle))
