import sys


""" N = input()
    
while True:    
    if N == "0":
        break

    elif N == N[::-1]:
        print( "yes")
    
    else:
        print("no") """

def main(input_file, output_file):
    with open(input_file, 'r') as f:
        while True:
            N = f.readline().strip()  # 각 줄에서 N을 읽습니다.
            
            if N == "0":
                break
            
            if N == N[::-1]:
                with open(output_file, 'a') as out:
                    out.write("yes\n")
            else:
                with open(output_file, 'a') as out:
                    out.write("no\n")

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)

