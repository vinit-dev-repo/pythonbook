async def greet():
    print("hello from inside the coroutine")
    return "done"

result = greet()             # nothing printed yet!
print(type(result))
result.close()              # close this unstarted inspection example
