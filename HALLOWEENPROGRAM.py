import pygame, sys, time

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
FullScreen = True
#  ----------------------
# The FilePath is the position of the data storage location
FilePath='DataStore.txt'
# -----------------------
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
            #Screen = font.render("1", 1, (0, 0, 0))
            print "Hi"
            #KeyEntry, StartFire, HeadingSel, DistanceSel,HeadingFirstTime,DistanceFirstTime,Adder= Setup.CheckForButton(event.pos[0], event.pos[1], KeyEntry,StartFire,HeadingSel,DistanceSel,HeadingFirstTime,DistanceFirstTime,Adder)
    pygame.display.flip()
    screen.fill([105,105,105])
