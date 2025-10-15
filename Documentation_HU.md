# Dokumentáció
## Többszörös hátizsák feladata

## A probléma leírása

A feladat a több hátizsák probléma megoldása. 
Ez egy kombinatorikus optimalizálási probléma, ahol adott n tárgy (mindegyiknek ismert értéke és súlya) 
és m hátizsák (kapacitással). A cél az, hogy a tárgyakat elhelyezzük a hátizsákokban úgy, hogy 
az összérték maximális legyen, és ne lépjük túl az egyes hátizsákok kapacitását.

Ez a probléma NP-teljes, így néhány hagyományos algoritmus (pl. dinamikus programozás) 
csak kis méretű esetekre alkalmazható. Nagyobb példák esetén metaheurisztikus algoritmusokra van szükség, 
mint például:

- Részecske-raj optimalizálás (PSO)
- Hibrid megoldás (ACO + Simulated Annealing)
- Evolúciós stratégiák

A projektben mindhárom algoritmus implementálása és tesztelése megtörtént, valamint egy memoizáló algoritmus is.

## Az algoritmusok leírása
### 1. Hibrid algoritmus (ACO + Szimulált lehűtés)
Lépések:

1. Hangyák inicializálása: Az ACO (Ant Colony Optimization) keretében több hangya indul, amelyek az optimális megoldás keresése közben feromonokkal jelölik az útjukat.
2. Feromon frissítése: A jobb megoldásokat találó hangyák erősebb nyomot hagynak, segítve a következő iterációkat.
3. Szimulált lehűtés (SA): Az ACO által talált megoldást finomhangolja a SA, amely a megoldás járulékos módosításait (hőmérsékleti gradiens mentén) vizsgálja.
    
### 2. Részezke-raj optimalizálás (PSO)
A PSO a természetes rajviselkedést modellezi. Az algoritmusban több "részecske" (megoldás) mozog a keresési térben.

Lépések:

1. Inicializáció: Az egyes részecskék kezdeti pozícióit és sebességét véletlenszerűen generáljuk.
2. Sebesség frissítése: A részecske sebességét az alábbi formula segítségével számítjuk, ahol:
    - tehetetlenségi együttható,
    - kognitív és szociális súlyok,
    - random szorzók.
3. Pozíció frissítése: A pozíció a sebesség és az előző pozíció alapján módosul.
4. Lokális és globális legjobb megoldás frissítése: Minden részecske megjegyzi a saját és a raj legjobb megoldását.
5. Iteráció: Az algoritmus az előírt iterációszámig fut.

### 3. Evolúciós stratégia
Az evolúciós stratégiák a természetes szelekció és evolúció folyamatát modellezik. A megoldás populációk formájában fejlődik generációkon keresztül.

Lépések:
1. Inicializáció: Véletlenszerű kezdeti populáció generálása, ahol minden egyed egy lehetséges megoldás.
2. Fitnesz értékelése: Minden egyed fitneszét kiszámítjuk, amely az adott megoldás minőségét jelzi.
3. Kiválasztás: A legjobb egyedek kiválasztása, amelyek részt vesznek az új generáció kialakításában.
4. Rekombináció és mutáció: Az új egyedeket keresztezéssel és véletlenszerű mutációkkal hozzuk létre.
5. Új generáció: Az új generáció a kiválasztott és módosított egyedekből áll.
6. Iteráció: Az algoritmus addig fut, amíg el nem érjük a maximális iterációszámot vagy egy előre meghatározott megállási feltételt.

### 4. Memoizációs algoritmus
Rekurzió és dinamikus programozás módszereinek ötvözése.

## Paraméterek és tesztesetek
### Paraméterek
- ### Hibrid:
  - #### ACO:
    - Alfa: 1
    - Beta: 5
    - Evaporációs ráta: 0.5
    - Feromon konstans: 100
    - Hangyák száma: 10
    - Iterációk száma: 100
  - #### Szimulált lehűtés:
    - Kezdeti hőmérséklet: 1000
    - Iterációk száma: 100
- ### PSO:
  - Rajméret: 30
  - Tehetetlenség: 0.8
  - Kognitív súly: 2.0
  - Szociális súly: 2.0
  - Iterációk száma: 1000 
- ### Evolúciós stratégia:
  - Populáció mérete: 40
  - Iterációk száma: 1000

### Tesztesetek
6 tesztesetre próbáltam ki:
  - Input 1: 5 hátizsák, 15 tárgy
  - Input 2: 2 hátizsák, 5 tárgy
  - Input 3: 3 hátizsák, 15 tárgy
  - Input 4: 5 hátizsák, 15 tárgy
  - Input 5: 5 hátizsák, 50 tárgy
  - Input 6: 10 hátizsák, 50 tárgy

## Eredmények

|         | Hibrid (exponenciális) | Hibrid (lineáris) | PSO  | Evolúciós | Memoizációs |
|---------|------------------------|-------------------|------|-----------|-------------|
| Input 1 | 355                    | 355               | 355  | 385       | 395         |
| Input 2 | 80                     | 80                | 90   | 90        | 90          |
| Input 3 | 320                    | 320               | 345  | 345       | 350         |
| Input 4 | 740                    | 740               | 740  | 740       | 740         |
| Input 5 | 1804                   | 1777              | 1990 | 2145      | -           |
| Input 6 | 2620                   | 2620              | 2430 | 2575      | -           |

## Következtetések és további célok
### Következtetések
Az algoritmusok futási ideje és pontossága tesztelésre került:

PSO: Gyorsabb megoldást ad nagyobb példákra, de a megoldás minősége a kezdeti paraméterezéstől függ.

Hibrid algoritmus: Lassabb futás, de precízebb megoldások kis és közepes problémák esetén.

Evolúciós stratégia: Az eredmények változatosak, és a paraméterek finomhangolása kritikus a jó megoldások eléréséhez. 
Gyors és hatékony módszer nagyobb problémák esetén. Összességében ez adta a legjobb megoldásokat.

Memoizációs algoritmus: Jó megoldásokat ad kisebb bemenetekre, viszont messze a leglassabb algoritmus, 
nagyobb bemenetekre nem is lehet használni lassúsága miatt.

### További célok
1. Az algoritmusok továbbfejlesztése (dinamikus paraméterhangolás).
2. Nagyobb méretű tesztadatok alkalmazása.
3. Három algoritmus kombinációjának kipróbálása (ACO + SA + PSO + Evolúciós stratégia).