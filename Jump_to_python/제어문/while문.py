# while
treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 {}번 찍었습니다.".format(treeHit))
    if treeHit == 10:
        print("나무 넘어갑니다.")

# while문 만들기 예제

prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number: """

number = 0
while number != 4:
    print(prompt)
    number = int(input())

# break
# coffee 자판기 예제

coffee = 10
while money:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("돈을 받았으니 커피를 줍니다.")
        coffee -= coffee
    elif money > 300:
        print("거스름돈 {}를 주고 커피를 줍니다.".format(money-300))
        coffee -= coffee
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다")
        print("남은 커피의 양은 {}개 입니다.".format(coffee))
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break

# continue
a = 0
while a < 10:
    a += 1
    if a % 2 == 0 : continue
    print(a)

# 무한 루프
while True:
    print("Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.")

