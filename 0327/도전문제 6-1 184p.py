import random

count = 0
trials = 1000
for i in range(trials):
    dice1= random.randint(1, 6)
    dice2 = random.randint(1, 6)
    if dice1 + dice2 == 6:
        count += 1
theoretical_probability = 5 / 36
experimental_probability = count / trials
print(f"총{trials}번 중 합이 6인 횟수: {count}")
print(f"실험적 확률: {experimental_probability:.4f}")
print(f"이론적 확률: {theoretical_probability:.4f}")