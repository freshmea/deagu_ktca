# 구구단을 출력하는 프로그램입니다.

def main():
    for j in range(8):
        print(f'{j+2}단')
        for i in range(8):
            print(f'{j+2} * {i+2} =', (j+2) * (i+2))

if __name__ == '__main__':
    main()