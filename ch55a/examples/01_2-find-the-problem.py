def process(data, flag1=False, flag2=False, flag3=False, verbose=False):
    result = []
    for d in data:
        if flag1:
            d = d.strip()
        if flag2:
            d = d.lower()
        if flag3:
            d = d.replace(" ", "_")
        if verbose:
            print("processed", d)
        result.append(d)
    return result
