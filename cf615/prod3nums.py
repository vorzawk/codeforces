from math import floor, sqrt, ceil

t = int(input())
for _ in range(t):
    a = -1
    b = -1
    n = int(input())
    i = 2
    while i*i < n:
        if n % i == 0:
            a = i
            n //= a
            break
        i += 1
    i = 2
    while i*i < n:
        if n % i == 0 and i != a:
            b = i
            n //= b
            break
        i += 1
    if a == -1 or b == -1 or n == 1 or n == a or n == b:
        print('NO')
        continue
    print('YES')
    print(a, b, n)



        


    

            

