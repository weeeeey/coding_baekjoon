'''
아기 상어가 성장해 청소년 상어가 되었다.

4×4크기의 공간이 있고, 크기가 1×1인 정사각형 칸으로 나누어져 있다.
공간의 각 칸은 (x, y)와 같이 표현하며, x는 행의 번호, y는 열의 번호이다. 한 칸에는 물고기가 한 마리 존재한다. 
각 물고기는 번호와 방향을 가지고 있다. 번호는 1보다 크거나 같고, 16보다 작거나 같은 자연수이며, 두 물고기가 같은 번호를 갖는 경우는 없다. 방향은 8가지 방향(상하좌우, 대각선) 중 하나이다.

오늘은 청소년 상어가 이 공간에 들어가 물고기를 먹으려고 한다. 
청소년 상어는 (0, 0)에 있는 물고기를 먹고, (0, 0)에 들어가게 된다. 
상어의 방향은 (0, 0)에 있던 물고기의 방향과 같다. 이후 물고기가 이동한다.

물고기는 번호가 작은 물고기부터 순서대로 이동한다. 
물고기는 한 칸을 이동할 수 있고, 이동할 수 있는 칸은 빈 칸과 다른 물고기가 있는 칸, 이동할 수 없는 칸은 상어가 있거나, 공간의 경계를 넘는 칸이다. 
각 물고기는 방향이 이동할 수 있는 칸을 향할 때까지 방향을 45도 반시계 회전시킨다. 
만약, 이동할 수 있는 칸이 없으면 이동을 하지 않는다. 그 외의 경우에는 그 칸으로 이동을 한다. 
물고기가 다른 물고기가 있는 칸으로 이동할 때는 서로의 위치를 바꾸는 방식으로 이동한다.

물고기의 이동이 모두 끝나면 상어가 이동한다. 
상어는 방향에 있는 칸으로 이동할 수 있는데, 한 번에 여러 개의 칸을 이동할 수 있다. 
상어가 물고기가 있는 칸으로 이동했다면, 그 칸에 있는 물고기를 먹고, 그 물고기의 방향을 가지게 된다. 
이동하는 중에 지나가는 칸에 있는 물고기는 먹지 않는다. 물고기가 없는 칸으로는 이동할 수 없다. 
상어가 이동할 수 있는 칸이 없으면 공간에서 벗어나 집으로 간다. 상
어가 이동한 후에는 다시 물고기가 이동하며, 이후 이 과정이 계속해서 반복된다.
'''
# 구현 + DFS 문제였음
# 물고기 이동 하는 것에는 문제 없었지만
# 상어가 먹이를 잡고 각각의 이동 경로마다 다른 그래프를 넘겨줌으로써 비교 했지만 그래프가 변경 되어버림
# 이 부분을 수정해줌

import sys
from copy import deepcopy

input = sys.stdin.readline
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def dfs(x, y, d, cnt):
    global ans, a, fish
    move_fish(x, y)
    while True:
        nx, ny = x + dx[d], y + dy[d]
        if not 0 <= nx < 4 or not 0 <= ny < 4:
            ans = max(ans, cnt)
            return
        if not a[nx][ny]:
            x, y = nx, ny
            continue

        temp_a, temp_fish = deepcopy(a), deepcopy(fish)
        temp1, temp2 = fish[a[nx][ny][0]], a[nx][ny]
        fish[a[nx][ny][0]], a[nx][ny] = [], []
        dfs(nx, ny, temp2[1], cnt + temp2[0] + 1)
        a, fish = temp_a, temp_fish
        fish[a[nx][ny][0]], a[nx][ny] = temp1, temp2
        x, y = nx, ny


def move_fish(sx, sy):
    for i in range(16):
        if fish[i]:
            x, y = fish[i][0], fish[i][1]
            for _ in range(9):
                nx, ny = x + dx[a[x][y][1]], y + dy[a[x][y][1]]
                if not 0 <= nx < 4 or not 0 <= ny < 4 or (nx == sx and ny == sy):
                    a[x][y][1] = (a[x][y][1] + 1) % 8
                    continue
                if a[nx][ny]:
                    fish[a[nx][ny][0]] = [x, y]
                a[nx][ny], a[x][y] = a[x][y], a[nx][ny]
                fish[i] = [nx, ny]
                break


a = [[] for _ in range(4)]
fish = [[] for _ in range(16)]
for i in range(4):
    temp = list(map(int, input().split()))
    for j in range(0, 7, 2):
        a[i].append([temp[j]-1, temp[j+1]-1])
        fish[temp[j]-1] = [i, j // 2]

ans = 0
d, cnt = a[0][0][1], a[0][0][0] + 1
fish[a[0][0][0]], a[0][0] = [], []
dfs(0, 0, d, cnt)
print(ans)
