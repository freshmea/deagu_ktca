# 야구 게임.
# 숫자 3개 만드리 1~ 9 까지
# 입력받기 숫자 3개
# 숫자가 일치하면 ball
# 숫자와 자리가 일치하면 strike

import random

def main():
    number_list = list()
    answer_list = list()
    ball = int()
    strike = int()
    i = int()
    
    while i < 3:
        number = random.randint(1, 9)
        if number in number_list:
            continue
        number_list.append(number)
        i += 1
    print(number_list)
    
    while strike != 3:
        answer_list.clear()
        strike = 0
        ball = 0
        for i in range(3):
            answer_list.append(int(input()))
        
        for i, ivalue in enumerate(number_list):
            for j, jvalue in enumerate(answer_list):
                if ivalue == jvalue:
                    if i == j:
                        strike += 1
                    else:
                        ball += 1 
        
        print(f'strike :{strike}, ball :  {ball}')

if __name__ == '__main__':
    main()