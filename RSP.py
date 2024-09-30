import random


result = 0

while result==0:
  user = input("가위, 바위, 보 중 하나를 선택하세요:")

  if(user == '가위'): userr = 1
  elif(user == '바위'): userr = 2
  else: userr = 3
  com = ['가위','바위','보']
  comcho = random.choice(com)
  if(comcho == '가위'): comr = 1
  elif(comcho == '바위'): comr = 2
  else: comr = 3

  #가위, 바위, 보에 각각 숫자를 부여하여 비교하기 쉽게함

  if(userr-comr == -1 or userr-comr == 2):
    print("컴퓨터가 이겼습니다!")
    #print(comcho)
    result+=1
  elif(userr-comr == 0):
    print("무승부입니다!")
    #print(comcho)
  else:
    print("당신이 이겼습니다!")
    #print(comcho)
    result+=1

    #조건문 안의 주석을 풀면 컴퓨터가 랜덤으로 선택한 가위, 바위, 보를 볼 수 있음
