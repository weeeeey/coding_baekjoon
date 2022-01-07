"""
배열 A[i][j] =i*j일때, 이것을 일차원 배열로 그대로 삽입한다.
이때의 배열을 오름차순 정렬 후 k 번째 수는 무엇일지 출력 (인덱스는 1부터 시작)
"""
# 처음에는 2차원 배열을 직접 만든뒤 일차원 배열에 넣어보는 생각을 해봄
# 하지만 최대값이 10^5 이기 떄문에 약 100억의 크기가 나옴 
# 이차원 배열을 만들라는게 아니라 다른 해법을 찾는 문제

# 만약 어떤 수가 있을시 그 값을 기준으로 각 행에 그 이하의 수가 몇개인지 구한 후
# 총 개수를 비교하여 k보다 큰지 작은지 판단하면 됨
# 이진 탐색을 활용하여 그 값을 계속 구하다보면 그 중에서 가장 작은 값을 찾을 수 있게 된다.

n = int(input())
k = int(input())

def sum_c(tar):
  cnt = 0 
  s = 0
  for i in range(1,n+1):
    s += min(tar//i,n)
  return s
result = 0
start, end = 1, n**2
while(start <= end):
  mid = (start + end)//2
  temp = sum_c(mid)
  if temp >= k:
    start = mid + 1
  else: #result 값이 계속 갱신하면서 그 중에서 가장 작은 값이 될 것이기 때문에 또다른 조건 필요x
        #이걸 해결하느라 시간 오래 잡아먹음
    end = mid - 1
    result = mid  

print(result)




