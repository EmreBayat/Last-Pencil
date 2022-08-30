# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 09:04:22 2022

@author: emre-
"""
import random
msg_1 = "How many pencils would you like to use:"
msg_4 = "Who will be the first (John, Jack):"


msg_2 = "The number of pencils should be numeric"
msg_3 ="The number of pencils should be positive"
msg_5 = "Choose between 'John' and 'Jack'"
msg_6 = "Possible values: '1', '2' or '3'"
msg_9 = "Too many pencils were taken"

def get_input():
    return input()
def check_player_name(x):
    if x.isalpha() == True:
        if x == 'John' or x =='Jack':
            return True
        else:
            print(msg_5)
            return False
def check_initialPencilNum(x):
    try:
        int(x)
        if int(x) > 0 :
            return True
        else:
            print(msg_3)
            return False
    except:
        print(msg_2) 
        return False

def set_pencil(x):
    global pencilNum
    flag = check_initialPencilNum(x)
    if flag == True:
        pencilNum = int(x)
    else:
        set_pencil(get_input())
def set_player(x):
    global Player1
    global turn
    global bot
    if check_player_name(x) == True:
        
        if x == 'John':
            Player1 = x
            turn = 'John'
            bot = 'Jack'
            
        else:
            Player1 = x
            turn = 'Jack'
            bot = 'Jack'
    else:
        print(msg_4)
        set_player(get_input())
def check_remain_pencil(x):
    if x > pencilNum:
        print(msg_9)
        return False
    return True

def take_action():
    
    if bot == turn:
        
        if pencilNum % 4 == 3:
            global chosen_number
            chosen_number = 2
            print(chosen_number)
        elif pencilNum % 4 == 2:
            chosen_number = 1
            print(chosen_number)
        elif pencilNum % 4 == 0:
            chosen_number = 3
            print(chosen_number)
        else:    
            if pencilNum == 1:
                chosen_number=1
                print(chosen_number)
            else:
                chosen_number = random.randint(1, 3)
                print(chosen_number)
                if check_remain_pencil(chosen_number)==True:         
                    chosen_number = chosen_number                
                else:
                    print(turn + "'s turn!")
                    take_action()
            
    else:
        try:
            x = input()
            if int(x) > 0 and int(x) < 4:
                if check_remain_pencil(int(x))==True:            
                    chosen_number = int(x)
                else:   
                    take_action() 
            else:
                print(msg_6)
                take_action()    
        except:
            print(msg_6)
            take_action()

def player_turn():
    global turn
    if turn =="John":
        turn ="Jack"
    else:        
        turn = "John"
        
def print_pencil(x):
    pencils=""
    for i in range(x):
        pencils +='|'
    print(pencils)    


    
print(msg_1)       
set_pencil(get_input())
print(msg_4) 
set_player(get_input())
print_pencil(pencilNum)
print(turn + "'s turn!")
while pencilNum >0:
    take_action()
    pencilNum = pencilNum - chosen_number
    if pencilNum <=0:
        break 
    print_pencil(pencilNum)
    player_turn()  
    print(turn + "'s turn!")
player_turn()  
print(turn + "'s won!")    


           