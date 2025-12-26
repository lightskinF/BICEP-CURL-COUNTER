# BICEP-CURL-COUNTER
Contatore per bicep curl con tutte le sue varianti, distintamente per braccio destro e sinistro.

Ho usato un tutorial per iniziare a fare le prime detection e usare la libreria mediapipe. La feature che ho aggiunto sta nell'aver implementato anche per il braccio destro il meccasnismo di contatore e quindi avere due variabili contatore distinte, rispettivamente per braccio destro e sinistro; lo stesso per il calcolo dell'angolo tra i "joints" di spalla, gomito e polso, per destra e sinistra, quindi il calcolo di due angoli e quindi due variabili. In alto a sinistra è possibile tener traccia del ripetizioni con braccio sinistro e in alto a destra le ripetizioni del braccio destro (oltre che essere stampate alla console sul terminale). 

Funzionamento molto semplice: basta runnare il programma "hey_youps.py". Chiaramente serve un interprete Python e le dipendenze, che sono presenti nella cartella "venv". Quando si vuole terminare il programma, basta premere il tasto "q" da tastiera.
