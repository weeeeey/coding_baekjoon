'''
lambda를 이용해서 정렬 기준을 세워주는 문제
국영수 순서대로
국어 점수 감소
국어 점수 같으면 영어 점수 증가
국 영 같으면 수학 점수 감소
모두 같으면 이름 순서
'''
import sys 
N = int(sys.stdin.readline()) 
table = [list(sys.stdin.readline().split())for i in range(N)]

table.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0])) 
for student in table: 
  sys.stdout.write(str(student[0])+ "\n")
