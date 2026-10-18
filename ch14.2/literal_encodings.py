# literal_encodings.py
word = "ol\u00e9"
print(word == "ol\xE9" == "ol" + chr(233))
source_bytes = word.encode("latin-1")
print(source_bytes.hex())
converted = source_bytes.decode("latin-1").encode("utf-8")
print(converted.hex(), converted.decode("utf-8") == word)
print(str(source_bytes), str(source_bytes, "latin-1"))
print("AZ".encode("cp500").hex(), "AZ".encode("ascii").hex())
try:
    compile("b'" + chr(233) + "'", "<byte-literal>", "eval")
except SyntaxError:
    print("Non-ASCII byte literal rejected")
