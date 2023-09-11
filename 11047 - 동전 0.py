#11047 - 동전 0 

N, K = map(int,input().split())

A_list = []
for _ in range(N):
    A_list.append(int(input()))
A_list(reverse=True)

answer = 0
for i in A_list:
    if K >= A_list:
        answer += K
        if K <=0:
            break
