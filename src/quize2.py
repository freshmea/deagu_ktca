import time


def main():
    question = []
    with open("data/question.txt", "r") as f:
        data = f.read()
        que = data.split(",")
        for qu in que:
            question.append(qu)
            print(type(qu))
    correct = [3, 2, 2, 3, 4, 3, 4, 2, 2, 2]
    answer = int()
    score = int()
    print("아주 쉬운 퀴즈 지금 부터 시작합니다!!")

    for i, qu in enumerate(question):
        print(qu)
        answer = int(input())
        if answer == correct[i]:
            score += 10
            print("정답입니다.")
        else:
            print("오답입니다.")
        time.sleep(1)

    print(f"퀴즈가 끝났습니다. 당신의 점수는 {score} 입니다.")


if __name__ == "__main__":
    main()
