import os
import pandas as pd
import general_functions as gf
import re

os.chdir('excel')


# vi står på rätt ställe


filer = ['CHRISTMAS GIFTS - ADRESSLISTA KUNDER - 2022 - EDEHEIM fixad.xlsx',
'Frank adresser.xlsx', 'Julklappar B2C 2022 2.xlsx', 'JulklappLista fixad.xlsx',
'XMAS 2022 SL.xlsx'
]

header = ['Ursprung', 'Antal enheter', 'Företagsnamn', 
'Gatuaddress', 'Postnummer', 'Postort', 
'Land', 'Kontaktperson', 'Telefonnummer', 
'Övrigt']
values = [list() for i in range(len(header))]
outname = 'clean.xlsx'

f = 'CHRISTMAS GIFTS - ADRESSLISTA KUNDER - 2022 - EDEHEIM fixad.xlsx'
df = pd.read_excel(f)
ursprung = 'Ostknivar MMD 1'
for index, row in df.iterrows():
    values[0].append(ursprung)
    values[1].append(None)
    values[2].append(row['FÖRETAG'])
    values[3].append(row['LEVERANSADRESS'])
    values[4].append(row['POSTNUMMER'])
    values[5].append(row['POSTADRESS'])
    values[6].append(row['LAND'])
    values[7].append(row['PERSON'])
    values[8].append(None)
    values[9].append(None)
    
f = 'Frank adresser.xlsx'
df = pd.read_excel(f)
ursprung = 'Ostknivar MMD 2'
for index, row in df.iterrows():
    if index != 0:
        values[0].append(ursprung)
        values[1].append(row['Unnamed: 8'])
        values[2].append(row['Unnamed: 0'])
        values[3].append(row['Unnamed: 2'])
        values[4].append(row['Unnamed: 3'])
        values[5].append(row['Unnamed: 4'])
        values[6].append(row['Unnamed: 5'])
        values[7].append(row['Unnamed: 1'])
        values[8].append(None)
        values[9].append(None)
        
f = 'Julklappar B2C 2022 2.xlsx'
df = pd.read_excel(f)
ursprung = 'Ostknivar MMD 2'
for index, row in df.iterrows():
    values[0].append(ursprung) # ursprung
    values[1].append(None) # antal enheter
    values[2].append(row['Unnamed: 3']) # företagsnamn
    values[3].append(row['Unnamed: 4']) # gatuadress
    values[4].append(row['Unnamed: 5']) # postnummer
    values[5].append(row['Unnamed: 6']) # postort
    values[6].append(row['Unnamed: 7']) # land
    values[7].append(f"{row['Förnamn']} {row['Efternamn']}") # kontaktperson
    values[8].append(None)              # telefonnummer
    values[9].append(row['Skickas eller lämnas'])              # övrigt


f = 'JulklappLista fixad.xlsx'
df = pd.read_excel(f)
ursprung = 'Digital island'
for index, row in df.iterrows():
    values[0].append(ursprung) # ursprung
    values[1].append(None) # antal enheter
    values[2].append(row['KUND']) # företagsnamn

    text = row['ADRESS']
    text = text.split(',')
    if len(text) == 1:
        values[3].append(None) # gatuadress
        values[4].append(None) # postnummer
        values[5].append(None) # postort
        values[6].append(None) # land
        values[7].append(None) # kontaktperson
        values[8].append(None)              # telefonnummer
        values[9].append(text[0])          # övrigt
    if len(text) == 3:
        values[3].append(text[0]) # gatuadress
        values[4].append(text[1]) # postnummer
        values[5].append(text[2]) # postort
        values[6].append('Sverige') # land
        values[7].append(None) # kontaktperson
        values[8].append(None)              # telefonnummer
        values[9].append(None)              # övrigt
        
f = 'XMAS 2022 SL.xlsx'
df = pd.read_excel(f)
ursprung = 'Ostknivar MMD 4'
for index, row in df.iterrows():
    values[0].append(ursprung) # ursprung
    values[1].append(None) # antal enheter
    values[2].append(row['FÖRETAG']) # företagsnamn
    values[3].append(row['LEVERANSADRESS']) # gatuadress
    values[4].append(row['POSTNUMMER']) # postnummer
    values[5].append(row['POSTADRESS']) # postort
    values[6].append(row['LAND']) # land
    values[7].append(row['PERSON']) # kontaktperson
    values[8].append(None)              # telefonnummer
    values[9].append(row['VAT'])              # övrigt

f = 'Julkorg D&A samt I&S till Mårten 221129.xlsx'
df = pd.read_excel(f)
ursprung = 'Pedal'
for index, row in df.iterrows():
    values[0].append(ursprung) # ursprung
    values[1].append(None) # antal enheter
    values[2].append(row['FÖRETAG']) # företagsnamn
    values[3].append(row['Adress']) # gatuadress
    values[4].append(row['Postnummer']) # postnummer
    values[5].append(row['ORT']) # postort
    values[6].append('Sverige') # land
    values[7].append(row['Till']) # kontaktperson
    values[8].append(None)              # telefonnummer
    values[9].append(None)              # övrigt

f = 'Julsäckar till Zacco sammanställning_221107.xlsx'
df = pd.read_excel(f)
ursprung = 'Zacco'
for index, row in df.iterrows():
    if row['Namn på beställare:'] != 'Totalt:':
        values[0].append(ursprung) # ursprung
        values[1].append(row ['Antal']) # antal enheter
        values[2].append(row['Företagsnamn:']) # företagsnamn

        adress = row['Adresser till de företag som ska ha säckarna skickade till sig:']
        adress = adress.split(',')
        if len(adress) == 3:
            values[3].append(adress[0]) # gatuadress
            values[4].append(''.join(re.findall(r'\d+', adress[1]))) # postnummer
            values[5].append(re.sub(r'[^a-zA-Z]+', '', adress[1])) # postort
            values[6].append(adress[2]) # land
        else:
            values[3].append(' '.join(adress)) # gatuadress
            values[4].append(None) # postnummer
            values[5].append(None) # postort
            values[6].append(None) # land

        values[7].append(row['Namn på den som säcken ska vara adresserad till:']) # kontaktperson
        values[8].append(None)              # telefonnummer
        extra = f"Tomma säckar: {row['Antal tomma säckar']} " * bool(row['Antal tomma säckar']) + f"Beställare {row['Namn på beställare:']}"
        values[9].append(extra)              # övrigt

f = 'Frakter timextender.xlsx'
df = pd.read_excel(f)
ursprung = 'Timextender'
for index, row in df.iterrows():
    values[0].append(ursprung) # ursprung
    values[1].append(row['bags']) # antal enheter
    values[2].append(row['Partner']) # företagsnamn
    adress = row['Adress']
    adress = adress.split(',')
    values[3].append(adress[0] + ' ' + adress[1]) # gatuadress
    values[4].append(adress[2]) # postnummer
    values[5].append(adress[3]) # postort
    values[6].append(row['Country']) # land
    values[7].append(row['Contact']) # kontaktperson
    values[8].append(None)              # telefonnummer
    values[9].append(row['Attention'])              # övrigt



clean_df = gf.make_df(header, values)

clean_df.to_excel(outname)