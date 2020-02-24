n = int(input())
i = 2
divisors = []
while i*i <= n:
    if n % i == 0:
        divisors.append(i)
        divisors.append(n//i)
    i += 1
divisors.sort()
print(divisors)

