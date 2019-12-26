from __future__ import print_function
N = int(raw_input())
nums = list(map(int, raw_input().split()))

def nearestOppParity(nums, N):
    numMoves = [None] * N
    def findNumMoves(index):
        if index < 0 or index >= N:
            return -1
        if visited[index] and not explored[index]:
            return -1
        visited[index] = True
        if numMoves[index] is not None:
            return numMoves[index]
        step = nums[index]
        if nums[index] % 2 == 0:
            if index + step < N and nums[index + step] % 2 != 0:
                numMoves[index] = 1
                visited[index] = True
                explored[index] = True
                return 1
            if index - step >= 0 and nums[index - step] % 2 != 0:
                numMoves[index] = 1
                explored[index] = True
                return 1
        else:
            if index + step < N and nums[index + step] % 2 == 0:
                numMoves[index] = 1
                explored[index] = True
                return 1
            if index - step >= 0 and nums[index - step] % 2 == 0:
                numMoves[index] = 1
                explored[index] = True
                return 1
        l = findNumMoves(index - nums[index])
        r = findNumMoves(index + nums[index])
        if l == -1 and r == -1:
#            numMoves[index] = -1
#            if index == 3:
#                print('returning {}'.format(- 1))
            return -1
        if l == -1:
#            numMoves[index] = r + 1
#            if index == 3:
#                print('returning {}'.format(r + 1))
            return r + 1
        if r == -1:
#            numMoves[index] = l + 1
#            if index == 3:
#                print('returning {}'.format(l + 1))
            return l + 1
        numMoves[index] = 1 + min(l, r)
#        if index == 3:
#            print('returning {}'.format(1 + min(l, r)))
        explored[index] = True
        return 1 + min(l, r)
    ans = []
    for i in range(N):
        explored = [False] * N
        visited = [False] * N
        movz = findNumMoves(i)
        explored[i] = True
        print(movz, end=' ')

nearestOppParity(nums, N)










