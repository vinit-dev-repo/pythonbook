# failed_sequence_store.py
def attempt(in_place):
    tasks = ["scan"]
    record = ("batch", tasks)
    try:
        if in_place:
            record[1] += ["check"]
        else:
            record[1] = record[1] + ["check"]
    except TypeError:
        print("store rejected")
    print(tasks, record[1] is tasks)

attempt(True)
attempt(False)
