t = int(input())
for _ in range(t):
    s = input()
    strtIdx = None
    endIdx = None
    for i,c in enumerate(s):
        if c == '1':
            strtIdx = i
            break
    for i,c in enumerate(reversed(s)):
        if c == '1':
            endIdx = len(s) - i - 1
            break
    cnt = 0
    if strtIdx == None or endIdx == None:
        print(cnt)
        continue
    for i in range(strtIdx, endIdx):
        if s[i] == '0':
            cnt += 1
    print(cnt)

