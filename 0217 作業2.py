'''輸入帳號密碼驗證,錯誤三次就鎖定'''

from 老男孩python import name

ac = []
a = [1, 2, 3, 4, 5]
block_read = open('blockname.txt', 'r')

count = 0
key_account = ''
block = ['a']
doin = True
while doin:

    login_acc = input("login acc:")

    login_pwd = input("login password:")
    for i, n in name.account.items():
        if login_acc == i and login_pwd == n:
            print('you login ok')
            doin = False
            break
    if doin == False:
        break
    if key_account == login_acc:
        count += 1
    key_account = login_acc
    if count > 1 or login_acc in block:
        print(key_account, 'is blocked')
        block.append(key_account)
        count = 0
else:
    print('done')
