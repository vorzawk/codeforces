g = input()
vs = {'a', 'e', 'i', 'o', 'u', 'y'}
res = []
for l in g:
    if l.lower() not in vs:
        res.append('.' + l.lower())
print(''.join(res))

