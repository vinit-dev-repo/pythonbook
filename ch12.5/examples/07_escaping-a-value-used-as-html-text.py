from html import escape

def render_html_text(template):
    out = []
    for part in template:
        if isinstance(part, str):
            out.append(part)                     # your own text: pass it through
        else:
            out.append(escape(str(part.value)))  # someone else's value: ESCAPE it
    return "".join(out)

comment = "<script>steal_cookies()</script>"

print("f-string :", f"<p>{comment}</p>")
print("t-string :", render_html_text(t"<p>{comment}</p>"))
