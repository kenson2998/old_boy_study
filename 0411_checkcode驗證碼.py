import random

int_list = [[x for x in range(65,91)],[x for x in range(97,123)],[x for x in range(0,10)]]
checkcode = ''

for i in range(4):
    current = random.sample(int_list[random.randint(0, 2)], 1)
    if current[0] <= 10:
        checkcode += str(current[0])
    else:
        checkcode += str(chr(current[0]))

print(checkcode)