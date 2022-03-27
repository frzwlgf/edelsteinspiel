
import random
import pygame
import os
import numpy as np
import sys
import neat
import pickle


pygame.font.init()


BREITE, HÖHE = 1000, 800
WIN = pygame.display.set_mode((BREITE,HÖHE))
pygame.display.set_caption("Dominion")
BLACK = (0,0,0)
WHITE = (255,255,255)
FARBE = (45,0,237)
NEUE_FARBE = (65,235,1)
Zweite_Farbe =  (13,190,21)
FPS = 30000
BildBreite , BildHöhe = 1000 , 600


Feld_Font = pygame.font.SysFont("comicsans",50)

Brett_image = pygame.image.load(os.path.join("Assets","Brett.jpg"))
Brett = pygame.transform.scale(Brett_image, (BildBreite, BildHöhe))

array=[]


Feld1 = np.array([0,0,0,0,2,2,2,2,
        2,2,2,2,2,2,2,2])

Feld2 = np.array([0,0,0,0,2,2,2,2,
        2,2,2,2,2,2,2,2])



def besterzug(Feld1,Feld2):
    
    bestezüge_gegner = []
    bestezüge = []
    
    for x in range (len(Feld2)):

        
        
        Feld1_1 = Feld1.copy()
        Feld2_1 = Feld2.copy()
        if Feld2[x]>1:
            s = 0
            Steine = Feld2[x]
            Feld2_1[x ]= 0
            while s < 100:
                s += 1
                while Steine > 0:
                    if x != 15:
                        x = x+1
                    else:
                        x = 0
        
                    Feld2_1[x] = 1+Feld2_1[x]
                    Steine = Steine-1
        
                if Feld2_1[x] > 1:
                    
                    Steine = Feld2_1[x]
    
                    Feld2_1[x] = 0
                    if x<8:
                        Steine = Steine+Feld1_1[7-x]
                        Feld1_1[7-x] = 0
                
                else:
                    s = 100
        Summe = 0
        for i in Feld2_1:
            Summe = Summe+i
        
        bestezüge.append(Summe)

        
        bestezüge_1 = []
        for y in range (len(Feld2)):
            
            Feld1_1_1 = Feld1_1.copy()
            Feld2_1_1 = Feld2_1.copy()
            if Feld1_1[y]>1:
                s = 0
                Steine = Feld1_1[y]
                Feld1_1_1[y]= 0
                while s < 100:
                    s += 1
                    while Steine > 0:

                        if y != 15:
                            y += 1
                        else:
                            y = 0
            
                        Feld1_1_1[y] = 1+Feld1_1_1[y]
                        Steine = Steine-1
            
                    if Feld1_1_1[y] > 1:
                        Steine = Feld1_1_1[y]
        
                        Feld1_1_1[y] = 0
                        if y<8:
                            Steine = Steine+Feld2_1_1[7-y]
                            Feld2_1_1[7-y] = 0
                    else:
                        s = 100
            Summe = 0
            for j in Feld1_1_1:
                Summe = Summe+j
            
            bestezüge_1.append(Summe)
        
        
        bestezüge_gegner.append(max(bestezüge_1))
        
    
    while 1>0:
        
        q = np.argmin(bestezüge_gegner) 
        p = min(bestezüge_gegner)
        if p == 100:
            
            return 100
        else:
            if Feld2[q]>1:
                
                return q
            else:
                bestezüge_gegner[q]=100
                




def zufalls_zug(Feld2):
    m_zuge = []
    for o,p in enumerate(Feld2):
        if p > 1:
            m_zuge.append(o)
    return random.choice(m_zuge)       




def draw(Feld1,Feld2):
    clock = pygame.time.Clock()
    clock.tick(10)

    WIN.blit(Brett,(0,0))
    lä = 50
    hö = 350
    for x,i in enumerate(Feld1):

        if x < 8:
            Zahl = str(i)
            
            
            Zahl_txt =  Feld_Font.render(Zahl,1,BLACK)
            WIN.blit(Zahl_txt,(lä,hö))
            lä = lä + 125
        else:
            hö = 495
            lä = 50
            for x,i in enumerate(reversed(Feld1)):
                if x < 8:
                    Zahl = str(i)


                    
                    Zahl_txt =  Feld_Font.render(Zahl,1,BLACK)
                    WIN.blit(Zahl_txt,(lä,hö))
                    lä = lä + 125
    lä = 50
    hö = 0
    i = 7
    while i < 15:
        i += 1
        Zahl = str(Feld2[i])
            
            
        Zahl_txt =  Feld_Font.render(Zahl,1,BLACK)
        WIN.blit(Zahl_txt,(lä,hö))
        lä = lä + 125

    hö = 180
    lä = 50
    for x,i in enumerate(reversed(Feld2)):
        if x > 7:
            Zahl = str(i)


                    
            Zahl_txt =  Feld_Font.render(Zahl,1,BLACK)
            WIN.blit(Zahl_txt,(lä,hö))
            lä = lä + 125



    pygame.display.update ()

def Zug_Spieler1(array,Feld1,Feld2):
   
            x=array[0]
            s=0
            Steine=Feld2[x]
            Feld2[x]=0
            while s < 100:
                s += 1
                while Steine>0:
                    if x!=15:
                        x=x+1
                    else:
                        x=0

                    Feld2[x]=1+Feld2[x]
                    Steine=Steine-1
                    #draw(Feld1,Feld2)
                if Feld2[x]>1:
                    Steine=Feld2[x]
    
                    Feld2[x]=0
                    if x<8:
                        Steine=Steine+Feld1[7-x]
                        Feld1[7-x]=0
                else:
                    s = 100

                #draw(Feld1,Feld2)
            return Feld2,Feld1

def Zug_Spieler2(array,Feld1,Feld2,genome):           
            x = array[0]
            s=0
            Steine=Feld1[x]
            Feld1[x]=0
            while s < 100:
                s += 1
                while Steine>0:
                    if x!=15:
                        x=x+1
                    else:
                        x=0
        
                    Feld1[x]=1+Feld1[x]
                    Steine=Steine-1
                    #draw(Feld1,Feld2)  
                if Feld1[x]>1:
                    Steine=Feld1[x]
    
                    Feld1[x]=0
                    if x<8:
                        Steine=Steine+Feld2[7-x]
                        genome.fitness += Feld2[7-x]
                        Feld2[7-x]=0

                else:
                    s=100
                
            #draw (Feld1,Feld2)   
              
            return Feld2,Feld1


def mauspoisition(array):
    feldbreite = 125
    feldhöhe = 150
    Mausx,Mausy = pygame.mouse.get_pos()
    if Mausy < feldhöhe*4 and Mausy > feldhöhe*3:
        if Mausx < feldbreite:
            array.append(15)
            return False
        elif Mausx < feldbreite*2:
            array.append(14)
            return False
        elif Mausx < feldbreite*3:
            array.append(13)
            return False

        elif Mausx < feldbreite*4:
            array.append(12)
            return False

        elif Mausx < feldbreite*5:
            array.append(11)
            return False

        elif Mausx < feldbreite*6:
            array.append(10)
            return False

        elif Mausx < feldbreite*7:
            array.append(9)
            return False

        elif Mausx < feldbreite*8:
            array.append(8)
            return False

    elif Mausy < feldhöhe*3 and Mausy > feldhöhe*2:
        if Mausx < feldbreite:
                array.append(0)
                return False
        elif Mausx < feldbreite*2:
                array.append(1)
                return False
        elif Mausx < feldbreite*3:
                array.append(2)
                return False

        elif Mausx < feldbreite*4:
                array.append(3)
                return False

        elif Mausx < feldbreite*5:
                array.append(4)
                return False

        elif Mausx < feldbreite*6:
                array.append(5)
                return False

        elif Mausx < feldbreite*7:
                array.append(6)
                return False

        elif Mausx < feldbreite*8:
                array.append(7)
                return False










def eval_genomes(genomes, config):




    for genome_id, genome in genomes:
        
        Feld1 = np.array([0,0,0,0,2,2,2,2,
        2,2,2,2,2,2,2,2])

        Feld2 = np.array([0,0,0,0,2,2,2,2,
        2,2,2,2,2,2,2,2])


        
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        genome.fitness = 0.0
                
        clock = pygame.time.Clock()

        array = [0]
        run = 0
        while run<100:
            
            run += 1
            
            genome.fitness += 1
            clock.tick(FPS)
            
            Myturn = besterzug(Feld1,Feld2)
            
            #Myturn = zufalls_zug(Feld2)
            if Myturn != 100:
                array.append(Myturn)
            
            if len (array) > 0:
                Feld2, Feld1 = Zug_Spieler1(array,Feld1,Feld2)
            else:
                genome.fitness += 10000/run
                run = 1000
                print("gewonnen")
            #draw (Feld1,Feld2)
            array = []
            

            
            output = net.activate(
        (Feld1[0],Feld1[1],Feld1[2],Feld1[3],Feld1[4],Feld1[5],Feld1[6],Feld1[7],Feld1[8],Feld1[9],
Feld1[10],Feld1[11],Feld1[12],Feld1[13],Feld1[14],Feld1[15],Feld2[0],Feld2[1],Feld2[2],Feld2[3],Feld2[4],
Feld2[5],Feld2[6],Feld2[7],Feld2[8],Feld2[9],Feld2[10],Feld2[11],Feld2[12],Feld2[13],Feld2[14],Feld2[15]))

            list1 = enumerate(output)
            list2 = sorted  (list1, key=lambda x:x[1])

            decision = []

            for i in reversed(list2):
                decision.append(i[0])
            
            while len(decision)>1:
                if Feld1[decision[0]] > 1:

                    array.append(decision[0])
                    break
                else:
                    decision.pop(0)
            
            if len(array) > 0:
                Feld2, Feld1 = Zug_Spieler2(array,Feld1,Feld2,genome)

                array = []
            else:
                run  = 1000
            
        genome.fitness = genome.fitness + sum(Feld1)
        






def karl_vs_Mensch ():
    
    clock = pygame.time.Clock()

    array = []
    run = True
    while run:
        clock.tick(FPS)
        Myturn = besterzug(Feld1,Feld2)
        array.append(Myturn)
        
        Zug_Spieler1(array,Feld1,Feld2)


        array = []
        nix_passiert = True
        while nix_passiert:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:

                        nix_passiert = mauspoisition(array)
    
        Zug_Spieler2(array,Feld1,Feld2)
        array = []
    pygame.quit()


def karl_vs_kai(config):

    #p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-85')
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(100))

    winner = p.run(eval_genomes, 5000)
    with open("best.pickle", "wb") as f:
        pickle.dump(winner, f)


if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')

    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)
    #karl_vs_Mensch ()
    karl_vs_kai(config)
    #test_best_network(config)