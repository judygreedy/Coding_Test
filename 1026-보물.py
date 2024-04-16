N = int(inut())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

#  A의 최솟값과 B의 최댓값을 곱한 후, 더함  

s = 0

for i in range(N):
    s += min(A)*+max(B)
    A.pop(a_list.index(min(a_list)))
    B.pop(b_list.index(max(b_list)))

   print(s)


# n = int(input())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# a.sort()
# s = 0
# for i in range(n):
#     b_max = max(b)
#     s += a[i] * b_max
#     b.remove(b_max)

# print(s)