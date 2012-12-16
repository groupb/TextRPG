###  Lost in Code Demo. C. Sgro, A.Mamyshev , M.Seegar , N. Alkaydi
#------------------------IMPORTED STUFFS-----------------------------------------
import sys
import time
from os import system
import pickle
import string
from random import randrange

#----------------------------EYE CANDY STUFFS------------------------------------
def print_b(str):
    print ('||',end=""), print (str, end="") , print ('||')

def deco():
    print ('||',end="")
    for b in range (22):
        print ('_|__',end="")
    print ('||')
    print ('||',end="")
    for b in range (22):
        print ('__|_',end="")
    print ('||')
#============================PLAYER PARAMS=======================================
health = 100
stamina = 100
intelligence = 0
player_inventory_init= ['']

#----------------------------Print Slow------------------------------------------
def save_inventory_initial():
    with open ('player_stats.txt','wb') as file:
        pickle.dump(player_inventory_init, file)

def open_inventory():
    with open ('player_stats.txt','rb') as file:
        global player_inventory
        player_inventory = pickle.loads(file.read())
        return player_inventory

def save_inventory():
    with open ('player_stats.txt','wb') as file:
        pickle.dump(player_inventory, file)


def print_slowly(str):
    for char in str:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
##        str.ljust(50,' ')

def check_player_params():
        print (health)
        print (stamina)
        print (intelligence)
    

#============================ACT 1================================================
#----------------------------RANDOMIZED EVENTS------------------------------------

def wake_up_1_bad_ladder():
    deco()
    print_b(' The ladder was not fixed properly. You are unfortunate enough to find that out having  ')
    print_b(' made third of the way up. You fall down. Going into the apartment [b]lock is the only  ')
    print_b('option now.                                                                             ')
    deco()
    global health
    health = health - 15
    while 1:
        action = input('>>')
        if action == 'health':
            check_player_params()
        if action == 'b':
            wake_up_1_aparments()          
        if action not in ['health', 'b']:
            print ('Wrong')
    wake_up_1_aparments()
    

def wake_up_1_good_ladder():
    print ('You climb the ladder successfully!') 
    wake_up_1_rooftop()

def wake_up_1_ladder_randomizer():
    randomize = ['1', '2']
    random_index = randrange(0,len(randomize))
    if randomize[random_index] == '1':
        wake_up_1_good_ladder()
    if randomize[random_index] == '2':
        wake_up_1_bad_ladder() 
    
    




#----------------------------MAIN STUFFS------------------------------------------
def wake_up_intro():
    print(' Lost in Code Demo. C. Sgro, A.Mamyshev , M.Seegar , N. Alkaydi ')
    print('')
    print('                         000                   00                            00 ')                                          
    print('                         000                   00                            00 ')                                          
    print('                         0001                  00                            00 ')                                          
    print('                         0 00 000 00 00  100   00 00  100   00101   100   10100 ')                                          
    print('                        00 00  00 00 00  0000  00 0  00 00  00000  00 00  00000 ')                                          
    print('                        00 00  00100 00    101 0000  00  01 00 00  00 10 001 00 ')                                          
    print('                        000001 00000 00  00001 00001 000000 00 00 100000 00  00 ')                                          
    print('                       1000000  000010  00  01 00 00 00     00 00  00    001 00 ')                                          
    print('                       001  00  001100  000001 00 00 00000  00 00  00000  00000 ')                                          
    print('                       00   00  00 100   00 00 00 000 1001  00 00   100   10 00 ')
    print('')
    print('')
    wake_up()

def wake_up():
    save_inventory_initial()
    deco() 
    print_b(' You wake up in the middle of the street. Your head hurts, you feel weak. However, you  ')
    print_b(' finally stand up realizing that sleeping in the middle of the street is not that smart ')
    print_b(' of an idea. You have to keep [m]oving.                                                 ')                                                       
    deco() 
    while 1:
        action = input('>>')
        if action == 'm':
            wake_up_1()
        if action not in ['m']:
            print('Wrong')



def wake_up_1():
    deco()
    print_b(' As you walk, you start realizing that streets are completely empty. Not a living soul. ')
    print_b(' You prefer to completely ignore this fact, however. The headache is killing you. You   ')
    print_b(' notice that there is a [ph]armacy right in front you. That is a good place to get meds.')
    print_b(' There\'s also a [s]edan type of vehicle on the opposite side of the street. It\'s trunk  ')
    print_b(' seems to be open.                                                                      ')
    print_b(' Hint: type \'health\' to see your HP.                                                    ')
    deco()
    while 1:
        action = input('>>')
        if action == 'health':
            check_player_params()
        if action == 's':
            wake_up_1_sedan()
        if action == 'ph':
            wake_up_1_pharmacy()
        if action not in ['s', 'health', 'ph']:
            print ('Wrong')
            
        
def wake_up_1_sedan():
    open_inventory()
    global player_inventory
    for item in player_inventory:
        
        if item == 'Hammer':
            deco()
            print_b(' There\'s nothing in the trunk anymore.                                                  ')
            deco()
            break
        elif 'Hammer' not in player_inventory:
            deco()
            print_b(' You approach the vehicle and find a hammer.                                            ')
            deco()
            player_inventory.append('Hammer')
            save_inventory()
            break


def wake_up_1_pharmacy():
    open_inventory()
    global player_inventory
    if 'Hammer' not in player_inventory:
        deco()
        print_b(' You approach the pharmacy. You attempt to open the door but it just won\'t open. You    ')
        print_b(' realize you need some kind \of tool to break the window and enter the pharmacy.        ')
        deco()
    elif 'Hammer' in player_inventory:
        deco()
        print_b(' You approach the window of the pharmacy and smash it with the hammer. You finally      ')
        print_b(' proceed inside. You see three stands with all kinds of medicine. You approach the one  ')
        print_b(' of the stands and You pick up a box with generic Asperine and take a handful of pills..')
        print_b(' You decide to sit down and just wait until the headache goes away...                   ')
        player_inventory.pop(1)
        save_inventory()
        wake_up_1_medicine()


def wake_up_1_medicine():
    deco()
    print_b(' 30 minutes later...                                                                    ')
    deco()
    print_b(' The headache is gone. You feel much better. You decide to find out what\'s going on and ')
    print_b(' the only way to find out what\'s going on is by getting on some rooftop. You use a  ')
    print_b(' backdoor to exit the pharmacy. You enter a small yard and you see a [l]adder that leads')
    print_b(' to the top of the building opposite of you, as well as an entrance to what seems like  ')
    print_b(' an apartment [b]lock.                                                                  ')
    deco()
    while 1:
        action = input('>>')
        if action == 'health':
            check_player_params()
        if action == 'l':
            wake_up_1_ladder_randomizer()
        if action == 'b':
            wake_up_1_aparments()          
        if action not in ['l', 'health', 'b']:
            print ('Wrong')

def wake_up_1_aparments():
    deco()
    print_b(' You enter the apartment block. The staircase leading to the rooftop is unnaturally     ')
    print_b(' clean and shiny, like everything you have seen since you woke up. You [c]ontinue along ')
    print_b(' the staircase...                                                                       ')
    deco()
    while 1:
        action = input('>>')
        if action == 'health':
            check_player_params()
        if action == 'c':
            wake_up_1_rooftop()
        if action not in ['c', 'health']:
            print ('Wrong')
    
    

        
def wake_up_1_rooftop():
    deco()
    print_b(' You successfully reach the rooftop. The first thing you notice that the entire city is ')
    print_b(' dead. Not only the area where you are at but... everything. Clouds haven\'t moved since ')
    print_b(' you first woke up. It almost seems like this city is not even real... You feel the     ')
    print_b(' presence of some entity behind you... Your curiosity makes you [t]urn around...        ')
    deco()
    while 1:
        action = input('>>')
        if action == 'health':
            check_player_params()
        if action == 't':
            wake_up_1_robot_encounter()
        if action not in ['t', 'health']:
            print ('Wrong')
            
    
    
        
    
def wake_up_1_robot_encounter():
    deco()
    print_b(' Entity:                                                                                ')
    print_b('         Welcome to the paradise. Man-made paradise. The perfect world full of numerous ')
    print_b(' opportunities. Too bad that you are alone here and have no idea what will happen if ')
    print_b(' you stay long enough... Let me help you.                                               ')

    weak = " Your attack is ineffective, I'd suggest learning a skill or aquiring a weapon.         "
    run = " Your fleeing leads to a dead end, time to turn back and face your fears.               " 
    print_b(' You:                                                                                   ') 
    print_b(' [W]here am I, and what in God\'s carnation are you?                                     ')
    print_b(' [A]ttack the android or [R]un away with fright.                                        ') 
    deco()
    while 1:
        action = input('>>')
        if action == 'W':
            wake_up_1_robot_encounter_2()
        if action == 'A':
            deco()
            print_b(weak)
            deco()
        if action == 'R':
            deco()
            print_b(run)
            deco()
        if action not in ['W','A','R']:
            print('incorrect')
            
def wake_up_1_robot_encounter_2():
    deco()
    print_b(' Entity:                                                                                ')
    print_b(' I am a program, man was my creator.You are in the paradise, or, as you perceive it, a  ')
    print_b(' virtual world. Numerous opportunities. You cannot stay here for too long unfortunately ')
    print_b(' otherwise your body that is somewhere out there will shut down... forever. Let me help ')
    print_b(' you with some things that will help you escape.                                        ')    
    wake_up_1_problem_1()

def wake_up_1_problem_1():
    deco()
    print_b(' Entity:                                                                                ')
    print_b(' You will need to solve certain puzzles to get out of the Paradise. The way youcan solve')
    print_b(' this is by putting in string number and the property assigned to the parameter,for     ')
    print_b(' example: 3 %None% ,or, 5 brick01IM.                                                    ')
    print_b(' In this case, you have to walk through the wall so tampering with the collision model  ')
    print_b(' of the object seems like a good idea...                                                ')
    deco()
    print_b(' def brick_wall_shader_1():                                                             ')
    print_b(' 1. BASE_TEXTURE_PARAMETER = brck01                                                     ')
    print_b(' 2. NORMAL_MAP_PARAMETER = brck01NM                                                     ')
    print_b(' 3. SPECULAR_MAP_PARAMETER = brck01SM                                                   ')
    print_b(' 4. BASE_PHYS_PARAMETER = brick                                                         ')                                           
    print_b(' 5. SELF_ILLUMINATION_PARAMETER = %None%                                                ')
    print_b(' 6. COLLISION_PARAMETER = SOLID                                                         ')                                           
    deco()
    while 1: 
        x = input(str('>> '))
        if x == '6 %None%':
            deco()
            print_b(' Entity:                                                                                ')
            print_b(' It wasn\'t that hard now, was it? Let\'s move on...                                      ')
            wake_up_1_problem_2()
        if x != '6 %None%':
            deco()
            print_b(' Entity:                                                                                ')
            print_b(' This is not the right answer. For every incorrect answer, you lose Stamina. Once it    ')
            print_b(' drains to 0, you will start losing your health points. Good thing that I\'m here with   ')
            print_b(' you right now. You don\'t lose anything.                                                ') 
       
            
    
    

def wake_up_1_problem_2():
    deco()
    print_b(' Entity:                                                                                ')
    print_b(' So dark around here. So you might want to turn the light. You want to type string      ')
    print_b(' number, for example, 5, and then a set of properties associated with the function. So  ')
    print_b(' ideally it should look like  (5 (NO_FILL, 70) ). Be careful though, doing something    ')
    print_b(' like that will make the floor disappear. What happens next is a mystery.               ')
    deco()
    print_b(' 1. brick_wall_shader_1(150,50,0)                                                       ')
    print_b(' 2. brick_wall_shader_1(0,50,0)                                                         ')
    print_b(' 3. brick_wall_shader_1(0,0,0)                                                          ')
    print_b(' 4. brick_wall_shader_1(150,0,0)                                                        ')
    print_b(' 5. tiled_floor_shader_344(FILL_FLAT, 0)                                                ')
    print_b(' 6. concrete_shader_4315(FILL_FLAT, 60)                                                 ')
    print_b(' 7. light_object(directional, gen_lamp.obj)                                             ')  
    print_b(' 8. light_active (0)                                                                    ')
    deco()
    while 1:
        x = input(str('>> '))
        if x == '8 (1)':
            deco()
            print_b(' Entity:                                                                                ')
            print_b(' Still a bit too dark here... But let\'s move on.                                       ')
            print_b(' Now that you know the basic, I need you to return a favor. I need to obtain certain    ')
            print_b(' items that I am not programmed to find. It is rather complicated. I need you to find   ')
            print_b(' those for me. I will tell you the rest soon enough.                                    ') 
            deco()
        if x != '8 (1)':
            deco()
            print_b(' Entity:                                                                                ')
            print_b(' That is not correct. Be careful with walls. You don\'t want to move those.              ')
            deco()

    
            
wake_up_intro()     





