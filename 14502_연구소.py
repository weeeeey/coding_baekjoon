'''
0,1,2로 이루어진 n*m 그래프가 있을때
2를 바이러스, 1은 벽, 0은 일반 상태로 가정한다.
2를 기준으로 상,하,좌,우에 바이러스를 퍼뜨릴수 있지만 벽으로 막혀있다면 불가능.
모든 감염 후 남겨진 0을 안정 영역이라고 한다.
벽을 추가로 3개씩 임의의 자리에 세웠을때 가장 큰 안전 영역의 크기는?
'''

import itertools
from collections import deque
import copy
n, m = map(int,input().split())
gr = [[] for i in range(n)] 
for i in range(n):
  gr[i] = list(map(int,input().split()))
#m 가로 n 세로
a = []
for i in range(n):
  for j in range(m):
    if gr[i][j] == 0:
      a.append((i,j))

pole = list(itertools.combinations(a,3))  #수 범위 자체가 낮고 메모리 제한과 시간이 여유로우니 조합을 이용해도 됨.
                                          #처음에는 큐에다가 담아서 체크할려고 했음.

def BFS(aa,a,b):
  q = deque()
  q.append((a,b))
  dx = [1,0,-1,0]
  dy = [0,1,0,-1]
  while(q):
    x,y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx>=n or ny>=m or nx<0 or ny<0:
        continue
      if aa[nx][ny] == 1:
        continue
      if aa[nx][ny] == 0:
        aa[nx][ny]=2
        q.append((nx,ny))

result = 0
for i in pole:
  temp = 0
  gr_c = copy.deepcopy(gr)
  gr_c[i[0][0]][i[0][1]] = 1
  gr_c[i[1][0]][i[1][1]] = 1
  gr_c[i[2][0]][i[2][1]] = 1
  for i in range(n):
    for j in range(m):
      if gr_c[i][j] == 2:
          BFS(gr_c,i,j)
  for i in range(n):
    for j in range(m):
      if gr_c[i][j] == 0:
        temp+=1
  if temp >result:
    result = temp
  
print(result)
