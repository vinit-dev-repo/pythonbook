temps = np.array([18, 25, 31, 15, 40, 22])

is_hot = temps > 25
print(is_hot)
print(temps[is_hot])       # only the values where the mask is True
print(temps[temps > 25])   # the same thing, written in one line
