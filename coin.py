import random


user_cointoss = input('Heads or Tails?\n').capitalize()
print('You picked ' + user_cointoss)
picks = ['Heads', 'Tails']
cointoss_random = random.choice(picks)
print('coin landed on', cointoss_random)


if user_cointoss == cointoss_random:
    print('you win!')
else:
    print('you lost boy!!!!!!!!!!!')