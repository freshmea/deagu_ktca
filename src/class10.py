import random


def main():
    sum = 0
    main_data = list()
    for i in range(100):
        main_data.append(random.randint(0, 100))
    print(main_data)
    for i in main_data:
        sum += i
    avr = sum / len(main_data)
    print(f"이 데이터의 평균은{avr:.1f} 입니다.")


if __name__ == "__main__":
    main()
