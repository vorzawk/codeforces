N = int(input())
for _ in range(N):
    p = input()
    f = {'U': 0, 'D': 0, 'L': 0, 'R': 0}
    for l in p:
        f[l] += 1
    f['U'] =  f['D'] = min(f['U'], f['D'])
    f['R'] =  f['L'] = min(f['R'], f['L'])

    if f['U'] == 0:
        f['R'] = f['L'] = min(1, f['R'])
    if f['R'] == 0:
        f['U'] = f['D'] = min(1, f['U'])
    print(2 * f['U'] + 2 * f['R'])
    print('U' * f['U'] + 'R' * f['R'] + 'D' * f['D'] + 'L' * f['L'])
