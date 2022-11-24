from os import system
from time import sleep

DIR_UP           = -1
DIR_STOPPED      = 0
DIR_DOWN         = 1





building_roof    = True
building_floors  = 9
building_parking = True

lift_floor       = 3
lift_open        = True
lift_dir         = DIR_STOPPED
lift_target_floor= 9

human_floor      = 6
human_in_lift    = True



system('cls')
   
while True:

    human_floor= int(input('Where is the human? '))
    human_in_lift= input('Is human inside lift(y/n)? ') =='y'
    call_lift = input('Call the lift(y/n)? ') =='y'

    if call_lift:
        if not human_in_lift:
            lift_target_floor = human_floor
        else:
            lift_target_floor= int(input('Where to? '))

    lift_open=False


    if lift_floor < lift_target_floor:
        speed = 1
        lift_dir = DIR_UP
    if lift_floor > lift_target_floor:
        speed = -1
        lift_dir = DIR_DOWN
    if lift_floor == lift_target_floor:
        speed = 0



    while True:

        lift_floor += speed


        if lift_floor == lift_target_floor:
            lift_open = True
            lift_dir  = DIR_STOPPED


        system('cls')

        if building_roof and lift_floor!=9:
            print('---|-----|----')
            print(' R |     |    ')
        elif building_roof and lift_floor==9:
            print('---|-----|----')
            print(' R | < > |    ')
            

        for floor in range(9,0,-1):
            
            a= '     '
            t= '     '
            s= ''
            

            
            if floor== lift_floor+1:
                if lift_dir == DIR_DOWN:
                    a= '  ⇩  '
                elif lift_dir == DIR_UP:
                    a= '  ⇧  '
                elif lift_dir == DIR_STOPPED and lift_open:
                    a= ' < > '
            elif floor== lift_floor:
                a='|   |'
                t='|---|'
                if human_in_lift:
                    a='| H |'

            elif floor== lift_floor-1:
                t='|---|'
            elif floor== human_floor:
                if not human_in_lift:
                    s = 'H'



            print(f'---|{t}|----')

            print(f'{floor:^3}|{a}|{s}')

            


        if building_parking and lift_floor != 1:
            print('---|     |----')
            print(' P |     |    ')
            print('---|-----|----')
        elif building_parking and lift_floor == 1:
            print('---||---||----')
            print(' P |     |    ')
            print('---|-----|----')

        
        sleep(1)
        if lift_floor == lift_target_floor:
            break

    sleep(.5)
    