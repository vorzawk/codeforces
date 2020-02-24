n = int(input())
dx = 1
for _ in range(n):
    a = int(input())
    if a % 2 == 0:
        print(a//2)
    else:
        print((a+dx)//2)
        dx *= -1

        
