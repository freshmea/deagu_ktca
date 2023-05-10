class Parent:
    def __init__(self):
        self.value = '테스트'
        print('부모 클래스의 생성자가 실행 되었다.')
        
    def test(self):
        print('부모 클래스의 메소드가 실행')
    
class Child(Parent):
    def __init__(self):
        # super().__init__()
        Parent.__init__(self)
        print('자식 클래스가 실행 되었습니다.')
        
def main():
    child = Child()
    print(child.value)
    child.test()
    
if __name__ == '__main__':
    main()
        