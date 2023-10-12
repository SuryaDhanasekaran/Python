def print_hist(h):
    for c in h:
        print(c,h[c])
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
h = histogram('parrot')

for key in sorted(h):
    print(key,h[key])
# print_hist(h)