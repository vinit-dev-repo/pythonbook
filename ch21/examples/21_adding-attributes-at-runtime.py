class Note:
    def __init__(self):
        self.title = "first"
        self.tags = ["python"]

note = Note()
live = vars(note)
snapshot = dict(vars(note))
note.title = "second"
note.tags.append("objects")
print(live["title"], snapshot["title"])
print(snapshot["tags"])
