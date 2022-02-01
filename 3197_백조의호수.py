'''
두 마리의 호수가 물과 얼음이 공존해 있는 그래프 위에 있다.
물 근처에 얼음이 있다면 얼음을 녹이는데 하루가 걸린다.
백조가 물 위로만 이동할 수 있다고 가정할때 두 마리의 백조가 만날 수 있는 날을 출력
(물이 얼음 녹이는 과정 상하좌우 , 백조 이동 상하좌우)
''' 
# 물이 얼음을 녹이는 과정과 백조가 물 위를 이동하는 과정을 bfs로 풀었지만 시간 초과가 뜸
# 1500*1500 이기 때문에 모든 과정을 다 따로따로 완탐 하면 시간 초과가 뜨게 됨.
# day에 따라 물이 얼음을 녹이는 과정과 백조가 물 위를 이동하는 과정을 동시에 처리
# 한번 방문한 곳을 다시는 방문하지 않고 다음에 어떤곳을 방문할 지 결정하기 위해서는 두개의 큐가 필요
# 현재 물 상태를 담은 큐, 다음 날에 녹아질 얼음을 담을 큐
# 현재 백조가 이동할 수 있는 큐, 백조가 다음 날에 움직일 수 있는 큐
# 즉, 물 조지기 -> 백조 이동 -> day+1 -> 물 조지기 -> 백조 이동 -> 반복 -> 만나면 끝 
from collections import deque
import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    while q:
        x, y = q.popleft()
        if x == x2 and y == y2:
            return 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if not c[nx][ny]:
                    if a[nx][ny] == '.':
                        q.append([nx, ny])
                    else:
                        q_temp.append([nx, ny])
                    c[nx][ny] = 1
    return 0

def melt():
    while wq:
        x, y = wq.popleft()
        if a[x][y] == 'X':
            a[x][y] = '.'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if not wc[nx][ny]:
                    if a[nx][ny] == 'X':
                        wq_temp.append([nx, ny])
                    else:
                        wq.append([nx, ny])
                    wc[nx][ny] = 1

m, n = map(int, input().split())
c = [[0]*n for _ in range(m)]
wc = [[0]*n for _ in range(m)]

a, swan = [], []
q, q_temp, wq, wq_temp = deque(), deque(), deque(), deque()

for i in range(m):
    row = list(input().strip())
    a.append(row)
    for j, k in enumerate(row):
        if a[i][j] == 'L':
            swan.extend([i, j])
            wq.append([i, j])
        elif a[i][j] == '.':
            wc[i][j] = 1
            wq.append([i, j])

x1, y1, x2, y2 = swan
q.append([x1, y1])
a[x1][y1], a[x2][y2], c[x1][y1] = '.', '.', 1
cnt = 0

while True:
    melt()
    if bfs():
        print(cnt)
        break
    q, wq = q_temp, wq_temp
    q_temp, wq_temp = deque(), deque()
    cnt += 1
