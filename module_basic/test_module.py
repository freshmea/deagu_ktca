PI = 3.14159265358979

def number_input():
    return float(input('반지름 입력: '))

def get_circumference(radius):
    return 2* PI* radius

def get_circle_area(radius):
    return PI * radius**2

def main():
    print(__name__)
    
if __name__ == '__main__':
    main()