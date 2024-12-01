################################################
# Programmeerimine I
# 2024/2025 sügissemester
#
# Projekt Tuto
# Teema: Keskendumise hindaja
#
#
# Autorid: Mattias Rahnu, Hugo Tristan Tammik
#
# Eeskuju: Saadud inspiratsiooni face_recognitioni projektikirjelduses olevatest näidetest,
#          loodud teemakohasemaks.
#
#Käivitamiseks:Vaja laadida C++ Build tools (installimisel vaja märkida desktop development, kõige ülemine ning vasakpoolseim)
#              Laadida vaja face_recognition: pip install face-recognition cmd-s
#              Laadida vaja ka opencv: pip install opencv-python
#
##################################################


import face_recognition
import cv2




# valib veebikaamera (0 on esimene (ainuke))
kaamera = cv2.VideoCapture(0)

# tulevad koordinaadid
face_locations = []
kontrollitav_kaader = True

# muutuja kasti (näo tuvastuskauguse) jaoks
d = 0.5
s = int(1/d)

#kaadrite arv (mitme kaadri tagant kontrollida kohalolu)
f = 1

# p - mitu kaadrit oldi kohal | n - mitu kaadrit ei tuvastatud inimest
p=0
n=0

while True:


    # vahelejäävad kaadrid
    i=0
    while i < f:
        #ret on tagastusväärtus
        ret, kaader = kaamera.read()
        i+=1

    # kontrollitav kaader
    if kontrollitav_kaader:
        # kaadri väiksemaks tegemine näo kiiremaks tuvastamiseks
        pisem_kaader = cv2.resize(kaader, (0, 0), fx=d, fy=d)

        # Näotuvastus - tuvastab ning lisab koordinaadid järjendisse face_locations
        face_locations = face_recognition.face_locations(pisem_kaader)
        # Juhul kui nägu ei tuvastatud
        if face_recognition.face_locations(pisem_kaader) != []:
            p +=1
        else:
            n +=1


    kontrollitav_kaader = not kontrollitav_kaader

    # Teeb kasti
    for (ülemine, parem, alumine, vasak) in face_locations:
        # näo asukoha toob tagasi e kasti asukoha muudab õigeks
        ülemine *= s
        parem *= s
        alumine *= s
        vasak *= s

        cv2.rectangle(kaader, (vasak, ülemine), (parem, alumine), (0, 0, 255), 2)

    # Näitab kontrollitavat kaadrit
    cv2.imshow('Video', kaader)
    

    # Vajutades q-d, lõpetab tegevuse
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

    

# Lõpetab tegevuse
kaamera.release()
cv2.destroyAllWindows()

# arvutused
print(p) #kaadrid, mil oldi kohal
print(n) #kaadrid, millal ei oldud kohal
if n != 0:
    print((p*100)/(p+n))
    if (p*100)/(p+n) > 80:
        print("Keskendusid väga palju!")
        
else:
    print("Keskendusid kogu aja!")
    
    
<<<<<<< HEAD:Keskendumise_hindaja-TOIMIV.py
    
=======
    
>>>>>>> 9ca31e633fec4f6e3d328a4eef62ca6977d2bb73:TOIMIB.py
