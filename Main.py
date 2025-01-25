import winsound
import pyautogui as pag  
import time
from python_imagesearch.imagesearch import imagesearch
from pynput.mouse import Button, Controller

#delay to let screen refresh and display every monster / citadel / crypt / ... and mercenary echange :)
delay = 1.0

#Nb of steps to scroll an entire kingdom horizontlly
nb_horizontal_moves = 32
#Nb of steps to scroll an entire kingdom horizontlly
nb_vertical_moves = 25

time1 = time.time()

mouse = Controller()

# Set pointer position
#mouse.position = (125, 734)
#mouse.click(Button.left, 1)
#time.sleep(1.5)
    
# frequency is set to 500Hz
freq = 500
 
# duration is set to 100 milliseconds            
dur = 500

trouve = False
              
#parcours du royaume du nord au sud 
for j in range(nb_vertical_moves) : 
    print('Start of ', j+1, 'th western scrolling ---->')
    #parcours horizontal d'un royaume complet d'ouest en est à ordonnée constante
    for i in range (nb_horizontal_moves) : 
        print(i+1, 'th step to the west (', j+1, 'th trip)')
        pos = imagesearch('.\Image assets\Exchange.PNG')
        #print('capture screen')
        if pos[0] != -1:                                                                               
            trouve = True
            #print("i=", i, ": trouvé :)")
            print("Found! Position : ", pos[0], pos[1])
            winsound.Beep(freq, dur)
            del pos
            break
        else : 
            #print("i =", i, " : KO :(")
            #position permettant de décaler exactement d'un écran vers la droite
            mouse.position = (125, 734)
            mouse.click(Button.left, 1)
            time.sleep(delay)
            del pos
    if trouve == True : 
        break
    else : 
        print('End of ', j+1, 'th western scrolling')
        #on descend de 20 unités dans les ordonnées
        mouse.position = (92, 744)
        mouse.click(Button.left, 1)
        print('Moving one step south')
        time.sleep(delay)
    #parcours horizontal d'un royaume complet d'est en ouest à ordonnée constante
    print('<---- Start of ', j+1, 'th eastern scrolling')
    i = 0
    for i in range (nb_horizontal_moves) : 
        pos = imagesearch('.\Image assets\Exchange.PNG')
        #print('capture screen')
        if pos[0] != -1:                                                                                 
            trouve = True
            #print("i=", i, ": trouvé :)")
            print("Found! Position : ", pos[0], pos[1])    
            winsound.Beep(freq, dur)
            del pos
            break
        else : 
            #print("i=,", i, " : KO :(")
            #position permettant de décaler exactement d'un écran vers la gauche
            mouse.position = (60, 734)
            mouse.click(Button.left, 1)
            print(i+1, 'th step to the east (', j+1, 'th trip)')
            del pos
        time.sleep(delay)
    
    if trouve == True : 
        break
    else : 
        print('End of ', j+1, 'th eastern scrolling')    
        #on descend de 20 unités dans les ordonnées
        mouse.position = (92, 744)
        mouse.click(Button.left, 1)
        print('Moving one step south')
    time.sleep(delay)
   
print("Done in : " + str(time.time() - time1) + " seconds")
