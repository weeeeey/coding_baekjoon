'''
n명의 병사 각각의 전투력이 주어졌을때 이것을 내림차순으로 정렬한다.
이 때 남아있는 병사의 수를 가장 많게 하도록 하기 위해 제외시켜야하는 병사의 수는?
'''
# 내림차순 최장 길이를 응용해서 문제를 풀었다,
# bisect_left는 오름차순이 기본이므로 역순을 취해서 넣어준뒤 다시 역순을 취해줌

import bisect
n = int(input())
arr = list(map(int,input().split()))
result = 0
temp = []
temp.append(arr[0])
for i in arr:
  
  if i < temp[-1]:
    temp.append(i)
  else:
    temp.sort()
    index = bisect.bisect_left(temp,i)
    temp[index-1] = i
    temp.sort(reverse = True)

print(len(arr)-len(temp))
