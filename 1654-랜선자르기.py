""" import sys
input=sys.stdin.readline

K , N = map(int,input().split())
lan = [int(input()) for _ in range(k)]
start, end = 1, max(lan) """

import sys

def main(input_file,output_file):
    with open(input_file, 'r') as f:
        K , N = map(int, f.readline().strip().split())
       # K , N = map(int,input().split())
        lan = [int(f.readline().strip()) for _ in range(K)]
        start, end = 1, max(lan)


        while start <= end:
            mid = (start+end)//2
            lines = 0

            # mid 길이 만큼 랜선 케이블을 나눔 
            for i in lan:
                lines += i//mid

            # 랜선의 수가 N 이상일 때
            if lines >= N :
                start = mid +1

            # 랜선의 수가 N 미만일 때
            else : 
                end = mid -1

    with open(output_file, 'w') as f_out:
        f_out.write(str(end))

# print(end)

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)

