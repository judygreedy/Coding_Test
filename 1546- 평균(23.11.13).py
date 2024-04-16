#1546 - 평균 23.11.13
n = int(input())
mylist = list(map(int, input().split()))
m=max(mylist)
sum=sum(mylist)
score_avg=0

score_avg= sum*100/m/ n


print(score_avg)

