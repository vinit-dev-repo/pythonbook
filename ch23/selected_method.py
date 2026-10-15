# selected_method.py
class CompactView:
    def heading(self):
        return "compact " + self.label

    def footer(self):
        return "short footer"

class DetailedView:
    def heading(self):
        return "detailed " + self.label

    def footer(self):
        return "long footer"

class SelectedView(CompactView, DetailedView):
    heading = DetailedView.heading

    def __init__(self, label):
        self.label = label

view = SelectedView("notes")
print(view.heading())
print(view.footer())
saved_function = SelectedView.heading
DetailedView.heading = lambda self: "replacement " + self.label
print(view.heading())
print(saved_function is SelectedView.heading)
