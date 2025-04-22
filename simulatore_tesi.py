# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 20:16:24 2025

@author: ciccolella Giovanni
"""
import numpy as np
import math
import pandas as pd
#simulatore
#il simulatore ha il compito di definire i dati contenuti nel csv
#ha anche il compito di variarli ogni qualvolta l'utente lo desidera
    
#questo è l'insieme delle funzioni che svolgono una sub-routine nella funzione simulatrice

def crea_base_temperatura(anni):
    #questa funzione crea una base per la serie storica delle temperature che verra successivamente ulteriormente modificata.
    #la base per questa serie viene creata simulando trimestre fiscale per trimestre fiscale, mese per mese
    #il trimestre fiscale viene associato per comodità a una stagione nonostante la corrispondenza non sia perfetta. 
    #questo processo può essere simulato piu volte a seconda del numero di anni da simulare desiderato
    anno=0
    
    for i in range(anni):
        
        anno+=1
        #andiamo a generare i mesi e a unirli in trimestri
        M01_Gennaio=simula_base_mese("M01_Gennaio","temperatura")[0]
        M02_Febbraio=simula_base_mese("M02_Febbraio","temperatura")[0]
        M03_Marzo=simula_base_mese("M03_Marzo","temperatura")[0]
        
        Q1_Inverno=np.concatenate((M01_Gennaio, M02_Febbraio,M03_Marzo))
        
        M04_Aprile=simula_base_mese("M04_Aprile","temperatura")[0]
        M05_Maggio=simula_base_mese("M05_Maggio","temperatura")[0]
        M06_Giugno=simula_base_mese("M06_Giugno","temperatura")[0]
        
        Q2_Primavera=np.concatenate((M04_Aprile, M05_Maggio,M06_Giugno))
        
        M07_Luglio=simula_base_mese("M07_Luglio","temperatura")[0]
        M08_Agosto=simula_base_mese("M08_Agosto","temperatura")[0]
        M09_Settembre=simula_base_mese("M09_Settembre","temperatura")[0]
        
        Q3_Estate=np.concatenate((M07_Luglio, M08_Agosto,M09_Settembre))
        
        M10_Ottobre=simula_base_mese("M10_Ottobre","temperatura")[0]
        M11_Novembre=simula_base_mese("M11_Novembre","temperatura")[0]
        M12_Dicembre=simula_base_mese("M12_Dicembre","temperatura")[0]
        
        Q4_Autunno=np.concatenate((M10_Ottobre, M11_Novembre,M12_Dicembre))
        #generati i trimestri possiamo ottenere la sequenza contenente le temperature simulate per un anno
        anno_corrente=np.concatenate((Q1_Inverno, Q2_Primavera,Q3_Estate,Q4_Autunno))
        if anno==1:
            anni=anno_corrente
        else :
            anni=np.concatenate((anni, anno_corrente))
    
    return anni

def crea_base_umidita(anni):
    #questa funziona ha lo stesso compito di "crea_base_temperatura" ma opera per ottenere una serie storica dell'umidità
    anno=0

    for i in range(anni):
        
        anno+=1
        #andiamo a generare i mesi e a unirli in trimestri
        M01_Gennaio=simula_base_mese("M01_Gennaio","umidità")[0]
        M02_Febbraio=simula_base_mese("M02_Febbraio","umidità")[0]
        M03_Marzo=simula_base_mese("M03_Marzo","umidità")[0]
        
        Q1_Inverno=np.concatenate((M01_Gennaio, M02_Febbraio,M03_Marzo))
        
        M04_Aprile=simula_base_mese("M04_Aprile","umidità")[0]
        M05_Maggio=simula_base_mese("M05_Maggio","umidità")[0]
        M06_Giugno=simula_base_mese("M06_Giugno","umidità")[0]
        
        Q2_Primavera=np.concatenate((M04_Aprile, M05_Maggio,M06_Giugno))
        
        M07_Luglio=simula_base_mese("M07_Luglio","umidità")[0]
        M08_Agosto=simula_base_mese("M08_Agosto","umidità")[0]
        M09_Settembre=simula_base_mese("M09_Settembre","umidità")[0]
        
        Q3_Estate=np.concatenate((M07_Luglio, M08_Agosto,M09_Settembre))
        
        M10_Ottobre=simula_base_mese("M10_Ottobre","umidità")[0]
        M11_Novembre=simula_base_mese("M11_Novembre","umidità")[0]
        M12_Dicembre=simula_base_mese("M12_Dicembre","umidità")[0]
        
        Q4_Autunno=np.concatenate((M10_Ottobre, M11_Novembre,M12_Dicembre))
        #generati i trimestri possiamo ottenere la sequenza contenente le temperature simulate per un anno
        anno_corrente=np.concatenate((Q1_Inverno, Q2_Primavera,Q3_Estate,Q4_Autunno))
        if anno==1:
            anni=anno_corrente
        else :
            anni=np.concatenate((anni, anno_corrente))
    return anni

def crea_base_pioggia(anni):
    #questa funziona ha lo stesso compito di "crea_base_temperatura" ma opera per ottenere una serie storica della pioggia
    anno=0

    for i in range(anni):
        
        anno+=1
        #andiamo a generare i mesi e a unirli in trimestri
        M01_Gennaio=simula_base_mese("M01_Gennaio","pioggia")[0]
        M02_Febbraio=simula_base_mese("M02_Febbraio","pioggia")[0]
        M03_Marzo=simula_base_mese("M03_Marzo","pioggia")[0]
        
        Q1_Inverno=np.concatenate((M01_Gennaio, M02_Febbraio,M03_Marzo))
        
        M04_Aprile=simula_base_mese("M04_Aprile","pioggia")[0]
        M05_Maggio=simula_base_mese("M05_Maggio","pioggia")[0]
        M06_Giugno=simula_base_mese("M06_Giugno","pioggia")[0]
        
        Q2_Primavera=np.concatenate((M04_Aprile, M05_Maggio,M06_Giugno))
        
        M07_Luglio=simula_base_mese("M07_Luglio","pioggia")[0]
        M08_Agosto=simula_base_mese("M08_Agosto","pioggia")[0]
        M09_Settembre=simula_base_mese("M09_Settembre","pioggia")[0]
        
        Q3_Estate=np.concatenate((M07_Luglio, M08_Agosto,M09_Settembre))
        
        M10_Ottobre=simula_base_mese("M10_Ottobre","pioggia")[0]
        M11_Novembre=simula_base_mese("M11_Novembre","pioggia")[0]
        M12_Dicembre=simula_base_mese("M12_Dicembre","pioggia")[0]
        
        Q4_Autunno=np.concatenate((M10_Ottobre, M11_Novembre,M12_Dicembre))
        #generati i trimestri possiamo ottenere la sequenza contenente le temperature simulate per un anno
        anno_corrente=np.concatenate((Q1_Inverno, Q2_Primavera,Q3_Estate,Q4_Autunno))
        if anno==1:
            anni=anno_corrente
        else :
            anni=np.concatenate((anni, anno_corrente))
    return anni


def simula_base_mese(tipo_mese,tipo_richiesta):
    #questo programma simula le temperature,l'umidità e le precipitazione di una mese utilizzando una distribuzione di gauss
    #tenendo conto della stagione da generare, ne varia:
    #il numero di giorni,la aspettativa di temperatura
    #i dati indicati fanno  riferemento ad anni simili a firenze 2024 https://www.ilmeteo.it/portale/archivio-meteo/Firenze/2024/Gennaio & https://www.lamma.toscana.it/clima-e-energia/climatologia/clima-firenze-1981-2010
    
    x=[]
    giorni=0
    aspettativa_di_temperatura_mensile=0
    aspettativa_di_umidità_mensile=0
    aspettativa_di_pioggia_mensile=0
    aspettativa_giorni_di_pioggia_mensile=0
    
    #specifiche stagionali
    if tipo_mese=="M01_Gennaio":
        giorni=31
        aspettativa_di_temperatura_mensile=8.7
        aspettativa_di_umidità_mensile=76.4
        aspettativa_di_pioggia_mensile=63
        aspettativa_giorni_di_pioggia_mensile=13
        
    if tipo_mese=="M02_Febbraio":
        giorni=28
        aspettativa_di_temperatura_mensile=10.8
        aspettativa_di_umidità_mensile=79.7
        aspettativa_di_pioggia_mensile=57
        aspettativa_giorni_di_pioggia_mensile=12
        
    if tipo_mese=="M03_Marzo":
        giorni=31
        aspettativa_di_temperatura_mensile=12.3
        aspettativa_di_umidità_mensile=	80.3
        aspettativa_di_pioggia_mensile=59
        aspettativa_giorni_di_pioggia_mensile=19
        
    if tipo_mese=="M04_Aprile":
        giorni=30
        aspettativa_di_temperatura_mensile=14.9
        aspettativa_di_umidità_mensile=	69.3
        aspettativa_di_pioggia_mensile=75
        aspettativa_giorni_di_pioggia_mensile=10
        
    if tipo_mese=="M05_Maggio":
        giorni=31
        aspettativa_di_temperatura_mensile=18.7
        aspettativa_di_umidità_mensile=69.0
        aspettativa_di_pioggia_mensile=69
        aspettativa_giorni_di_pioggia_mensile=11
        
    if tipo_mese=="M06_Giugno":
        giorni=30
        aspettativa_di_temperatura_mensile=22.4
        aspettativa_di_umidità_mensile=65.2
        aspettativa_di_pioggia_mensile=56
        aspettativa_giorni_di_pioggia_mensile=7
        
    if tipo_mese=="M07_Luglio":
        giorni=31
        aspettativa_di_temperatura_mensile=27.6
        aspettativa_di_umidità_mensile=55.8
        aspettativa_di_pioggia_mensile=33
        aspettativa_giorni_di_pioggia_mensile=3
        
    if tipo_mese=="M08_Agosto":
        giorni=31
        aspettativa_di_temperatura_mensile=28.5
        aspettativa_di_umidità_mensile=	55.8
        aspettativa_di_pioggia_mensile=50
        aspettativa_giorni_di_pioggia_mensile=4
        
    if tipo_mese=="M09_Settembre":
        giorni=30
        aspettativa_di_temperatura_mensile=21.3
        aspettativa_di_umidità_mensile= 67.1
        aspettativa_di_pioggia_mensile=78
        aspettativa_giorni_di_pioggia_mensile=13
        
    if tipo_mese=="M10_Ottobre":
        giorni=31
        aspettativa_di_temperatura_mensile=17.8
        aspettativa_di_umidità_mensile= 81.2
        aspettativa_di_pioggia_mensile=102
        aspettativa_giorni_di_pioggia_mensile=20
        
    if tipo_mese=="M11_Novembre":
        giorni=30
        aspettativa_di_temperatura_mensile=11
        aspettativa_di_umidità_mensile= 73.5
        aspettativa_di_pioggia_mensile=112
        aspettativa_giorni_di_pioggia_mensile=7
        
    if tipo_mese=="M12_Dicembre":
        giorni=31
        aspettativa_di_temperatura_mensile=6.9
        aspettativa_di_umidità_mensile= 72.2
        aspettativa_di_pioggia_mensile=91
        aspettativa_giorni_di_pioggia_mensile=12
        
    #generazione la stringa delle temperature della stagione
    if tipo_richiesta=="temperatura":
        
        temperatura_mensile_serie = np.random.normal(aspettativa_di_temperatura_mensile, 2.0, giorni)
        for i in range(len(temperatura_mensile_serie)):
            temperatura_mensile_serie[i]=math.floor(temperatura_mensile_serie[i])
            
        return temperatura_mensile_serie,"ff"
    
    if tipo_richiesta=="umidità":
        
        umidità_mensile_serie= np.random.normal(aspettativa_di_umidità_mensile, 5.0, giorni)
        for i in range(len(umidità_mensile_serie)):
            umidità_mensile_serie[i]=math.floor(umidità_mensile_serie[i])
            #aggiungiamo una parte del ciclo per evitare il remoto seppur possibile caso in cui l'umidità raggiunga valori troppo alti
            if umidità_mensile_serie[i]>95:
                umidità_mensile_serie[i]=math.floor(95.0)
        return umidità_mensile_serie,"ff"
    
    if tipo_richiesta=="pioggia":
        #nel ottenere e simulare la pioggia viene utilizzato un metodo piu complesso di temperatura e umdità
        #utilizziamo una distribuzione binomial di nunpy per ottenere i giorni in cui pioverà all'interno del mese simulato
        #per ottenere i dati necessari per questa distribuzione e per terminare il processo di "simulazione" della pioggia procediamo per gradi
        
        #1 andiamo a ottenere la possibilità che in un dato giorno si verifichi "l'evento pioggia",utilizzando "aspettativa_giorni_di_pioggia_mensile" e "giorni=30"
        
        probabilità_evento_pioggia_giornaliero=aspettativa_giorni_di_pioggia_mensile/giorni
        
        #2 utilizziamo la distribuzione binomiale numpy per simulare quante volte e quando all'interno del mese pioverà
        #  impostiamo il numero di tentativi a 1 in quanto ci intiressa sapere se in un dato giorno piove e quindi è necessario simulare "l'evento" solo una volta al giorno
        # il valore di probabilità sarà quello calcolato nel passaggio precedente mentre quello della dimensione degli array sarà uguale ai giorni del mese simulato
        
        base_binaria_simulazione_giorni_di_pioggia=np.random.binomial(n=1, p=probabilità_evento_pioggia_giornaliero, size=giorni)
        #3 otteniamo con un brevissimo ciclo quante volte ha piovuto
        
        numero_giorni_di_pioggia_simulati=0
        for x in base_binaria_simulazione_giorni_di_pioggia:
            if x==1:
                numero_giorni_di_pioggia_simulati+=1
        if numero_giorni_di_pioggia_simulati==0:
            numero_giorni_di_pioggia_simulati=1
        
        #4 calcoliamo l'aspettativa di pioggia giornaliera
        #per farlo creiamo una costante che eviti di creare nella simulazione giorni in cui la quantità di pioggia è anormale oltre certi limiti
        costante_attenuante=1
        if numero_giorni_di_pioggia_simulati+2<aspettativa_giorni_di_pioggia_mensile:
            costante_attenuante=1-((aspettativa_giorni_di_pioggia_mensile-numero_giorni_di_pioggia_simulati)/aspettativa_giorni_di_pioggia_mensile)
        aspettativa_di_pioggia_giornaliera=(aspettativa_di_pioggia_mensile/numero_giorni_di_pioggia_simulati)*costante_attenuante
        math.floor(aspettativa_di_pioggia_giornaliera)

        #5 simuliamo con una distribuzione normale di numpy la quantità di pioggia in ogni  giorno di pioggia determinato precedentemente
        #  utilizziamo come aspettativa l'aspettativa di pioggia giornaliera e come numero di simulazioni il "numero_giorni_di_pioggia_simulati"
        
        stringa_pioggia_incompleta=np.random.normal(aspettativa_di_pioggia_giornaliera, 2, numero_giorni_di_pioggia_simulati)
        
        #6 la"stringa_pioggia_incompleta"potrebbe contenere dei valori inferiori ad 1 a causa del funzionamento del "np.random.normal"
        #  quindi viene utilizzato un ciclo per risolvere questo problema
        for i in range (len(stringa_pioggia_incompleta)):
            if stringa_pioggia_incompleta[i]<1:
                stringa_pioggia_incompleta[i]=1
            
        #7 utilizziamo un ciclo per inserire nella sequenza binaria che ha simulato in quali giorni durante il mese piove,i dati ottenuti dall'ultrima distribuzione
        #  scambiamo quindi tutti i dati binari "1" con un numero della sequenza "stringa_pioggia_incompleta"
        contatore_iterazioni=0
        numeri_1_incontrati=0 
        for y in base_binaria_simulazione_giorni_di_pioggia:
            contatore_iterazioni+=1
            if y==1:
                numeri_1_incontrati+=1
                base_binaria_simulazione_giorni_di_pioggia[contatore_iterazioni-1]=stringa_pioggia_incompleta[numeri_1_incontrati-1]
                
        #8 al termine del ciclo la "stringa_pioggia_incompleta" non conterra piu valori binari per indicare in quali giorni del mese è piovuto,
        #  bensì questa stringa conterra "0" nei giorni in cui non è piovuto affatto ed il valore della pioggia giornaliera simulata nei giorni in cui è piovuto.
        #  non ci resta che cambiare il nome della serie storica in maniera di avere un nome piu consono al contenuto
        
        pioggia_mensile_serie=base_binaria_simulazione_giorni_di_pioggia
        return pioggia_mensile_serie,"ff"
    #print(x)
    #print("mese")




    
#print(crea_base_temperatura(1))
#print(crea_base_umidita(1))
#print(crea_base_pioggia(1))
#print(len(crea_base_pioggia(1)))
#print(len(crea_base_temperatura(1)))
#print(len(crea_base_umidita(1)))


#la successiva parte del codice mira a simulare la variazione di un determinato asset finanziario nel tempo

def dati_asset(tipo_richiesta,nome_asset):
#questa funzione serve a ottenere in maniera comoda i dati riguardante gli asset(es. colture)
#questa funzione contiene i prezzi target a cui i prezzi degli specifici asset tendono
    

    dizionario_asset={
        #questo dizionario, in particolare,contiene tutti i dati riguardo gli asset che possono servire agli altre funzioni
        #in ordine i dati nella lista collegata a cisacun asset sono: 
        # 1 prezzo medio a cui l'asset"tende",2 prezzo minimo,3 prezzo massimo,4 tonnelate per ettaro prodotte in media
        # 5 data inizio coltivazione,6 data raccolta
        "grano_primaverile":(500,250,750,5,60,196),"carote":(400,200,600,50,80,150),"patate":(640,400,840,33,90,210)   
        }
    #partiamo col creare un eccezione che ci consenta di mandare in output i nomi di tutti gli elementi(asset) all'interno del dizionario  
    
    if tipo_richiesta=="lista_asset":
        lista_asset=[]
        for x in dizionario_asset:
            lista_asset.append(x)
        return lista_asset
    
    
    determinante_della_richiesta=0
    #questa parte della funzione serve a selezionare il giusto dato all'interno del dizionario
    if tipo_richiesta=="centro":
        determinante_della_richiesta=0
    elif tipo_richiesta=="minimo":
        determinante_della_richiesta=1
    elif tipo_richiesta=="massimo":
        determinante_della_richiesta=2
    elif tipo_richiesta=="base_produzione_per_ettaro":
        determinante_della_richiesta=3
    elif tipo_richiesta=="data_semina":
        determinante_della_richiesta=4
    elif tipo_richiesta=="data_raccolta":
        determinante_della_richiesta=5
    
        
    #quest'ultima parte della funzione rappresenta l'output della richiesta fatta
    asset_selezionato=dizionario_asset[nome_asset]
    richiesta_ultimata=asset_selezionato[determinante_della_richiesta]
    return richiesta_ultimata

def crea_base_temporale(anni):
    #questa funzione va a creare il riferimento temporale delle altre serie storiche
    #essa supporta le altre funzioni andando a creare un riferimento facilmente comprensibile ai giorni dell'anno
    #parallelamente alle altre serie storiche questa funzione quindi provvede il giorno dell'anno a cui gli altri dati si riferiscono
    #la scelta di utilizzare una funzione invece che un elenco fisso per creare questa serie serve a rendere il programma più modulare
    
    #questa variabile serve a capire quale sarà l'ultimo anno ad essere analizzata 
    #ad esempio se questa variabile indica l'anno "2025" l'ultimo anno ad essere analizzato sara il "2024"
    anno_corrente_di_riferimento=2025
    #il prossimo ciclo da analizzare crea una lista degli anni simulati
    lista_di_anni_da_analizzare=[]
    for i in range(anni):
        anno_da_aggiungere=anno_corrente_di_riferimento-anni+i
        lista_di_anni_da_analizzare.append(anno_da_aggiungere)
    #la prossima lista ha lo scopo di contenere la durata dei mesi
    durata_mesi=[["Gennaio",31],["Febbraio",28],["marzo",31],["aprile",30],["maggio",31],["giugno",30],["luglio",31],["agosto",31],["settembre",30],["ottobre",31],["novembre",30],["dicembre",31]]
    #il prossimo ciclo ha come scopo creare la serie cronologica di un singolo anno e sommarla agli altri anni
    base_temporale=[]
    for anno in lista_di_anni_da_analizzare:
        anno_da_aggiungere=[]
        for mese in durata_mesi:
            for giorno in range(1,mese[1]+1):
                giorno_creato=str(giorno)+" "+mese[0]+" "+str(anno)
                
                anno_da_aggiungere.append(giorno_creato)
    
    
        base_temporale=base_temporale+anno_da_aggiungere
    
    
    
    
    #base_temporale=lista_di_anni_da_analizzare#"aaaaaaaaaaaaaaaaa" 
    
    
    return base_temporale


def simula_prezzo_asset(asset,anni):
    
    #questa funzione cerca di simulare il prezzo di un asset nel tempo 
    #utilizza il principio della "random walk", ovvero partendo da un valore dato il prezzo sale e scende in maniera parzialmente randomica
    #vengono utilizzati delle probabilità pesate in maniera dinamica all'interno della random walk per garantire 
    #che il prezzo mantenga valori ragionevoli
    
    
    centro=dati_asset("centro",asset)
    minimo=dati_asset("minimo",asset)
    massimo=dati_asset("massimo",asset)
    
    range_prezzo=massimo-minimo
    sezione_prezzi_superiore=massimo-centro
    sezione_prezzi_inferiore=centro-minimo
    valore_di_partenza=np.random.uniform(((minimo//100)*110),((massimo//100)*90))
    valore_di_partenza=round(valore_di_partenza,2)
    array_serie_storica_prezzi=[]
    #stabilito il valori di minimo e di massimo,il valore a cui il prezzo della funziona"tende" e il valore di partenza della"random walk"(usando random.uniform)
    #si può iniziare la random walk
    prezzo=valore_di_partenza
    unità_lunghezza_camminata=centro/1000
    for x in range(anni):
        for giorno in range(0,365):
            #print(giorno)
            #per determinare la lunghezza della camminata moltiplichiamo l'apposita unità per un estrazione da un "dado con facce pesate"
            #quest'ultima utilizzata in questo modo diminuisce la possibilità di estrazione quanto più è alto il valore da estrarre
            #sarà piu facile estrarre un 3 che un 9
            tiro=np.random.randint(100)
            taglia=0
            if tiro<15:
                taglia=1 
            elif tiro<27:
                taglia=2
            elif tiro<40:
                taglia=3
            elif tiro<52:
                taglia=4 
            elif tiro<63:
                taglia=5
            elif tiro<73:
                taglia=6
            elif tiro<82:
                taglia=7
            elif tiro<90:
                taglia=8 
            elif tiro<95:
                taglia=9
            elif tiro<98:
                taglia=10
            else:
                taglia=0
            lunghezza_camminata=unità_lunghezza_camminata*taglia
            #a questo punto bisogna determinare il"verso della cammminata".considerando che questa "camminata ha solo due versi
            #bisognera solo decidere se in questo giorno il prezzo dell'azione dovrà salire o scendere
            #questo accadra in maniera tale da privilegiare a livello di probabilità uno dei due comportamenti in maniera dinamica
            probabilità_dinamica=0.5
            
            if prezzo<=minimo:
                probabilità_dinamica=1
                
            elif prezzo>=massimo:
                probabilità_dinamica=0
                
            else:
                k=0.10
                #k può essere al più 0.5
                if prezzo > centro:
                    distanza_dal_centro=prezzo-centro
                    distanza_dal_centro_relativa=distanza_dal_centro/(sezione_prezzi_superiore)
                    
                    probabilità_dinamica-=k*(distanza_dal_centro_relativa)
                elif prezzo < centro:
                    distanza_dal_centro=centro-prezzo
                    distanza_dal_centro_relativa=distanza_dal_centro/(sezione_prezzi_inferiore)
                
                    probabilità_dinamica+=k*(distanza_dal_centro_relativa)
                
                
                
            decisore=np.random.binomial(n=1, p=probabilità_dinamica, size=1)
            #print(decisore)
            if decisore==1:
                prezzo+=lunghezza_camminata
            elif decisore==0:
                prezzo-=lunghezza_camminata
            #print(prezzo)
            
            prezzo=round(prezzo,2)
            
            #print(prezzo)
            array_serie_storica_prezzi.append(prezzo)
    
            
    array_serie_storica_prezzi=np.array(array_serie_storica_prezzi)
    #print(array_serie_storica_prezzi)
    return(array_serie_storica_prezzi,"place_holder")

#simula_prezzo_asset("carote",2)

def simula_creazione_campi():
    #questa funzione simula brevemente la creazione di campi in numero e taglia variabile
    campi=[]
    numero_campi = np.random.randint(4,10)
    for campo in range(numero_campi):
        campi.append(np.random.randint(1,25))
    campi=np.array(campi)
    return campi

def popola_campi(campi_da_popolare,colture):
    #questa funziona cerca di popolare i campi precedentemente generati
    scheda_gemella_colture=[]
    for x in campi_da_popolare:
        scheda_gemella_colture.append(np.random.choice(colture))
    return scheda_gemella_colture
        
def crea_base_produzione_campi(campi_vuoti,campi_popolazione):
    #questa funziona calcola la produzione dei campi simulati
    lista_produzione=[]
    numero_campi=len(campi_vuoti)
    
    for n in range(numero_campi):
        produzione_campo=(campi_vuoti[n])*dati_asset("base_produzione_per_ettaro", (campi_popolazione[n]))
        
        lista_produzione.append(produzione_campo)
    return lista_produzione
    

def simula_semina_raccolta_vendita_data(popolazione_campi):
    #questa funziona simula le date in cui i prodotti agricoli vengono simulati e raccolti
    #questo avviene utitlizzando delle aspettative riguardo ai giorni di semina e raaaccolta e applicando un ritardo/anticipo casuale per rendere il tutto più credibile
    
    #successivamentela funzione simula il giorno in cui i prodotti vari prodotti agricoli vengono venduti
    #vengono utilizzate per la simulazione la data di raccolta simulata e un "delay" casuale che rappresenta il tempo che l'agricoltore utilizza per conservare e vendere la merce
    lista_asset=dati_asset("lista_asset",None)
    semina_provvisoria=[]
    raccolta_provvisoria=[]
    vendita_provvisoria=[]
    
    for pianta in lista_asset:
        data_semina_simulata=(dati_asset("data_semina",pianta))-7+(np.random.randint(14))
        data_raccolta_simulata=(dati_asset("data_raccolta",pianta))-7+(np.random.randint(14))
        semina_provvisoria.append(data_semina_simulata)
        raccolta_provvisoria.append(data_raccolta_simulata)
        #qui inizia la parte del ciclo volta a determinare la data di vendita
        data_vendita_provvisoria=data_raccolta_simulata+(np.random.randint(2,30))
        vendita_provvisoria.append(data_vendita_provvisoria)
        
    date_semina=[]
    date_raccolta=[]
    date_vendita=[]
    for tipo_pianta in popolazione_campi:
        indice_di_riferimento=lista_asset.index(tipo_pianta)
        date_semina.append(semina_provvisoria[indice_di_riferimento])
        date_raccolta.append(raccolta_provvisoria[indice_di_riferimento])
        date_vendita.append(vendita_provvisoria[indice_di_riferimento])
    

    return date_semina,date_raccolta,date_vendita

def simulazione_vendita(serie_vendita,campi_popolazione,base_produzione,asset_simulati,anno_considerato):
    #questa funzione serve a ottenere i dati riguardanti i profitti ottenuti dalle varie merci
    
    #si parte importando la lista degli asset e creando una lista di valori numerici
    #questa lista una volta aggiornata rappresentera i profitti annuali per coltura
    lista_asset=dati_asset("lista_asset",None)
    
    profitti_annuali_per_coltura=[]
    for asset in lista_asset:
        profitti_annuali_per_coltura.append(0)
        
    #procediamo creando un contatore e utilizzando il seguente ciclo per ottenere i valori numerici di profitto richiesti
    #il contatore aumenterà di 1 ogni qualvolta si considerera un nuovo campo tra quelli generati
    
    contatore=0
    profitti_annuali_per_campo=[]
    profitti_annuali_totali=0
    profitti_annuali_per_coltura=profitti_annuali_per_coltura
    for campo in campi_popolazione:
        giorno_vendita=serie_vendita[contatore]
        #il prossimo parametro rappresenta l'indice della coltura analizzata nella lista degli asset
        #è utile perchè nel passaggio successivo si può isolare la serie storica del prezzo dell'asset considerato dagli altri asset
        indice_coltura_analizzato=lista_asset.index(campo)
        lista_asset_analizzata=asset_simulati[indice_coltura_analizzato]
        #nel prossimo passaggio risolviamo il problema di quale anno stiamo analizzando
        giorno_vendita_effettivo=giorno_vendita+(anno_considerato*365)
        
        #ora si può selezionare il prezzo di vendita nel giorno di vendita
        prezzo_di_vendita_effettivo=lista_asset_analizzata[giorno_vendita_effettivo]
        
        #dopo aver calcolato il prezzo di vendita possiamo moltiplicarlo per la quantità prodotta e ottenere cosi il profitto per il campo preso in considerazione
        profitto_campo_considerato=prezzo_di_vendita_effettivo*(base_produzione[contatore])
        profitto_campo_considerato=round(profitto_campo_considerato,2)
        #ora per ottenere un output coerente modifichiamo le variabile create subito prima del ciclo
        #per prima il profitto annuale per campo
        profitti_annuali_per_campo.append(profitto_campo_considerato)
        #per seconda tramite una semplice addizione aumentiamo i profitti totali
        profitti_annuali_totali+=profitto_campo_considerato
        #poi andiamo ad ottenere il profitto per coltura annuale
        #per farlo utilizziamo "indice_coltura_analizzato"(creato in precedenza) per capire quale elemento aumentare all'interno della lista in output
        profitti_annuali_per_coltura[indice_coltura_analizzato]+=profitto_campo_considerato
        #terminiamo il ciclo aumentando il contatore di uno nel caso in cui quello preso in considerazione non sia l'ultimo campo analizzato
        contatore+=1
        
    #prima di terminare la funziona si può fare in modo che i dati in uscita abbiano lo stesso numero di cifre con la virgola
    for i in range(len(profitti_annuali_per_coltura)):
        profitti_annuali_per_coltura[i]=round(profitti_annuali_per_coltura[i],2)
    
    profitti_annuali_totali=round(profitti_annuali_totali,2)
    
    return profitti_annuali_per_campo,profitti_annuali_per_coltura,profitti_annuali_totali
    #RICOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOORDATI
    #DI FARE IN MODO DI RENDERE COMPATIBILI LE FUNZIONI
    #ATTUALMENTE QUELLE DI SOTTO NON FUNZIONANO SE VENGONO CONSIDERATI PIU DI UN ANNO


#il simulatore ha il compito di definire i dati contenuti nel csv
#ha anche il compito di variarli ogni qualvolta l'utente lo desidera
def simula_dati(anni):
    
    #il simulatore ha il compito di creare un set di dati credibile e coerente
    
    #il primo passo è simulare i dati che riguardano i fattori provenienti dal tempo
    #atmosferico in una zona temperata
    serie_temperatura=crea_base_temperatura(anni)
    serie_umidità=crea_base_umidita(anni)
    serie_pioggia=crea_base_pioggia(anni)
    #il secondo è simulare i valori azionari dei prodotti agricoli che desideriamo inserire nella simulazione
    
    lista_asset=dati_asset("lista_asset",None)
    asset_simulati=[]
    for asset in lista_asset:
        asset_simulati.append((simula_prezzo_asset(asset,anni))[0])
        
    #per ottenere un riferimento cronologico coerente andiamo a creare una base temporale di riferimento per le serie storiche
    serie_giorni_anni_simulati=crea_base_temporale(anni)
    #il prossimo passo è simulare la creazione di campi, iniziando la creazione di quest'ultimi
    campi_vuoti=simula_creazione_campi()
    #a questo punto bisogna popolare i campi con le diverse colture
    campi_popolazione=popola_campi(campi_vuoti,lista_asset)
    #le due liste ottenute con questo metodo saranno rispettivamente i campi vuoti con la loro dimensione e le colture con cui questi campi vengono seminati
    
    #a questo punto si può procedere simulando la produzione di prodotti agricoli
    #questa prima funzione crea una base per la produzione dei campi simulati precedentemente
    base_produzione=crea_base_produzione_campi(campi_vuoti,campi_popolazione)
    
    #il prossimo passaggio è simulare quando le colture vengono seminate e raccolte
    #viene simulato anche il giorno in cui le varie colture vengono vendute
    #queste date sono diverse per ogni anno 
    serie_semina=[]
    serie_raccolta=[]
    serie_vendita=[]
    
    serie_profitti_per_campo=[]
    serie_profitti_per_tipo_di_coltura=[]
    serie_profitti_totale=[]
    
    anno_considerato=0
    for x in range(anni):
        data_semina_raccolta_e_vendita=simula_semina_raccolta_vendita_data(campi_popolazione)
        data_semina=data_semina_raccolta_e_vendita[0]
        data_raccolta=data_semina_raccolta_e_vendita[1]
        data_vendita=data_semina_raccolta_e_vendita[2]
        serie_semina.append(data_semina)
        serie_raccolta.append(data_raccolta)
        serie_vendita.append(data_vendita)
    #succesivamente si possono determinare i guadagni per campo,per tipo di coltura,e totali
    #queste viene fatto utilizzando le serie storiche contenenti i prezzi degli asset generati in precedenza
    #viene utilizzato il prezzo di vendità del giorno in cui le merci vengono vendute(questo giorno è stato simulato nel passaggio precedente)
        dati_entrate=simulazione_vendita(data_vendita,campi_popolazione,base_produzione,asset_simulati,anno_considerato)
        profitti_per_campo=dati_entrate[0]
        profitti_per_tipo_di_coltura=dati_entrate[1]
        profitti_totale=dati_entrate[2]
        serie_profitti_per_campo.append(profitti_per_campo)
        serie_profitti_per_tipo_di_coltura.append(profitti_per_tipo_di_coltura)
        serie_profitti_totale.append(profitti_totale)
        
        anno_considerato+=1
        
    #print(serie_giorni_anni_simulati,serie_temperatura,serie_umidità,serie_pioggia,asset_simulati)
    #print(campi_vuoti,campi_popolazione,base_produzione)
    #print(serie_semina,serie_raccolta,serie_vendita)
    #print(serie_profitti_per_tipo_di_coltura,serie_profitti_totale)
    #print(serie_profitti_totale)
    #print(asset_simulati[0])
    return ([serie_giorni_anni_simulati,serie_temperatura,serie_umidità,serie_pioggia],[serie_giorni_anni_simulati,asset_simulati],[serie_semina,serie_raccolta,serie_vendita,serie_profitti_per_campo],[campi_vuoti,campi_popolazione,base_produzione],[serie_profitti_totale,serie_profitti_per_tipo_di_coltura])    
#il successivo è un test per la funzione simula dati,per effetuarlo è sufficente eliminare il successivo "#"
simula_dati(3)
#print(simula_dati(3)[4])


def crea_dataset(anni,richiesta_opzionale):
    #questa parte del programma crea un dataset di pandas dai dati che sono stati simulati in forma di liste(o array)
    
    dati_input_completi=simula_dati(anni)
    
    #il primo dataset comprende delle serie storiche che comprendono tutti gli anni simulati dalle funzioni precedenti
    
    dati_atmosferici=dati_input_completi[0]
    #dati_atmosferici={
    #    "data":dati_atmosferici[0],
    #    "temperatura":dati_atmosferici[1],
    #    "umidità":dati_atmosferici[2],
    #    "precipitazione":dati_atmosferici[3],
        
    #   }
    #print(dati_atmosferici)
    #il primo dataset comprende delle serie storiche che comprendono tutti gli anni simulati dalle funzioni precedenti
    base_serie_storiche=dati_atmosferici
    
    data_frame_atmosferico = pd.DataFrame(base_serie_storiche)
    data_frame_atmosferico = data_frame_atmosferico.transpose()
    
    #nel secondo dataset vengono inseriti le serie storiche dei prezzi degli asset simulati
    dati_asset_misti=dati_input_completi[1]
    
    prezzi_beni=dati_asset_misti[1]
    dati_asset_finali=[]
    dati_asset_finali.append(dati_asset_misti[0])
    for x in prezzi_beni:
        dati_asset_finali.append(x)
    
    data_frame_asset=pd.DataFrame(dati_asset_finali)
    data_frame_asset=data_frame_asset.transpose()
    
    #nel terzo dataset inseriamo i giorni in cui sono avvenuti per ogni asset la semina,la raccolta e la vendita, e quanto hanno fruttato le colture in ogni anno
    serie_per_coltura=dati_input_completi[2]

    dataframe_per_coltura=pd.DataFrame(serie_per_coltura)
    
    #nel quarto dataset sono presenti delle descrizioni riguardante i vari campi
    #ci sono informazioni riguardanti la dimensione,il tipo di coltura e la quantita prodotta per ogni campo generato
    serie_per_campo=dati_input_completi[3]
    
    dataframe_per_campo=pd.DataFrame(serie_per_campo)
    
    #nel quinto dataset sono presenti le informazioni sui profitti totali e quelli per tipo di coltivazione
    serie_per_profitti_finali=dati_input_completi[4]
    dataframe_per_profitti_finali=pd.DataFrame(serie_per_profitti_finali)
    #print(data_frame_atmosferico)
    return data_frame_atmosferico,data_frame_asset,dataframe_per_coltura,dataframe_per_campo,anni,dataframe_per_profitti_finali

#print(crea_dataset(3))
def modifica_csv(anni):
    #questa parte del programma ridefinisce il file csv con i nuovi dati simulati
    input_dataframes=crea_dataset(anni,None)
    #questo è il primo csv con le serie storiche degli anni simulati
    primo_csv=input_dataframes[0]
    primo_csv.to_csv('primo_csv.csv', index=False)
    #questo è il secondo csv con i valori che gli asset assumono durante l'anno
    secondo_csv=input_dataframes[1]
    secondo_csv.to_csv('secondo_csv.csv', index=False)
    #questo è il terzo csv per indicare i giorni di vendita,semina e raccolta 
    
    terzo_csv=input_dataframes[2]
    terzo_csv.to_csv('terzo_csv.csv', index=False)
    
    #questo è il csv contenente informazioni riguardo i campi generati 
    #in ordine sono inseriti :la dimensione,il tipo di coltura,la quantita prodotta, la lista dei profitti per anno
    campi_csv=input_dataframes[3]
    campi_csv.to_csv('campi_csv.csv', index=False)
    
    print("il simulatore ha generato i valori richiesti dall'app e ha modificato i rilevanti file csv")
    
    
    
modifica_csv(3)