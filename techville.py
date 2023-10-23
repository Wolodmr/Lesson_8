def start_engine():
    print('starting_engine')

def move_forward():
    print('moving forward')

def turn(direction):
    print(f'turning {direction}')

def stop_engine():
    print('stopping engine')

def follow_roundabout(exit_number):
    print('we entering the roundabout')
    print(f'taking exit_number {exit_number} from the roundabout')


start_engine()

destination = input('Where do you want to go?  ')
if destination  == 'library':
    move_forward()
    turn('left')
    print('we arrived at the library')
if destination  == 'tech park':
    move_forward()
    turn('right')
    print('we arrived at the tech park')
if destination  == 'hospital':
    move_forward()
    follow_roundabout(1)
    print('we arrived at the hospital')
if destination  == 'mall':
    move_forward()
    follow_roundabout(2)
    turn('left')
    print('we arrived at the mall')
if destination  == 'airport':
    move_forward(3)
    follow_roundabout(3)
    move_forward()
    turn('left')
    print('we arrived at the airport')
if destination  == 'univercity':
    move_forward()
    follow_roundabout(4)
    move_forward()
    turn('right')
    print('we arrived at the univercity')
if destination  == 'stadium':
    move_forward()
    follow_roundabout(4)
    move_forward()
    turn('left')
    print('we arrived at the stadium')



    







