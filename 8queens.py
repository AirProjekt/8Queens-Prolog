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



# Ovdje postavljamo �irinu i visinu polja jedne �elije te broj �elija
width=50
height=50
N = 8

# Postavljamo razmak izme�u �elija
margin=0

#Stvaramo dvodimenzionalno polje koje je jednostavno lista unutar liste
grid=[]
for row in range(N):
    #Dodajemo praznu listu koja �e u sebi imate podatke o svako �eliji
    grid.append([])
    for column in range(N):
        grid[row].append(0) # Dodaj podatak u �eliju

#Preko dodatnog paketa pyswip pozivamo predikat iz prologa
#koji nam vra�a listu rje�enja te svako rje�enje spremamo
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
 
# Postavljanje �irine i visine ekrana
size=[50*N,50*N]
screen=pygame.display.set_mode(size)

# Postavljanje titule zaslona
pygame.display.set_caption("My Chess")

# Kreiranje podloge na koju �emo iscrtavati
background = pygame.Surface(screen.get_size())

# Popunjavamo ekran za crnom pozadinom
background.fill(black)

#Petlja �e se izvr�avati dokle god korisnik ne iza�e van.
done=False

# Koristi se za definiranje kolko �esto se ekran osvje�ava
clock=pygame.time.Clock()


#Stvaranje referenci na onoliko slika kolko �e biti ih na plo�i
#te ih se mo�e referencirati preko polja
pictures = []

for row in range(N):
    pictures.append(row)

for row in range(N):
    pictures[row] = pygame.image.load("white_queen.png").convert()
    pictures[row].set_colorkey(black)


# -------- Glavna programska petlja -----------
while done==False:
    # Svo procesiranje doga�aja ide ispod ovog komentara
    for event in pygame.event.get(): # Korisnik je ne�to u�inio
        if event.type == pygame.QUIT: # Ako korisnik stisne izlaz
            done=True # Zastavica koja govorio da se mo�e iza�i iz petlje
        #Provjeravamo da li je korisnik pritisnuo na neku tipku
        if event.type == pygame.KEYDOWN:
            #Ako je pritisnuo gore onda pove�avamo number za jedan te pristupamo
            #sljede�em rje�enju koje smo dobili iz prologa koje smo spremili
            #u polje rje�enje, isto tako i za tipku dolje osim �to se vra�amo u
            #polju tj. smanjujemo vrijednost
            if event.key == pygame.K_UP:
                if number != 19:
                    number += 1
                    print number
            if event.key == pygame.K_DOWN:
                if number != 0:
                    number -= 1
                    print number
            
    # Svo procesiranje doga�aja ide iznad ovog komentara
    
    
    # Sav kod za iscrtavanja ide ispod ovog komentara
    # Postavljanje pozadine zaslona
    screen.fill(black)

    # Iscrtavanje plo�e
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
    #Mjenjanje iscrtavanja slika s obzirom na rje�enje koje smo dobili iz Prologa
    #rje�enja se nalaze unutar polja koje smo definirali na po�etku te se vrijednosti iz polja
    #mjenjaju s obzirom na pritisak tipke gore ili dolje
    for res in range(N):
          position = [width*(solutions[number][res]-1),height*res]
          screen.blit(pictures[res],position)
          

    # Sav kod za iscrtavanje ide iznad ovog komentara
    
    
    # Ograni�i na 20 frame-a po sekundi
    clock.tick(20)

    # Osvje�avanje ekrana s onim �to smo iscrtali
    pygame.display.flip()
    
#Bez ove linije program puca prilikom izlaska
pygame.quit ()

