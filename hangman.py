import pygame
import math
import random


pygame.init()
WIDTH,HEIGHT=1000,700
win=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Hangman Game!")
FPS=60   
clock=pygame.time.Clock()
run=True
music=pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)



#fonts
LETTER_FONT=pygame.font.SysFont('comicsans',40)
WORD_FONT=pygame.font.SysFont('comicsans',60)
TITLE_FONT=pygame.font.SysFont('comicsans',40)
CREATION_FONT=pygame.font.SysFont('comicsans',20)
CREATION_FONT_=pygame.font.SysFont('comicsans',30)


#button variables
RADIUS=20
GAP=15
letters=[] 
startx=round((WIDTH-(RADIUS*2+GAP)*13)/2)

starty=400
A=65
for i in range(26):
    x=startx+GAP*2+((RADIUS*2+GAP)*(i%13))
    y=starty+((i//13)*(GAP+RADIUS*2))
    letters.append([x,y,chr(A+i),True])

    
    
    #loadimages
images=[]

for i in range(7):
    image=pygame.image.load("hangman"+str(i)+".png")
    images.append(image)


    
    
    
    #game variables
hangman_status=0
words=["COMPUTER","HANG","DEVELOPER"]
word=random.choice(words)
guessed=[]




#color
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,200,0)
PURPLE=(102,0,102)
SHADOW=(192,192,192)
LIGHTBLUE=(0,0,255)
bg=(255, 166, 0) 
circle=(207, 14, 14)
try_=(114, 45, 224)

    
def draw():
    
    win.fill(bg)
    #title
    text=TITLE_FONT.render("WELCOME TO HANGMAN",1,BLACK)
    win.blit(text,(WIDTH/2-text.get_width()/2,20))
    #creation
    text=CREATION_FONT.render("GUESS THE WORD....???",1,BLACK)
    win.blit(text,(400,180))
    #info
    textinfo=CREATION_FONT_.render("WHAT TO DO:-GUESS THE WORD IN 6 CHANCES OTHERWISE THE MAN WOULD BE HANGED. ",1,RED)
    win.blit(textinfo,(30,650))
        #score
    text=CREATION_FONT_.render("CHANCES: "+str(6-hangman_status),1,BLACK)
    win.blit(text,(850,20))
    #displaying
    display_word= ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word +=  "_ "
    text=WORD_FONT.render(display_word,1,BLACK)
    win.blit(text,(400,200))
        
    #draw buttons
    for  letter in letters:
        x,y,ltr,visible=letter
        if visible:
            
            
        
            pygame.draw.circle(win,BLACK,(x,y),RADIUS,3)
            text=LETTER_FONT.render(ltr,1,BLACK)
            win.blit(text,(x-text.get_width()/2,y-text.get_height()/2))
    win.blit(images[hangman_status],(150,100))
    pygame.display.update()
    
while run:
    clock.tick(FPS)
    draw()
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            m_x,m_y=pygame.mouse.get_pos()
            
            for letter in letters:
                x,y,ltr,visible=letter
                if visible:
                    dis=math.sqrt((x-m_x)**2+(y-m_y)**2)
                    if dis<RADIUS:
                        letter[3]=False
                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_status+=1
            won=True
            for letter in word:
                if letter not in guessed:
                    won=False
                    break
            if won:
                win.fill(BLACK)
                text=WORD_FONT.render("YOU WON!!!",1,GREEN)
                win.blit(text,(WIDTH/2-text.get_width()/2,HEIGHT/2-text.get_height()/2))
                pygame.display.update()
                pygame.time.delay(3000)
                run=False
            if hangman_status==6:
                win.fill(BLACK)
                text=WORD_FONT.render("YOU lose!!!",1,RED)
                text2=CREATION_FONT.render("Word was",1,RED)
                text3=CREATION_FONT_.render(word,1,GREEN)
                win.blit(text,(WIDTH/2-text.get_width()/2,HEIGHT/2-text.get_height()/2))
                win.blit(text2,(400,400))
                win.blit(text3,(400,450))
                pygame.display.update()
                pygame.time.delay(3000)
                run=False    
                     
                
            
pygame.quit()