print(eval("2 ** 10"))

source = "answer = 6 * 7"
namespace = {}
exec(source, namespace)
print(namespace["answer"])
