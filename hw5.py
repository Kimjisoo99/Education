def read_single_digit(n) :
    if n == 1 :
        print('일', end = ' ')
    elif n == 2 :
        print('이', end = ' ')
    elif n == 3 :
        print('삼', end = ' ')
    elif n == 4 :
        print('사', end = ' ')
    elif n == 5 :
        print('오', end = ' ')
    elif n == 6 :
        print('육', end = ' ')
    elif n == 7 :
        print('칠', end = ' ')
    elif n == 8 :
        print('팔', end = ' ')
    elif n == 9 :
        print('구', end = ' ')

def read_number(n) :
    first = n // 100
    second = n % 100 // 10
    third = n % 10
    read_single_digit(first)
    read_single_digit(second)
    read_single_digit(third)
    

n = int(input('세 자리 정수 입력: '))
read_number(n)
