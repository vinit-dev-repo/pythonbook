group_a = frozenset({"amy", "ben"})
group_b = frozenset({"cara", "dan"})
print(sorted(group_a), sorted(group_b))       # sorted() shows the members in a fixed order

set_of_groups = {group_a, group_b}            # a SET of sets — needs frozensets inside
print(len(set_of_groups))                     # both frozensets fit inside a set
print(group_a in set_of_groups)               # a frozenset can be looked up like anything else

meeting_notes = {group_a: "Monday 10am"}      # a frozenset as a dict KEY
print(meeting_notes[group_a])                 # look it up the normal way, instead of printing the whole dict
