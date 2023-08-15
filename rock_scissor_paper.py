import random
SetOfChoices = {1:'rock', 2:'paper', 3:'scissor'}
computer_choices =['rock', 'paper', 'scissor' ]
your_wins = 0
your_losses = 0

while True:
    computer_choice = random.choice(computer_choices)
    print(SetOfChoices)
    user_choice = input('please enter a number from the list:  <enter done for exit>  \n> ' )
    if user_choice == 'done':
        print(f'your wins are equal to {your_wins}  <<<>>>  and your losses are equal to {your_losses}')
        break
    elif (user_choice.isdigit() == 1) or (user_choice.isdigit() == 2) or (user_choice.isdigit() == 3): 
        user_choice = SetOfChoices.get(int(user_choice))
        sharayet_bord_user = ((user_choice =='rock' and computer_choice=='scissor') or \
                            (user_choice=='paper' and computer_choice=='rock') or \
                            (user_choice=='scissor' and computer_choice=='paper'))
        sharayet_bord_computer = ((user_choice=='scissor' and computer_choice=='rock') or \
                                (user_choice=='rock' and computer_choice=='paper') or \
                                (user_choice=='paper' and computer_choice=='scissor'))
        sharayet_draw = ((user_choice=='scissor' and computer_choice=='scissor') or \
                        (user_choice=='rock' and computer_choice=='rock') or \
                        (user_choice=='paper' and computer_choice=='paper'))
        x = (f'your choice is {user_choice} and computer choice was {computer_choice}')
        if sharayet_bord_user:
            your_wins+=1
            print('>>>>> you win <<<<< \n>>>>', x,'\n')
        elif sharayet_bord_computer:
            your_losses+=1
            print('>>>>> you loose <<<<< \n>>>>', x, '\n') 
        elif sharayet_draw:
            print('>>>>> draw <<<<< \n>>>>', x, '\n')
        else:
            print('You entered wrong number!! \n\n ')
            pass
    else:
        print('enter wrong value :(  please enter a number from 1 to 3  \n\n ')