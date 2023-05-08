# 무작위 로또 변호 출력하기
import random

def main():
    number_list = list()
    i = int()
    while i < 6:
        number = random.randint(1, 45)
        if number in number_list:
            continue
        number_list.append(number)
        i += 1
    print(number_list)

if __name__ == '__main__':
    main()