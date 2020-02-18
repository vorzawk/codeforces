n = int(input())
num1 = 1
num2 = 1
i = 2
cnt = 0
while i*i <= n:
    while n % i == 0:
        if cnt % 2 == 0:
            num1 *= i
        else:
            num2 *= i
        n //= i
        cnt += 1
    i += 1
# prime numbers are guaranteed to be odd
if cnt % 2 == 0:
    num1 *= i
else:
    num2 *= i

print(max(num1, num2))

