# (Class2) 1181 - 단어 정렬

import sys

def main(input_file, output_file):
    with open(input_file, 'r') as f:
        N = int(f.readline().strip())  # 첫 번째 줄에서 N을 읽습니다.

        words = [f.readline().strip() for _ in range(N)]  # 다음 N 줄에서 단어들을 읽습니다.

    # set으로 중복제거 
    words_list = list(set(words))

    # 사전 순으로 정렬 (파이썬의 정렬 방식에 맞게 사전 순으로 먼저 구현)
    words_list.sort()
    
    # 길이 순으로 정렬
    words_list.sort(key=lambda x: len(x))

    with open(output_file, 'w') as f:
        for word in words_list:
            f.write(word + '\n')  # 파일에 단어와 개행 문자를 함께 씁니다.

if __name__ == "__main__":
    # 첫 번째와 두 번째 인자를 input_file, output_file로 설정합니다.
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    main(input_file, output_file)
 
