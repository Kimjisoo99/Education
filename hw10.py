import os
import pickle

filename = 'score.bin'

def input_scores():
    s = []
    i = 1
    while True :
        n = int(input(f'#{i}? '))
        if n < 0 :
            break
        s.append(n)
        i += 1

    return s




def get_average(lst) :
    total = 0
    for n in lst :
        total += n
    return total / len(lst)

def save_data(scores, average) :
    with open(filename, 'wb') as file:
        pickle.dump(scores, file)
        pickle.dump(average, file)

def load_data():
    with open(filename, 'rb') as file:
        scores = pickle.load(file)
        average = pickle.load(file)
    return scores, average



if os.path.exists(filename):
    print('[파일 읽기]')
    scores, average = load_data()

else :
    print('[점수 입력]')
    scores = input_scores()
    average=get_average(scores)
    save_data(scores, average)

print('\n[점수 출력]')
print('개인점수:', end = ' ')
for i in range(len(scores)):
    print(f'{scores[i]}', end = ' ')
print()  
print(f'평균: {average:.1f}')

    
