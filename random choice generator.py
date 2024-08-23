import random
l = []
c = ''
mode = input('Welcome to spin the wheel but with no wheel\n1 to Choose one thing\n2 to reorder everything')
while c != 'stop':
    c = input('Choice {}: '.format(len(l)+1))
    l.append(c)
l.pop()
if mode == '1':
    print('We chose...', random.sample(l, 1))
if mode == '2':
    str = ''
    shuffled = random.sample(l, len(l))
    for i in range(len(shuffled)):
        if i < len(shuffled)-1:
            str += shuffled[i] + ', '
        else:
            str += shuffled[i]
    print('Reordered...\n'+str)
