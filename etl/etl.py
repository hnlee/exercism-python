def transform(old):
    new = dict((k.lower(), i) for k in j
               for i, j in old.iteritems())
    return new
