import sys

# setting up
t = int(sys.stdin.readline())
# set up  f which is the memoization array  : f[i, k]  is the minimum of kill point used up to i when player 1 end at i after kill k+1 boss at i
f = [[0 for i in range(2)] for x in range(10)]
for x in range(0, t):
    n = int(sys.stdin.readline())
    # clean f after each use
    for i in range(n + 1):
        f[i][0] = 0
        f[i][1] = 0
    a = list(map(int, sys.stdin.readline().split()))

    # set up 1 and 2 and start at 3 as these are special cases and need to be prepared in advance
    f[0][0] = a[0]
    f[0][1] = 1
    if (n > 1):
        f[1][1] = a[0] + a[1]
        f[1][0] = a[0] + a[1] + 1
    if (n > 2):
        f[2][0] = a[0] + a[2]
        f[2][1] = a[0] + a[2] + 1
    for i in range(3, n):
        # if it end at  pos 3 ( 4 of start from 1 ) we consider 2 cases :
        # 1: if the player  kill 2 :
        f[i][1] = a[i] + a[i - 1] + min(min(f[i - 3][0], f[i - 3][1]), min(f[i - 4][0], f[i - 4][1]))
        # 2: if the player kill 1
        f[i][0] = a[i] + min(min(f[i - 1][0], f[i - 1][1]), min(f[i - 2][0], f[i - 2][1]))
    # print the result
    # remember to check n
    res = f[0][0]
    # we consider 3 case :
    if n > 1:
        # the 1st player end the game by killing the final boss
        res = min(f[n - 1][1], f[n - 1][0])
    if n > 2:
        # we end the game by killing one final bos
        res = min(res, f[n - 2][0], f[n - 2][1])
    if n > 3:
        # we end the game by killing two final boss
        res = min(res, f[n - 3][0], f[n - 3][1])
    print(res)