# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 19:57:35 2025

@author: Ciccolella Giovanni
"""

import dash_mantine_components as dmc
from dash import Dash, _dash_renderer, html, callback, Output, Input
import pandas as pd
#a questo punto del programma si importano due moduli che contengono funzioni e sottoprogrammi
#questi moduli servono per simulare i dati ed elaborarli
#essi sono inseriti come moduli per rendere la lettura di questo programma più comoda e semplice

import modulo_elaborazione_dati as dem
import simulatore_tesi as sim

_dash_renderer._set_react_version("18.2.0")


dataset_iniziale=sim.crea_dataset(3,None)

numero_anni=dataset_iniziale[4]
lista_anni_presi_in_considerazione=[str((2025-numero_anni)+i) for i in range(numero_anni)]

#questa parte del programma definisce la pagina che indica il tempo meteorolgico

#i primi dati da "imporatre" nel programma sono quelli riguardanti la temperatura,
#ciò avviene con la funzione"dem.seleziona_converti_serie" contenuta nel modulo "modulo_elaborazione_dati"

dati_temperatura= dem.seleziona_converti_serie(dataset_iniziale,"temperatura")
#print(dati_temperatura)

#subito dopo i dati da "imporatre" nel programma sono quelli riguardanti l'umidità',
#ciò avviene con la funzione"dem.seleziona_converti_serie" contenuta nel modulo "modulo_elaborazione_dati"

dati_umidità= dem.seleziona_converti_serie(dataset_iniziale,"umidità")
#print(dati_umidità)

#a questo punto occore importare i dati riguardanti le precipitazioni
#ciò avviene con la funzione"dem.seleziona_converti_serie" contenuta nel modulo "modulo_elaborazione_dati"

dati_precipitazioni= dem.seleziona_converti_serie(dataset_iniziale,"precipitazioni")
#print(dati_precipitazioni)

#il prossimo passaggio contiene le opzioni di scelta del grafico della temperatura

opzioni_temperatura_umidità_precipitazioni={"mese":["01","02","03","04","05","06","07","08","09","10","11","12"],"anno":lista_anni_presi_in_considerazione,"totale":["totale"],"medie mese per anno":lista_anni_presi_in_considerazione}
lista_numero_giorni_al_mese=[31,28,31,30,31,30,31,31,30,31,30,31]


# occore importare i dati riguardanti le serie storiche dei prezzi degli asset
dati_azionari= dem.seleziona_converti_serie(dataset_iniziale,"azionari")
#print(dati_azionari)

# è necessario importare i dati riguardanti i giorni di semina,raccolta e vendita delle colture, e altri dati riguardanti i campi agricoli e i profitti derivanti da questi ultimi
dati_giorni_vari_colture=dem.seleziona_converti_serie(dataset_iniziale,"colture")
#print(dati_giorni_vari_colture)

#"selezionatore_anni_campi" serve a selezionare quale anno si sta visualizzando nella tabella dei campi
#"opzioni_anni_campi" sono gli anni disponibile nella selezione
opzioni_anni_campi=lista_anni_presi_in_considerazione
#print(opzioni_anni_campi)

#"dati_profitti_finali" contiene i dati divisi per anno dei profitti derivanti dalle coltivazioni divisi per tipo di coltivazione e il totale
dati_profitti_finali=dem.seleziona_converti_serie(dataset_iniziale,"profitti_finali")
#print(dati_profitti_finali)

selezionatore_anni_campi=dmc.Select(
            label="tipo di visualizzazione",
            allowDeselect="False",
            placeholder="Select one",
            id="selettore_anno_visualizzato_tabella_campi",
            value="2024",

            data=[{"value":str(opzioni),"label":("visualizza "+str(opzioni))} for opzioni in opzioni_anni_campi],
            w=200,
            mb=10,
        )

#"grafico_campi_home" contiene il grafico che introduce varie informazioni riguardo i campi agricoli
#le variabili head, body e caption servono a determinare il contenuto della tabella e verranno introdotte dinamicamente
#questa variabie contiene solo un ID in quanto funzionano in base a un dash callback che le modifica in maniera interattiva
grafico_campi_home=dmc.Table(id="righe_tabella_campi")

#"tabella_profitti_home" contiene le informazioni riguardo i profitti per ogni anno esponendoli anche considerando le diverse colture che li generano
tabella_profitti_home=dmc.Table(id="tabella_profitti_finali")

#la prossima parte di codice contiene stringhe di testo che vengono visualizzate nella pagina home

contenuto_testuale_inzio_home_pt1="App Impresa Agricola è un programma che simula e analizza dati riguardanti un'azienda nel settore primario e nello specifico un'azienda agricola.\n"
contenuto_testuale_inzio_home_pt2="Il programma contiene tre diverse sezioni organizzate attraverso delle tabs presnti subito al di sopra di questa descrizione;le sezioni sono: home,weather,simulazione mercato azionario.\n"
contenuto_testuale_inzio_home_pt3="In questa schermata sono presenti due tabelle interattive i cui dati variano a seconda dell'anno selezionato.\n"
contenuto_testuale_inzio_home_pt4="l'interezza dei dati presenti nelle tabelle e nei grafici del programma viene generata utilizzando distribuzioni statische; a ogni lancio del programma viene utilizzato un nuovo set di dati simulati"



contenuto_testuale_tabella1_home_pt1="In questa prima tabella vengono visualizzati dati inerenti all'azienda agricola,le righe rappresantano i diversi campi agricoli dell'azienda analizzata mentre le colonne i diversi tipi di dato."
contenuto_testuale_tabella1_home_pt2="I dati sono in ordine,partendo da sinistra verso destra: il nome del_campo, la sua dimensione, che tipo di coltura vi è coltivata, la produzione espressa in quintali,\nil giorno di semina, quello di raccolta, quello di vendita e i profitti relativi al campo."
contenuto_testuale_tabella1_home_pt3="I giorni di semina,raccolta e vendita , insieme ai profitti per campo, cambiano in base all'anno selezionato, mentre gli altri dati rimangono gli stessi indipendentemente da quest'ultimo"

contenuto_testuale_tabella2_home_pt1="Nella seconda tabella venogno visualizzati i profitti dell'intera azienda agricola nell'anno selezionato."
contenuto_testuale_tabella2_home_pt2="Oltre ai profitti totali viene visualizzato quanto ha prodotto ogni tipo di coltura."
contenuto_testuale_tabella2_home_pt3=""
#la variabile "contenuto_home" contiene l'intera tab responsabile di mostrare e organizzare la schermata introduttiva del programma
contenuto_home=dmc.Box([
    dmc.Flex(gap="xl",direction="column",children=[
        html.Div(children=(
        html.Div(contenuto_testuale_inzio_home_pt1,style={ "margin": 0,"padding": 0}),
        html.Div(contenuto_testuale_inzio_home_pt2,style={ "margin": 0,"padding": 0}),
        html.Div(contenuto_testuale_inzio_home_pt3,style={ "margin": 0,"padding": 0}),
        html.Div(contenuto_testuale_inzio_home_pt4,style={ "margin": 0,"padding": 0}))
        ),
        selezionatore_anni_campi,
        grafico_campi_home,
        html.Div(children=(
        html.Div(contenuto_testuale_tabella1_home_pt1,style={ "margin": 0,"padding": 0}),
        html.Div(contenuto_testuale_tabella1_home_pt2,style={ "margin": 0,"padding": 0}),
        html.Div(contenuto_testuale_tabella1_home_pt3,style={ "margin": 0,"padding": 0}))
        ),
        tabella_profitti_home,
        
        html.Div(children=(
        html.Div(contenuto_testuale_tabella2_home_pt1,style={ "margin": 0,"padding": 0}),
        html.Div(contenuto_testuale_tabella2_home_pt2,style={ "margin": 0,"padding": 0}),
        html.Div(contenuto_testuale_tabella2_home_pt3,style={ "margin": 0,"padding": 0}))
        ),
        ])
    
    ],style={"marginTop": 8, "padding": 24})




#"grafico_mercato_azionario" contiene il grafico che confronta i prezzi del mercato azionario nel tempo
#"dominio_valori_azionario" delinea il range entro cui viene mostrato il grafico
dominio_valori_azionario=[150,900]

grafico_mercato_azionario=dmc.AreaChart(
    h=720,
    dataKey="giorno",
    data=dati_azionari,
    series = [
        {"name": "grano_primaverile", "color": "indigo.6"},
        {"name": "carote", "color": "orange.6"},
        {"name": "patate", "color": "teal.6"}
    ],
    curveType="linear",
    tickLine="xy",
    withXAxis=False,
    withDots=False,
    yAxisProps={"domain": dominio_valori_azionario}
)

#la variabile "tab_mercato_azionario" contiene l'intera tab responsabile di mostrare e organizzare i dati riguardanti le variazioni dei prezzi del mercato azionario

#le variabili "testo_mercato_azionario" sono stringhe che spiegano all'utente il funzionamento della pagina riguardo il mercato azionario

testo_mercato_azionariopt1="Questa pagina mostra la simulazione del prezzo di tre prodotti agricoli. "
testo_mercato_azionariopt2="I prezzi di questi prodotti vengono mostrati durante l'intero periodo analizzato dal programma nelle pagine precedenti. "
testo_mercato_azionariopt3="quando nel simulatore vengono vendute le merci agricole viene utilizzato il prezzo espresso da questo grafico nel giorno di vendita per ottenere i profitti."
testo_mercato_azionario=testo_mercato_azionariopt1+testo_mercato_azionariopt2+testo_mercato_azionariopt3

tab_mercato_azionario=dmc.Box([
    dmc.Flex(gap="xl",direction="column",children=[
        
        dmc.Text(testo_mercato_azionario),
        
        grafico_mercato_azionario,
        dmc.Text(""),
        ])
    
    ],style={"marginTop": -25, "padding":75 })




#la variabile "weather_macro_tab" contiene l'intera tab responsabile di mostrare e organizzare i dati riguardanti la temperatura,umidità e precipitazioni
#la variabile "descrizione_weather_tab" dascrive il contenuto della pagina che mostra i dati meteorologici simulati.

descrizione_weather_tabpt1="Questa pagina contiene tre grafici diversi contenenti i dati metereologici che forniscono in maniera interattiva il contesto ambientale dell'azienda. "
descrizione_weather_tabpt2="vengono mostrati i dati riguardo la temperatura, l'umidità e le precipitazioni; ciò avviene tramite un grafico lineare. "
descrizione_weather_tabpt3="Il tipo di visualizzazione e l'arco temporale dei dati può essere cambiato dinamicamente tramite i menù a tendina."

descrizione_weather_tab=descrizione_weather_tabpt1+descrizione_weather_tabpt2+descrizione_weather_tabpt3


weather_macro_tab=dmc.Box([
    html.Div([
        html.P(children=[descrizione_weather_tab],style={"marginTop": 8, "padding": 24})
        ]),
    dmc.Group(preventGrowOverflow=False,grow=True,children=[
    #dmc.Flex(gap="xl",direction="row",align="center",children=[
    
    html.Div(children=[
    dmc.Flex(gap="xl",direction="column",children=[
        # la box successiva è destinata a contenere i dati inerenti alla temperatura
        html.Div([
            #dmc.Text("temperatura"),
            #dmc.Text("temperatura"),
            
            
            dmc.Text("1 Temperatura"),
            html.Div(
    [
         
     
         #creiamo i selettori che permettono la visualizzazione di diverse sezioni del grafico
         #il primo selettore selezione il tipo di visualizzazione
         dmc.Flex(gap="l",direction="rows",children=[
             
         dmc.Select(
            label="tipo di visualizzazione",
            allowDeselect="False",
            placeholder="Select one",
            id="tipo-di-grafico-temperatura",
            value="mese",
#            data=[
#                {"value": "mese", "label": "visualizza un mese"},
#                {"value": "anno", "label": "visualizza un anno"},
#                {"value": "totale", "label": "visualizza il totale"},
#                
#            ],
            data=[{"value":str(opzioni),"label":("visualizza "+str(opzioni))} for opzioni in opzioni_temperatura_umidità_precipitazioni.keys()],
            w=200,
            mb=10,
        ),
         dmc.Select(
            label="specifica l'anno                   ",
            allowDeselect="False",
            placeholder="seleziona anno",
            id="mese-appare-scompare-temperatura",
            
            value="2024",
            display=False,
            
            data=[{"value":str(opzioni),"label":("l'anno scelto è "+str(opzioni))} for opzioni in lista_anni_presi_in_considerazione],
            w=200,
            mb=10,
        ),
         
         
        #il terza selettore seleziona la specifica vista selezionata
        dmc.Select(
            label="seleziona cosa visualizzare",
            allowDeselect="False",
            placeholder="2024",
            id="sottotipo-di-grafico-temperatura",
            value="2024",
#            data=[
#                {"value": "mese", "label": "visualizza un mese"},
#                {"value": "anno", "label": "visualizza un anno"},
#                {"value": "totale", "label": "visualizza il totale"},
#                
#            ],
            
            #data=[{"value":str(opzioni),"label":("visualizza "+str(opzioni))} for opzioni in opzioni_temperatura.keys()],
            w=200,
            mb=10,
        )
        
        ]),
        dmc.Text(id="selected-value-temperatura"),
         
         
         
         
         
         
         
         
         
         
         
         
         
         
   
         
         
         
        # selettore_temperatura,
         #qui inizia la funzione che crea il grafico della serie storica delle temperatura
         dmc.LineChart(
         h=300,
         dataKey="giorno",
         id="grafico_temperatura",
         data=dati_temperatura,
         series = [
        {"name": "valore", "color": "indigo.6"},
        
        ],
    curveType="Monotone",
    tickLine="xy",
    withXAxis=False,
    withDots=False,
                    )
        
     
        
     

    ],
    style={"marginTop": 8, "padding": 24})
            ]),
        
        
        
        # la box successiva è destinata a contenere i dati inerenti all'umidità
        dmc.Box([
            dmc.Text("2 Umidità"),
            html.Div(
    
    [
         
     
         #creiamo i selettori che permettono la visualizzazione di diverse sezioni del grafico
         #il primo selettore selezione il tipo di visualizzazione
         dmc.Flex(gap="l",direction="rows",children=[
             
         dmc.Select(
            label="tipo di visualizzazione",
            allowDeselect="False",
            placeholder="Select one",
            id="tipo-di-grafico-umidità",
            value="mese",
#            data=[
#                {"value": "mese", "label": "visualizza un mese"},
#                {"value": "anno", "label": "visualizza un anno"},
#                {"value": "totale", "label": "visualizza il totale"},
#                
#            ],
            data=[{"value":str(opzioni),"label":("visualizza "+str(opzioni))} for opzioni in opzioni_temperatura_umidità_precipitazioni.keys()],
            w=200,
            mb=10,
        ),
         dmc.Select(
            label="specifica l'anno                   ",
            allowDeselect="False",
            placeholder="seleziona anno",
            id="mese-appare-scompare-umidità",
            
            value="2024",
            display=False,
            
            data=[{"value":str(opzioni),"label":("l'anno scelto è "+str(opzioni))} for opzioni in lista_anni_presi_in_considerazione],
            w=200,
            mb=10,
        ),
         
         
        #il terza selettore seleziona la specifica vista selezionata
        dmc.Select(
            label="seleziona cosa visualizzare",
            allowDeselect="False",
            placeholder="2024",
            id="sottotipo-di-grafico-umidità",
            value="2024",
#            data=[
#                {"value": "mese", "label": "visualizza un mese"},
#                {"value": "anno", "label": "visualizza un anno"},
#                {"value": "totale", "label": "visualizza il totale"},
#                
#            ],
            
            #data=[{"value":str(opzioni),"label":("visualizza "+str(opzioni))} for opzioni in opzioni_temperatura.keys()],
            w=200,
            mb=10,
        )
        
        ]),
        dmc.Text(id="selected-value-umidità"),
         
         # selettore_umidità,
         #qui inizia la funzione che crea il grafico della serie storica dell'umidità'
         dmc.LineChart(
         h=300,
         dataKey="giorno",
         id="grafico_umidità",
         data=dati_umidità,
         series = [
        {"name": "valore", "color": "indigo.6"},
        
        ],
    curveType="Monotone",
    tickLine="xy",
    withXAxis=False,
    withDots=False,
                    )
        
     
        
     

    ]            
    ,style={"marginTop": 8, "padding": 24})
            ]),
        # la box successiva è destinata a contenere i dati inerenti alle precipitazioni
        dmc.Box([
            dmc.Text("3 Precipitazioni"),
            html.Div(
    [
     
         
         #creiamo i selettori che permettono la visualizzazione di diverse sezioni del grafico
         #il primo selettore selezione il tipo di visualizzazione
         dmc.Flex(gap="l",direction="rows",children=[
             
         dmc.Select(
            label="tipo di visualizzazione",
            allowDeselect="False",
            placeholder="Select one",
            id="tipo-di-grafico-precipitazioni",
            value="mese",
#            data=[
#                {"value": "mese", "label": "visualizza un mese"},
#                {"value": "anno", "label": "visualizza un anno"},
#                {"value": "totale", "label": "visualizza il totale"},
#                
#            ],
            data=[{"value":str(opzioni),"label":("visualizza "+str(opzioni))} for opzioni in opzioni_temperatura_umidità_precipitazioni.keys()],
            w=200,
            mb=10,
        ),
         dmc.Select(
            label="specifica l'anno                   ",
            allowDeselect="False",
            placeholder="seleziona anno",
            id="mese-appare-scompare-precipitazioni",
            
            value="2024",
            display=False,
            
            data=[{"value":str(opzioni),"label":("l'anno scelto è "+str(opzioni))} for opzioni in lista_anni_presi_in_considerazione],
            w=200,
            mb=10,
        ),
         
         
        #il terza selettore seleziona la specifica vista selezionata
        dmc.Select(
            label="seleziona cosa visualizzare",
            allowDeselect="False",
            placeholder="2024",
            id="sottotipo-di-grafico-precipitazioni",
            value="2024",
#            data=[
#                {"value": "mese", "label": "visualizza un mese"},
#                {"value": "anno", "label": "visualizza un anno"},
#                {"value": "totale", "label": "visualizza il totale"},
#                
#            ],
            
            #data=[{"value":str(opzioni),"label":("visualizza "+str(opzioni))} for opzioni in opzioni_temperatura.keys()],
            w=200,
            mb=10,
        )
        
        ]),
         #qui inizia la funzione che crea il grafico della serie storica delle precipitazioni
         dmc.AreaChart(
         h=300,
         dataKey="giorno",
         id="grafico_precipitazioni",
         data=dati_precipitazioni,
         series = [
        {"name": "valore", "color": "indigo.6"},
        
        ],
    curveType="Monotone",
    tickLine="xy",
    withXAxis=False,
    withDots=False,
                    ),
    dmc.Text(id="selected-value-precipitazioni"),
        
    ],style={"marginTop": 8, "padding": 24})
            ]),
        ],
        )],style={"marginTop": 8, "padding": 24,"max-height":"50%","min-height":"50%","background":"white"}),
    
        ]),
    ])
#style={"marginTop": 8, "padding": 24,"height":"50%"}

app = Dash(external_stylesheets=dmc.styles.ALL)


app.layout = dmc.MantineProvider([
    dmc.Alert(
       "Sviluppo di una dashboard in Python per l'analisi delle prestazioni aziendali nel settore primario",
       title="Tesi di informatica di Giovanni Ciccolella",
       color="violet",
    ),
    
    html.H1("App Azienda Agricola"),
    
    
    dmc.Tabs(
    [
        dmc.TabsList(
            [
                dmc.TabsTab("Home", value="home"),
                dmc.TabsTab("Weather", value="weather"),
                dmc.TabsTab("Simulazione mercato azionario", value="azioni"),
                
            ]
        ),
        dmc.TabsPanel(contenuto_home, value="home"),
        dmc.TabsPanel(tab_mercato_azionario, value="azioni"),
        dmc.TabsPanel(weather_macro_tab, value="weather"),
        
    ],
    value="home",
    color="red",
    orientation="horizontal",
    variant="default",
    
)
    
])

#a questo punto del codice ci sono tutti i callback dell'app

#questo callback si occupa di influenzare l'output visivo della tabella dei campi agricoli
@callback(
    Output("righe_tabella_campi", "children"),
    Output("tabella_profitti_finali", "children"),      
    
    Input("selettore_anno_visualizzato_tabella_campi", "value")
          )
def selettore_anno_campi_agricoli(valore_primo_selettore):
    #all'interno di questa funzione del callback come prima cosa otteniamo un indice utilizzabile nelle liste di python dall'input 
    indice_anno=opzioni_anni_campi.index(valore_primo_selettore)
    #riportiamo in questo callback i dati  statici sui campi
    dati_statici_sui_campi=dati_giorni_vari_colture[1]
    #dati_statici_sui_campi=[0,1,2,3,4]
    #creiamo dinamicamente i dati dinamici sui campi
    dati_dinamici_sui_campi=(dati_giorni_vari_colture[0])[indice_anno]
    #ricreiamo una tabella unica con tutti le informazioni ottenute
    #print(dati_dinamici_sui_campi)
    #x=dati_dinamici_sui_campi[0]
    #print(x[0])
    
    #i prossimi dati sono le colonne i cui dati rimangono invariati negli anni
    dati_ettari=dati_statici_sui_campi.take([0])
    #print(dati_ettari)
    dati_popolazione=dati_statici_sui_campi.take([1])
    dati_base_produzione=dati_statici_sui_campi.take([2])
    
    #i prossimi dati sono le colonne i cui dati cambiano a seconda degli anni
    dati_giorno_semina=dati_dinamici_sui_campi[0]
    dati_giorno_raccolta=dati_dinamici_sui_campi[1]
    dati_giorno_vendita=dati_dinamici_sui_campi[2]
    dati_profitti=dati_dinamici_sui_campi[3]
    

    dati_sui_campi_unici={
        "ettari":dati_ettari,
        "popolazione":dati_popolazione,
        "base produzione":dati_base_produzione,
        "giorno semina":dati_giorno_semina,
        "giorno raccolta":dati_giorno_raccolta,
        "giorno vendita":dati_giorno_vendita,
        "profitti":dati_profitti,
        
        }
    
    #print(dati_sui_campi_unici)
    
    #creiamo quindi una tabella
    elementi_tabella=[{"nome":(("campo ")+str(x)),
                        "ettari":(dati_sui_campi_unici["ettari"])[x],
                       "popolazione":(dati_sui_campi_unici["popolazione"])[x],
                       "base produzione":(dati_sui_campi_unici["base produzione"])[x],
                       "giorno semina":(dati_sui_campi_unici["giorno semina"])[x],
                       "giorno raccolta":(dati_sui_campi_unici["giorno raccolta"])[x],
                       "giorno vendita":(dati_sui_campi_unici["giorno vendita"])[x],
                       "profitti":(dati_sui_campi_unici["profitti"])[x],}for x in range(len(list(dati_ettari)))]
    #elementi_tabella=""
    #print()
    #print(len(dati_ettari))
    #print(elementi_tabella)
    

    
    
    
    
    
    
    
    #righe=dmc.TableTr(children=elements)
    
    righe = [
    dmc.TableTr(
        [
            dmc.TableTd(element["nome"]),
            dmc.TableTd(element["ettari"]),
            dmc.TableTd(element["popolazione"]),
            dmc.TableTd(element["base produzione"]),
            dmc.TableTd(element["giorno semina"]),
            dmc.TableTd(element["giorno raccolta"]),
            dmc.TableTd(element["giorno vendita"]),
            dmc.TableTd(element["profitti"]),
            
            
        ]
    )
    for element in elementi_tabella
]

    corpo_tabella_campi = dmc.TableTbody(righe)
    
    voci_per_campo = dmc.TableThead(
        dmc.TableTr(
            [
                dmc.TableTh("Nome campo"),
                dmc.TableTh("ettari"),
                dmc.TableTh("popolazione"),
                dmc.TableTh("base produzione"),
                dmc.TableTh("giorno semina"),
                dmc.TableTh("giorno raccolta"),
                dmc.TableTh("giorno vendita"),
                dmc.TableTh("profitti"),
            ]
        )
    )
    

    descrizione_tabella_campi = dmc.TableCaption("Descrizione dei campi")
    
    #si procede creando dinamicamente la seconda tabella
    dati_generali_profitti_finali=dati_profitti_finali
    dati_dinamici_profitti_finali=dati_generali_profitti_finali[indice_anno]
    dati_divisi_per_coltura_profitti=dati_dinamici_profitti_finali[1]
    
    dati_profitti_grano_primaverile_finali=dati_divisi_per_coltura_profitti[0]
    dati_profitti_carote_finali=dati_divisi_per_coltura_profitti[1]
    dati_profitti_patate_finali=dati_divisi_per_coltura_profitti[2]
    dati_profitti_totali_finali=dati_dinamici_profitti_finali[0]
    
    
    
    profitti_tabella=[{"grano primaverile":dati_profitti_grano_primaverile_finali,"carote":dati_profitti_carote_finali,"patate":dati_profitti_patate_finali,"totale":dati_profitti_totali_finali,
        
        }]
    
    righe_profitti= [
    dmc.TableTr(
        [
            dmc.TableTd(profitto["grano primaverile"]),
            dmc.TableTd(profitto["carote"]),
            dmc.TableTd(profitto["patate"]),
            dmc.TableTd(profitto["totale"]),
            
            
            
        ]
    )
    for profitto in profitti_tabella
]
    
    corpo_profitti = dmc.TableTbody(righe_profitti)
    
    voci_profitti = dmc.TableThead(
        dmc.TableTr(
            [
                
                dmc.TableTh("grano primaverile"),
                dmc.TableTh("carote"),
                dmc.TableTh("patate"),
                dmc.TableTh("totale"),
                
            ]
        )
    )
    descrizione_profitti = dmc.TableCaption("Descrizione dei profitti")
    
    
    
    #print("")
    
    
    
    #questo è il risultato del callback:il contenuto di due tabelle
    tabella_intera_7_voci=[voci_per_campo,corpo_tabella_campi,descrizione_tabella_campi]
    
    #tabella_mini_profitti_finali=""
    tabella_mini_profitti_finali=[voci_profitti,corpo_profitti,descrizione_profitti]
    
    
    
    
    
    return tabella_intera_7_voci,tabella_mini_profitti_finali




#i prossimi callback servono all'interno della tab sul tempo atmosferico

#il prossimo callback serve a sincronizzare i due selettori che si occupano di terminare l'output del grafico delle temperature
@callback(
    Output("sottotipo-di-grafico-temperatura", "data"),
          Output("mese-appare-scompare-temperatura", "disabled"),
          Output("sottotipo-di-grafico-temperatura", "value"),
          
          Input("tipo-di-grafico-temperatura", "value")
          )
def selettore_valore_primo_temperatura(valore_primo_selettore):
    #l'output primario consiste nelle opzioni che si rendono disponibili nel secondo selettore
    output_primario_secondo_selettore= [{"value":scelta_sottotipo,"label":scelta_sottotipo}for scelta_sottotipo in opzioni_temperatura_umidità_precipitazioni[valore_primo_selettore]
   ]
                                       
    #print(output_primario_secondo_selettore)
    #il prossimo valore determina un booleano utile nel caso si scelga una visualizzazione di tipo mensile,per stabilire di quale anno il mese richiesto debba essere
    booleano_apparizione_mese=True
    #la prossima variabile è la variabile iniziale preselezionata dal secondo selettore
    preselezione="2024"
    if valore_primo_selettore=="mese":
        booleano_apparizione_mese=False
    if valore_primo_selettore=="mese":
        preselezione="01"
    if valore_primo_selettore=="totale":
        preselezione="totale"
    
    return output_primario_secondo_selettore,booleano_apparizione_mese,preselezione        
    
#il prossimo callback organizza e modifica l'output visivo  del grafico delle temperature
#ricorda di cambiare l'output e la funzione di ritorno
@callback(
    Output("grafico_temperatura", "data"),
    Output("grafico_temperatura", "dataKey"),
          Input("tipo-di-grafico-temperatura", "value"),
          Input("sottotipo-di-grafico-temperatura", "value"),
          Input("mese-appare-scompare-temperatura", "value")
          )
def selezione_selettori_temperatura(valore_primo_selettore,valore_secondo_selettore,valore_anno_selettore_in_dubbio):
    dati_di_partenza=dati_temperatura
    dati_finale=dati_di_partenza
    #la prossima variabile selezione il nome del primo dato da utilizzare nel grafico
    stringa_datakey="giorno"
    if valore_primo_selettore=="anno":
        
        #
        numero_totale_anni=numero_anni
        anno_selezionato=int(valore_secondo_selettore)
        #definiamo il valore dell'inizio della prima e ultima selezione, quella dell'anno
        anni_di_distanza_da_anno_corrente=2025-anno_selezionato
        indice_anno_partendo_dal_basso=numero_totale_anni-anni_di_distanza_da_anno_corrente
        giorno_inizio_anno=365*indice_anno_partendo_dal_basso
        #applichiamo la selezione
        dati_finale=dati_finale[giorno_inizio_anno:(giorno_inizio_anno+365)]
        
    elif valore_primo_selettore=="medie mese per anno":
        numero_totale_anni=numero_anni
        anno_selezionato=int(valore_secondo_selettore)
        #definiamo il valore dell'inizio della prima e ultima selezione, quella dell'anno
        anni_di_distanza_da_anno_corrente=2025-anno_selezionato
        indice_anno_partendo_dal_basso=numero_totale_anni-anni_di_distanza_da_anno_corrente
        giorno_inizio_anno=365*indice_anno_partendo_dal_basso
        #applichiamo la selezione
        dati_finale=dati_finale[giorno_inizio_anno:(giorno_inizio_anno+365)]
        #a differenza della selezione precedente(anno), è necessario ottenere dei dati derivati da questa prima selezione 
        #overo le medie per ogni mese,per farlo dividiamo questa selezione in varie sottoselezioni
        giorni_mesi_passati=0
        lista_medie_mesi=[]
        for giorni_al_mese in lista_numero_giorni_al_mese :
            #il primo passo è creare la selezione dei dati totali inerente al mese analizzato
            selezione_mensile_corrente=dati_finale[giorni_mesi_passati:(giorni_mesi_passati+giorni_al_mese)]
            #selezione_mensile_corrente=selezione_mensile_corrente["valore"]
            x=[(x["valore"])for x in selezione_mensile_corrente]
            selezione_mensile_corrente=x
            #print(selezione_mensile_corrente)
            #print(x)
            
            media=(sum(selezione_mensile_corrente))//len(selezione_mensile_corrente)
            
            lista_medie_mesi.append(media)
            #print(lista_medie_mesi)
            
            #a questo punto è necessario memorizzare il numero di giorni al mese per la prossima iterazione del ciclo
            giorni_mesi_passati+=giorni_al_mese
            
        #terminato il ciclo rilasciamo in output le medie dei mesi
        lista_con_dizionario_medie=[]
        for i in range(len(lista_medie_mesi)):
            x={"mese":str((opzioni_temperatura_umidità_precipitazioni["mese"])[i]),"valore":int(lista_medie_mesi[i])}
            #print(x)
            lista_con_dizionario_medie.append(x)
        dati_finale=lista_con_dizionario_medie
        stringa_datakey="mese"
    elif valore_primo_selettore=="mese":
        
        numero_totale_anni=numero_anni
        anno_selezionato=int(valore_anno_selettore_in_dubbio)
        #definiamo il valore dell'inizio della prima selezione, quella dell'anno
        anni_di_distanza_da_anno_corrente=2025-anno_selezionato
        indice_anno_partendo_dal_basso=numero_totale_anni-anni_di_distanza_da_anno_corrente
        giorno_inizio_anno=365*indice_anno_partendo_dal_basso
        #applichiamo la prima selezione
        dati_finale=dati_finale[giorno_inizio_anno:(giorno_inizio_anno+365)]
        
        #definiamo il valore della seconda selezione
        mese_richiesto=int(valore_secondo_selettore)
        durata_mese_scelto=lista_numero_giorni_al_mese[mese_richiesto-1]
        if mese_richiesto==1:
            giorno_partenza_selezione=0
        else:
            giorno_partenza_selezione=sum(lista_numero_giorni_al_mese[0:(mese_richiesto-1)])
            #print(giorno_partenza_selezione)
            
        #applichiamo la seconda selezione
        dati_finale=dati_finale[giorno_partenza_selezione:(giorno_partenza_selezione+durata_mese_scelto)]
        #print(dati_finale)
        
        
    elif valore_primo_selettore=="totale":
        dati_finale=dati_di_partenza
    
    
    
    
    return dati_finale,stringa_datakey
            
#il prossimo callback serve a sincronizzare i due selettori che si occupano di terminare l'output del grafico delle umidità
@callback(
    Output("sottotipo-di-grafico-umidità", "data"),
          Output("mese-appare-scompare-umidità", "disabled"),
          Output("sottotipo-di-grafico-umidità", "value"),
          
          Input("tipo-di-grafico-umidità", "value")
          )
def selettore_valore_primo_umidità(valore_primo_selettore):
    #l'output primario consiste nelle opzioni che si rendono disponibili nel secondo selettore
    output_primario_secondo_selettore= [{"value":scelta_sottotipo,"label":scelta_sottotipo}for scelta_sottotipo in opzioni_temperatura_umidità_precipitazioni[valore_primo_selettore]
   ]
                                       
    #print(output_primario_secondo_selettore)
    #il prossimo valore determina un booleano utile nel caso si scelga una visualizzazione di tipo mensile,per stabilire di quale anno il mese richiesto debba essere
    booleano_apparizione_mese=True
    #la prossima variabile è la variabile iniziale preselezionata dal secondo selettore
    preselezione="2024"
    if valore_primo_selettore=="mese":
        booleano_apparizione_mese=False
    if valore_primo_selettore=="mese":
        preselezione="01"
    if valore_primo_selettore=="totale":
        preselezione="totale"
    
    return output_primario_secondo_selettore,booleano_apparizione_mese,preselezione        
    
#il prossimo callback organizza e modifica l'output visivo  del grafico delle umidità
#ricorda di cambiare l'output e la funzione di ritorno
@callback(
    Output("grafico_umidità", "data"),
    Output("grafico_umidità", "dataKey"),
          Input("tipo-di-grafico-umidità", "value"),
          Input("sottotipo-di-grafico-umidità", "value"),
          Input("mese-appare-scompare-umidità", "value")
          )
def selezione_selettori_umidità(valore_primo_selettore,valore_secondo_selettore,valore_anno_selettore_in_dubbio):
    dati_di_partenza=dati_umidità
    dati_finale=dati_di_partenza
    #la prossima variabile seleziona il nome del primo dato da utilizzare nel grafico
    stringa_datakey="giorno"
    
    #il primo caso da analizzare è quello in cui si seleziona la visualizzazione di tipo "anno"
    if valore_primo_selettore=="anno":
        
        #
        numero_totale_anni=numero_anni
        anno_selezionato=int(valore_secondo_selettore)
        #definiamo il valore dell'inizio della prima e ultima selezione, quella dell'anno
        anni_di_distanza_da_anno_corrente=2025-anno_selezionato
        indice_anno_partendo_dal_basso=numero_totale_anni-anni_di_distanza_da_anno_corrente
        giorno_inizio_anno=365*indice_anno_partendo_dal_basso
        #applichiamo la selezione
        dati_finale=dati_finale[giorno_inizio_anno:(giorno_inizio_anno+365)]
    
    
    #il secondo caso da analizzare è quello in cui si seleziona la visualizzazione di tipo "medie mese per anno"
    elif valore_primo_selettore=="medie mese per anno":
        numero_totale_anni=numero_anni
        anno_selezionato=int(valore_secondo_selettore)
        #definiamo il valore dell'inizio della prima e ultima selezione, quella dell'anno
        anni_di_distanza_da_anno_corrente=2025-anno_selezionato
        indice_anno_partendo_dal_basso=numero_totale_anni-anni_di_distanza_da_anno_corrente
        giorno_inizio_anno=365*indice_anno_partendo_dal_basso
        #applichiamo la selezione
        dati_finale=dati_finale[giorno_inizio_anno:(giorno_inizio_anno+365)]
        #a differenza della selezione precedente(anno), è necessario ottenere dei dati derivati da questa prima selezione 
        #overo le medie per ogni mese,per farlo dividiamo questa selezione in varie sottoselezioni
        giorni_mesi_passati=0
        lista_medie_mesi=[]
        for giorni_al_mese in lista_numero_giorni_al_mese :
            #il primo passo è creare la selezione dei dati totali inerente al mese analizzato
            selezione_mensile_corrente=dati_finale[giorni_mesi_passati:(giorni_mesi_passati+giorni_al_mese)]
            #selezione_mensile_corrente=selezione_mensile_corrente["valore"]
            x=[(x["valore"])for x in selezione_mensile_corrente]
            selezione_mensile_corrente=x
            #print(selezione_mensile_corrente)
            #print(x)
            
            media=(sum(selezione_mensile_corrente))//len(selezione_mensile_corrente)
            
            lista_medie_mesi.append(media)
            #print(lista_medie_mesi)
            
            #a questo punto è necessario memorizzare il numero di giorni al mese per la prossima iterazione del ciclo
            giorni_mesi_passati+=giorni_al_mese
            
        #terminato il ciclo rilasciamo in output le medie dei mesi
        lista_con_dizionario_medie=[]
        for i in range(len(lista_medie_mesi)):
            x={"mese":str((opzioni_temperatura_umidità_precipitazioni["mese"])[i]),"valore":int(lista_medie_mesi[i])}
            #print(x)
            lista_con_dizionario_medie.append(x)
        dati_finale=lista_con_dizionario_medie
        stringa_datakey="mese"
        
#il terzo caso da analizzare è quello in cui si seleziona la visualizzazione di tipo "mese" che utilizza la variabile di input "mese-appare-scompare-umidità" riferita al selttore del mese appare scompare
    elif valore_primo_selettore=="mese":
        
        numero_totale_anni=numero_anni
        anno_selezionato=int(valore_anno_selettore_in_dubbio)
        #definiamo il valore dell'inizio della prima selezione, quella dell'anno
        anni_di_distanza_da_anno_corrente=2025-anno_selezionato
        indice_anno_partendo_dal_basso=numero_totale_anni-anni_di_distanza_da_anno_corrente
        giorno_inizio_anno=365*indice_anno_partendo_dal_basso
        #applichiamo la prima selezione
        dati_finale=dati_finale[giorno_inizio_anno:(giorno_inizio_anno+365)]
        
        #definiamo il valore della seconda selezione
        mese_richiesto=int(valore_secondo_selettore)
        durata_mese_scelto=lista_numero_giorni_al_mese[mese_richiesto-1]
        if mese_richiesto==1:
            giorno_partenza_selezione=0
        else:
            giorno_partenza_selezione=sum(lista_numero_giorni_al_mese[0:(mese_richiesto-1)])
            #print(giorno_partenza_selezione)
            
        #applichiamo la seconda selezione
        dati_finale=dati_finale[giorno_partenza_selezione:(giorno_partenza_selezione+durata_mese_scelto)]
        #print(dati_finale)
  
#il quarto e ultimo caso da analizzare è quello in cui si seleziona la visualizzazione di tipo "totale"        
    elif valore_primo_selettore=="totale":
        dati_finale=dati_di_partenza
    
    
    
    
    return dati_finale,stringa_datakey
        
#il prossimo callback serve a sincronizzare i due selettori che si occupano di terminare l'output del grafico delle precipitazioni
@callback(
    Output("sottotipo-di-grafico-precipitazioni", "data"),
          Output("mese-appare-scompare-precipitazioni", "disabled"),
          Output("sottotipo-di-grafico-precipitazioni", "value"),
          
          Input("tipo-di-grafico-precipitazioni", "value")
          )
def selettore_valore_primo_precipitazioni(valore_primo_selettore):
    #l'output primario consiste nelle opzioni che si rendono disponibili nel secondo selettore
    output_primario_secondo_selettore= [{"value":scelta_sottotipo,"label":scelta_sottotipo}for scelta_sottotipo in opzioni_temperatura_umidità_precipitazioni[valore_primo_selettore]
   ]
                                       
    #print(output_primario_secondo_selettore)
    #il prossimo valore determina un booleano utile nel caso si scelga una visualizzazione di tipo mensile,per stabilire di quale anno il mese richiesto debba essere
    booleano_apparizione_mese=True
    #la prossima variabile è la variabile iniziale preselezionata dal secondo selettore
    preselezione="2024"
    if valore_primo_selettore=="mese":
        booleano_apparizione_mese=False
    if valore_primo_selettore=="mese":
        preselezione="01"
    if valore_primo_selettore=="totale":
        preselezione="totale"
    
    return output_primario_secondo_selettore,booleano_apparizione_mese,preselezione        
    
#il prossimo callback organizza e modifica l'output visivo  del grafico delle precipitazioni
#ricorda di cambiare l'output e la funzione di ritorno
@callback(
    Output("grafico_precipitazioni", "data"),
    Output("grafico_precipitazioni", "dataKey"),
          Input("tipo-di-grafico-precipitazioni", "value"),
          Input("sottotipo-di-grafico-precipitazioni", "value"),
          Input("mese-appare-scompare-precipitazioni", "value")
          )
def selezione_selettori_precipitazioni(valore_primo_selettore,valore_secondo_selettore,valore_anno_selettore_in_dubbio):
    dati_di_partenza=dati_precipitazioni
    dati_finale=dati_di_partenza
    #la prossima variabile seleziona il nome del primo dato da utilizzare nel grafico
    stringa_datakey="giorno"
    
    #il primo caso da analizzare è quello in cui si seleziona la visualizzazione di tipo "anno"
    if valore_primo_selettore=="anno":
        
        #
        numero_totale_anni=numero_anni
        anno_selezionato=int(valore_secondo_selettore)
        #definiamo il valore dell'inizio della prima e ultima selezione, quella dell'anno
        anni_di_distanza_da_anno_corrente=2025-anno_selezionato
        indice_anno_partendo_dal_basso=numero_totale_anni-anni_di_distanza_da_anno_corrente
        giorno_inizio_anno=365*indice_anno_partendo_dal_basso
        #applichiamo la selezione
        dati_finale=dati_finale[giorno_inizio_anno:(giorno_inizio_anno+365)]
    
    
    #il secondo caso da analizzare è quello in cui si seleziona la visualizzazione di tipo "medie mese per anno"
    elif valore_primo_selettore=="medie mese per anno":
        numero_totale_anni=numero_anni
        anno_selezionato=int(valore_secondo_selettore)
        #definiamo il valore dell'inizio della prima e ultima selezione, quella dell'anno
        anni_di_distanza_da_anno_corrente=2025-anno_selezionato
        indice_anno_partendo_dal_basso=numero_totale_anni-anni_di_distanza_da_anno_corrente
        giorno_inizio_anno=365*indice_anno_partendo_dal_basso
        #applichiamo la selezione
        dati_finale=dati_finale[giorno_inizio_anno:(giorno_inizio_anno+365)]
        #a differenza della selezione precedente(anno), è necessario ottenere dei dati derivati da questa prima selezione 
        #overo le medie per ogni mese,per farlo dividiamo questa selezione in varie sottoselezioni
        giorni_mesi_passati=0
        lista_medie_mesi=[]
        for giorni_al_mese in lista_numero_giorni_al_mese :
            #il primo passo è creare la selezione dei dati totali inerente al mese analizzato
            selezione_mensile_corrente=dati_finale[giorni_mesi_passati:(giorni_mesi_passati+giorni_al_mese)]
            #selezione_mensile_corrente=selezione_mensile_corrente["valore"]
            x=[(x["valore"])for x in selezione_mensile_corrente]
            selezione_mensile_corrente=x
            #print(selezione_mensile_corrente)
            #print(x)
            
            media=(sum(selezione_mensile_corrente))//len(selezione_mensile_corrente)
            
            lista_medie_mesi.append(media)
            #print(lista_medie_mesi)
            
            #a questo punto è necessario memorizzare il numero di giorni al mese per la prossima iterazione del ciclo
            giorni_mesi_passati+=giorni_al_mese
            
        #terminato il ciclo rilasciamo in output le medie dei mesi
        lista_con_dizionario_medie=[]
        for i in range(len(lista_medie_mesi)):
            x={"mese":str((opzioni_temperatura_umidità_precipitazioni["mese"])[i]),"valore":int(lista_medie_mesi[i])}
            #print(x)
            lista_con_dizionario_medie.append(x)
        dati_finale=lista_con_dizionario_medie
        stringa_datakey="mese"
        
#il terzo caso da analizzare è quello in cui si seleziona la visualizzazione di tipo "mese" che utilizza la variabile di input "mese-appare-scompare-precipitazioni" riferita al selttore del mese appare scompare
    elif valore_primo_selettore=="mese":
        
        numero_totale_anni=numero_anni
        anno_selezionato=int(valore_anno_selettore_in_dubbio)
        #definiamo il valore dell'inizio della prima selezione, quella dell'anno
        anni_di_distanza_da_anno_corrente=2025-anno_selezionato
        indice_anno_partendo_dal_basso=numero_totale_anni-anni_di_distanza_da_anno_corrente
        giorno_inizio_anno=365*indice_anno_partendo_dal_basso
        #applichiamo la prima selezione
        dati_finale=dati_finale[giorno_inizio_anno:(giorno_inizio_anno+365)]
        
        #definiamo il valore della seconda selezione
        mese_richiesto=int(valore_secondo_selettore)
        durata_mese_scelto=lista_numero_giorni_al_mese[mese_richiesto-1]
        if mese_richiesto==1:
            giorno_partenza_selezione=0
        else:
            giorno_partenza_selezione=sum(lista_numero_giorni_al_mese[0:(mese_richiesto-1)])
            #print(giorno_partenza_selezione)
            
        #applichiamo la seconda selezione
        dati_finale=dati_finale[giorno_partenza_selezione:(giorno_partenza_selezione+durata_mese_scelto)]
        #print(dati_finale)
  
#il quarto e ultimo caso da analizzare è quello in cui si seleziona la visualizzazione di tipo "totale"        
    elif valore_primo_selettore=="totale":
        dati_finale=dati_di_partenza
    
    
    
    
    return dati_finale,stringa_datakey        
        
        
        
        
if __name__ == "__main__":
    app.run(debug=False)