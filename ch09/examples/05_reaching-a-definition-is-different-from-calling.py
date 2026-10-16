compact_labels = True
print("choosing a formatter")
if compact_labels:
    def render_label(code):
        print("inside compact formatter")
        return "[" + code + "]"
else:
    def render_label(code):
        return "Item: " + code

saved_formatter = render_label
print("formatter selected")
print(saved_formatter("K7"))
