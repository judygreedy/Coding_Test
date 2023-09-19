# 2108 - 통계학

import sys

N = int(sys.stdin.readline())
N_list = []

for i in range(n):
    N_list.append(int(input()))

N_list.sort()#중앙값을 구하기 위해 정렬

print(round(sum(N_list)/len(N_list)))#1) 산술평균
print(N_list[len(N_list)//2])#2) 중앙값

#최빈값
dic=dict()
for i in N_list:#빈도수 구하기
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
        
mx=max(dic.values())#빈도수 중 최대값 구하기
mx_dic=[]#최빈값 숫자를 저장할 배열

for i in dic:#빈도수 딕셔너리에서
    if mx==dic[i]:#최빈값의 key저장
        mx_dic.append(i)

if len(mx_dic)>1:#최빈값이 여러개라면
    print(mx_dic[1])#두번째로 작은 값  3)최빈값
else:#하나라면
    print(mx_dic[0])#해당 값 출력  3)최빈값
    
print(max(N_list)-min(N_list))#4) 범위