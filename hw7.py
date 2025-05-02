print('[구입]')

shopping_bag = []
n = {}

while True:
    item = input('상품명? ')
    if item == '':
        break
    num = int(input('수량은? '))
    print(f'장바구니에 {item} {num}개가 담겼습니다.\n')
    shopping_bag.append(item)
    n[item] = num
    
print(f'\n>>>장바구니 보기:{n}')
    
print(f'\n[검색]')

check_item = input('장바구니에서 확인하고자 하는 상품은? ')
check_num = n[check_item]
print(f'{check_item}은(는) {check_num}개 담겨 있습니다.')
