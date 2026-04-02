user = ""
password = ""
while user != "admin" or password != "pythonisfun":
    user = input("사용자 이름을 입력하시오: ")
    password = input("암호를 입력하시오: ")
    if user != "admin" or password != "pythonisfun":
        print("사용자 이름 또는 암호가 잘못되었습니다. 다시 시도하십시오.")
print("로그인 성공")