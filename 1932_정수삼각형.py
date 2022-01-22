'''
피라미드 모양의 정수 삼각형이 있다.
맨 위층에서부터 시작해서 아래에 있는 수중 하나를 선택하여 아래층으로 내려올때
맨 아래층에서 최대값이 나오게 하는 경로에 있는 수의 합을 출력
'''
#a[i][j] = a[i][j] + max(a[i-1][j-1],a[i-1][j])
n = int(input())
tree = [[] for i in range(n)]
for i in range(n):
  tree[i] = list(map(int,input().split()))
for i in range(1,n):
  for j in range(len(tree[i])):
    l = j-1
    r = j
    if j-1<0:
      left = 0
    else:
      left = tree[i-1][j-1]
    if j>=len(tree[i-1]):
      right = 0
    else:
      right = tree[i-1][j]
    tree[i][j] = tree[i][j]+max(left,right)

print(max(tree[n-1]))



