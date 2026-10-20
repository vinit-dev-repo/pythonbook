from functools import partial

class ActionBatch:
    def __init__(self, actions):
        self.actions = tuple(actions)

    def __call__(self):
        results = []
        for action in self.actions:
            results.append(action())
        return results

events = []

def record_event(kind, value):
    events.append((kind, value))
    return len(events)

actions = [partial(record_event, "checked", "K4"),
           partial(record_event, "stored", "K4")]
batch = ActionBatch(actions)
actions.clear()
print(events)
print(batch())
print(events)
print(ActionBatch([])())
