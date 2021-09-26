print('Pyviewer v1.4 made by JUN')
from threading import current_thread
import time
import sys
try:
    from keyboard import is_pressed
    import pygame
except ModuleNotFoundError:
    import os
    os.system('pip install keyboard')
    os.system('pip install pygame')
    from keyboard import is_pressed
    import pygame
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
pygame.display.set_caption("Pyviewer v1.3(beta)")
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
            if(is_pressed(keys[linenum][x])):
                pygame.draw.rect(screen,white,[x*100+5,linenum*100+5,90,90])
                if(ispre[linenum][x]==0):
                    ispre[linenum][x]=1
                    total[linenum][x]+=1
                    tmp+=1
                    tot+=1
        for x in range(0,len(keys[linenum])):
            if not is_pressed(keys[linenum][x]):
                pygame.draw.rect(screen,gray,[x*100+5,linenum*100+5,90,90])
                ispre[linenum][x]=0
        for x in range(0,len(keys[linenum])):
            if(showtot):
                pygame.draw.rect(screen, gray, [5,205,90,90])
            if(showkey):
                a=font.render(str(blit[linenum][x]),True,black)
                screen.blit(a,(43+100*x,100*linenum+45))
            if(shownum):
                a=font.render(str(total[linenum][x]),True,black)
                screen.blit(a,(5+100*x,linenum*100+65))
            if(showtot):
                totl = font.render("TOT",True,black)
                screen.blit(totl,(30,235))
                sumtotl = font.render(str(tot),True,black)
                screen.blit(sumtotl,(30,260))
        now=time.time()-starter
        if(now>=1):
            sec=time.time()-stt
            if(showavg):
                pygame.draw.rect(screen, gray, [205,205,90,90])
            if(showcur):
                pygame.draw.rect(screen, gray, [105,205,90,90])
            if(tmp>max):
                max=tmp
            if(showcur):
                curt = font.render("CUR",True,black)
                screen.blit(curt,(130,235))
                cur = font.render(str(tmp),True,black)
                screen.blit(cur,(130,260))
            if(tmp!=0):
                avg=(avg*sec+tmp)/(sec+1)
                n+=1
            if(showavg):
                avgt= font.render("AVG",True,black)
                screen.blit(avgt,(230,235))
                avgg = font.render(str(int(avg)),True,black)
                screen.blit(avgg,(230,260))
            prev=tmp
            tmp=0
            starter=time.time()
            continue
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
