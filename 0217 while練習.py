#while 練習


age =56
count = 0
while count < 3 :
    guess_age = int(input("guess:"))

    if guess_age > age :
        print('too bigger')
    elif guess_age == age :
        print('you got it.')
        break
    else :
        print('smaller')

    count += 1
    if count == 3 :
        countine_confirm = input('do you want to keep guessing?')
        count = 0