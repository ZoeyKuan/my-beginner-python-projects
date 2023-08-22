import random
choices = []

def randomSelect(var):
    listNumber = len(var) + 1
    selected = random.randint(0, len(var))
    print('your randomly selected msg:', var[selected])

print('Welcome to Spin the wheel but without the wheel! To stop type ]/')

while True:
    listNumber = len(choices) + 1
    choice = input('Choice no. ' + str(listNumber) + ':')
    if ']/' in choice:
        #randomSelect(choices)
        selected = random.randint(0, len(choices))
        print('your randomly selected msg:', choices[selected])
        break
    else:
        choices.append(choice)
        listNumber = len(choices) + 1