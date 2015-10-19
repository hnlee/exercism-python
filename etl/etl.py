def transform(old):
    new = {}
    for i in old:
        for j in old[i]:
            new[j.lower()] = i
    return new
