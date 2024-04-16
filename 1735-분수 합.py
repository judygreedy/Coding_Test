# 1735- 분수 합 

def mx(A,B):
    while A % B !=0 :
        mod = A % B 
        A = B
        B = mod
    return B

A,B = map(int,input().split())
C,D = map(int,input().split())

M = mx(A*D + C*B,B*D)
print((A*D + C*B)//M,(B*D)//M )



