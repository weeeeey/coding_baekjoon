'''
리스트에서 가장 길게 증가한 수열의 길이를 구하는 문제이다.
이 문제에서 알게 된것 
1. LIC 알고리즘 ( 최장 증가 부분 수열 )
- 초기 리스트 arr이 있을때, d와 x라는 리스트를 만든다. 
  이때 d는 길이 리스트이고, x는 비교를 하는 리스트이다.
  초기값 d[0]에 1을 삽입 
  x에 arr[0]을 삽입
  (1,n)까지 인덱스를 거치면서 arr[i]의 값이 x의 마지막 원소값(가장 큰 수)보다 크다면 길이 d[i] = d[i-1]+1
  만약 작다면, arr[i]가 x 리스트에서 어느 위치에 있는지 알아낸 후 그 위치의 d 값에 +1 한 것이 d[i]
  그리고 그 위치에 있는 x의 원소값을 arr[i]로 치환해준다
  마지막까지 수행 후 d값에서 가장 큰 값이 lic이다.
  
2. bisect 라이브러리 
-bisect_left(arr,target) -> 정렬이 되어있는 arr 리스트에서 target이 들어갈 위치를 리턴함
                        [1,2,4]에서 3이 들어갈 위치는 2이다
-bisect_right(arr,target) -> 정렬이 되어있는 arr 리스트에서 target이 들어갈 오른쪽 위치를 리턴함
                        [1,2,4,4,4,5]에서 4가 들어갈 위치는 5이다.
            이것을 응용하면 left-right 로 특정 값이 리스트에서 몇번 들어가 있는지 알 수 있다.
                        
'''
# 계속 시간 초과가 돼서 이것저것 해보느라 오래걸림
# d라는 리스트를 처음부터 n 크기 만큼 할당한 후 만졌더니 그리 되어버림

import sys
input = sys.stdin.readline
from bisect import bisect_left
n = int(input())
arr = list(map(int,input().split()))
d = []
x = [arr[0]]
d.append(1) 
for i in range(1,n):
  if arr[i] > x[-1]:
    d.append(d[-1]+1)
    x.append(arr[i])
  else:
    x[bisect_left(x,arr[i])] = arr[i]
    
print(max(d))
