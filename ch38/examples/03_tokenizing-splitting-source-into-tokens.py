import tokenize
import io

source = "total = price * 3\n"
for tok in tokenize.generate_tokens(io.StringIO(source).readline):
    print(tok)
