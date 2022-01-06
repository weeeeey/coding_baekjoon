'''
숫자 카드는 정수 하나가 적혀져 있는 카드이다. 
상근이는 숫자 카드 N개를 가지고 있다. 
정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 (상근이가 몇 개 가지고 있는지) 구하는 프로그램을 작성하시오.
'''

n = int(input())
n_arr = list(map(int,input().split()))
m = int(input())
m_arr = list(map(int,input().split()))
n_arr.sort()
result = [0]*20000001

for i in range(n):
    result[n_arr[i]] += 1

for i in range(m):
    print(result[m_arr[i]], end = ' ')
    
# 이진탐색 컨텐츠에 포함되어 있는데 최대값과 최소값의 차가 2천만이라 계수 정렬을 이용해서 풀이했다
