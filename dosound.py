import os,sys,pygame
def setexception(text):
    print(text)
    os.system('pause')
    sys.exit()
try:from playsound import playsound
except:
    os.system('pip install playsound')
    from playsound import playsound
def dosound(linenum,x,selectinglist):
    selected=selectinglist[linenum][x]
    try:pygame.mixer.Sound(f'audio/{selected}').play()
    except:setexception(f'audio/{selected} not found')