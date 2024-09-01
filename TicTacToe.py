import os
import sys

clear = lambda:os.system('cls')
symbol = ''

 #used to display the game function
def game_disp(row1, row2, row3):
    
    
    
    print("   " + ' | ' + "   " + ' | ' + "   ")
    print(' ' + row1[0] + ' ' + ' | '+' ' + row1[1] +' '+ ' | '+' ' + row1[2]+ ' ')
    print("   " + ' | ' + "   " + ' | ' + "   ")
    print("---------------")
    print("   " + ' | ' + "   " + ' | ' + "   ")
    print(' ' + row2[0] + ' ' + ' | '+' ' + row2[1] +' '+ ' | '+' ' + row2[2]+ ' ')
    print("   " + ' | ' + "   " + ' | ' + "   ")
    print("---------------")
    print("   " + ' | ' + "   " + ' | ' + "   ")
    print(' ' + row3[0] + ' ' + ' | '+' ' + row3[1] +' '+ ' | '+' ' + row3[2]+ ' ')
    print("   " + ' | ' + "   " + ' | ' + "   ")
   


    

     
     
#Asking user to select a symbol
def take_input():
    while(True):
        symbol = input("Choose symobl (X, 0): ").upper()
        if symbol not in ['X', '0']:
            print('Please Choose Either X or 0(zero)')
            input()
            clear()
        else:
            break
    
    print("Player 1 is "+ symbol+' Press Enter to continue: ')
    input()
    return symbol

#creating the sequence of the game  
def setValue(symbol):
    if symbol == 'X':
        play_sequence = ['#','X', '0', 'X', '0', 'X', '0', 'X', '0', 'X']
    else:
        play_sequence = ['#','0', 'X', '0', 'X', '0', 'X', '0', 'X', '0']
         

    return play_sequence

def game_check(row1, row2, row3, game_list):
    mark=""
    if (row1[0] == row1[1] == row1[2] == 'X' or row1[0] == row1[1] == row1[2] == '0'):
        mark = row1[0]
        return (True, mark)
    elif (row2[0] == row2[1] == row2[2] == 'X' or row2[0] == row2[1] == row2[2] == '0'):
        mark = row2[0]
        return (True, mark)
    elif (row3[0] == row3[1] == row3[2] == 'X' or row3[0] == row3[1] == row3[2] == '0'):
        mark = row3[0]
        return (True, mark)
    elif ((row1[0] == row2[0] == row3[0] == 'X' or row1[0] == row2[0] == row3[0] == '0')):
        mark = row1[0]
        return (True, mark)
    elif ((row1[1] == row2[1] == row3[1] == 'X' or row1[1] == row2[1] == row3[1] == '0')):
        mark = row1[1]
        return (True, mark)
    elif ((row1[2] == row2[2] == row3[2] == 'X' or row1[2] == row2[2] == row3[2] == '0')):
        mark = row1[2]
        return (True, mark)
    elif ((row1[0] == row2[1] == row3[2] == 'X' or row1[0] == row2[1] == row3[2] == '0')):
        mark = row1[0]
        return (True, mark)
    elif ((row1[2] == row2[1] == row3[0] == 'X' or row1[2] == row2[1] == row3[0] == '0')):
        mark = row1[2]
        return (True, mark)
    elif len(game_list) <= 1:
        return ('Draw', mark)
    else:
        return (False, mark)

def game_logic(game_list, symbol):
    row1 = [" ", " ", " "]
    row2 = [' ', ' ', ' ']
    row3 = [' ', ' ', ' ']
    position  = []
    stp = True
    while(stp):
        clear()
        game_disp(row1, row2, row3)
        val_pos = int(input("Please Enter the position (1 to 9): "))
        if val_pos not in position:
            if val_pos <=3:
                position.append(val_pos)
                row1[val_pos-1] = game_list.pop(1)
            elif val_pos <=6:
                position.append(val_pos)
                row2[val_pos-4] = game_list.pop(1)
            elif val_pos <=9:
                position.append(val_pos)
                row3[val_pos-7] = game_list.pop(1)
            else:
                print("Invalid position!!")
                
            check, mark = game_check(row1, row2, row3, game_list)    
            if check == True and mark == symbol:
                clear()
                game_disp(row1, row2, row3)
                print(f"Player1 '{mark}' wins the game ")
                stp = True
                input()
                break
            elif check ==  True and mark != symbol:
                clear()
                game_disp(row1, row2, row3)
                print(f"Player2 '{mark}' wins the game ")
                stp = True
                input()
                break      
            elif check == 'Draw':
                clear()
                game_disp(row1, row2, row3)
                print("This game is a Draw")
                stp = True
                input()
                break
            else:
                pass
              
            
        else:
            print('That position is occupied.')
            input()
            continue
    play_again()
    
    
def play_again():
    clear()
    val = input('Do you want to play again (y/n): ') 
    if val == 'y' or val == 'Y':
        game_play()
    elif val == 'n' or val == 'N':
        sys.exit() 
    else:
        sys.exit() 
    

def game_play():
    
    symbol = take_input()
    game_list = setValue(symbol)
    game_logic(game_list, symbol)
    
    
game_play() 