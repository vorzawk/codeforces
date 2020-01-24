n, m = map(int, input().split())
totArea = n*m
totArea -= totArea % 2
print(totArea // 2)
