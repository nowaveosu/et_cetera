#로또번호 생성기

import random
numbers = []
for i in range(1,46):
    numbers.append(i)

print("밤무리의 로또추천번호는~~")
for i in range(6):
    print(random.choice(numbers), end = ' ' )
    
    if i == 5:
        print("입니다!")