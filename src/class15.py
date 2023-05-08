def main():
    dict_a = {'choi': 170,
              'kim': 165,
              'lee': 180,
              'su': 150,
              'park': 177}
    print(dict_a)
    print(dict_a['choi'])
    
    # dict 에 추가
    dict_a['james'] = 200
    print(dict_a)
    del dict_a['su']
    print(dict_a)
    dict_a['choi'] = 180
    print(dict_a)
    
    # key = input()
    # if key in dict_a:
    #     print(dict_a[key])
    # else:
    #     print('그런 데이터는 없습니다.')
        
    print(dict_a.get('su'))
    for i in dict_a:
        print(i)
    print(dict_a.keys())
    print(dict_a.values())
    print(dict_a.items())

if __name__ == '__main__':
    main()