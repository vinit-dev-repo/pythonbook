list_answer = sum([i * i for i in range(1000)])
generator_answer = sum(i * i for i in range(1000))
assert list_answer == generator_answer == 332833500
print("both give the expected answer:", list_answer == generator_answer)
