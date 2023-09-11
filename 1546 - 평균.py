#1546 - 평균
""" sub = int(input()) 
score_list = list(map(int, input().split()))
max_score = max(score_list) """

def main(input_file, output_file):
    with open(input_file, 'r') as f:
        while True:
            sub = f.readline().strip()
            
            if not sub:  # 파일의 끝에 도달하면 종료
                break
            
            sub = int(sub)  # 정수로 변환
            score_list = list(map(int, f.readline().split()))  # 점수를 읽고 정수 리스트로 변환
            max_score = max(score_list)
            
            new_list = [score/max_score * 100 for score in score_list]  # List comprehension 사용
            test_avg = sum(new_list) / sub
            
            # 결과를 출력 파일에 쓰기
            with open(output_file, 'a') as out:
                out.write(f"{test_avg:.2f}\n")  # 소수점 두 자리까지만 출력

if __name__ == "__main__":
    import sys
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)



