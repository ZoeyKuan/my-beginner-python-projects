import random
l = []
while True:
    c = input('Welcome to spin the wheel but with no wheel\nChoice {}: '.format(len(l)+1))
    l.append(c)
    if c == 'stop':
        b = random.sample(l, 1)
        print('We chose...', b[0])
        break
