from time import sleep

for number in range(10+1):
    print(number, end="\r")
    sleep(0.5)
    if number >= 10:
        print('shhhhhhhhhhhhh', end="\r")
        sleep(1)
        print(f'BOOOOOOOOOOM!!!', end="\r")
        sleep(2)
        print(f'\033[1;7;31mSILENCE!!!!!!!!\033[m')
