'''
n*n 그래프에서 아기 상어 1마리(9)와 물고기(1,2,3,4,5,6)들의 크기가 그래프상 위치에 주어졌다.
이떄 아기 상어는 1초에 상하좌우로 다음 규칙에 따라 이동 가능하다.
1. 더 이상 먹을 물고기가 없다면 엄마 상어를 호출
2. 먹을 수있는 물고기가 1마리라면 먹으러 감
3. 먹을 물고기가 복수일 경우 가장 가까운 물고리를 먹음
4. 가장 가까운 거리의 물고기가 여러마리 일 경우 
  가장 위에 있는 물고기
  그러한 물고기가 여러마리 일 경우, 가장 왼쪽 물고기를 먹음
다음 규칙에 따라 먹이를 먹을때 아기 상어가 엄마 상어를 호출하는 시간은?
'''
# BFS로 풀었는데 계속 답이 다르게 나와서 로직에 문제가 있나 계속 고민함
# 생각해보니 아기 상어 처음 위치를 수정해주지 않아서 틀렸던거였음


from collections import deque
n = int(input())
gr = [[0]*n for i in range(n)]
shark = (0,0,0)
for i in range(n):
  gr[i] = list(map(int,input().split()))

for i in range(n):
  for j in range(n):
    if gr[i][j] == 9:
      shark = (2,i,j)
      gr[i][j] = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def BFS(s):
  global gr
  global n 
  body, sx, sy = s 
  eat = [] #거리랑 물고기 크기 저장하기
  q = deque()
  q.append ((sx,sy))
  distance = [[-1]*n for i in range(n)]
  distance[sx][sy] = 0
  while(q):
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or ny < 0 or nx>= n or ny>=n:
        continue
      if gr[nx][ny] > body:
        continue
      if distance[nx][ny] != -1:
        continue
      if gr[nx][ny] == 0 or gr[nx][ny] == body:
        distance[nx][ny] = distance[x][y] + 1
        q.append((nx,ny))
      if 0<gr[nx][ny]<body:
        distance[nx][ny] = distance[x][y] + 1
        q.append((nx,ny))
        eat.append((distance[nx][ny],nx,ny))

  if eat:
    eat.sort(key = lambda x:(x[0],x[1],x[2]))
    return eat[0]
  else:
    return False

time = 0
e = 0

while(True):
  temp = BFS(shark)
  if temp == False:
    print(time)
    break
  else:
    gr[temp[1]][temp[2]] = 0
    e += 1
    time += temp[0] 
    if e >= shark[0]:
      shark = (shark[0]+1,temp[1],temp[2])
      e = 0
    else:
      shark = (shark[0],temp[1],temp[2])
