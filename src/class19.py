import random

def main():
    list_var = list()
    
    # for i in range(1000):
    #     list_var.append(random.random()*100)
    list_var = [random.random()*100 for i in range(1000)]
    
    list_var = [i**2 for i in range(1000)]
    
    print(list_var)
    print(max(list_var))
    print(min(list_var))
    print(sum(list_var))

if __name__ == '__main__':
    main()