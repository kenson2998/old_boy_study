import random

int_list = [[x for x in range(65, 91)], [x for x in range(97, 123)], [x for x in range(0, 10)]]
checkcode = ''
for i in range(4):
    current = random.sample(int_list[random.randint(0, 2)], 1)
    if current[0] <= 10:
        checkcode += str(current[0])
    else:
        checkcode += str(chr(current[0]))

print(checkcode)

#  老師的寫法
checkcode = ''

for i in range(4):
    current = random.randrange(0, 4)
    if current == i:
        tmp = chr(random.randint(65, 90))
    else:
        tmp = random.randint(0, 9)
    checkcode += str(tmp)

print(checkcode)
