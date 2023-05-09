import random

def main():
    hanguls = list("가나다라마바사아자차카파타하")
    
    with open('data/info.txt', 'w') as file:
        for i in range(1000):
            name = random.choice(hanguls) + random.choice(hanguls) + random.choice(hanguls)
            weight = random.randrange(40, 100)
            height = random.randrange(140, 200)
            print(f"{name}, {weight}, {height}\n")
            file.write(f"{name}, {weight}, {height}\n")

if __name__ == '__main__':
    main()