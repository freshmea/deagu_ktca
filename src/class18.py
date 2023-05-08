import time

def main():
    number = 0
    time_tick = time.time()+5
    print(time_tick)
    while time.time() < time_tick:
        number += 1
    print(f'이 컴퓨터는 5초동안 {number} 만큼 세었다.')

if __name__ == '__main__':
    main()