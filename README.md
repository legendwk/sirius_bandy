# Sirius Bandy
## Generellt
Instruktioner kring hur man hanterar all kod. 

Koden är skriven i Python 3.9.5

### Använda paket
```
pandas
pptx
```

## Datainsamling
Datainsamlingen kan startas genom:
```
from get_data import Game
g = Game('sirius', 'edsbyn')
g.collector_raw('20221121 sirius edsbyn halvlek 1')
```

### Händelser
Följande händelser och eventuella underhändelser är vi intresserade av:
* **skott** - bollen skjuts mot mål
  * **utanför** - skottet missar mål och går till utkast
  * **räddning** - målvakten räddar
  * **täckt** - skottet når inte mål då det täcks undan av spelare
* **mål** - det blir mål
  * **straffområde** - bollen skjuts inifrån straffområdet 
  * **lång** - bollen skjuts utanför straffområdet
  * **fast** - det blir mål på en fast situation (hörna, straff, frislag)
* **bolltapp** - en spelare förlorar bollen "av egen maskin"
  * **tappad** - spelaren tappar bara kontrollen (dålig dribbling)
  * **passförsök** - spelaren försöker sig på en passning och tappar bollen (dålig passning)
* **närkamp** - det uppstår en närkampssituation som vinns av spelare i laget som anges. 
* **brytning** - spelare i laget som anges bryter boll påväg till motståndare.
* **frislag** - domaren dömer frislag
* **hörna** - domaren dömer hörna
* **straff** - domaren dömer straff
* **utvisning** - domaren dömer utvisning
  * **5** - fem minuters utvisning
  * **10** - tio minuters utvisning 
* **inslag** - bollen går ut och det blir inslag
* **utkast** - bollen hamnar hos målvakten
* **avslag** - det blir avslag
* **passning** - ett lag lägger en farlig passning 
  * **straffområde** - "inlägg" från kant in i straffområde
  * **lång** - långboll
* **friläge** - spelare får ett friläge
* **offside** - spelar i lag åker offside, motstådarna får bollen
* **resning** - laget i fråga rensar bort bollen, motståndarna får den utan närkamp
* **stop** - halvleken slut, programmet avslutas
* **boll** - laget har bollinnehav
* **timeout** - lag tar timeout. Kan även användas utan lag för valfritt (längre) matchstopp. 

### Synca klockan i collector_raw:
För att ändra tiden i realtid vid datainsamling i ```collector_raw``` (t.ex. om videon pausats).
```
clock HH:MM:SS
```

kommer ändra tiden att matcha input.

### Clean CSV
Kommer bara fungera ifall Raw CSV slutar med "tid, stop".

För att starta krävs
```
from get_data import Game
g = Game('sirius', 'edsbyn')
g.clean_csv('20221121 sirius edsbyn halvlek 1', '20221221 sirius edsbyn halvlek 1 CLEAN')
```

### Ask for-metoderna
* Man ska alltid kunna kringgå frågorna genom att ange 0




