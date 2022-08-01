# Q4. 2개의 숫자를 입력하여 그 사이에 소수가 몇 개인지 출력하는 함수를 만들어 봅시다.

## 소수: 1과 자기 자신만을 약수로 가지는 수


def is_prime_number(num):
    if num == 1:
        return False
    for divider in range(2, num):
        if num == divider:
            continue
        if num % divider == 0:
            return False
    return True


start = int(input("시작 숫자: "))
end = int(input("끝 숫자: "))

for n in range(start, end + 1):
    if is_prime_number(n):
        print(n)
