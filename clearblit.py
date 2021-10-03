class clearblit:
    def __init__(self,keys,blit):pass
    def clearblit(self,keys,blit):
        for i in range(len(keys)):
            for j in range(len(keys[i])):
                if(keys[i][j]=='space'):blit[i][j]=' '
                elif(keys[i][j]=='left'):blit[i][j]='m1'
                elif(keys[i][j]=='right'):blit[i][j]='m2'
                else:blit[i][j]=keys[i][j].upper()
        return blit

if __name__=='__main__':
    print('This is not a main code.')
    import sys
    sys.exit()