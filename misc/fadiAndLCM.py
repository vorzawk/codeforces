def gcd(a,b):
    if a == 0:
        return b
    return gcd(b % a, a)

def lcm(a,b):
    return a*b // gcd(a,b)

def solve():
    n = int(input())
    if n == 1:
        print(1,1)
        return
    
    i = 2
    ans = [n,1]
    while i*i <= n:
        if n % i == 0 and lcm(i, n//i) == n:
            if max(i, n//i) < max(ans):
                ans = [i, n//i]
        i += 1
    print(ans[0], ans[1])
    
solve()
