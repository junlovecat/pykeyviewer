print('Pyviewer v1.2 made by JUN')
from keyboard import is_pressed
import pygame
import time
import sys
sys.stdin=open('stdin.txt')
isp=input().split(' ')
n=len(isp)
blit=input().split(' ')
showkey,shownum,showtot,showcur,showavg=map(int,input().split())
tmp=0
max=0
sec=0
avg=0
total=[0 for i in range(n)]
ispre=[0 for i in range(n)]
got=[]
black=(0,0,0)
white=(255,255,255)
gray=(128,128,128)
if(showavg+showcur+showtot==0):
    size=[100*n+5,100]
else:
    size=[100*n+5,200]
pygame.init()
pygame.display.set_caption("Pyviewer v1.2")
screen= pygame.display.set_mode(size)
clock=pygame.time.Clock()
font = pygame.font.SysFont(None,30)
got.append(sum(total))
ispressing=[0 for i in range(0,n)]
ischecked=True
nowcur=[0]
stt=time.time()
while(1):
    #for CUR
    if(ischecked):
        starter=time.time()
        ischecked=False
    #show key
    for x in isp:
        if(is_pressed(x)):
            pygame.draw.rect(screen,white,[isp.index(x)*100+5,5,90,90])
            if(ispressing[isp.index(x)]==0):
                ispressing[isp.index(x)]=1
                total[isp.index(x)]+=1
                tmp+=1
        if not is_pressed(x):
            pygame.draw.rect(screen,gray,[isp.index(x)*100+5,5,90,90])
            ispressing[isp.index(x)]=0
    if(showtot):
        pygame.draw.rect(screen, gray, [5,105,90,90])
    if(showkey):
        for x in blit:
            a=font.render(x,True,black)
            screen.blit(a,(43+100*(blit.index(x)),45))
    #show NUM, TOT, CUR, AVG
    if(shownum):
        for x in range(len(total)):
            a=font.render(str(total[x]),True,black)
            screen.blit(a,(5+100*x,65))
    if(showtot):
        totl = font.render("TOT",True,black)
        screen.blit(totl,(30,135))
        sumtotl = font.render(str(sum(total)),True,black)
        screen.blit(sumtotl,(30,160))
    now=time.time()-starter
    if(now>=1):
        if(showavg):
            pygame.draw.rect(screen, gray, [205,105,90,90])
        if(showcur):
            pygame.draw.rect(screen, gray, [105,105,90,90])
        if(tmp>max):
            max=tmp
        if(showcur):
            curt = font.render("CUR",True,black)
            screen.blit(curt,(130,135))
            cur = font.render(str(tmp),True,black)
            screen.blit(cur,(130,160))
        if(tmp!=0):
            avg = (avg * sec + tmp) / (sec + 1)
            n+=1
        if(showavg):
            avgt= font.render("AVG",True,black)
            screen.blit(avgt,(230,135))
            avgg = font.render(str(int(sum(total)/(time.time()-stt))),True,black)
            screen.blit(avgg,(230,160))
        prev=tmp
        tmp=0
        ischecked=True
    
    #TRUE MAIN
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()