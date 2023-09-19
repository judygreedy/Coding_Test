#1931 - 회의실 배정
import sys

N = int(input())

N_list = [list(map(int, input().split())) for _ in range(N)]

N_list = sorted(N_list, key = lambda x:(x[1], x[0]))

start , end = 0 ,0

for time in meeting_list:
    if(time[0] >= start):
        start = time[1]
        N_list += 1
        
print(N_list)
