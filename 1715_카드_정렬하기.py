'''
정렬된 카드 묶음들이 n개 주어졌다고 가정한다.
이때 a,b 묶음이 있을때 두 묶음을 합쳐서 하나로 만드는 데에는 a+b 번의 비교가 필요하다.
10장, 20장, 40장이 주어졌다면
(10+20)+(30+40) = 100 번
만약 비교 순서를 바꾼다면
(10+40)+(50+20) = 120 번이 된다.

최소한의 비교 횟수를 출력하라
'''
# 갯수가 적은 묶음끼리 먼저 비교한다면 최소한의 횟수가 된다는건 캐치함
# fibo를 이용해서 풀을려고 했지만 같은 갯수의 묶음들이 주어졌을경우 두 묶음끼리 묶고 나온 것을 묶으면 더 크므로 반례가 생김
# ex ) 3 3 3 3
# 이때 첫번쨰 두번쨰, 세번째 네번쨰를 처음부터 묶으면 답은 (3+3) + (3+3) + (3+3+3+3) = 24가 나옴
# fibo를 이용할 경우에는 27이 나온다.
# 리스트에서 최소값 두개 끼리 묶어서 더하는걸 구하는 것은 우선순위 큐를 이용해서 구할 수 있다.
# 최소값 두개를 뽑아서 더한 것을 다시 큐에 넣으면 그 중에서 제일 작은 두 값을 도출할 수 있으니까
# cf)우선순위 큐 부분을 sort()를 이용해서 바꾸면 시간 초과가 뜸. 
#[우선 순위 큐를 이용한 경우]

import heapq
n = int(input())
arr = [] 
for i in range(n):
  heapq.heappush(arr,int(input()))
result = 0
while(len(arr)!=1):
  one = heapq.heappop(arr)
  two = heapq.heappop(arr)
  temp = one+two
  result += temp
  heapq.heappush(arr,temp)
  
print(result)

#[sort 이용해서 시간 초과 뜨는 경우]

n = int(input())
arr = [] 
for i in range(n):
  arr.append(int(input()))
result = 0
while(len(arr)!=1):
  arr.sort(reverse=True)
  one = arr.pop()
  two = arr.pop()
  temp = one+two
  result += temp
  arr.append(temp)
  
print(result)


# [fibo를 이용해서 틀린 코드]
num = int(input())
gr = [0]*num 
for i in range(num):
  gr[i] = int(input())
gr.sort()
result = [0]*num

def fibo(i):
  global result
  global gr 
  if i<1:
    return gr[i]
  else:
    return gr[i]+result[i-1]

for i in range(num):
  result[i] = fibo(i)
sum = 0
for j in range(-2,-len(result),-1):
    sum+=result[j]
result[-1] +=sum
print(result[-1])
