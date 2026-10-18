old_counter = counter
del sys.modules["counter"]
import counter    # creates and runs the module again
print(old_counter is counter)
