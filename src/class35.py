import math

def main():
    try:
        # 1
        var = int(input('반지름 입력하시오: '))
        print('원의 반지름 :', var)
        print('둘레 :', 2 * math.pi * var)
        print('넓이 :', math.pi * var**2)
    except Exception as exception:
        # 2
        print(' 에러 발생')
        print('type exception :', type(exception))
        print('exception :', exception)
        
    else:
        # 3
        print('정상 실행 되었음.')
    finally:
        # 4
        print('에러처리 끝 지점.')
        # 1, 3, 4...
        # 1, 2, 4...
    print('끝 지점.')
    
if __name__ == '__main__':
    main()