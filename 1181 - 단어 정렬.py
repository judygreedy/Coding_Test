# (Class2) 1181 - 단어 정렬

N = int(input())

words= []
for i in range(N):
    words.append(input())

#set으로 중복제거 
words_list = list(set(words))


#사전 순으로 정렬 (파이썬의 정렬 방식에 맞게 사전 순으로 먼저 구현)
words_list.sort()
#길이 순으로 정렬
#words_list.sort(key=len)
words_list.sort(key=lambda x:len(x))

for word in words_list:
    print(word)

 
