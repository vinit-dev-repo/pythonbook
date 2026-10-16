from display_records import InheritedClient

item = InheritedClient("Noor", 1)
item.region = "south"
print(item)

class NamesOnly(InheritedClient):
    def gathered_fields(self):
        return [("name", self.name)]

brief = NamesOnly("Noor", 1)
brief.region = "south"
print(brief)
print("stored region:", brief.region)
