
def error_f():
    number = int(input('정수 입력'))

    if number > 0:
        raise NotImplementedError
    else :
        raise

def main():
    try:
        error_f()
    except NotImplementedError:
        print('아직 구현이 안되었어요.')
    except ValueError:
        print('숫자만 입력 하라고!')
    except:
        print("?? ")

if __name__ == '__main__':
    main()
