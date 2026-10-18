def fresh_constructor(cls):
    def build(*args, **kwargs):
        return cls(*args, **kwargs)

    return build

class DraftNote:
    def __init__(self, text):
        self.text = text

OriginalDraftNote = DraftNote
DraftNote = fresh_constructor(DraftNote)
draft_one = DraftNote("one")
draft_two = DraftNote("two")
print("fresh constructor:", type(draft_one) is OriginalDraftNote, draft_one is draft_two)
