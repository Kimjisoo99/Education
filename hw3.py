def get_fixed_price() :
    before_price = int(after_price / (100 - percent) * 100)
    return before_price

percent = int(input('할인율은? '))
after_price = int(input('A 상품의 할인된 가격은? '))

A = get_fixed_price()

after_price = int(input('B 상품의 할인된 가격은? '))

B = get_fixed_price()

print('A 상품의 정가는', A, '원')
print('B 상품의 정가는', B, '원')
