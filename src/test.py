def main():
    num_of_man = int()
    num_of_woman = int()
    num_of_man = input('남학생의 수를 입력하시오')
    num_of_woman = input('여학생의 수를 입력하시오')
    man_ratio = num_of_man/(num_of_woman + num_of_man)
    woman_ratio = num_of_woman/(num_of_woman + num_of_man)
    print(f'남자의 비율 : {man_ratio:.2} \n  여자의 비율 : {woman_ratio:.2}')

if __name__ == '__main__':
    main()