# tesi
Per il funzionamento del progamma è necessario, in aggiunga alla installazione standard di Python,
installare le seguenti librerie:
pandas e dash-mantine-components (che a sua volta installerà dash e tutto il software necessario).

Per utilizzare il programma cliccare sul file python "app", copiare nel browser l'url che compare nel terminale, 
utilizzare il programma seguendole istruzioni al suo interno.

In questa repository sono presenti i seguenti file:

"app": file python principale del programma.

"modulo_elaborazione_dati": file python contenente un modulo che non deve essere lanciato dall'utente 
                            ma viene richiamato automaticamente dal file principale.
                            Il file elabora i dati in uscita dal simulatore.

"simulatore_tesi": file python contenente un modulo che non deve essere lanciato dall'utente 
                   ma viene richiamato automaticamente dal file principale.
                   Il file simula i dati necessari per il programma attraverso distribuzioni statistiche.
		               Il file genera utilizzando i dati simulati i 4 csv, che seguono nell'elenco, in cui
		               scrive e/o aggiorna le informazioni.

"primo_csv": file csv contenente dati riguardanti il tempo metereologico	

"secondo_csv":file csv contenente dati riguardanti i prezzi simulati dal programma

"terzo_csv":file csv contenente dati riguardanti date e profitti simulati dal programma

"campi_csv":file csv contenente dati riguardanti i campi agricoli simulati dal programma
