import datetime
import math
import pygame
import random
import buttons
import time
pygame.init()

display_width = 1000
display_height = 600
number_of_destinations = 2
number_of_destinations_requested = 2
Next_btn = 0

points = list(range(number_of_destinations-1))
print("points = ",points)
random.shuffle(points)
print("shuffeled points = ",points)


x_points_rand_coordinate = [0 for i in range(number_of_destinations)]
y_points_rand_coordinate = [0 for i in range(number_of_destinations)]

print("x points coordinate = ",x_points_rand_coordinate)
print("y points coordinate = ",y_points_rand_coordinate)


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Real Time Multi-Distant Transportation Routing System')
icon = pygame.image.load('user.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()


black = (0,0,0)
white = (255,255,255)

###########################

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

#############################

###############################3
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
################################################

for x in range(0, number_of_destinations):
    x_points_rand_coordinate[x] = random.randint(200, display_width)
    y_points_rand_coordinate[x] = random.randint(0, display_height)

############# Buttons ###############

#create button instances
start_img = pygame.image.load('start_btn.png').convert_alpha()
exit_img = pygame.image.load('exit_btn.png').convert_alpha()
plus_img = pygame.image.load('plus_btn.png').convert_alpha()
minus_img = pygame.image.load('minus_btn.png').convert_alpha()
refresh_img = pygame.image.load('Referesh_btn.png').convert_alpha()
left_arrow_img = pygame.image.load('left_arrow_btn.png').convert_alpha()
right_arrow_img = pygame.image.load('right_arrow_btn.png').convert_alpha()
left_button = buttons.Button(50, 300, left_arrow_img, 0.4)
right_button = buttons.Button(110, 300, right_arrow_img, 0.4)
plus_button = buttons.Button(110, 360, plus_img, 0.4)
minus_button = buttons.Button(50, 360, minus_img, 0.4)
refresh_button = buttons.Button(50, 420, refresh_img, 0.4)
exit_button = buttons.Button(50, 550, exit_img, 0.4)





x =  (x_points_rand_coordinate[0])
y = (y_points_rand_coordinate[0])
# x =  300
# y = 300
x_change = 0
y_change = 0
car_speed = 0
time_interval =0


crashed = False


while not crashed:



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        ############ car horizontal movement ################
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
        ############ car vertical movement ################
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_change = -5
            elif event.key == pygame.K_DOWN:
                y_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_change = 0
    ######### update horizontal position of the car based on the event#############
    x += x_change
    ######### update horizontal position of the car based on the event#############
    y += y_change
    ##***##
    #print(event)
    ######################

    gameDisplay.fill(white)





    ############### title text ####################
    font = pygame.font.Font('freesansbold.ttf', 12)
    TextSurf, TextRect = text_objects("Controls", font)
    TextRect.center = ((90, 5))
    gameDisplay.blit(TextSurf, TextRect)
    ########################################
    ############### number of distinations text ####################
    TextSurf, TextRect = text_objects("Number of distinations = " + str(number_of_destinations_requested), font)
    TextRect.center = ((90, 50))
    gameDisplay.blit(TextSurf, TextRect)
    ########################################
    ############### number of drivers text ####################
    TextSurf, TextRect = text_objects("Number of drivers = 1 ", font)
    TextRect.center = ((90, 70))
    gameDisplay.blit(TextSurf, TextRect)
    ########################################

    ############### Used  Method ####################
    TextSurf, TextRect = text_objects("Method Used: Random ", font)
    TextRect.center = ((90, 150))
    gameDisplay.blit(TextSurf, TextRect)
    ########################################

    ############### Total Distance text ####################
    d=0.0

    for i in range(0, number_of_destinations-1):
        d = d + math.sqrt((x_points_rand_coordinate[i+1]-x_points_rand_coordinate[i])**2+(y_points_rand_coordinate[i+1]-y_points_rand_coordinate[i])**2)
    d='%.2f' % d
    TextSurf, TextRect = text_objects("Total distance = "+str(d), font)
    TextRect.center = ((90, 165))
    gameDisplay.blit(TextSurf, TextRect)
    ########################################

    ############### time text ####################
    TextSurf, TextRect = text_objects("Time = "+ str(time_interval), font)
    TextRect.center = ((90, 180))
    gameDisplay.blit(TextSurf, TextRect)
    ########################################



    font2 = pygame.font.Font('freesansbold.ttf', 24)
    ################################################
    # generate random numbers

    ############### separating line drawing #########################
    pygame.draw.line(gameDisplay,(0,0,0),(200,0),(200,600),5)

    ################# drawing destination points #######################

    # for i in range(0, number_of_destinations):
    #     #pygame.draw.circle(gameDisplay, (200, 100, 0), (x_points_rand_coordinate[i], y_points_rand_coordinate[i]),
    #       #             radius=10)
    #     img = font2.render(str(i), True, (250,0,0))
    #     rect = img.get_rect()
    #     pygame.draw.rect(img, (250,0,0), rect, 1)
    #     gameDisplay.blit(img, (x_points_rand_coordinate[i], y_points_rand_coordinate[i]))

    ################# drawing destination points links #######################
    # for p in points :
    #
    #     pygame.draw.line(gameDisplay,(0,200,0),(x_points_rand_coordinate[p], y_points_rand_coordinate[p]),(x_points_rand_coordinate[p+1], y_points_rand_coordinate[p+1]),width=1)
    # # #pygame.draw.line(gameDisplay,(0,200,0),(x_points_rand_coordinate[0], y_points_rand_coordinate[0]),(x_points_rand_coordinate[1], y_points_rand_coordinate[1]),width=1)

    ##################################################

    carImg = pygame.image.load('user.png')
    carImg = pygame.transform.scale(carImg, (40, 40))
    carImg = pygame.transform.rotate(carImg, 270)

    # ################# car image rotation #######################
    # #
    # theta = math.degrees(math.atan((y_points_rand_coordinate[1]-y_points_rand_coordinate[0])/ (x_points_rand_coordinate[1]-x_points_rand_coordinate[0])))

    ################################ number of destinations #######################################
    ################default #####################
    for i in range(0, number_of_destinations):
        img = font2.render(str(i), True, (250, 0, 0))
        rect = img.get_rect()
        pygame.draw.rect(img, (250, 0, 0), rect, 1)
        gameDisplay.blit(img, (x_points_rand_coordinate[i], y_points_rand_coordinate[i]))

    time_1 = time.time()

    for p in points:
        pygame.draw.line(gameDisplay, (0, 200, 0), (x_points_rand_coordinate[p], y_points_rand_coordinate[p]),
                            (x_points_rand_coordinate[p + 1], y_points_rand_coordinate[p + 1]), width=1)

    time_2 = time.time()

    time_interval = time_2 - time_1
    time_interval = '%.6f' % time_interval
    print(time_interval)

    ############################################################################

    if plus_button.draw(gameDisplay):
        print('plus button pressed')
        number_of_destinations_requested = number_of_destinations_requested+1
        print('number_of_destinations_requested = ',number_of_destinations_requested)

    if minus_button.draw(gameDisplay):
        print('minus button pressed')
        number_of_destinations_requested = number_of_destinations_requested-1
        print('number of destinations = ', number_of_destinations_requested)

    if refresh_button.draw(gameDisplay):
        print('exit button pressed')
        print('number_of_destinations_requested = ', number_of_destinations_requested)
        number_of_destinations = number_of_destinations_requested
        x_points_rand_coordinate = [0 for i in range(number_of_destinations)]
        y_points_rand_coordinate = [0 for i in range(number_of_destinations)]
        for x in range(0, number_of_destinations):
            x_points_rand_coordinate[x] = random.randint(200, display_width)
            y_points_rand_coordinate[x] = random.randint(0, display_height)
        points = list(range(number_of_destinations - 1))
        x = (x_points_rand_coordinate[0])
        y = (y_points_rand_coordinate[0])

    # if start_button6.draw(gameDisplay):
    #     print('START6')
    #
    #     points = list(range(number_of_destinations - 1))
    #     print("points = ", points)
    #     # random.shuffle(points)
    #     # print("shuffeled points = ", points)
    #     for p in points:
    #         pygame.draw.line(gameDisplay, (0, 200, 0), (x_points_rand_coordinate[p], y_points_rand_coordinate[p]),
    #                          (x_points_rand_coordinate[p + 1], y_points_rand_coordinate[p + 1]), width=1)

    # ########################## car image ####################################
    # carImg = pygame.transform.rotate(carImg, 90-theta)
    # car(x, y)


    ################# buttons ############################33

    if left_button.draw(gameDisplay):
        print('left button pressed')
        Next_btn=Next_btn+1
        x = (x_points_rand_coordinate[Next_btn])
        y = (y_points_rand_coordinate[Next_btn])

    if right_button.draw(gameDisplay):
        print('right button pressed')
        Next_btn=Next_btn+1
        x = (x_points_rand_coordinate[Next_btn])
        y = (y_points_rand_coordinate[Next_btn])


    if exit_button.draw(gameDisplay):
        print('EXIT')
        crashed = True


    #################################

    ################# car image rotation #######################
    #
    # theta = math.degrees(math.atan((y_points_rand_coordinate[1] - y_points_rand_coordinate[0]) / (
    #             x_points_rand_coordinate[1] - x_points_rand_coordinate[0])))
    theta = 0

    ########################## car image ####################################
    carImg = pygame.transform.rotate(carImg, 90-theta)
    car(x, y)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()


