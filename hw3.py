def get_fixed_price() :
    fixed_price = int(discounted_price / (100 - percent) * 100)
    return fixed_price

percent = int(input('할인율은? '))
discounted_price = int(input('A 상품의 할인된 가격은? '))

A_fp = get_fixed_price()

discounted_price = int(input('B 상품의 할인된 가격은? '))

B_fp = get_fixed_price()

print('A 상품의 정가는', A_fp, '원')
print('B 상품의 정가는', B_fp, '원')
