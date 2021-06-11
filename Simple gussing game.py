count = 5
b = int(input("enter your guess::"))
while b>=10:
    a =int(input("No,Try one more time:"))
    if a<=10:
        print("great")
        break
    if count ==0:
        print("sorry no more chances")
        break
    count = count - 1
else:
    print("great")
