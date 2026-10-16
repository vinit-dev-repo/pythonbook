from decimal import getcontext

context = getcontext()
print(context.prec)          # current arithmetic precision, in significant digits
