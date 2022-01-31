'''
청소년 상어는 더욱 자라 어른 상어가 되었다. 
상어가 사는 공간에 더 이상 물고기는 오지 않고 다른 상어들만이 남아있다. 
상어에는 1 이상 M 이하의 자연수 번호가 붙어 있고, 모든 번호는 서로 다르다. 
상어들은 영역을 사수하기 위해 다른 상어들을 쫓아내려고 하는데, 1의 번호를 가진 어른 상어는 가장 강력해서 나머지 모두를 쫓아낼 수 있다.

N×N 크기의 격자 중 M개의 칸에 상어가 한 마리씩 들어 있다. 
맨 처음에는 모든 상어가 자신의 위치에 자신의 냄새를 뿌린다. 
그 후 1초마다 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동하고,
자신의 냄새를 그 칸에 뿌린다. 냄새는 상어가 k번 이동하고 나면 사라진다.

각 상어가 이동 방향을 결정할 때는, 먼저 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡는다. 
그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 잡는다. 
이때 가능한 칸이 여러 개일 수 있는데, 그 경우에는 특정한 우선순위를 따른다. 
우선순위는 상어마다 다를 수 있고, 같은 상어라도 현재 상어가 보고 있는 방향에 따라 또 다를 수 있다. 
상어가 맨 처음에 보고 있는 방향은 입력으로 주어지고,  그 후에는 방금 이동한 방향이 보고 있는 방향이 된다.

모든 상어가 이동한 후 한 칸에 여러 마리의 상어가 남아 있으면, 가장 작은 번호를 가진 상어를 제외하고 모두 격자 밖으로 쫓겨난다.

'''
# 단순 구현 문제였는데
# 튜플이랑 배열을 비교했다가 안먹혀서 틀리고
# 겹치는 순간의 조건을 잘못 생각해서 계속 오답이 나옴


dx = [-1,1,0,0]
dy = [0,0,-1,1]
n, m, k = map(int,input().split())
gr = [[0]*n for i in range(n)]

for i in range(n):
  gr[i] = list(map(int,input().split()))

s_d = list(map(int,input().split())) # 상어가 지금 보는 방향   

'''
1. 위를 향할떄 우선순위
2. 아래를 
3. 왼쪽
4. 오른쪽
'''

s_p = [[[0]*4 for i in range(4)] for j in range(m)]
for i in range(m):
  for j in range(4):
    s_p[i][j] = list(map(int,input().split())) # 방향일때 이동 우선순위

s_loc = [[0,0,0] for i in range(m)]   # 방향,x,y
for i in range(n):
  for j in range(n):
    if gr[i][j] > 0:
      s_loc[gr[i][j]-1] = [s_d[gr[i][j]-1],i,j]

visit = [[0]*n for j in range(n)] # 각 좌표에 새겨진 k
for i in range(m):
  x,y = s_loc[i][1:3]
  visit[x][y] = k
  

def empty(num,s,a,b):
  global gr
  dir = s_p[num-1][s-1]
  for i in range(4):
    na = a + dx[dir[i]-1]
    nb = b + dy[dir[i]-1]
    if na<0 or nb<0 or na>=n or nb>=n:
      continue
    if gr[na][nb] == 0:
      return (dir[i],na,nb)
  return False

def scent(num,s,a,b):
  global gr
  dir = s_p[num-1][s-1]
  for i in range(4):
    na = a + dx[dir[i]-1]
    nb = b + dy[dir[i]-1]
    if na<0 or nb<0 or na>=n or nb>=n:
      continue
    if gr[na][nb] == num:
      return (dir[i],na,nb) 
  return (s,a,b)

cnt = m
time = 0
while(True):

  if time >1000:
      print(-1)
      break
  if cnt == 1 :
    print(time)
    break
  loc = [] # 상어가 이동한 좌표 저장
  for i in range(m):
    if s_loc[i] == [-1,-1,-1]:
      continue
    see, x, y = s_loc[i]
    temp = empty(i+1,see,x,y)        
    dir,nx,ny = 0,0,0
    if temp == False:
      dir,nx,ny = scent(i+1,see,x,y)
      s_loc[i] = [dir,nx,ny]
      loc.append([nx,ny])
    else:
      dir,nx,ny = temp
      s_loc[i] = [dir,nx,ny]
      loc.append([nx,ny])
  time+=1
 
  for i in range(n):        # 지나온 족적들에 -1
    for j in range(n):
      if [i,j] not in loc and visit[i][j] > 0 :
        visit[i][j] -= 1
        if visit[i][j] == 0:
          gr[i][j] = 0
 
  for i in range(m):      
    if s_loc[i] == [-1,-1,-1]:
      continue
    a,b,c = s_loc[i]
    if gr[b][c] == 0 or gr[b][c] == i+1:
        gr[b][c] = i+1
        visit[b][c] = k
    else:
        s_loc[i] = [-1,-1,-1]
        cnt-=1
