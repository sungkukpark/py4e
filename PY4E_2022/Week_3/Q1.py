# Q1. 숫자를 입력 받고 그 숫자의 구구단을 출력하는 함수를 만들어 봅시다. 다만 아래의 조건을 만족해 주세요.
## 조건 1: 홀 수 번째만 출력하기
## 조건 2: 값이 50이하인 것만 출력하기

num = int(input("숫자를 입력해주세요: "))
for mul in range(1, 10):
    result = num * mul
    ## 조건 1: 홀 수 번째만 출력하기
    if mul % 2 == 0:
        continue
    ## 조건 2: 값이 50이하인 것만 출력하기
    if result > 50:
        continue
    print(f"{num} * {mul} = {num * mul}")
