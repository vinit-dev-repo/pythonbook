import math
import random
from statistics import NormalDist, StatisticsError, median

model = NormalDist(mu=40, sigma=3)
shared_state = random.getstate()
readings = model.samples(8, seed=71)
ordered = sorted(readings)
middle_pair_mean = (ordered[3] + ordered[4]) / 2
print('sample size:', len(readings))
print('sample median:', round(median(readings), 3))
print('median agrees:', median(readings) == middle_pair_mean)
print('same local seed:', readings == model.samples(8, seed=71))
print('shared stream unchanged:', random.getstate() == shared_state)
try:
    NormalDist(mu=40, sigma=-3)
except StatisticsError:
    print('negative spread rejected')

u = math.nextafter(1.0, 0.0)
print('below one:', u < 1.0, 'scaled:', 6 + 2 * u)
