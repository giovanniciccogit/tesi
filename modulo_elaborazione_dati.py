# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 21:18:35 2025

@author: cicco
"""

import dash_mantine_components as dmc
#
#la prossima funzione seleziona la serie della temperatura e offre un output in formato accettabiled da "mantine"
def seleziona_converti_serie(dataset_iniziale,richiesta):
    
    #n corrisponde a quale dataset di panda ci si sta riferendo
    #i corrisponde a quali colonne si prendono in considerazione
    n=0
    i=0
    #result è la variabile che esprimera il risultato in forma di dizionario
    risultato={}
    
    
    
    if richiesta=="temperatura":
        n=0
        i=1
    elif richiesta=="umidità":
        n=0
        i=2
    elif richiesta=="precipitazioni":
        n=0
        i=3
    elif richiesta=="azionari":
        n=1
    elif richiesta=="colture":
        n=2
    elif richiesta=="profitti_finali":
        n=5
    
    
    risultato_parziale=(dataset_iniziale[n])
    #il caso in di n== 0 comprende l'elaborazione dei dati proveniente dal primo dataset di panda overo i dati riguardanti temperatura,umidità e precipitazioni
    if n==0:
        risultato_forma_dizionario = [{'giorno': (risultato_parziale[0])[selettore], 'valore': (risultato_parziale[i])[selettore]} for selettore in range(len(risultato_parziale[i]))]
        #print(risultato_forma_dizionario)
    
        risultato=risultato_forma_dizionario
        
        
    elif n==1:
        #il caso in di n== 0 comprende l'elaborazione dei dati proveniente dal secondo dataset di panda ovvero i dati riguardanti le variazioni dei prezzi degli asset azionari
        
        #si ottiene un dizionario che tiene conto dell'esistenza di tre asset finanziari
        risultato_forma_dizionario = [{'giorno': (risultato_parziale[0])[selettore], 'grano_primaverile': (risultato_parziale[1])[selettore], 'carote': (risultato_parziale[2])[selettore],'patate': (risultato_parziale[3])[selettore]} for selettore in range(len(risultato_parziale[0]))]
        
        risultato=risultato_forma_dizionario
        
    elif n==2:
        #risultato_forma_dizionario=risultato_parziale
        
        risultato=dataset_iniziale[n],dataset_iniziale[n+1]
    #elif n==3 manca perche è "contenuto" in elif n==2
    #elif n==4 manca perchè contiene come output l numero di anni richiesto
    elif n==5:
        
        risultato=dataset_iniziale[n]
        #print(risultato)
    
    
    return risultato
















