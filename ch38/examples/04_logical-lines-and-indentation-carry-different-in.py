import io
import tokenize

source = "if True:\n    total = (-2 +\n             5)  # combine\nprint(total)\n"
selected = {tokenize.INDENT, tokenize.DEDENT, tokenize.NEWLINE,
            tokenize.NL, tokenize.COMMENT, tokenize.NUMBER}
for token in tokenize.generate_tokens(io.StringIO(source).readline):
    if token.type in selected or token.string == "-":
        print(tokenize.tok_name[token.type], repr(token.string))
