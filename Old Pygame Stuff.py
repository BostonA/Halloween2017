import pygame, sys, time, Setup, Extra, Math

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
## Functions
def ToString (List): # Coverts List to String
    return ''.join(List)
## Vars - Setup
KeyEntry = []
HeadingList = []
AllHeadingDistance=[]
DistanceList = []
Expanded_Line =[]
num = 3.5
Heading = "NULL"
Distance = "NULL"
StartFire = True
HeadingFirstTime = True
DistanceFirstTime = True
Even = True
Loaded = False
Armed = False
DoneWait = False
Potato1 = True
Tank2 = False
Fire = False
HeadingSel = False
DistanceSel = False
Adder = False
Free = False
## Pygame Setup
pygame.init()
if not FullScreen:
    screen =  pygame.display.set_mode([800,480])
elif FullScreen:
    screen =  pygame.display.set_mode([800,480], pygame.FULLSCREEN )
screen.fill([105,105,105])
pygame.display.set_caption('Spudnik Pi')
a = pygame.image.load('Logo.png')
b = pygame.image.load('Logo.png')
a = pygame.transform.scale(a, (75, 75))
pygame.display.set_icon(b)
Smallfont = pygame.font.Font(None, 25)
font = pygame.font.Font(None, 50)
Bigfont = pygame.font.Font(None, 100)
## File Setup
reading_file=open(FilePath, 'r') #Opens File
lines=reading_file.readlines()
GoodLine = lines[len(lines) - 1]
OldGood = GoodLine
oldLinesGood = lines #Sets up lines for comparison
print "Waiting For Data..." #Fancy Command Line thing
# Render Titles
Title = font.render("Pick Your Candy", 1, (0, 0, 0))
HeadingLogo = Smallfont.render("Heading:", 1, (0, 0, 0))
HeadingLogoPos = [10, 120]
DistanceLogo = Smallfont.render("Distance:", 1, (0, 0, 0))
DistanceLogoPos = [180, 120]
ScreenPos = [15, 220]
pygame.display.flip()
while True:
    pygame.draw.rect(screen, [75, 75, 75], [0, 0, 625, 100], 0)
    Setup.Shapes(screen)
    screen.blit(a,(5,12.5))
    screen.blit(Title, TitlePos)
    screen.blit(Key1, Key1Pos)
    screen.blit(Key2, Key2Pos)
    screen.blit(Key3, Key3Pos)
    screen.blit(Key4, Key4Pos)
    screen.blit(Key5, Key5Pos)
    screen.blit(Key6, Key6Pos)
    screen.blit(Key7, Key7Pos)
    screen.blit(Key8, Key8Pos)
    screen.blit(Key9, Key9Pos)
    screen.blit(Key0, Key0Pos)
    screen.blit(KeyBK, KeyBKPos)
    screen.blit(HeadingLogo, HeadingLogoPos)
    screen.blit(DistanceLogo, DistanceLogoPos)
    pygame.draw.rect(screen, [0, 0, 0], [10,145, 155, 45], 1)
    pygame.draw.rect(screen, [0, 0, 0], [180,145, 155, 45], 1)
    if HeadingSel:
        if HeadingFirstTime:
            KeyEntry = HeadingList
            HeadingFirstTime = False
        else:
            HeadingList = KeyEntry
        pygame.draw.rect(screen, [0, 0, 0], [5,120, 165, 75], 1)
    elif DistanceSel:
        if DistanceFirstTime:
            KeyEntry = DistanceList
            DistanceFirstTime = False
        else:
            DistanceList = KeyEntry
        pygame.draw.rect(screen, [0, 0, 0], [175,120,165, 75], 1)
    HeadingNumRender = font.render(ToString(HeadingList), 1, (0, 0, 0))
    screen.blit(HeadingNumRender, [10, 145])
    DistanceNumRender = font.render(ToString(DistanceList), 1, (0, 0, 0))
    screen.blit(DistanceNumRender, [180, 145])
    Fire,Potato1,StartFire=Extra.WebsiteControl(screen, Smallfont, ToString(Heading), Distance, AllHeadingDistance, Fire, Potato1, StartFire)
    pygame.draw.circle(screen, [255,0,0], [400,165], 40, 0)
    pygame.draw.circle(screen, [0,0,0], [400,165], 33, 1)
    Add = Smallfont.render("Add", 1, (0, 0, 0))
    screen.blit(Add, [385,153])
    if Adder:
        print "Looper"
        Heading = ToString(HeadingList)
        Distance = ToString(DistanceList)
        print Distance
        Angle = Math.Maths(Distance)
        AllHeadingDistance.append([ToString(HeadingList),ToString(DistanceList), Angle])
        Adder = False
    Even,num,Fire = Extra.ArmSequence(Loaded,Even,Potato1, screen, font, Bigfont, Armed, num, StartFire,Tank2, Fire)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_ESCAPE:
                pygame.quit()
                break
            if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                if StartFire:
                    if Armed:
                        print "Firing"
                    if Tank2:
                        Armed = True
                        StartFire = False
                        Potato1 = False
                        Tank2 = False
                        Fire = True
                        num=3.5
                    elif Potato1:
                        Tank2 = True
                    else:
                        Potato1=True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #Screen = font.render("1", 1, (0, 0, 0))
            if not StartFire:
                 KeyEntry, StartFire, HeadingSel, DistanceSel,HeadingFirstTime,DistanceFirstTime,Adder= Setup.CheckForButton(event.pos[0], event.pos[1], KeyEntry,StartFire,HeadingSel,DistanceSel,HeadingFirstTime,DistanceFirstTime,Adder)
            if StartFire:
                if Armed:
                    print "Firing"
                if Tank2:
                    Armed = True
                    StartFire = False
                    Potato1 = False
                    Tank2 = False
                    Fire = True
                    num=3.5
                elif Potato1:
                    Tank2 = True
                else:
                    Potato1=True
    pygame.display.flip()
    screen.fill([105,105,105])

    if len(KeyEntry) < 8:
        Screenf = font.render(''.join(KeyEntry), 1, (0, 0, 0))
    else:
        Screenf = font.render("Ov.Flow", 1, (0, 0, 0))
    screen.blit(Screenf, ScreenPos)
