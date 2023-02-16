import time

for number in range(30+1):
    print(number, end="\r")
    time.sleep(0.5)
    if number >= 30:
        print(f'BOOOOOOOOOOM!!!')
          