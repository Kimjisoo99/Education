def get_radius(prompt) :
    r = int(input(prompt))
    return r

def get_circle_area(r) :
    circle_area = 3.14*r*r
    return circle_area

int_r = get_radius('넓이를 구하고자 하는 원의 반지름은? ')
result = get_circle_area(int_r)
print('반지름', int_r, end='')
print('인 원의 넓이 = 3.14 x', int_r, 'x', int_r, '=', result)
