city = "São Paulo"
print(city.encode("utf-8"))
print(city.encode("iso8859-1"))

try:
    city.encode("cp437")
except UnicodeEncodeError as e:
    print(e)

print(city.encode("cp437", errors="ignore"))
print(city.encode("cp437", errors="replace"))
print(city.encode("cp437", errors="xmlcharrefreplace"))
