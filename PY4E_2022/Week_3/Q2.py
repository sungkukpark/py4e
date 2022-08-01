# Q2. 가위바위보 업그레이드 버젼을 함수로 만들어 봅시다. 아래와 같은 조건을 만족해 주세요.
## 조건 1: 게임을 몇 판을 진행할 것인지 입력을 받아주기
## 조건 2: 0, 1, 2, "가위", "바위", "보" 이외에 다른 입력을 받으면 재입력 받기
## 조건 3: 게임종료 후 나와 컴퓨터의 총 전적 출력하기

# 아래의 코드를 추가하면 됩니다
import random

# 0 ~ 2 숫자를 랜덤으로 뽑아내는 코드
computer = random.randint(0, 2)

# # 출력
# 나: 가위
# 컴퓨터: 바위
# 컴퓨터 승리!

import random

# 진입 함수
def main():
    run_tests()
    run_game()


# 게임 함수
def run_game():
    playerInput = input("플레이어 입력: ")
    npcInput = generate_npm_input()
    result = rock_scissor_paper(playerInput, npcInput)
    print(f'플레이어는 "{playerInput}"를 냈습니다.')
    print(f'컴퓨터는 "{npcInput}"를 냈습니다.')
    print(f'결과는 "{result}"입니다.')


# 테스트 함수
def run_tests():
    assert rock_scissor_paper("가위", "가위") == "무승부"
    assert rock_scissor_paper("가위", "바위") == "컴퓨터 승리"
    assert rock_scissor_paper("가위", "보") == "플레이어 승리"
    assert rock_scissor_paper("바위", "바위") == "무승부"
    assert rock_scissor_paper("바위", "가위") == "플레이어 승리"
    assert rock_scissor_paper("바위", "보") == "컴퓨터 승리"
    assert rock_scissor_paper("보", "보") == "무승부"
    assert rock_scissor_paper("보", "가위") == "컴퓨터 승리"
    assert rock_scissor_paper("보", "바위") == "플레이어 승리"


# NPC 입력 생성 함수
def generate_npm_input():
    return enum_to_rsp(random.randint(0, 2))


# 숫자를 가위 바위 보로 변환하는 함수
def enum_to_rsp(input):
    return {0: "가위", 1: "바위", 2: "보"}[input]


# 가위 바위 보 실행 함수
def rock_scissor_paper(playerInput, npcInput):
    playerEnum = playerInput
    npcEnum = npcInput
    if playerEnum == npcEnum:
        return "무승부"
    if playerEnum == "가위":
        if npcInput == "바위":
            return "컴퓨터 승리"
        else:
            return "플레이어 승리"
    elif playerEnum == "바위":
        if npcInput == "가위":
            return "플레이어 승리"
        else:
            return "컴퓨터 승리"
    else:
        if npcInput == "가위":
            return "컴퓨터 승리"
        else:
            return "플레이어 승리"


main()
