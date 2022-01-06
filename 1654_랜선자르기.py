'''
n개의 랜선을 가지고 있을때 
k개의 랜선을 얻을 수 있는 최대 랜선의 길이 값.
'''
#채점률 85%에서 제로디비젼에러가 뜨길래 왜 그런가 했는데 start 값 초반을 0으로 둬서 그랬다
#start 를 1로 두니까 해결

n, k = map(int,input().split()) #n는 갖고 있는 랜선 개수, k은 필요한 랜선 개수
arr =  [0]*n
for i in range(n):
  arr[i] = int(input())
result = 0 
start = 1
end = max(arr) #최대의 랜선 값을 구하는것이기 때문에 가장 큰 선을 기준으로 잘라봄
               #만약 최소의 길이를 기준으로 반토막씩 냈다면 최대값을 못구하는 경우도 있음
while( start <= end ):
  sum = 0
  mid = (start+end)//2
  for i in arr:
    sum += (i//mid)
    
  if sum < k :
    end = mid - 1
  else:
    start = mid + 1
    result = mid #랜선 자체가 이전 값보다 크다는 것이므로 굳이 또 비교할 필요 x
print(result)
