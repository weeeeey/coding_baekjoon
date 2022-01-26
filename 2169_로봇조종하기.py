'''
위치 그래프 n*m에서 각각의 인덱스에 대한 지역들의 가치가 주어진다.
0,0 에서 출발하여 n,m에 도달한다고 가정했을때 탐사한 지역들의 가치의 합의 최대값은?
(탐사한 지역은 방문 x)
( 왼쪽 오른쪽 아래 로만 이동 가능)
'''
# 처음에는 BFS로 풀려고 했지만 각각의 경로에 대해 방문 그래프를 짠다면 1000^3이 되므로 패스
# dp 문제로써 규칙성을 찾기
# 해당 지역의 값은 dp[x-1][y] , dp[x][y-1], dp [x][y+1] 중 가장 큰 값을 더한것이다.
# 세 값을 동시에 비교할 수 없으므로 나누어준다
# 왼쪽에서 온 경우는 왼쪽과 위에 값을 비교해서 온 것이고
# 오른쪽에서 온 경우는 오른쪽과 위에 값을 비교해서 온 것
# 각각의 행에 대해 left right배열을 만들어주어 위 왼쪽 오른쪽을 비교하고
# 가장 큰 값을 그래프에 넣어준다.

n,m = map(int,input().split())
gr = [[0]*m for i in range(n)]
v = [[False]*m for i in range(n)]
for i in range(n):
  gr[i] = list(map(int,input().split()))
for i in range(1,m):
  gr[0][i] = gr[0][i-1] + gr[0][i]
left = [1e9]*m
right = [1e9]*m
for i in range(1,n):
  for j in range(m):
    if j<=0:
      right[0] = gr[i-1][0] + gr[i][0]
    else:
      right[j] = max(gr[i-1][j],right[j-1])+ gr[i][j]
  for j in range(m-1,-1,-1):
    if j>=(m-1):
      left[j] = gr[i-1][j] +gr[i][j]
    else:
      left[j] = max(gr[i-1][j],left[j+1]) + gr[i][j]
  for j in range(m):
    gr[i][j] = max(right[j],left[j])
    
print(gr[n-1][m-1])
