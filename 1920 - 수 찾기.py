#1920 - 수 찾기 

import sys
from collections import Counter

N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))

N_cnt = Counter(N_list)
for num in M_list:
  if N_cnt[num]:
    print(1)
  else:
    print(0)

""" 런타임 에러 
N = int(input())
N_list = list(map(int, input().split()))

M = int(input())
M_list = list(map(int, input().split()))

def binary(target, N, start, end):
    if start > end : 
        return 0
    m = (start + end)//2
    if 1== N[m] : 
        return 1
    elif 1 < N[m] :
        return binary(1, N, start,m-1)
    else : 
        return binary(1, N, m+1 , end)

for target in range(M) : 
    start = 0
    end = len(N) -1
    print(binary(1,N,start,end)) """
    


