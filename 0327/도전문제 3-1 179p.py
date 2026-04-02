import random

tries = 0
guess = 0
answer = random.randint(1,100)

print("1부터 100 사이의 숫자를 맞추시오")

while guess != answer and tries < 10:
    guess = int(input("숫자를 입력하시오: "))
    tries = tries + 1
    if guess < answer:
        print("너무 낮음!")
    elif guess > answer:
        print("너무 높음!")

if guess == answer:
    print("축하합니다. 시도횟수=", tries)
else:
    print(f"아쉽네요. 10번의 기회를 모두 사용했습니다. 정답은 {answer}였습니다.")