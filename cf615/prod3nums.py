from math import floor, sqrt, ceil
def findPrimeFac(num):
    ans = []
    lim = ceil(sqrt(num))
    while num % 2 == 0:
        ans.append(2)
        num //= 2
    for p in range(3, lim, 2):
        while num % p == 0:
            ans.append(p)
            num //= p
    if num != 1:
        ans.append(num)
    return ans

t = int(input())
for _ in range(t):
    n = int(input())
    primeFacs = findPrimeFac(n)
    #print(primeFacs)
    freq = {}
    for p in primeFacs:
        if p not in freq:
            freq[p] = 0
        freq[p] += 1
    numDist = 0
    ans = []
    l = list(freq.keys())
    if len(l) >= 2:
        a = l[0]
        b = l[1]
        c = n // (a * b)
        if c != a and c != b and c != 1:
            print("YES")
            assert n == a*b*c
            print(a, b, c)
        else:
            print("NO")
    elif len(l) == 0 or freq[l[0]] < 6:
        print("NO")
    else:
        print("YES")
        p = l[0]
        print(p, p*p, n//(p ** 3))
    

            

