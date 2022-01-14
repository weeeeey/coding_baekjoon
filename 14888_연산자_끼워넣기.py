'''
n개의 수들이 주어졌을때 연산자를 끼워 넣어 최대값과 최소값을 구하는 문제
* 연산자 우선순위 무시
* 수의 순서 섞지 않기
'''
# DFS,BFS로 풀 수 있는 문제
# BFS로 풀었다가 피똥쌈
# arr이라는 리스트를 우선순위 q에 넣었다고 가정했을떄
# q에 넣은후에 arr을 조작하면 q에 들어가있는 arr에 해당하는 리스트도 같이 조작되어버림
# 이걸 몰라서 겁나 해맴
from collections import deque
num = int(input())
arr = list(map(int,input().split()))
cal = list(map(int,input().split()))

result = []
q = deque()
q.append((arr[0],[0,0,0,0],1))

while(q):
  ans, temp,cnt = q.popleft()
  [a,b,c,d] = temp
  

  if temp == cal:
    result.append(ans)
  if cnt >= num:
    continue
  for i in range(4):
    if temp[i] < cal[i]:
      if i == 0:
        q.append((ans+arr[cnt],[a+1,b,c,d],cnt+1))
      elif i == 1:
        q.append((ans-arr[cnt],[a,b+1,c,d],cnt+1))
      elif i == 2:
        q.append((ans*arr[cnt],[a,b,c+1,d],cnt+1))
      else:
        if ans >= 0:
          q.append((ans//arr[cnt],[a,b,c,d+1],cnt+1))
        else:
          q.append(((ans*(-1)//arr[cnt])*(-1),[a,b,c,d+1],cnt+1))
print(max(result))
print(min(result))
