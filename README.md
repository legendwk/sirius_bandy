# Sirius Bandy
## Generellt
Kort instruktion för hur koden bör användas.  

Koden är skriven i Python 3.9.5. 

Tanken bakom insamlings- och sammanställningsverktyget är att den är uppdelad i fristående steg. 

**Insamlingen** är indelad i två delmoment; datainsamlingen i ```Game.collector_raw``` där användaren under en match noterar vad som händer, och datarensningen i ```Game.clean_csv``` där den insamlade datan formateras på rätt sätt och användaren får korrigera eventuella felinmatningar.

**Sammanställningen** av en match sker i ```Stats``` och av flera matcher i ```CompileStats```. Här räknar programmet ihop statistik utifrån en eller flera ```.csv```-filer från datainsamlingen.

**Presentationen** skapas i ```PP```. Ska en matchrapport skapas används ```PP.make_game_report``` och för en säsongsrapport ```PP.make_season_report```. Här genereras en Powerpoint-presentation där statistiken från sammanställningen presenteras.

### "Kommentera bort" kod
I ```runme.py``` finns mycket överflödig och redudnat kod. En majoritet av denna kod utförs dock inte då filen körs. Detta är eftersom den "kommenterats bort", det vill säga den är markerad som en beskrivande kommentar och inte som kod att köra.

Detta kan göras på två sätt:

* För enstaka rader används ```#```, det gör så att resten av raden markeras som en kommentar enligt nedan:
```
# här kommer lite kommentarer
# print('hello, world)
x = 3 + 2 # x är 5
```
* För längre stycken påbörjas och avslutas en kommentar med tre "fnuttar", antingen ```"""``` eller ```'''```. Notera att den typen av "fnutt" som används för att starta kommentaren måste användas för att avsluta den enligt nedan:
```
'''
inget av det som skrivs här kommer utföras.
x = 3 + 2
'''
```
Detta kan med fördel användas av användaren i ```rumme.py``` för att slippa ta bort och skriva om kod hela tiden.

 
### Använda biliotek
```
pandas
numpy
matplotlib
python-pptx
```
### Import av egna filer 
```
from get_data import Game
from get_stats import Stats
from get_pp import PP
import general_functions as gf
from compile_stats import CompileStats
```

### Filsökväg
Generellt antar vi att mapp-arkitekturen ser ut som den gör på Github. Flera metoder är specialanpassade för att placera olika filer i rätt mapp, men det fungerar bara ifall upplägget ser likadant ut på allas datorer. 

Jag har använt filen ```runme.py``` för att anropa metoder och funktioner.

Vi utgår från att filsökvägen till en början är ```sirius_bandy ```-foldern. Jag avänder **Visual Studio Code** och då fungerar alla imports.

## Datainsamling
Datainsamlingen kan startas genom:
```
teams = {'iks', 'vet'}
filename = '20221213 Vetlanda BK - IK Sirius halvlek 1'
os.chdir('data\\2023\\raw')

g = Game(teams)
g.collector_raw(filename)
g.clean_csv(filename)
```
Jätteviktigt är att man inte kan ha snedstreck eller andra "konstiga" skiljetecken i filnamnet! Undvik helst alla skiljtetecken.

### Förkortning -> lag
Används dessa förkortningar vid inmatningen måste inte ```.csv```-filerna ändras vid rapportskapande. Notera att dessa endast förekommer i ```konstanter.py```-filen så de är relativt enkla att ändra.
* *iks* -> Sirius
* *bol* -> Bollnäs
* *bro* -> Broberg
* *eds* -> Edsbyn
* *fri* -> Frillesås
* *gri* -> Gripen
* *ham* -> Hammarby
* *mot* -> Motala
* *rät* -> Rättvik
* *vän* -> Vänersberg
* *saik* -> Sandviken
* *vet* -> Vetlanda
* *villa* -> Villa Lidköping
* *vsk* -> Västerås

### Händelser i Game.collector_raw
Följande händelser och eventuella underhändelser är vi intresserade av. Varje händelse utom **stop** ska vara kopplat till ett lag. I vissa fall kan man vilja kringgå det, exempelvis när det blir ett längre avbrott bör **timeout** användas (för att bollinnehavsstatistiken ska bli rätt) då kan lag **0** väljas. Helst bör zon (**z1**-**z9**) och spelare (**1-99**) även anges. 
* **skott** - bollen skjuts mot mål.
  * **utanför** - skottet missar mål och går till utkast.
  * **räddning** - målvakten räddar.
  * **täckt** - skottet når inte mål då det täcks undan av spelare.
* **skottyp** - notera efter skott/mål för varje avslut.
  * **friställande** - en längre passning når fram till en anfallspelare i ett läge där denna antingen är fri, eller i ett sådant läge att den snabbt kan ta sig fram till ett ohotat skottläge i straffområdet.
  * **inlägg** - bollen passas in i straffområdet från endera kant. 
  * **utifrån** - skott från håll. 
  * **dribbling** - enskild spelare för bollen in i straffområdet och skapar skottläge. Tydligt stark individuell prestation. 
  * **centralt** - ett anfall där flera spelare driver in bollen centralt i straffområde, ofta genom passningsspel såväl i som utanför straffområdet.
  * **fast** - fast situation. Exempelvis straff, hörna eller frislag. 
  * **retur** - skott efter retur. 
* **mål** - det blir mål.
  * **spelmål** - målet tillkom i spel.
  * **hörnmål** - målet tillkom på hörna, inklusive hörnretur.
  * **straffmål** - målet tillkom på straff, inklusive straffretur.
  * **frislagsmål** - målet tillkom på frislag, inklusive frislagsretur.
* **bolltapp** - en spelare förlorar bollen "av egen maskin".
  * **tappad** - spelaren tappar bara kontrollen (ex dålig dribbling).
  * **passförsök** - spelaren försöker sig på en passning och tappar bollen (dålig passning).
* **närkamp** - det uppstår en närkampssituation som vinns av spelare i laget som anges. 
* **brytning** - spelare i laget som anges bryter boll påväg till motståndare.
* **frislag** - domaren dömer frislag.
* **hörna** - domaren dömer hörna, zonen anger vilken sida hörnan slås från. 
* **straff** - domaren dömer straff.
* **40** - Sirius spelar bollen till Sune Gustafsson i eget straffområde. 
* **utvisning** - domaren dömer utvisning.
  * **5** - fem minuters utvisning.
  * **10** - tio minuters utvisning.
* **inslag** - bollen går ut och det blir inslag.
* **utkast** - bollen hamnar hos målvakten.
* **avslag** - det blir avslag.
* **passning** - ett lag spelar en intressant passning.
  * **straffområde** - inlägg/inspel från kant in i straffområde.
  * **lång** - långboll/lyft.
  * **farlig** - passningen ställer den anfallande spelaren fri eller relativt fri i farligt läge. 
* **friläge** - spelare får ett friläge.
* **offside** - spelar i lag åker offside, motstådarna får bollen.
* **rensning** - laget i fråga rensar bort bollen, motståndarna får den utan närkamp.
* **stop** - halvleken slut, programmet avslutas.
* **boll** - laget har bollinnehav.
* **timeout** - lag tar timeout. Kan även användas utan lag för valfritt (längre) matchstopp. 
* **kontring** - lag har kontringsläge.

### Spelare
Alla events kan knytas till en spelare genom att dennes nummer anges. Programmet känner igen spelare som siffror mellan 1 och 99.  2023/24 års Siriusspelare finns sparade med nummer, namn, position och bild i ```constants.py``` för senare bruk.    


### Synca klockan i collector_raw:
För att ändra tiden vid datainsamling i ```collector_raw``` (t.ex. om videon pausats) gör följande: 
```
clock MM:SS
```
 klockslag över 45 minuter (```MM:SS```) kommer antas vara felinmatade tider från andra halvlek och ändras till ```MM:SS-45:00```). Vill man mot förmodan ändra klockan under tilläggstid får detta göras i CSV-filen i efterhand. 
### Ta bort föregående inmatning i collector_raw
Ta bort föregående inmatning genom att ange ```del``` direkt i ```collector_raw```. Detta ska anges utan några andra tecken. Vid behov kan rader tas bort manuellt ur ```.csv```-filerna.
### Game.clean_csv
Kommer bara fungera ifall raw_csv:s sista rad är "stop, MM:SS".
#### Ask for-metoderna
* Man ska alltid kunna kringgå frågorna genom att ange 0. Jag har inaktiverat ```ask_for_zone```-metoden då man ofta inte anger det, och väldigt sällan skriver fel. 

## Sammanställning av statistik 
Filen ```get_stats.py``` används för att skapa ett statistikojekt från en csv-fil enligt oavstående (notera att vi antas stå i mappen ```data\\2023\\raw```):

```
filename = '20220930 IK Sirius - Villa Lidköping halvlek 1 clean.csv'
os.chdir('..\\clean')
s_villa1 = Stats(filename)
```

### Statistik från en hel match
För att kringgå det fakturm att vi sparar data halvleksvis har jag implementerat en ```__add__```-metod i ```Stats```-objektet. Detta medför att vi få datan från en hel match genom att addera två objekt:
```
f1 = '20220930 IK Sirius - Villa Lidköping halvlek 1 clean.csv'
f2 = '20220930 IK Sirius - Villa Lidköping halvlek 2 clean.csv'

s_villa1 = Stats(f1) 
s_villa2 =  Stats(f2)
s_villa_hel = s_villa1 + s_villa2
``` 
Objektet har en fullständig ```Stats.prints```-dictionary. Däremot finns det inga Dataframe-objekt i det nya objektet, så mer ingående statistik kan inte göras (om inte ```__add__```) uppdateras. Vi antar även att additionen bara görs för objekt skapade på samma match; ser de olika objektens ```self.teams``` olika ut kommer det bli problem. 

### Statistik från flera matcher
Filen ```compile_stats.py``` sammanställer data från flera matcher i ett ```CompileStats```-objekt. Den tar som input filsökväg till en mapp endast fylld med csv-filer, och hur många av dessa som ska sammanställas (räknat i bokstavsordning). Jag har fyllt ```data\\compile``` med mappar innehållande olika sorters match-csv-filer.

För att sammanställa statistiken från de tio senaste matcherna sedan returnera den i ett ```Stats```-objekt används:

```
os.chdir('..\\..\\..')
all_games = 'data\\compile\allla'
cs = CompileStas(all_games, N = 10)
s_last_ten = cs.return_stats_obj()
```

```Stats```-objektet har nu ett fullt ```Stats.prints```-dictionary och bär instansvariablen ```Stats.number_of_games``` som är antalet csv-filer som sammanställts. 

Om inget annat anges kommer alla filer i mappen (såvida det inte finns flera än 1000 stycken) sammanställas. 


## Presentation 
Filen ```get_pp.py``` används för att skapa PowerPoint-presentationer med statsitik från ```Stats```-objekt, den använder sig av ```get_plot.py``` för att skapa diagram. Klassen ```PP``` har två huvudmetoder: ```PP.get_game_report``` och ```PP.get_season_report```. 

Matchrapporten antas få ett ```Stats```-objekt med data från en halvlek eller match, medan säsongsrapporten från en längre period (från ett ```CompileStats```-objekt, det vill säga). 

Dessa rapporter skapas på följande vis:
```
os.chdir('powerpointer\\matchrapporter')
pp = PP(s_villa_hel)
pp.make_game_report()

os.chdir('..\\säsongsrapporter')
pp = PP(s_last_ten)
pp.make_season_report()
```
Notera att rapportskaparmetoderna utgår från att vi står i mapp ```powerpointer//vår mapp``` för att hitta bilder. Ställ alltid directory i ```powerpointer\\matchrapporter``` för matchrapporter och ```powerpointer\\säsongsrapporter``` för säsongsrapporter.


## Övriga filer
### general_functions
I filen ```general_functions.py``` finns en rad funktioner som används av de olika klasserna, men som inte passar att ha som metod i någon av dem. 

En av dem som kan anropas med jämna mellanrum är ```clean_up()```. Den raderar alla plot-bilder och PowerPoint-filer som autogenereras av de olika ```PP```-metoderna, förutsatt att rapporttyperna ligger i sina respektive mappar. 
### constants
Filen ```constants.py``` innehåller en rad konstanter som används i de olika filerna. Bland annat alla Elitserieklubbars färger, fullständiga klubbnamn och relativ sökväg till en mapp med deras loggor samt information om Sirius alla spelare. 

