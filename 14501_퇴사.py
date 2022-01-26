'''
날짜 n과 날짜별로 상담을 완료하는 시간 t와 상담을 했을때 금액 p를 입력 받는다.
n+1일쨰 되는 날 퇴사를 하기 위해 n일동안 최대한 많은 상담 이익을 구하는 프로그램을 짜보시오.
'''
# 1일차에 상담을 진행한다고 가정하면 {1일차때의 상담 이익 + (1일차 상담이 끝난 후 남은 상담들의 최대 이익)} 이 최대 수익이 된다.
# 이것을 반대로 생각해보면 현재 상담 일자의 이윤 + 지금까지 상담을 마친 최대 이윤을 계산하면 된다.
# s[i] 를 i번째 날부터 마지막 날까지 낼 수 있는 최대 이익이라고 가정.


n = int(input())
arr = [[0,0] for i in range(n)]
for i in range(n):
  arr[i] = list(map(int,input().split()))
s = [0]*(n+1)
max_value = 0 
for i in range(n-1,-1,-1):
  time = arr[i][0] + i

  if time <=n:
    s[i] = max(arr[i][1] + s[time], max_value)
    max_value = s[i]
  else:
    s[i] = max_value
print(max_value)
