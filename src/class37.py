import math as m
import turtle
import random

def main():
    print(m.sin(m.pi/2))
    print(m.sin(1)**2+m.cos(1)**2)
    print(random.uniform(10, 20))
    print(random.randrange(10, 20))
    
    list_a = [1,2,3,4,5,6,7,8,9]
    print(random.choices(list_a, k = 3))
    print(list_a)
    random.shuffle(list_a)
    print(list_a)
    # for i in range(100):
    #     # 중복 안됨.
    #     print(random.sample(list_a, k =3))
    

if __name__ == '__main__':
    main()