#로또번호 생성기

import random
numbers = []
for i in range(1,46):
    numbers.append(i)
result = []
print("밤무리의 로또추천번호는~~")
for i in range(6):
    result.append(random.choice(numbers))
#중복제거
result = list(set(result))
if len(result) < 6:
    result.append(random.choice(numbers))
print(result, "입니다!")