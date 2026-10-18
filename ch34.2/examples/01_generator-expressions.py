squares_list = [x * x for x in range(5)]        # built immediately, all 5 values
squares_gen = (x * x for x in range(5))          # iterator created; no squares produced yet

print(squares_list)
print(squares_gen)              # shows the generator object, not values
print(list(squares_gen))         # NOW it runs, producing all 5 values
