import copy

class ReviewDraft:
    def __init__(self, notes):
        self.notes = list(notes)

draft = ReviewDraft(["check title"])
shallow = copy.copy(draft)
deep = copy.deepcopy(draft)
draft.notes.append("check links")
print(shallow is draft, shallow.notes is draft.notes)
print(shallow.notes)
print(deep.notes)
