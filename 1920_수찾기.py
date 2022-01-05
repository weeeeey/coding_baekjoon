# [정렬 후 이진 탐색을 한 경우]
# 최대 log10000만 하니까 시간초과 x

n = int(input())
n_arr = list(map(int,input().split()))
m = int(input())
m_arr = list(map(int,input().split()))

n_arr.sort()

def binary_search(tar):
  start = 0
  end = n-1
  while ( start <= end ):
    mid = (start+end)//2
    if n_arr[mid] == tar:
      return 1
    if n_arr[mid] > tar:
      end = mid - 1
    else :
      start = mid + 1
  return 0

for i in m_arr:
  print( binary_search(i))
  
# [집합 자료형 이용]
# 공간과 시간 최소화
# set으로 중복 줄이지 않으면 시간 초과 
n = int(input())
n_arr = set(list(map(int,input().split())))
m = int(input())
m_arr = list(map(int,input().split()))

for i in m_arr:
  if i in n_arr:
    print(1)
  else:
    print(0)
