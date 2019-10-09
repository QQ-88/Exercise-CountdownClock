import time
import datetime

while True:
    y = input('What year? ')
    m = input('What month? ')
    d = input('What day? ')
    h = input('What hour? ')
    mi = input('What minute? ')
    s = input('What second? ')


    user_date = datetime.datetime(int(y), int(m), int(d), int(h), int(mi), int(s))
    today = datetime.datetime.today()

    if today > user_date:
       print('\n Time in the past, try again.\n')
    else:
        for t in range(5):
            today = datetime.datetime.today()
            diff = user_date - today
            time.sleep(2.5)
            print(f'Remaining time: {diff}')
        break