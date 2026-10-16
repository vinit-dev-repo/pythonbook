import weakref

class Image:
    def __init__(self, name):
        self.name = name

# an ordinary dict keeps every value alive for as long as the dict lives
strong = {}
strong["logo"] = Image("logo")
del strong["logo"]                    # only removing it lets the Image go

# a WeakValueDictionary does not keep its values alive
cache = weakref.WeakValueDictionary()
picture = Image("logo")
cache["logo"] = picture
print("in the cache while something else holds it:", "logo" in cache)

del picture                           # now nothing else points at the Image
print("still in the cache once the last real reference goes:", "logo" in cache)
