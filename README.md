<p align="center">
  <img src="demo.gif" width="700">
</p>

<br/>


# BICEP-CURL-COUNTER
Contatore per bicep curl con tutte le sue varianti, distintamente per braccio destro e sinistro.

Ho usato un tutorial per iniziare a fare le prime detection e usare la libreria mediapipe. La feature che ho aggiunto sta nell'aver implementato anche per il braccio destro il meccasnismo di contatore e quindi avere due variabili contatore distinte, rispettivamente per braccio destro e sinistro; lo stesso per il calcolo dell'angolo tra i "joints" di spalla, gomito e polso, per destra e sinistra, quindi il calcolo di due angoli e quindi due variabili. In alto a sinistra è possibile tener traccia delle ripetizioni con braccio sinistro e in alto a destra le ripetizioni del braccio destro (oltre che essere stampate alla console sul terminale). 

COME USARLO: basta runnare il programma "hey_youps.py".  Quando si vuole terminare il programma, basta premere il tasto "q" da tastiera.


ASPETTI TECNICI: Chiaramente c'è bisogno di un IDE (tipo Visual Code) per lanciare il programma e installare un interprete Python (per le librerie come mediapipe e open-cv serve una versione Python 3.8 (come 3.8.12), ma anche una 3.9 l'ho provata e va bene, NON versioni maggiori!). Fatto questo, poi, bisogna installare le dipendenze, le ho messe tutte nel file "requirements.txt"; per fare ciò, da terminale basta eseguire: "pip install -r requirements.txt" e premere invio. NB: per chi ha già una versione Python maggiore a 3.9, come me, basta creare un virtualenv con la versione di Python specificata(3.8.12); infatti è presente anche la cartella "venv" come guida per ricordare questa cosa fondamentale. Quindi creare un virtualenv basato su quella versione Python e installare le dipendenze nel file "requirements.txt" come scritto prima.
