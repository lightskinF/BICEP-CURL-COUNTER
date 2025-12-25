#devo usare python versione 3.11, la 3.13 non va bene, per scaricare libreria mediapipe!
import cv2
import mediapipe as mp
import numpy as np

#FUNZIONE PER CALCOLARE L'ANGOLO TRA 3 PUNTI
def calculate_angle(a,b,c):             #gli passo 3 punti come liste di coordinate x,y di spalla, gomito, polso
    a=np.array(a)  #primo punto
    b=np.array(b)  #secondo punto
    c=np.array(c)  #terzo punto

    radians=np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])   #calcolo l'angolo in radianti tra i 3 punti
    angle=np.abs(radians*180.0/np.pi)   #converto in gradi

    if angle>180.0:
        angle=360-angle

    return angle

#VARABILI PER CURL COUNTER
left_counter=0
right_counter=0
stage1=None
stage2=None

#INIZIALIZZAZIONE MEDIAPIPE
mp_drawing=mp.solutions.drawing_utils       #i componenti di mediapipe sono sempre solutions. questa variabile per visulaizzare le nostre pose
mp_pose=mp.solutions.pose               #modello per stima posa!

#VIDEO FEED setup x la webcam
cap=cv2.VideoCapture(0)     #setto il videocapture device (webcam o una camera in generale, collegata alla macchina)
#attento al numero 0, devi capire tu, forse non è questo, dipende dalla tua camera!!!!!!!!!! solitamente, prova con 0,1,2,3
if not cap.isOpened():
    print(" Webcam non aperta")
    exit()

with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:   #inizializzo il modello di posa con i suoi parametri, 50% accuracy, puoi metterla piu alta ma poi non sempre fa la detection
    while cap.isOpened():
        ret, frame=cap.read()   #ret non ci interessa, ma frame ci DA L'IMMAGINE DALLA NOSTRA WEBCAM, raccolgo in questa variabile

        image=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)   #converto l'immagine da BGR a RGB, perche mediapipe lavora in RGB e mp_pose quindi pose sopra con la with è un istanza di tipo mediapipe
        image.flags.writeable=False    #per ottimizzare le prestazioni, dico che l'immagine non è scrivibile

        #fa la detection della posa
        results=pose.process(image)    #processo l'immagine con il modello di posa, e salvo i risultati nella variabile results

        image.flags.writeable=True     #ora l'immagine è scrivibile di nuovo, perche dobbiamo disegnare sopra i landmarks
        image=cv2.cvtColor(image, cv2.COLOR_RGB2BGR)   #riconverto l'immagine da RGB a BGR per visualizzarla con opencv e disegnare sopra i landmarks!


        #estrazione delle landmarks della posa, cioe 33 punti chiave (joints) del corpo umano
        try:
            landmarks=results.pose_landmarks.landmark   #estraggo i landmarks dalla variabile results

            #ESTRAIAMO LE COORDINATE DEI LANDMARKS DI SPALLE, BRACCIA E GOMITO PER FARE IL CALCOLO DELL'ANGOLO
            #lo faccio per il braccio sinistro ma puoi farlo anche per il destro cambiando LEFT in RIGHT, e poi fare un altro counter per il destro; COSì FACCIO.

            left_shoulder=[landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]   #estraggo le coordinate x e y della spalla sinistra
            left_elbow=[landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]   #estraggo le coordinate x e y del gomito sinistro
            left_wrist=[landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,  landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]   #estraggo le coordinate x e y del polso sinistro

            right_shoulder=[landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]  
            right_elbow=[landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]   
            right_wrist=[landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,  landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]

            #calcoliamo l'angolo tra spalla, gomito e polso SINISTRO
            angle1=calculate_angle(left_shoulder, left_elbow, left_wrist)   #funzione, definita a riga 6, che calcola l'angolo tra 3 punti
            #per il destro fai lo stesso, raccogli l'angolo e poi per visualizzarlo fai cv2.putText come sotto
            angle2=calculate_angle(right_shoulder, right_elbow, right_wrist)

            #visualizziamo l'angolo sull'immagine
            cv2.putText(image, str(angle1), 
                        tuple(np.multiply(left_elbow, [640,480]).astype(int)),   #metto l'angolo vicino al gomito, moltiplico per la risoluzione della webcam
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2, cv2.LINE_AA
                        )
            
            cv2.putText(image, str(angle2), 
                        tuple(np.multiply(right_elbow, [640,480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2, cv2.LINE_AA
                        )

            #FACCIO IL COUNTER DEI CURLS. sia per il braccio sinistro che per il destro

            if angle1>155:    #se l'angolo è piu di 155 gradi, il braccio è disteso
                stage1="down"
            if angle1<32 and stage1=="down":   #se l'angolo è meno di 32 gradi, il braccio è piegato
                stage1="up"
                left_counter+=1    #incremento il counter di 1
                print(left_counter)   #stampo il counter sulla console

            if angle2>155:
                stage2="down"
            if angle2<32 and stage2=="down":
                stage2="up"
                right_counter+=1
                print(right_counter)
            

        except:
            pass    #la camera magari non vede tutti landmark nel momento in cui mi inquadra, quindi semplicemente vado avanti senza fare nulla
    
        #MOSTRO ALLO SCHERMO IL COUNTER E LO STAGE
        cv2.rectangle(image, (0,0), (225,73), (245,117,16), -1)   #disegno un rettangolo in alto a sinistra per visualizzare il counter e lo stage
        cv2.putText(image, 'REPS VALIDE SINISTRA:', (15,12), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
        cv2.putText(image, str(left_counter), (10,60), 
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
        
        cv2.rectangle(image, (350,0), (575,73), (245,117,16), -1)   #disegno un rettangolo in alto a destra per visualizzare il counter per la destra
        cv2.putText(image, 'REPS VALIDE DESTRA:', (400,12), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
        cv2.putText(image, str(right_counter), (400,60), 
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
        
        

        #disegno i landmarks della posa sull'immagine
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,  #questi 3 parametri FONDAMENTALI servono per disegnare i landmarks
                                  mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), #cambio colore, spessore e raggio dei cerchi dei landmarks
                                  mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2)
                                  )

        cv2.imshow("BICEPS_COUNTER", image) #CI PERMETTE DI visualizzarla, l'immagine sopra "frame", infatti gleila passi come secondo parametro!

        if cv2.waitKey(10) & 0xFF == ord('q'):    #SE PREMO q O ESCO DALLO SCHERMO, FAI IL BREAK AL LOOP E RILASCI LA WEBCAM ELIMINANDO TUTTE LE FINESTRE. 0XFF indica cosa inserisci da tastiera
            break

    #PER USCIRE DALLA FINESTRA della fotocamer quindi PREMI 'q'

cap.release()   #rilascio la webcam
cv2.destroyAllWindows   ()  #distruggo tutte le finestre create da opencv






