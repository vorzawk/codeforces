n = map(int, input())
nums = list(map(int, input().split()))
oddCnt = 0
evenCnt = 0
for num in nums[:3]:
    if num % 2 == 0:
        evenCnt += 1
    else:
        oddCnt += 1
if oddCnt > 1:
    for i, num in enumerate(nums):
        if num % 2 == 0:
            print(i+1)
            break
else:
    for i, num in enumerate(nums):
        if num % 2 != 0:
            print(i+1)
            break
