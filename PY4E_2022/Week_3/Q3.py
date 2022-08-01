# Q3. 2개의 숫자를 입력하여 그 사이에 짝수만 출력하는 함수를 만들어 봅시다. 그리고 중앙값도 함께 출력 해봅시다.(단, 중앙값이 홀수가 아닐 경우에는 중앙값은 출력을 하지 않고, 짝수인 수만 출력한다)

# 중앙값: 정중앙에 있는 값

# 특정 두 숫자 사이의 수들을 리스트로 만드는 법

# n = 1
# m = 10
# numbers = [ i for i in range(n,m+1)] # [1,2,3,4,5,6,7,8,9,10]
# # range(시작 숫자, 끝 숫자 + 1)

start = int(input("시작 숫자: "))
end = int(input("끝 숫자: "))

print(f"{start}..{end} 사이 짝수인 값들: ")
for num in range(start, end + 1):
    if num % 2 == 0:
        print(num)

median = int((start + end) * 0.5)
print(median)
if median % 2 != 0:
    print(f"중앙값: {median}")
