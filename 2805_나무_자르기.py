'''
n개의 나무들이 있을떄 이것을 절단하여 뗴어낸 부분들의 합이 m 이상이면 집에 가져간다
단 기존 나무들을 최대한으로 남겨두기 위해 자르는 길이의 최대값을 구해야 함
'''
n, m = map(int,input().split()) #n 나무의 수, m 필요 나무 길이
arr = list(map(int,input().split()))
end =  max(arr)
start = 1   
result = 0
while( start <= end ):
  mid = (start+end)//2
  sum = 0 
  for i in arr:
    lengh = i - mid if i>=mid else 0
    sum+=lengh
  if sum < m :
    end = mid - 1
  else :
    result = mid
    start = mid + 1
print(result)
