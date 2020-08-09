import sys
sys.setrecursionlimit(5000)

dx = [1, 0, -1]
dy = [1, 0, -1]

def dfs(area, x, y):
    area[x][y] = 0
    for i in dx:
        for j in dy:
            next_x = x + i
            next_y = y + j
            if area[next_x][next_y] == 1:
                dfs(area, next_x, next_y)

def solver(w, h):
    ans = 0
    area = [[0]*(w+2)]
    for i in range(h):
        area.append([0]+list(map(int, input().split()))+[0])
    area.append([0]*(w+2))

    for i in range(1, h+1):
        for j in range(1, w+1):
            if area[i][j] == 1:
                ans += 1
                dfs(area, i, j)
    return ans

while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    print(solver(w, h))

