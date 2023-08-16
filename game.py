import pygame
import sys
import random
import time
import dictionary



pygame.init()
win = pygame.display.set_mode((1010,710)) 
pygame.display.set_caption("Table Game") 

bg = pygame.image.load("images//bg.jpg") 
player = pygame.image.load("images/me.png") 
bot = pygame.image.load("images/bot.png") 
button_png = pygame.image.load("images/mess.png")
one = pygame.image.load("images/1.png")
two = pygame.image.load("images/2.png")
three = pygame.image.load("images/3.png")
four = pygame.image.load("images/4.png")
five = pygame.image.load("images/5.png")
six = pygame.image.load("images/6.png")


random_int = 0
start_pos = 1
start_posb = 1
x1 = 900
y1 = 450
x2 = 900
y2 = 450

turn = 1
skip_bot1 = 0
skip_me1 = 0

# @profile
def main():
    def choose_turn():
        global turn,skip_bot1,skip_bot2,skip_bot3

        turn += 1
        if turn % 2 == 0:


            if start_posb == 9 or start_posb == 15 or start_posb == 21:
                skip_bot1 += 1
                if skip_bot1 % 2 != 0:
                    turn += 1
                    return False

            end()
            bot_buttton(1.5)
            jump()


    def button(cur,rect,seconds):
        global x1,y1,start_pos,random_int,skip_me1,skip_me2,skip_me3, turn
        
        if start_pos == 9 or start_pos == 15 or start_pos == 21 :
            skip_me1 += 1
            if skip_me1 % 2 != 0:
                choose_turn()
                return False


        if turn % 2 == 1:
     
            if rect.collidepoint(cur):
                click = pygame.mouse.get_pressed()
                mouse = pygame.mouse.get_pos()
                
                if 880 <mouse[0] and 1010 > mouse[0]:
                    if 625 < mouse[1] and 670 > mouse[1]:
                        if click[0] == 1:
                            random_int = random.randint(3,3)

                            show_cube(random_int) 
                            
                            pygame.display.update()
                            time.sleep(seconds)

                            for i in dictionary.liss:
                                if i['id'] == random_int + start_pos or i['id'] >= 23:

                                    end()
                                    while i['id'] != start_pos:
                                        x1 =  dictionary.liss[start_pos]['x']
                                        y1 =  dictionary.liss[start_pos]['y']


                                        win.blit(bg, (0,0) )  
                                        win.blit(player, (x1,y1) )
                                        win.blit(bot, (x2,y2) )
                                        win.blit(button_png, (880,625))
                                        pygame.display.update()
                                        time.sleep(0.3)

                                        start_pos += 1

                                        if start_pos in [23]:
                                            time.sleep(1)
                                            sys.exit()


                                    jump()
                                    random_int = 0
                                    choose_turn()
                                    break

    def bot_buttton(seconds):
        global x2,y2,start_posb,random_int
        if turn % 2 == 0:
            random_int_b = random.randint(1,6)

            show_cube(random_int_b) 

            pygame.display.update()
            time.sleep(seconds)

            for i in dictionary.liss:
                if i['id'] == random_int_b + start_posb or i['id'] >= 23:
                    while i['id'] != start_posb:
                        x2 =  dictionary.liss[start_posb]['x']
                        y2 = dictionary.liss[start_posb]['y']
                        win.blit(bg, (0,0) )  
                        win.blit(player, (x1,y1) )

                        win.blit(bot, (x2,y2) )
                        win.blit(button_png, (880,625))
                        pygame.display.update()
                        time.sleep(0.3)
                        start_posb += 1

                        if start_posb in [23]:
                            time.sleep(1)
                            sys.exit() 

                    random_int_b = 0
                    choose_turn()
                    break



    def end():
        global x1,y1,x2,y2,start_pos,start_posb ,random_int
        if start_pos in [17] and random_int == 6:
            while 23 != start_pos:
                x1 =  dictionary.liss[start_pos]['x']
                y1 =  dictionary.liss[start_pos]['y']


                win.blit(bg, (0,0) )  
                win.blit(player, (x1,y1) )
                win.blit(bot, (x2,y2) )
                win.blit(button_png, (880,625))
                pygame.display.update()
                time.sleep(0.3)
                start_pos += 1


        if start_pos in [18] and random_int in [5,6]:
            while 23 != start_pos:
                x1 =  dictionary.liss[start_pos]['x']
                y1 =  dictionary.liss[start_pos]['y']


                win.blit(bg, (0,0) )  
                win.blit(player, (x1,y1) )
                win.blit(bot, (x2,y2) )
                win.blit(button_png, (880,625))
                pygame.display.update()
                time.sleep(0.3)
                start_pos += 1
            

        if start_pos in [19] and random_int in [4,5,6]:
            while 23 != start_pos:
                x1 =  dictionary.liss[start_pos]['x']
                y1 =  dictionary.liss[start_pos]['y']


                win.blit(bg, (0,0) )  
                win.blit(player, (x1,y1) )
                win.blit(bot, (x2,y2) )
                win.blit(button_png, (880,625))
                pygame.display.update()
                time.sleep(0.3)
                start_pos += 1


        if start_pos in [20] and random_int in [3,4,5,6]:
            while 23 != start_pos:
                x1 =  dictionary.liss[start_pos]['x']
                y1 =  dictionary.liss[start_pos]['y']


                win.blit(bg, (0,0) )  
                win.blit(player, (x1,y1) )
                win.blit(bot, (x2,y2) )
                win.blit(button_png, (880,625))
                pygame.display.update()
                time.sleep(0.3)
                start_pos += 1

        if start_pos in [21] and random_int in [2,3,4,5,6]:
            while 23 != start_pos:
                x1 =  dictionary.liss[start_pos]['x']
                y1 =  dictionary.liss[start_pos]['y']


                win.blit(bg, (0,0) )  
                win.blit(player, (x1,y1) )
                win.blit(bot, (x2,y2) )
                win.blit(button_png, (880,625))
                pygame.display.update()
                time.sleep(0.3)
                start_pos += 1

        if start_pos in [22] and random_int in [1,2,3,4,5,6]:
            while 23 != start_pos:
                x1 =  dictionary.liss[start_pos]['x']
                y1 =  dictionary.liss[start_pos]['y']


                win.blit(bg, (0,0) )  
                win.blit(player, (x1,y1) )
                win.blit(bot, (x2,y2) )
                win.blit(button_png, (880,625))
                pygame.display.update()
                time.sleep(0.3)
                start_pos += 1

        if start_posb in [17] and random_int == 6:
            while 23 != start_posb:
                x2 =  dictionary.liss[start_posb]['x']
                y2 =  dictionary.liss[start_posb]['y']


                win.blit(bg, (0,0) )  
                win.blit(player, (x1,y1) )
                win.blit(bot, (x2,y2) )
                win.blit(button_png, (880,625))
                pygame.display.update()
                time.sleep(0.3)
                start_posb += 1

        if start_posb in [18] and random_int in [5,6]:
            while 23 != start_posb:
                x2 =  dictionary.liss[start_posb]['x']
                y2 =  dictionary.liss[start_posb]['y']


                win.blit(bg, (0,0) )  
                win.blit(player, (x1,y1) )
                win.blit(bot, (x2,y2) )
                win.blit(button_png, (880,625))
                pygame.display.update()
                time.sleep(0.3)
                start_posb += 1
        if start_posb in [19] and random_int in [4,5,6]:
            while 23 != start_posb:
                x2 =  dictionary.liss[start_posb]['x']
                y2 =  dictionary.liss[start_posb]['y']


                win.blit(bg, (0,0) )  
                win.blit(player, (x1,y1) )
                win.blit(bot, (x2,y2) )
                win.blit(button_png, (880,625))
                pygame.display.update()
                time.sleep(0.3)
                start_posb += 1
        if start_posb in [20] and random_int in [3,4,5,6]:
            while 23 != start_posb:
                x2 =  dictionary.liss[start_posb]['x']
                y2 =  dictionary.liss[start_posb]['y']


                win.blit(bg, (0,0) )  
                win.blit(player, (x1,y1) )
                win.blit(bot, (x2,y2) )
                win.blit(button_png, (880,625))
                pygame.display.update()
                time.sleep(0.3)
                start_posb += 1
        if start_posb in [21] and random_int in [2,3,4,5,6]:
            while 23 != start_posb:
                x2 =  dictionary.liss[start_posb]['x']
                y2 =  dictionary.liss[start_posb]['y']


                win.blit(bg, (0,0) )  
                win.blit(player, (x1,y1) )
                win.blit(bot, (x2,y2) )
                win.blit(button_png, (880,625))
                pygame.display.update()
                time.sleep(0.3)
                start_posb += 1
        if start_posb in [22] and random_int in [1,2,3,4,5,6]:
            while 23 != start_posb:
                x2 =  dictionary.liss[start_posb]['x']
                y2 =  dictionary.liss[start_posb]['y']


                win.blit(bg, (0,0) )  
                win.blit(player, (x1,y1) )
                win.blit(bot, (x2,y2) )
                win.blit(button_png, (880,625))
                pygame.display.update()
                time.sleep(0.3)
                start_posb += 1



                    
    def jump():
        global x1,y1,x2, y2, start_pos, start_posb
        if start_pos == 12:
            win.blit(bg, (0,0) )
            win.blit(player, (x1,y1) ) 
            win.blit(bot, (x2,y2) )
            win.blit(button_png, (880,625))
            pygame.display.update()
            time.sleep(1.5)
            x1 = dictionary.liss[5]['x']
            y1 = dictionary.liss[5]['y']
            start_pos = dictionary.liss[5]['id']
            pygame.display.update()
            win.blit(player, (x1,y1) )
            win.blit(bot, (x2,y2) )
            win.blit(button_png, (880,625))
            pygame.display.update()

            win.blit(bg, (0,0) ) 
            win.blit(player, (x1,y1) ) 
            win.blit(bot, (x2,y2) )  
            win.blit(button_png, (880,625))
            pygame.display.update()     
            time.sleep(1)

        if start_pos == 16:
            win.blit(bg, (0,0) )
            win.blit(player, (x1,y1) )
            win.blit(bot, (x2,y2) )
            win.blit(button_png, (880,625))
            pygame.display.update()
            time.sleep(1.5)
            x1 = dictionary.liss[17]['x']
            y1 = dictionary.liss[17]['y']
            start_pos = dictionary.liss[17]['id']
            pygame.display.update()  
            win.blit(player, (x1,y1) )
            win.blit(bot, (x2,y2) )
            win.blit(button_png, (880,625))
            pygame.display.update() 

            win.blit(bg, (0,0) )  
            win.blit(player, (x1,y1) )  
            win.blit(bot, (x2,y2) )  
            win.blit(button_png, (880,625))
            pygame.display.update()     
            time.sleep(1)        

        if start_posb == 12:
            win.blit(bg, (0,0) )
            win.blit(player, (x1,y1) )
            win.blit(bot, (x2,y2) )
            win.blit(button_png, (880,625))
            pygame.display.update()
            time.sleep(1.5)
            x2 = dictionary.liss[5]['x']
            y2 = dictionary.liss[5]['y']
            start_posb = dictionary.liss[5]['id']
            win.blit(player, (x1,y1) )
            win.blit(bot, (x2,y2) )
            win.blit(button_png, (880,625))
            pygame.display.update() 


        if start_posb == 16:
            win.blit(bg, (0,0) )
            win.blit(player, (x1,y1) )
            win.blit(bot, (x2,y2) )
            win.blit(button_png, (880,625))
            pygame.display.update()
            time.sleep(1.5)
            x2 = dictionary.liss[17]['x']
            y2 = dictionary.liss[17]['y']
            start_posb = dictionary.liss[17]['id']
            win.blit(player, (x1,y1) )
            win.blit(bot, (x2,y2) )
            win.blit(button_png, (880,625))
            pygame.display.update() 

     


                    
                         
        
    def show_cube(random_int, x = 900, y = 540):
        if random_int == 1:
            win.blit(one, (x,y))
        if random_int == 2:
            win.blit(two, (x,y))
        if random_int == 3:
            win.blit(three, (x,y))
        if random_int == 4:
            win.blit(four, (x,y))
        if random_int == 5:
            win.blit(five, (x,y))
        if random_int == 6:
            win.blit(six, (x,y))



    clock = pygame.time.Clock() 

    square = pygame.Rect((0,0), (1032,1032))

    run = True
    while(run):
        clock.tick(30) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  
                    button(event.pos,square ,1.5) 


        
        win.blit(bg, (0,0) ) 
        win.blit(player, (x1,y1) ) 
        win.blit(bot, (x2,y2) ) 

        win.blit(button_png, (880,625))
        pygame.display.update()
        

        



    pygame.quit()

main()