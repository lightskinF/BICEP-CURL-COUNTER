# BICEP-CURL-COUNTER
Contatore per bicep curl con tutte le sue varianti, distintamente per braccio destro e sinistro.

Ho usato un tutorial per iniziare a fare le prime detection e usare la libreria mediapipe. La feature che ho aggiunto sta nell'aver implementato anche per il braccio destro il meccasnismo di contatore e quindi avere due variabili contatore distinte, rispettivamente per braccio destro e sinistro; lo stesso per il calcolo dell'angolo tra i "joints" di spalla, gomito e polso, per destra e sinistra, quindi il calcolo di due angoli e quindi due variabili. In alto a sinistra è possibile tener traccia delle ripetizioni con braccio sinistro e in alto a destra le ripetizioni del braccio destro (oltre che essere stampate alla console sul terminale). 

COME USARLO: basta runnare il programma "hey_youps.py".  Quando si vuole terminare il programma, basta premere il tasto "q" da tastiera.


ASPETTI TECNICI: Chiaramente c'è bisogno di un IDE (tipo Visual Code) per lanciare il programma e installare un interprete Python. Fatto questo, poi, bisogna installare le dipendenze; le ho messe tutte nel file "requirements.txt"; per fare ciò, da terminale basta eseguire:  
