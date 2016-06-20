# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 12:24:53 2016

@author: Josh
"""
import random

def print_menu():
    print('Welcome to Rock Paper Scissors')
    print('1. Start a new game')
    print('2. Quit')
    print()
    
menu_choice = 0
print_menu()
while menu_choice != 2:
    print()    
    print_menu()
    try:    
        menu_choice = int(input('Select from the Menu: '))
        if menu_choice == 1:
            print()
            player = str(input('Type: Rock, Paper, or Scissors?\n'))
            print()
            comp = random.randint(1,3)
            if player == 'Rock' or player == 'rock':
                    if comp == 1:
                        print("It's a tie!")
                    elif comp == 2:
                        print("Paper beats Rock, you lose.")
                    else:
                        print("Rock beats Scissors, you win!")
            elif player == 'Paper' or player == 'paper':
                    if comp == 1:
                        print("Paper beats Rock, you Win!")
                    elif comp == 2:
                        print("It's a tie!")
                    else:
                        print("Scissors beats Paper, you lose.")
            elif player == 'Scissors' or player == 'scissors':
                    if comp == 1:
                        print("Rock beats Scissors, you lose.")
                    elif comp == 2:
                        print("Scissors beats Paper, you win!")
                    else:
                        print("It's a tie.")
            else:
                    print("Please chose Rock, Paper, or Scissors.")
    except ValueError:
        print("Please choose from the menu.")
