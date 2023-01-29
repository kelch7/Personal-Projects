#Rock, paper, scissors 
import random
def play():
   
    user_pick = input('Rock, Paper or scissors?\n').capitalize()
    print('You picked '+ user_pick)
    picks=['Rock', 'Paper', 'Scissors']
    Opponent_pick = random.choice(picks)
    print('Computer picked '+Opponent_pick)
    #Game begins with if/else statements
    if user_pick == 'Rock': 
        if Opponent_pick == 'Rock':
            print('It is a Tie')
        elif Opponent_pick == 'Paper':
            print('Opponent wins')
        elif Opponent_pick == 'Scissors':
            print('You Win')        
    elif user_pick == 'Paper':
        if Opponent_pick == 'Paper':
            print('It is a Tie')
        elif Opponent_pick == 'Rock':    
            print('You win!')
        elif Opponent_pick == 'Scissors':
            print('Opponent wins!')
    elif user_pick == 'Scissors':
        if Opponent_pick == 'Scissors':
            print('It is a tie!')
        elif Opponent_pick == 'Rock':
            print('Opponent wins! cause Rock smashes scissors!')
        elif Opponent_pick == 'Paper':
            print('You win! cause Scissors tears Paper!')
    else:
        print('You have to pick either rock or paper or scissors')
def main():
    x = input('Hello Friend! Want to play a game?\nyes or no?\n').lower()
    if x == 'yes':
        play()
    else:
        exit()   
    while True:
        pick2 = input('Do you want to play again?\nyes or no ? \n').lower()
        if pick2 == 'yes':
            play()
        else:
            break
main()                                        