from string.templatelib import convert

def render(template):
    out = []
    for part in template:
        if isinstance(part, str):
            out.append(part)
        else:
            value = convert(part.value, part.conversion) if part.conversion else part.value
            out.append(format(value, part.format_spec))
    return "".join(out)

price = 12.3456
print(render(t"total: {price:.2f}"))
