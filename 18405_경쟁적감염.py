'''
1초마다 그래프에 있는 바이러스들이 상하좌우로 자신의 넘버를 퍼뜨렸을떄
s초에서 (a,b)에 위치한 바이러스의 값은?
'''
import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int,input().split())
q = []
gr = [[] for i in range(n)]
for i in range(n):
  gr[i] = list(map(int,input().split()))
  for j in range(n):
    if gr[i][j] != 0:
      q.append((gr[i][j],0,i,j))
s,a,b = map(int,input().split())
dx = [1,0,-1,0]
dy = [0,1,0,-1]
q.sort()
virus = deque(q)
while(virus):
  v,t,x,y = virus.popleft()
  if t == s:
    break
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx <n and 0 <= ny <n and gr[nx][ny]==0:
      gr[nx][ny] = v
      virus.append((v,t+1,nx,ny))

print(gr[a-1][b-1])
