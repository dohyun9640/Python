weight = float(input("몸무게 kg 단위를 입력하시오.:"))
cm = float(input("키를 센티미터 단위로 입력하시오.:"))
height = cm/100
bmi = (weight / (height**2))
print("당신의 BMI=", bmi)