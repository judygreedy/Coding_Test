# 11659 - 구간합 구하기 1 
import sys

n = int(sys.stdin.readline().split())
suNO, quizNo = map(int.input()split())
numbers = map(int.input()split())
prefix_sum =[0]
temp=0

for i in numbers:
    temp = temp + i
    prefix_sum.append(temp)

for i in range(quizNo):
    s, e = map(int.input()split())
    print(precix_sum[e]- prefix_sum[s-1])