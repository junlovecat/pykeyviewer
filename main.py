print('Pyviewer v1.5 made by JUN')
from threading import current_thread
import time
import sys
from keyboard import press
import win32api
try:
    from keyboard import is_pressed
    import pygame
except ModuleNotFoundError:
    import os
    os.system('pip install keyboard')
    os.system('pip install pygame')
    from keyboard import is_pressed
    import pygame
state_left = win32api.GetKeyState(0x01)
state_right = win32api.GetKeyState(0x02)
pressed_left=False
pressed_right=False
def ispressed(key):
    global state_left,state_right,pressed_left,pressed_right
    if(key=='left'):
        ns_left=win32api.GetKeyState(0x01)
        if(state_left!=ns_left):
            state_left=ns_left
            if(ns_left<0):
                pressed_left=True
                return True
            else:
                pressed_left=False
                return False
        else:
            return pressed_left
    else:
        ns_right=win32api.GetKeyState(0x02)
        if(state_right!=ns_right):
            state_right=ns_right
            if(ns_right<0):
                pressed_right=True
                return True
            else:
                pressed_right=False
                return False
        else:
            return pressed_right
sys.stdin=open('stdin.txt')
line=int(input())
keys=[0 for i in range(line)]
n=0
linemax=-987654321
for i in range(line):
    keys[i]=list(map(str,input().split()))
    n+=len(keys[i])
    if(linemax<len(keys[i])):
        linemax=len(keys[i])
blit=[[0 for j in range(len(keys[i]))] for i in range(len(keys))]
for i in range(len(keys)):
    for j in range(len(keys[i])):
        if(keys[i][j]=='space'):
            blit[i][j]=' '
        elif(keys[i][j]=='left'):
            blit[i][j]='m1'
        elif(keys[i][j]=='right'):
            blit[i][j]='m2'
        else:
            blit[i][j]=keys[i][j].upper()
showkey,shownum,showtot,showcur,showavg=map(int,input().split())
tmp=0
max=0
sec=0
avg=0
total=[[0 for j in range(len(keys[i]))] for i in range(len(keys))]
cur_list=[[0 for j in range(len(keys[i]))] for i in range(len(keys))]
ispre=[[0 for j in range(len(keys[i]))] for i in range(len(keys))]
got=[]
black=(0,0,0)
white=(255,255,255)
gray=(128,128,128)
if(showavg+showcur+showtot+showcur,showavg==0):
    size=[100*linemax+5,100*(line+1)]
else:
    size=[100*linemax+5,100*(line+2)]
pygame.init()
pygame.display.set_caption("Pyviewer v1.5")
screen=pygame.display.set_mode(size)
font=pygame.font.SysFont(None,30)
ischecked=True
stt=time.time()
tot=0
starter=time.time()
ischecked=False
while(1):
    for linenum in range(0,line):
        for x in range(0,len(keys[linenum])):
            if(keys[linenum][x] in ['left','right']):
                if(ispressed(keys[linenum][x])):
                    pygame.draw.rect(screen,white,[x*100+5,linenum*100+5,90,90])
                    if(ispre[linenum][x]==0):
                        ispre[linenum][x]=1
                        total[linenum][x]+=1
                        tmp+=1
                        tot+=1
            else:
                if(is_pressed(keys[linenum][x])):
                    pygame.draw.rect(screen,white,[x*100+5,linenum*100+5,90,90])
                    if(ispre[linenum][x]==0):
                        ispre[linenum][x]=1
                        total[linenum][x]+=1
                        tmp+=1
                        tot+=1
        for x in range(0,len(keys[linenum])):
            if(keys[linenum][x] in ['left','right']):
                if not ispressed(keys[linenum][x]):
                    pygame.draw.rect(screen,gray,[x*100+5,linenum*100+5,90,90])
                    ispre[linenum][x]=0
            else:
                if not is_pressed(keys[linenum][x]):
                    pygame.draw.rect(screen,gray,[x*100+5,linenum*100+5,90,90])
                    ispre[linenum][x]=0
        for x in range(0,len(keys[linenum])):
            if(showtot):pygame.draw.rect(screen, gray, [5,line*100+5,90,90])
            if(showkey):
                screen.blit(font.render(str(blit[linenum][x]),True,black),(43+100*x,100*linenum+45))
            if(shownum):
                a=font.render(str(total[linenum][x]),True,black)
                screen.blit(a,(5+100*x,linenum*100+65))
            if(showtot):
                totl = font.render("TOT",True,black)
                screen.blit(totl,(30,line*100+35))
                sumtotl = font.render(str(tot),True,black)
                screen.blit(sumtotl,(30,line*100+60))
        now=time.time()-starter
        if(now>=1):
            sec=time.time()-stt
            if(showavg):pygame.draw.rect(screen, gray, [205,line*100+5,90,90])
            if(showcur):pygame.draw.rect(screen, gray, [105,line*100+5,90,90])
            if(tmp>max):max=tmp
            if(showcur):
                curt = font.render("CUR",True,black)
                screen.blit(curt,(130,line*100+35))
                cur = font.render(str(tmp),True,black)
                screen.blit(cur,(130,line*100+60))
            if(tmp!=0):
                avg=(avg*sec+tmp)/(sec+1)
                n+=1
            if(showavg):
                avgt= font.render("AVG",True,black)
                screen.blit(avgt,(230,line*100+35))
                avgg = font.render(str(int(avg)),True,black)
                screen.blit(avgg,(230,line*100+60))
            prev=tmp
            tmp=0
            starter=time.time()
            continue
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
