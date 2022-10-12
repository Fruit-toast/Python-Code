import time
import random
print("Hello, I am going to be breaking your password")
print("First, please put in if it will be a pin or a password, a password can contain numbers, a pin cannot contain letters.")
v1 = '0'
while v1 != '1' and v1 != '2' and v1 !='3' and v1 != '4':
    v1 = input("Please type 1 for password, 2 for a 4 digit pin, 3 for a 6 digit pin and 4 for an 8 digit pin: ")
if v1 == '1':
    print('ok')
    len_pass = 0
    while len_pass != -1:
        passw = list(input('Enter a password: '))
        len_pass = int(len(passw))
        if len_pass >= 7:
            print('Please input a shorter password')
        else:
            break
    chars = list('abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890')
    test_pass = []
    start = time.time()
    while(test_pass != passw):
        test_pass = random.sample(chars, len_pass)
    end = time.time()
    print('Password found after ', int(start-end) ,' seconds! ', test_pass)
elif v1 == '2':
    print('Ok')
    PIN = input('Please Put in a 4-digit PIN: ')
    tralse = PIN.isnumeric()
    if str(tralse) == 'False' or len(PIN) != 4:
        print('that is not a valid PIN')
    else:
        print('that is a valid PIN, the test will begin shortly.')
        def time_convert(sec):
            mins = sec // 60
            sec = sec % 60
            hours = mins // 60
            ins = mins % 60
            print("Time Lapsed = {0}:{1}:{2}" .format(int(hours),int(ins),sec))
    start_time = time.time()
    CrackedPIN = random.randint(0,9999)
    while CrackedPIN != PIN:
        CrackedPIN = int(CrackedPIN) + 1
        CrackedPIN = str(CrackedPIN)
        while len(CrackedPIN) < 4:
            CrackedPIN = ('0' + str(CrackedPIN))
        #print(CrackedPIN)
        if CrackedPIN == '10000':
            CrackedPIN = '0'
    end_time = time.time()
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)

elif v1 == '3':
    print('Ok')
    PIN = input('Please Put in a 6-digit PIN: ')
    tralse = PIN.isnumeric()
    if str(tralse) == 'False' or len(PIN) != 6:
        print('that is not a valid PIN')
    else:
        print('that is a valid PIN, the test will begin shortly.')
        def time_convert(sec):
            mins = sec // 60
            sec = sec % 60
            hours = mins // 60
            ins = mins % 60
            print("Time Lapsed = {0}:{1}:{2}" .format(int(hours),int(ins),sec))
        start_time = time.time()
        CrackedPIN = random.randint(0,999999)
        while CrackedPIN != PIN:
            CrackedPIN = int(CrackedPIN) + 1
            CrackedPIN = str(CrackedPIN)
            while len(CrackedPIN) != 6:
                CrackedPIN = ('0' + str(CrackedPIN))
            if CrackedPIN == '999999':
                CrackedPIN = '0'
            #print(CrackedPIN)
    end_time = time.time()
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)

elif v1 == '4':
    print('Ok')
    PIN = input('Please Put in a 8-digit PIN: ')
    tralse = PIN.isnumeric()
    if str(tralse) == 'False' or len(PIN) != 8:
        print('that is not a valid PIN')
    else:
        print('that is a valid PIN, the test will begin shortly.')
        def time_convert(sec):
            mins = sec // 60
            sec = sec % 60
            hours = mins // 60
            ins = mins % 60
            print("Time Lapsed = {0}:{1}:{2}" .format(int(hours),int(ins),sec))
    start_time = time.time()
    CrackedPIN = random.randint(0,99999999)
    while CrackedPIN != PIN:
        CrackedPIN = int(CrackedPIN) + 1
        CrackedPIN = str(CrackedPIN)
        while len(CrackedPIN) != 8:
            CrackedPIN = ('0' + str(CrackedPIN))
        #print(CrackedPIN)
        if CrackedPIN == '99999999':
            CrackedPIN = '0'
    end_time = time.time()
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
print('Finished')
