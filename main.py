import os
import time
import random

#linklist = ['https://google.com', 'https://hulu.com', 'https://peacock.com', 'https://apply.duq.edu', 'https://amazon.com', 'https://youtube.com', 'https://reddit.com', 'https://www.transferology.com/index.htm', 'https://www.parchment.com/', 'https://apply.commonapp.org/']
linklist = ['https://google.com']
linklist2 = linklist
param1 = abs(int(input('Shortest amount of time (s)? ')))
param2 = abs(int(input('Longest amount of time (s)? ')))

if param2 <= param1:
    print('Upper bound insufficient. Rectifying... ')
    param2 += param1
    param2 += 2

while True:
    if len(linklist) == 1:
        linklist = linklist2
    else:
        pass
    x = random.choice(linklist)
    y = random.randint(param1, param2)
    if len(linklist) > 1:
        linklist.remove(x)
    else:
        pass
    time.sleep(y)
    os.system(f'open {x}')