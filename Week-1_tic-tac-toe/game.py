import random
# create matrix 3x3 as battle field, digit are used as move's coordinate
field = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]
# combination whiches can bring Victory
win_positions = [
                (1,2,3,),
                (4,5,6,),
                (7,8,9,),
                (1,5,9,),
                (3,5,7,),
                (1,4,7,),
                (2,5,8,),
                (3,6,9,),
                 ]

# some additional vars
all_steps = [1,2,3,4,5,6,7,8,9]
computer_steps_history = []
person_steps_hystory = []

cross_or_zero = ['0', 'X']
status = False

person_sign = random.choice(cross_or_zero) # random choise sign for person
cross_or_zero.remove(person_sign)
computer_sign = cross_or_zero[0]



def computer_step():
    step = random.choice(all_steps)
    computer_steps_history.append(step)
    all_steps.remove(step)
    print(f"Computer's step is {step}")
    return step
        
        


# func for human steps, choose a step, save it to history, delete from all steps list 
def person_move():
    move = input("Ваш ход! ")
    # check move is digit 
    while move.isdigit()is not True:
        move = input("Выберете другой ход! ")
    # check if move is free
    if int(move) in all_steps:
        move = int(move)
        person_steps_hystory.append(move)
        all_steps.remove(move)
        return move
    else:
        move = input("Выберете другой ход! ")

# check  if there is winning combination 
def check_status(lst:list)-> bool:
    for steps in win_positions:
        if set(steps).issubset(lst):
            return True
# just for printing matrix with actual information
def print_matrix():        
    for row in field:
        print(*row)
    print('#'* 90)

# this func for changing digit to player's
def change_sign(sign, step):
    for i in range(len(field)):
        if step in field[i]:
            field[i][field[i].index(step)] = sign
            break
# main func for game
def game_processing():
    print(f"You play with {person_sign}")
    print_matrix()
    global status   
    while status != True:
        if len(all_steps) > 0:
            change_sign(person_sign,person_step())
            status = check_status(person_steps_hystory)
            print_matrix()
            print(f"You play with {person_sign}")
            print(f"Computer play with {computer_sign}")
            if status == True:
                message = f"The Winner is {person}"
                break
            else:
                change_sign(computer_sign,computer_step())
                status = check_status(computer_steps_history)
                print_matrix()
                if status == True:
                    message = "The Winner is Computer"
                    break
        else:
            message = "it is Draw"
            return message
    return message
person = input("Let's start game, What's your name ")
print(game_processing())