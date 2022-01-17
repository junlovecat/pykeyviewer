print('Pyviewer v1.10 made by JUN')
from os import remove
import time
import sys
import win32api
import clearblit
import os
from dosound import dosound
def setexception(text):
    print(text)
    os.system('pause')
    sys.exit()
try:
    from PySide2.QtWidgets import QApplication
    from keyboard import is_pressed
    import pygame
    from PySide2.QtWidgets import QMessageBox
    from PySide2 import QtGui
except ModuleNotFoundError:
    os.system('pip install keyboard')
    os.system('pip install pygame')
    os.system('pip install pyside2')
    os.system('pip install threading')
    from keyboard import is_pressed
    import pygame
    from PySide2.QtWidgets import QMessageBox
    from PySide2 import QtGui
except:
    setexception('내부 오류 발생')
try:
    dl=open('deletestats.txt','r')
    if(dl.readline()=='True'):
        try:remove('stats.txt')
        except:pass
        dl.close()
        remove('deletestats.txt')
    else:
        dl.close()
        remove('deletestats.txt')
except:pass
state_left=win32api.GetKeyState(0x01)
state_right=win32api.GetKeyState(0x02)
pressed_left=False
pressed_right=False
def ispressed(key):
    global state_left,state_right,pressed_left,pressed_right
    if(key=='left'):
        ns_left=win32api.GetKeyState(0x01)
        if(state_left!=ns_left):
            state_left=ns_left
            if(ns_left<0):pressed_left=True;return True
            else:pressed_left=False;return False
        else:return pressed_left
    else:
        ns_right=win32api.GetKeyState(0x02)
        if(state_right!=ns_right):
            state_right=ns_right
            if(ns_right<0):pressed_right=True;return True
            else:pressed_right=False;return False
        else:return pressed_right
try:f=open('change_for_key.txt','r')
except:setexception('change_for_key.txt가 존재하지 않음.')
keytext=f.readlines()
line=int(keytext[0][0])
keys=[0 for _ in range(line)]
linemax=-987654321
keycut=keytext[1:-1]
for i in range(len(keycut)):
    keys[i]=keycut[i][0:-1].split()
    if len(keys[i])>linemax:
        linemax=len(keys[i])
blit=clearblit.clearblit(keys,[[0 for _ in range(len(keys[i]))] for i in range(len(keys))]).clearblit(keys,[[0 for _ in range(len(keys[i]))] for i in range(len(keys))])
try:
    showkey=keytext[-1][0]
    shownum=keytext[-1][1]
    showtot=keytext[-1][2]
    showcur=keytext[-1][3]
    showavg=keytext[-1][4]
    hitsound=keytext[-1][5]
except:setexception('showkey,shownum,showtot,showcur,showavg,hitsound 6 needed')
try:f=open('change_for_hitsound.txt','r')
except:setexception('change_for_hitsound.txt가 존재하지 않음.')
hittext=f.readlines()
if int(hittext[0][0])!=line:setexception('change_for_hitsound.txt의 줄 수가 맞지 않음.')
hitcut=hittext[1:-1]
hit=[0 for _ in range(line)]
for i in range(len(hitcut)):
    hit[i]=hitcut[i][0:-1].split()
    if len(hit[i])!=len(keys[i]):
        setexception('change_for_hitsound.txt의 내용이 change_for_key.txt와 맞지 않음.')
if int(hittext[-1][0])!=1:
    setexception('마지막 줄에는 1이 있어야 함.')
tmp=0;max=0;sec=0;avg=0
total=[[0 for _ in range(len(keys[i]))] for i in range(len(keys))]
ispre=[[0 for _ in range(len(keys[i]))] for i in range(len(keys))]
black=(0,0,0)
white=(255,255,255)
gray=(128,128,128)
if(showavg+showcur+showtot+showcur,showavg==0):size=[100*linemax+5,100*(line+1)]
else:size=[100*linemax+5,100*(line+2)]
pygame.init()
pygame.mixer.init()
select=pygame.mixer.Sound('audio/select.wav')
pygame.display.set_caption("Pyviewer v1.10")
screen=pygame.display.set_mode(size)
font=pygame.font.SysFont(None,30)
stt=time.time()
tot=0
starter=time.time()
time.sleep(1)
try:
    stats=open('stats.txt','r')
    try:
        status=list(map(int,str(stats.read()).split()))
        counter=0
        for x in range(line):
            for y in range(len(keys[x])):
                total[x][y]=status[counter]%10000000
                for i in range(len(total)):
                    tot+=sum(total[i])
                counter+=1
                if(counter>=len(status)):breaking=True;break
    except IndexError:pass
    except:
        total=[[0 for _ in range(len(keys[i]))] for i in range(len(keys))]
        tot=0
        try:os.remove('stats.txt')
        except:pass
except:pass
while(1):
    for linenum in range(0,line):
        for x in range(0,len(keys[linenum])):
            if(keys[linenum][x] in ['left','right']):
                if(ispressed(keys[linenum][x])):
                    pygame.draw.rect(screen,white,[x*100+5,linenum*100+5,90,90])
                    if(ispre[linenum][x]==0):
                        if(hitsound):dosound(linenum,x,hit)
                        ispre[linenum][x]=1
                        total[linenum][x]+=1
                        tmp+=1
                        tot+=1
            else:
                if(is_pressed(keys[linenum][x])):
                    pygame.draw.rect(screen,white,[x*100+5,linenum*100+5,90,90])
                    if(ispre[linenum][x]==0):
                        if(hitsound):dosound(linenum,x,hit)
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
            if(showtot):
                pygame.draw.rect(screen, gray, [5,line*100+5,90,90])
                totl=font.render("TOT",True,black)
                screen.blit(totl,(30,line*100+35))
                sumtotl=font.render(str(tot%100000),True,black)
                screen.blit(sumtotl,(30,line*100+60))
            if(showkey):screen.blit(font.render(str(blit[linenum][x]),True,black),(43+100*x,100*linenum+45))
            if(shownum):
                a=font.render(str(total[linenum][x]),True,black)
                screen.blit(a,(5+100*x,linenum*100+65))
        now=time.time()-starter
        if(now>=1):
            sec=time.time()-stt
            if(showavg):pygame.draw.rect(screen,gray,[205,line*100+5,90,90])
            if(showcur):pygame.draw.rect(screen,gray,[105,line*100+5,90,90])
            if(tmp>max):max=tmp
            if(showcur):
                curt=font.render("CUR",True,black)
                screen.blit(curt,(130,line*100+35))
                cur=font.render(str(tmp),True,black)
                screen.blit(cur,(130,line*100+60))
            if(tmp!=0):avg=(avg*sec+tmp)/(sec+1)
            if(showavg):
                avgt=font.render("AVG",True,black)
                screen.blit(avgt,(230,line*100+35))
                avgg=font.render(str(int(avg)),True,black)
                screen.blit(avgg,(230,line*100+60))
            prev=tmp
            tmp=0
            starter=time.time()
            continue
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            QApplication()
            msgBox=QMessageBox()
            msgBox.setWindowIcon(QtGui.QPixmap("info.png"))
            msgBox.setText("Are you saving the stats?")
            msgBox.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
            msgBox.setDefaultButton(QMessageBox.Yes)
            ans=msgBox.exec_()
            if(ans==QMessageBox.Yes):
                stat=open("stats.txt",'w')
                for xxx in range(line):
                    data=''
                    for yyy in total[xxx]:data=data+str(yyy)+' '
                    stat.write(data)
                    stat.write('\n')
                stat.close()
            else:
                msgBox=QMessageBox()
                msgBox.setWindowIcon(QtGui.QPixmap("info.png"))
                msgBox.setText("Do you want to delete the stats?")
                msgBox.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
                msgBox.setDefaultButton(QMessageBox.No)
                ans=msgBox.exec_()
                if(ans==QMessageBox.Yes):
                    dl=open('deletestats.txt','w')
                    dl.write('True')
                    dl.close()
                else:quit()
            quit()