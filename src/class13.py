def main():
    list_a = [1, 2, 3, 'choi', 'su', 'gil']
    list_b = list()
    list_c = [1.1, 21, 'nanaaaaaa']
    print(type(list_a))
    print(type(list_b))
    print(list_a[3])
    # list_d = list_a+list_c
    list_a.extend(list_c)
    list_d = list_a
    print(list_d)
    print(len(list_d))
    # print(list_d[9])
    list_d.append('dadaaaaa')
    print(list_d)
    list_d.insert(3, 4)
    print(list_d)
    list_d.insert(4, [5, 6, 7, 8])
    print(list_d)
    
    ## 요소제거하기.
    # del list_d[list_d.index(1.1)]
    # del list_d[8]
    list_d.remove(1.1)
    
    print(list_d)
    pop1 = list_d.pop(0)
    print(list_d)
    print(pop1)

if __name__ == '__main__':
    main()