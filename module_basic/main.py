import test_module as test

def main():
    radius = test.number_input()
    print(f"둘레 : {test.get_circumference(radius)}")
    print(f"면적 : {test.get_circle_area(radius)}")
    print(__name__)
    
if __name__== '__main__':
    main()