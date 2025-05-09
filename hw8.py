def buy(d) :
    print('[구입]')
    item = input('상품명? ')
    if item == '':
        return False
    num = int(input('수량은? '))
    d[item] = num
    print(f'장바구니에 {item} {num}개가 담겼습니다.')
    print()
    

def show(d):
    print(f'>>> 장바구니 보기: {d}')

def find(d):
    f = input('장바구니에서 확인하고자 하는 상품은? ')
    if f in d :
        print(f'{f}은(는) {d[f]}개 담겨 있습니다.')
    else :
        print(f'장바구니에 {f}은(는) 없습니다.')
        



shopping_bag = {}
while True :
    if buy(shopping_bag) == False :
        break

print()

show(shopping_bag)

print()

print('[검색]')
find(shopping_bag)
