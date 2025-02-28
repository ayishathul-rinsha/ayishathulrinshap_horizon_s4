import pygame
import random
import time
import math

pygame.init()
WIDTH=500
HEIGHT=500
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pygame project")
holding = False
start_time=0
duration=0
radius = 20
vel=5
circles=[]
win.fill((255,255,255))
flag=False
prev_x=-1
prev_y=-1
pathlength=0
path=[]
font=pygame.font.Font(None,16)
count=1

running = True
while running:
    keys=pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:               #to exit the window
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  #to detect right-click
            if event.button==3:
                if circles:
                    circles.pop()                   #to remove the last circle from the stack
                    win.fill((255,255,255))
                    pathlength-=path.pop()
                    if len(circles)==1:
                        pathlength=0.0
                    for color,x,y,radius,prev_x,prev_y in circles:
                        pygame.draw.circle(win,color,(x,y),(radius))
                        pygame.draw.line(win,(0,0,0),(prev_x,prev_y),(x,y),1)
                    a="Path Length = "+str(pathlength)
                    text=font.render(a,True,(0,0,0))
                    win.blit(text,(50,50))
                flag=True
            elif event.button==1:                   #to detect left-click
                holding = True
                start_time=time.time()
                flag=False
        elif event.type == pygame.MOUSEBUTTONUP:    #to detect if hand taken from the mousepad
            if flag==False:
                holding = False
                duration=time.time()-start_time
                radius=duration*50                  #to increase the radius according to the duration held
                x,y=event.pos
                if len(circles)==0:
                    prev_x=-1
                    prev_y=-1
                if prev_x==-1 and prev_y == -1:
                    prev_x=x
                    prev_y=y
                length=math.sqrt(((prev_x-x)**2)+((prev_y-y)**2))
                path.append(length)
                pathlength=sum(path)
                color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
                circles.append((color,x,y,radius,prev_x,prev_y))
                win.fill((255,255,255))
                for color,x,y,radius,prev_x,prev_y in circles:
                    pygame.draw.circle(win,color,(x,y),(radius))
                    pygame.draw.line(win,(0,0,0),(prev_x,prev_y),(x,y),1)
                a="Path Length = "+str(pathlength)
                text=font.render(a,True,(0,0,0))
                win.blit(text,(50,50))
                prev_x=x
                prev_y=y
                
        elif event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:      #to detect if spacekey is pressed
            while circles:
                circles.pop()
            path.clear
            pathlength=0
            prev_x=-1
            prev_y=-1
            win.fill((255,255,255))

        elif event.type==pygame.KEYDOWN and event.key == pygame.K_s:
            filename=f"image_{count}.png"
            pygame.image.save(win,filename)
            count+=1
    
    pygame.display.flip()

pygame.quit
