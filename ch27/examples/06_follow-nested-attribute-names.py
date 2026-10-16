from collections import namedtuple
from operator import attrgetter

Location = namedtuple("Location", "aisle slot")
Pick = namedtuple("Pick", "label location")
pick = Pick("spares", Location("C", 4))
read_pick = attrgetter("label", "location.aisle")
print(read_pick(pick))
print(read_pick(pick._replace(location=Location("A", 2))))
print(pick.location.aisle)
