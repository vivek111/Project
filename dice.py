#!/usr/bin/python3
# Dice simulator. Project for http://redd.it/2aaeou
# author: wukaem
 
import random
 
# Two dictionaries containing data to draw every side of 6-sided dice.
# For example side '3' is represented by segments 0, 4, 2, 3, 7 from
# DICE_SEGMENTS printed one below another.
 
DICE_SEGMENTS = {
    0: '   .-------.',
    1: '   |       |',
    2: '   |   O   |',
    3: '   |     O |',
    4: '   | O     |',
    5: '   | O   O |',
    6: '   | O O O |',
    7: "   '-------'",
}
 
SIDE_REPR = (
    (0, 1, 2, 1, 7),
    (0, 3, 1, 4, 7),
    (0, 4, 2, 3, 7),
    (0, 5, 1, 5, 7),
    (0, 5, 2, 5, 7),
    (0, 6, 1, 6, 7),
)
 
 
def dice_img_lst(side):
    """
   Returns list of 5 strings. Every string is one row of dice side image.
   """
    img_lst = []
    for segment_num in SIDE_REPR[side-1]:
        img_lst.append(DICE_SEGMENTS[segment_num])
    return img_lst
 
 
def roll_dice(num):
    """
   Returns list of random integers representing sides of 6-sided dice.
   Parameter num is number of dice that should be rolled.
   """
    return [random.randint(1, 6) for _ in range(num)]
 
 
def dice_image(dice_lst):
    """
   Returns string with all dice presented side by side.
   @dice_lst: list of integers (1 to 6).
   """
    dice_lst_img = []
    for side in dice_lst:
        dice_lst_img.append(dice_img_lst(side))
    rows = []
    for i in range(5):
        rows.append(''.join(segment[i] for segment in dice_lst_img))
    return '\n'.join(rows)
 
 
def ask_question1():
    """
   Function asks question about number of dice. Returns integer from 1 to 5.
   """
    print('\nHow many dice do you want to roll? (1-5)')
    while True:
        ans = input('> ')
        try:
            ans = int(ans)
        except ValueError:
            print('\nGive me a number. Try again.')
            continue
        if ans in range(1, 6):
            return ans
        print('\nRoll at least 1 dice and no more than 5. Try again.')
 
 
def ask_question2(num):
    """
   Function takes number of dice and asks if change this number, leave
   it without change, or quit program. Returns integer from 1 to 5 or -1.
   """
    question = ("Type 'q' to quit, 'c' to change number of dice,\n"
                "or hit <Enter> to roll {} dice again.".format(num))
    print(question)
    new_num = 0
    while not new_num:
        ans = input('> ')
        if ans == '':
            new_num = num
        elif ans.lower()[0] not in ('q', 'c'):
            print('Wrong answer.\n')
            print(question)
            continue
        elif ans.lower()[0] == 'q':
            new_num = -1
        else:
            new_num = ask_question1()
    return new_num
 
 
def main():
    """
   Main function.
   """
    print('\n       Welcome to DICE SIMULATOR')
    no_dice = ask_question1()
    while no_dice != -1:
        print('\n   Rolling {} dice:\n'.format(no_dice))
        dice_list = roll_dice(no_dice)
        print(dice_image(dice_list))
        print('\n   Total: {}\n'.format(sum(dice_list)))
        no_dice = ask_question2(no_dice)
    print('Goodbye!')
 
 
if __name__ == "__main__": main()