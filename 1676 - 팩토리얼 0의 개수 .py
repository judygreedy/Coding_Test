# 1676 - 팩토리얼 0의 개수 

def count(N):
    count = 0
    while N >= 5:
        N //= 5
        count += N
    return count

N = int(input())
print(count(N))
