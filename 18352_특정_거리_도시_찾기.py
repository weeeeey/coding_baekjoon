'''
n개의 도시와 m개의 도로 정보가 주어진다.
단방향 그래프에서 x에서 출발하여 최단으로 각각의 도시에 도착했을때 떨어진 거리가 k 인 경우를 모두 구하시오 
'''

import sys
input = sys.stdin.readline
from collections import deque
n, m, k, x = map(int,input().split())
gr = [[] for i in range(n+1)]
for i in range(m):
  a, b = map(int,input().split())
  gr[a].append(b)
q = deque()
q.append(x)
result= []
distance = [-1]*(n+1)
distance[x] = 0 


while(q):
  node = q.popleft()
  for i in gr[node]:
    if distance[i] == -1:
      distance[i] = distance[node]+1
      q.append(i)

      
for i in range(1,n+1):
  if distance[i] == k:
    result.append(i)
if len(result) == 0:
  print(-1)
else:
  result.sort()
  for i in result:
    print(i)
