import random
print("행운의 매직볼로 오늘의 운세를 출력합니다. ")
answers = random. randint(1, 8)
if answers == 1:
    print("확실히 이루어집니다.")
elif answers == 2:
    print("좋아 보이네요")
elif answers == 3:
    print("믿으셔도 됩니다.")
elif answers == 4:
    print("저의 생각은 괜찮을지도 모릅니다.")
elif answers == 5:
    print("아무일도 없을 겁니다.")
elif answers == 6:
    print("집밖에 나가지 마시죠.")
else:
    print("다시 질문해주세요.")