letters = ["p", "q", "r", "s"]
request = slice(None, None, -1)
start, stop, step = request.indices(len(letters))
print((start, stop, step))
print([letters[index] for index in range(start, stop, step)])
print(letters[start:stop:step])
