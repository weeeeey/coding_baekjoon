'''
T라는 출발지점에서부터 상하좌우 한방향으로 쭉 이동했을 경우 S를 만나면 NO를 출력
이때 X라는 지점 세군대에 O를 덮어씌워서 T가 S를 만나지 않는 경우가 있다면 YES를 출력
'''
# DFS 재귀를 이용해서 품
# 계속 안되길래 뭐가 문제이지 했는데
# X를 만난경우 재귀를 이용하여 풀었을때 리턴을 안해줌
'''
def DFS(a):
  if a==True :
    return 0
  else:
    return DFS(True) #재귀를 짤때 리턴값 해주는거 잊지말자
'''
from collections import deque
import copy
from itertools import combinations
num = int(input())
gr = [[] for i in range(num)]
for i in range(num):
  gr[i]=list(input().split())
result = False
temp=[]
teacher = []
for i in range(num):
  for j in range(num):
    if gr[i][j] == 'X':
      temp.append((i,j))
    if gr[i][j] == 'T':
      teacher.append((i,j))

com = deque(list(combinations(temp,3)))

def DFS(gra,x,y,a,b):
  if (x+a) >=num or (y+b) >= num or (x+a) < 0 or (y+b) < 0:
    return False
  if gra[x+a][y+b] == 'X':
    
    DFS(gra,x+a,y+b,a,b)
  if gra[x+a][y+b] == 'S':
    return True
  if gra[x+a][y+b] == 'O':
    return False
  

dx = [-1,0,1,0]
dy = [0,1,0,-1]


def search(graph):
  for j in teacher:
    for z in range(4):
      if DFS(graph,j[0],j[1],dx[z],dy[z]) == True : #한번이라도 S를 만나면 True
        return True
  return False

while(com):
  i = com.popleft()
  gr_c = copy.deepcopy(gr)
  gr_c[i[0][0]][i[0][1]] = 'O'
  gr_c[i[1][0]][i[1][1]] = 'O'
  gr_c[i[2][0]][i[2][1]] = 'O'
  if search(gr_c) == True: #한번이라도 학생을 마주치면 O가 세워진 장소들은 감시 피하지 못한다는거
    result = False
    continue
  else:
    result = True
    break
print("YES" if result == True else "NO")
