initial_money = 50
goal = 250
wins = 0
win_rate = 0.4

for i in range(100) :
    cash = initial_money
    while cash > 0 and cash < goal:
            if cash < win_rate:
                cash = cash + 1
            else:
                cash = cash - 1
    if cash == goal : wins = wins +1

print(f"승률 설정: {win_rate * 100}%")
print("초기 금액 $%d" % initial_money)
print("목표 금액$%d" % goal)
print("100번 중에서 %d번 성공" % wins)

# 승률이 40%로 설정된 경우, 100번의 시도에서 목표 금액에 도달하는 횟수가 출력됩니다.
# 승률이 낮을수록 목표 금액에 도달하는 횟수가 줄어들게 됩니다.