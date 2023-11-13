#11720- 숫자의 합 


n=int(input())
numbers= list(input())
sum = 0 # 변수 선언

for i in numbers:
    sum = sum + int(i) #numbers에 있는 각 자리수를 가져와 더하기 

print(sum) 
