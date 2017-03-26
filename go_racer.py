import pygame
import time
import random
import sys

file = 'On_The_Table.mp3'
pygame.init()

height = 600
width = 800

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)

car_width = 40
car_height = 80

block_color = (53,115,255)

bright_red = (255,0,0)
bright_green = (0,255,0)

gameDisplay = pygame.display.set_mode((width,height))
pygame.display.set_caption('go racer!')
clock = pygame.time.Clock()

carImg = pygame.image.load('car.png')
pygame.display.set_icon(carImg)

pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()

#buttons
green = (0,200,0)

def things_dodged(count):
    font = pygame.font.SysFont(None,25)
    text = font.render("Score: "+str(count), True, black)
    gameDisplay.blit(text, (0,0))

def things(thingx,thingy,thingw,thingh,color):
    pygame.draw.rect(gameDisplay,block_color,[thingx, thingy,thingw, thingh])

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def text_objects(text,font):
    textSurface = font.render(text,True,black)
    return textSurface,textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',100)
    textsurf,textrect = text_objects(text, largeText)
    textrect.center = ((width/2),(height/2))
    gameDisplay.blit(textsurf,textrect)
    pygame.display.update()
    time.sleep(5)
    game_loop()

def crash():
    largeText = pygame.font.SysFont('freesansbold.ttf',100)
    textsurf,textrect = text_objects("You Crashed!", largeText)
    textrect.center = ((width/2),(height/2))
    gameDisplay.blit(textsurf,textrect)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button("Play Again",150,450,100,50,green,bright_green,"play")
        button("Quit!",550,450,100,50,red,bright_red,"quit")
        pygame.display.update()
        clock.tick(15)


def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
        if click[0] == 1 and action!=None:
            if action == "play":
                game_loop()
            elif action == "quit":
                pygame.quit()
    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))
    smallText = pygame.font.Font('freesansbold.ttf',20)
    textSurf, textRect  = text_objects(msg, smallText)
    textRect.center = (x+(w/2), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)

def game_intro(text):

    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',100)
        textsurf,textrect = text_objects(text, largeText)
        textrect.center = ((width/2),(height/2))
        gameDisplay.blit(textsurf,textrect)

        button("GO!",150,450,100,50,green,bright_green,"play")
        button("QUIT!",550,450,100,50,red,bright_red,"quit")

        #pygame.draw.rect(gameDisplay, red, (550,450,100,50))
        
        pygame.display.update()
        clock.tick(15)

def game_loop():

    pygame.mixer.music.play(-1)
    
    x = (width * 0.45)
    y = (height * 0.8)
    gameExit = False
    x_change = 0

    thing_startx = random.randrange(0,width)
    thing_starty = -600
    thing_speed = 5
    thing_width = 80
    thing_height = 80

    dodged = 0
    
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        x+=x_change
        gameDisplay.fill(white)
        things(thing_startx,thing_starty,thing_width,thing_height,block_color)
        thing_starty += thing_speed        
        car(x,y)
        things_dodged(dodged)
        
        if x > width + car_width or x < -car_width:
            crash()

        if thing_starty > height:
            thing_starty = 0 -thing_height
            thing_startx = random.randrange(0,width)
            dodged+=1
            thing_speed+=0.25
            
        if y < thing_starty+thing_height:
            if x > thing_startx and x < thing_startx+thing_width or x+car_width > thing_startx and x+car_width < thing_startx + thing_width:
                crash()
        
        pygame.display.update()
        clock.tick(60)

game_intro('go racer!')
game_loop()
pygame.quit()
quit()
