# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://cs.simpson.edu

import pygame
from pyswip import Prolog

# Definiranje boja
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)



# Ovdje postavljamo širinu i visinu polja jedne èelije te broj èelija
width=50
height=50
N = 8

# Postavljamo razmak izmeðu èelija
margin=0

#Stvaramo dvodimenzionalno polje koje je jednostavno lista unutar liste
grid=[]
for row in range(N):
    #Dodajemo praznu listu koja æe u sebi imate podatke o svako æeliji
    grid.append([])
    for column in range(N):
        grid[row].append(0) # Dodaj podatak u æeliju

#Preko dodatnog paketa pyswip pozivamo predikat iz prologa
#koji nam vraæa listu rješenja te svako rješenje spremamo
#u zasebno polje
solutions = []
number = 0
prolog = Prolog()
prolog.consult('queens.pl')
for result in prolog.query("solution(S)", maxresult = 20):
    print (result)
    solutions.append(number)
    solutions[number] = result["S"]
    number += 1

number = 0



# Inicijalizacija pygame-a
pygame.init()
 
# Postavljanje širine i visine ekrana
size=[50*N,50*N]
screen=pygame.display.set_mode(size)

# Postavljanje titule zaslona
pygame.display.set_caption("My Chess")

# Kreiranje podloge na koju æemo iscrtavati
background = pygame.Surface(screen.get_size())

# Popunjavamo ekran za crnom pozadinom
background.fill(black)

#Petlja æe se izvršavati dokle god korisnik ne izaðe van.
done=False

# Koristi se za definiranje kolko èesto se ekran osvježava
clock=pygame.time.Clock()


#Stvaranje referenci na onoliko slika kolko æe biti ih na ploèi
#te ih se može referencirati preko polja
pictures = []

for row in range(N):
    pictures.append(row)

for row in range(N):
    pictures[row] = pygame.image.load("white_queen.png").convert()
    pictures[row].set_colorkey(black)


# -------- Glavna programska petlja -----------
while done==False:
    # Svo procesiranje dogaðaja ide ispod ovog komentara
    for event in pygame.event.get(): # Korisnik je nešto uèinio
        if event.type == pygame.QUIT: # Ako korisnik stisne izlaz
            done=True # Zastavica koja govorio da se može izaæi iz petlje
        #Provjeravamo da li je korisnik pritisnuo na neku tipku
        if event.type == pygame.KEYDOWN:
            #Ako je pritisnuo gore onda poveæavamo number za jedan te pristupamo
            #sljedeæem rješenju koje smo dobili iz prologa koje smo spremili
            #u polje rješenje, isto tako i za tipku dolje osim što se vraæamo u
            #polju tj. smanjujemo vrijednost
            if event.key == pygame.K_UP:
                if number != 19:
                    number += 1
                    print number
            if event.key == pygame.K_DOWN:
                if number != 0:
                    number -= 1
                    print number
            
    # Svo procesiranje dogaðaja ide iznad ovog komentara
    
    
    # Sav kod za iscrtavanja ide ispod ovog komentara
    # Postavljanje pozadine zaslona
    screen.fill(black)

    # Iscrtavanje ploèe
    for row_rect in range(N):
        for column_rect in range(N):
            if row_rect % 2 == 0:
                if column_rect % 2 == 0:
                    color = black
                else:
                    color = white
            else:
                if column_rect % 2 == 0:
                    color = white
                else:
                    color = black
            if grid[row_rect][column_rect] == 1:
                color = green
            pygame.draw.rect(screen,color,[(margin+width)*column_rect+margin,(margin+height)*row_rect+margin,width,height])
    #Mjenjanje iscrtavanja slika s obzirom na rješenje koje smo dobili iz Prologa
    #rješenja se nalaze unutar polja koje smo definirali na poèetku te se vrijednosti iz polja
    #mjenjaju s obzirom na pritisak tipke gore ili dolje
    for res in range(N):
          position = [width*(solutions[number][res]-1),height*res]
          screen.blit(pictures[res],position)
          

    # Sav kod za iscrtavanje ide iznad ovog komentara
    
    
    # Ogranièi na 20 frame-a po sekundi
    clock.tick(20)

    # Osvježavanje ekrana s onim što smo iscrtali
    pygame.display.flip()
    
#Bez ove linije program puca prilikom izlaska
pygame.quit ()

