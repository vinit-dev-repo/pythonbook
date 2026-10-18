import itertools

servers = itertools.cycle(["Ann", "Bo", "Cy"])
tables = [1, 2, 3, 4, 5]

for table in tables:
    print(f"Table {table} -> {next(servers)}")
