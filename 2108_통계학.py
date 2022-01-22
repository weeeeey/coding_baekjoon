'''
산술 평균: n개의 수들의 합을 n으로 나눈 값(소수점 첫째 자리에서 반올림)
중간값:n(홀수)개의 수들중 중간 값을 출력
최빈값 : 최대로 많이 발생하는 수를 출력(동일한 값들이 있을 경우 그 수들중  두번쨰로 작은 값을 출력)
범위 : 최대값 - 최소값
'''
# 계수정렬을 이용해서 최빈값을 구했는데 음수가 들어올 경우 리스트에 들어오지 못한다는 것을 간과했음
# 마이너스일 경우의 리스트를 따로 만들어서 양수 리스트와 합해서 정렬하는 것으로 해결함
# 산술 평균에서 오류 발생 
# 음수일 경우 -9.7이면 -10이 되어야 한다
# 합이 음수일 경우 -0.5를 더한 다음에 소수점을 버리는 것으로 해결함

n = int(input())
arr =[]
for i in range(n):
  arr.append(int(input()))
arr.sort()
s = sum(arr)
if s>=0:
  print(int((s/n)+0.5))
else:
  print(int((s/n)-0.5))
print(arr[n//2])

temp = [[0,0] for i in range(max(arr)+1)]
temp_m = [[0,0] for i in range((min(arr)*(-1))+1)]
for i in arr:
  if i>=0:
    temp[i][0] = i
    temp[i][1]+=1
  else: 
    temp_m[i*(-1)][1]+=1
    temp_m[i*(-1)][0] = i

result = temp+temp_m
result.sort(key = lambda x:(-x[1],x[0]))
if result[0][1] == result[1][1]:
  print(result[1][0])
else: 
  print(result[0][0])
print(arr[-1]-arr[0])
