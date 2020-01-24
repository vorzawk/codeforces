n = int(input())
friends = list(map(int, input().split()))
for i in range(len(friends)):
    friends[i] -= 1
inDegrees = [0] * n
outDegrees = [0] * n
for i, f in enumerate(friends):
    if f == -1:
        continue
    inDegrees[f] += 1
    outDegrees[i] += 1
#print(inDegrees)
#print(outDegrees)

chains = []
for i in range(n):
    if inDegrees[i] == 0 and outDegrees[i] == 0:
        chains.append((i, i))
    elif inDegrees[i] == 0 and outDegrees[i] == 1:
        k = i
        while outDegrees[k] == 1:
            k = friends[k]
        chains.append((i, k))
#print(chains)

for i in range(len(chains)):
    friends[chains[i][1]] = chains[(i+1) % len(chains)][0]

for f in friends:
    print(f+1, end=' ')




