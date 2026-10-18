scores = [85]
inner = (scores,)
outer = (inner,)
scores.append(90)
print(outer)
print(outer[0] is inner, inner[0] is scores)
