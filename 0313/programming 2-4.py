hours = int(input("시간을 입력하시오: "))
minutes = int(input("분을 입력하시오: "))

seconds = (hours*3600) + (minutes*60)

print(hours, "시간", minutes, "분은", seconds, "초입니다.")