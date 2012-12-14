###  Lost in Code Demo. C. Sgro, A.Mamyshev , M.Seegar , N. Alkaydi
#------------------------IMPORTED STUFFS-----------------------------------------
import sys
import time
from os import system
import pickle
import string
from random import randrange
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
        player_inventory = pickle.loads(file.read())
        global player_inventory
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
    print('The ladder was not fixed properly. You are unfortunate enough to find that out having made \
third of the way up. You fall down. Going into the apartment block is the only option now')
    global health
    health = health - 15
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
    print_slowly('You wake up in the middle of the street. Your head hurts, you feel weak. However, you finally stand up \
realizing that sleeping in the middle of the street is not that smart of an idea. You have to keep [m]oving.')
    while 1:
        action = input('>>')
        if action == 'm':
            wake_up_1()
        if action not in ['m']:
            print('Wrong')



def wake_up_1():
    print ('As you walk, you start realizing that streets are completely empty. Not a living soul. You prefer to completely \
ignore this fact, however. The headache is killing you. You notice that there is a [ph]armacy right in front you. \
That is a good place to get meds. There\'s also a [s]edan type of vehicle on the opposite side of the street. \
Its trunk seems to be open. ')
    print ('Hint: type \'health\' to see your HP.')
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
            print ('There\'s nothing in the trunk anymore. ')
            break
        elif 'Hammer' not in player_inventory:
            print ('You approach the vehicle and find a hammer.') 
            player_inventory.append('Hammer')
            save_inventory()
            break


def wake_up_1_pharmacy():
    open_inventory()
    global player_inventory
    if 'Hammer' not in player_inventory:
        print ('You approach the pharmacy. You attempt to open the door but it just won\'t open. You realize you need some kind \
of tool to break the window and enter the pharmacy.')
    elif 'Hammer' in player_inventory:
        print ('You approach the window of the pharmacy and smash it with the hammer. You finally proceed inside. \
You see three stands with all kinds of medicine. You approach the one of the stands and You pick up a box with generic \
Asperine and take a handful of pills... You decide to sit down and just wait until the headache goes away... \
headache go away.')
        player_inventory.pop(1)
        save_inventory()
        wake_up_1_medicine()


def wake_up_1_medicine():
    print ('30 minutes later...')
    print ('The headache is gone. You feel much better. You decide to find out what\'s going on and the only way way to find out \
what\'s going on is by getting on some rooftop. You use a backdoor to exit the pharmacy. You enter a small yard and you see \
a [l]adder that leads to the top of the building opposite of you, as well as an entrance to what seems like an apartment [b]lock.')
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
    print('You enter the apartment block. The staircase leading to the rooftop is unnaturally clean and shiny, like everything you have seen since you woke up. \
You [c]ontinue along the starcase...')
    while 1:
        action = input('>>')
        if action == 'health':
            check_player_params()
        if action == 'c':
            wake_up_1_rooftop()
        if action not in ['c', 'health']:
            print ('Wrong')
    
    

        
def wake_up_1_rooftop():
    print ('You successfully reach the rooftop. The first thing you notice that the entire city is dead. Not only the area where \
you are at but... everything. Clouds haven\'t moved since you first woke up. It almost seems like this city is not even real... \
You feel the presence of some entity behind you... Your curiosity makes you [t]urn around... ')
    while 1:
        action = input('>>')
        if action == 'health':
            check_player_params()
        if action == 't':
            wake_up_1_robot_encounter()
        if action not in ['t', 'health']:
            print ('Wrong')
            
    
    
        
    
def wake_up_1_robot_encounter():
    print ('Entity: Welcome to the paradise. Man-made paradise. The perfect world full of numerous opportunities. \
Too bad that you are alone here and and have no idea what will happen if you stay long enough... \
Let me help you. ')
    weak = "Your attack is ineffective, I'd suggest learning a skill or aquiring a weapon."
    run = "Your fleeing leads to a dead end, time to turn back and face your fears."
    print("You:\n[W]here am I, and \
what in God's carnation are you?\n[A]ttack the android\n[R]un away with fright.\n\n")
    while 1:
        action = input('>>')
        if action == 'W':
            wake_up_1_robot_encounter_2()
        if action == 'A':
            print(weak)
        if action == 'R':
            print(run)
        if action not in ['W','A','R']:
            print('incorrect')
            
def wake_up_1_robot_encounter_2():
    print("Entity: I am a program, man was my creator.\n\
You are in the paradise, or, as you perceive it, a virtual world. Numerous opportunities. You cannot stay here for too long unfortunately otherwise your body that is \
somewhere out there will shut down... forever. Let me help you with some things that will help you escape. ")
    wake_up_1_problem_1()

def wake_up_1_problem_1():
    print ('Entity: You will need to solve certain puzzles to get out of the Paradise. The way you can solve this is by putting in string number and the property assigned to the parameter, for example 3 %None% or 5 brick01IM. ')
    print ('In this case, you have to walk through the wall so tampering with the collision model of the object seems like a good idea...') 
    print ('def brick_wall_shader_1():\n1. BASE_TEXTURE_PARAMETER = brck01\n2. NORMAL_MAP_PARAMETER = brck01NM\n3. SPECULAR_MAP_PARAMETER = brck01SM\n4. BASE_SURFACE_PARAMETER = brick\n5. SELF_ILLUMINATION_PARAMETER = %None%\n6. COLLISION_PARAMETER = SOLID')
    while 1: 
        x = input(str('>> '))
        if x == '6 %None%':
            print ('Entity: It wasnt that hard now, was it?')
            wake_up_1_problem_2()
        if x != '6 %None%':
            print ('Entity: This is not the right answer. For every incorrect answer, you lose Stamina. Once Stamina drains to 0, you will start losing your health points. \
Good thing that I\'m here with you right now. You don\'t lose anything. ') 
        
    
    

def wake_up_1_problem_2():
    print('Entity: So dark around here. So you might want to turn the light. You want to type string number, for example 5, and then a set of properties associated with the function. So ideally is should')
    print('look like  5 (NO_FILL, 70). Be careful though, doing something like that will make the floor disappear. What happens next is a mystery.')
    print('1. brick_wall_shader_1(150,50,0)\n2. brick_wall_shader_1(0,50,0)\n3. brick_wall_shader_1(0,0,0)\n4. brick_wall_shader_1(150,0,0)\n5. tiled_floor_shader_344(FILL_FLAT, 0)\n6. concrete_shader_4315(FILL_FLAT, 60)\n7. light_object(directional, gen_lamp.obj)')
    print('8. light_active (0)')
    while 1:
        x = input(str('>> '))
        if x == '8 (1)':
            print ('Entity: Still a bit too dark here... But let\'s move on')
        if x != '8 (1)':
            print ('Entity: That is not correct. Be careful with walls. You don\'t want to move those. ')

def wake_up_1_end():
    print ('Entity: Now that you know the basic, I need you to return a favor. I need to obtain certain items that I am not programmed to find. It is rather complicated. I need \
you to find those for me. I will tell you the rest later. ') 
    print ('Thanks for playing! More to come soon! :D ') 
    
    
            
wake_up_intro()     





