password = 'a123456'
i = 3 
while True :
    pwd = input(' Please enter the password:') 
    if pwd == password :
        print(' Successful!' )
        break
    else:
        i = i - 1 
        print(' Wrong password! You still have', i , 'chances')
        if i == 0:
            break
