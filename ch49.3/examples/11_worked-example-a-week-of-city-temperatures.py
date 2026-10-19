import numpy as np

# rows: London, Tokyo, Nairobi   columns: Mon..Sun
temps = np.array([
    [12, 14, 11, 9,  10, 13, 15],   # London
    [22, 24, 23, 25, 26, 24, 21],   # Tokyo
    [18, 19, 17, 20, 21, 19, 18],   # Nairobi
])
cities = np.array(["London", "Tokyo", "Nairobi"])

# 1. hottest day per city -> collapse across columns (axis=1)
hottest_per_city = temps.max(axis=1)
print("Hottest day per city:", hottest_per_city)

# 2. mean temperature per city -> again axis=1
city_means = temps.mean(axis=1)
for city, mean in zip(cities, city_means):
    print(f"{city}: {mean:.1f} C average")

# 3. mask the freezing days (below 0) -- none here, so lower the bar to "cool" (<12)
cool_mask = temps < 12
print("Cool days mask:")
print(cool_mask)
print("Cool readings:", temps[cool_mask])
