import pygame, sys, time, CommunicateControl
Locs = [[1, 1, 2], [2, 3, 3], [4, 4, 2]]
oldLinesGood = ""

## Created By Boston Abrams
##
##
##
## -------------  Info -------------
## Escape(esc) or enter will quit
##
##
## -------------  Options  -------------
## If you want FullScreen on or not.
FullScreen = False
#  ----------------------
# The FilePath is the position of the data storage location
FilePath='DataStore.txt'
# -----------------------
ButtonPress = 0
## Functions
def ToString (List): # Coverts List to String
    return ''.join(List)
## Pygame Setup
pygame.init()
if not FullScreen:
    screen =  pygame.display.set_mode([800,480])
elif FullScreen:
    screen =  pygame.display.set_mode([800,480], pygame.FULLSCREEN )
screen.fill([105,105,105])
pygame.display.set_caption('CandyBot')
Smallfont = pygame.font.Font(None, 25)
font = pygame.font.Font(None, 50)
Bigfont = pygame.font.Font(None, 100)

FilePath = "SysStore.txt"
reading_file=open(FilePath, 'r') #Opens File
lines=reading_file.readlines()
GoodLine = lines[len(lines) - 1]
OldGood = GoodLine
# Render Titles
Title = font.render("Pick Your Candy", 1, (0, 0, 0))
Candy1 = font.render("Candy 1", 1, (0, 0, 0))
Candy2 = font.render("Candy 2", 1, (0, 0, 0))
Candy3 = font.render("Candy 3", 1, (0, 0, 0))
Candy4 = font.render("Candy 4", 1, (0, 0, 0))
TitlePos = [265, 15]
Candy1Pos = [100, 150]
Candy2Pos = [540, 150]
Candy3Pos = [100, 350]
Candy4Pos = [540, 350]
pygame.display.flip()
while True:
    #pygame.draw.rect(screen, [75, 75, 75], [0, 0, 625, 100], 0)
    #screen.blit(a,(5,12.5))
    screen.blit(Title, TitlePos)
    screen.blit(Candy1, Candy1Pos)
    screen.blit(Candy2, Candy2Pos)
    screen.blit(Candy3, Candy3Pos)
    screen.blit(Candy4, Candy4Pos)
    pygame.draw.rect(screen, [0, 0, 0], [5,60, 390, 200], 1)
    pygame.draw.rect(screen, [0, 0, 0], [5, 275, 390, 200], 1)
    pygame.draw.rect(screen, [0, 0, 0], [405,275,390, 200], 1)
    pygame.draw.rect(screen, [0, 0, 0], [405,60,390, 200], 1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_ESCAPE:
                pygame.quit()
                break
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x = event.pos[0]
            y = event.pos[1]
            if 5 < x < 395 and 60 < y < 260:
                print "#1"
                ButtonPress = 1
                #Screen = font.render("1", 1, (0, 0, 0))
            elif 405 < x < 795 and 60 < y < 260:
                print "#2"
                ButtonPress = 2
            elif 5 < x < 395 and 275 < y < 475:
                print "#3"
                ButtonPress = 3
            elif 405 < x <795 and 275 <y <475:
                print "#4"
                ButtonPress = 4
            #KeyEntry, StartFire, HeadingSel, DistanceSel,HeadingFirstTime,DistanceFirstTime,Adder= Setup.CheckForButton(event.pos[0], event.pos[1], KeyEntry,StartFire,HeadingSel,DistanceSel,HeadingFirstTime,DistanceFirstTime,Adder)
    pygame.display.flip()
    screen.fill([105,105,105])
    CommunicateControl.Code(ButtonPress)
    Reading_file=open(FilePath, 'r')
    lines=reading_file.readlines()
    #print lines
    ToY = False
    xCord = 0
    yCord = 0
    GoodLine = lines[len(lines) - 1] #GoodLine is the last line of the file!
    if len(lines) > len(oldLinesGood): # If there are more lines in the new one one was added. So then that line should be read
        DoneWait = True
        for z in lines:
            if z == " ":
                ToY = True
            else:
                if ToY:
                    
                elif not ToY:
                    
    else:
        DoneWait = False
    
    
    
    oldLinesGood = lines
    OldGood = GoodLine