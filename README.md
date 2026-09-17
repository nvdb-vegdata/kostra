
# KOSTRA-leveranse 2026

Årets KOSTRA-rapport fra Nasjonal vegdatabank (NVDB) skal bruke samme metodikk som ble brukt for fjorårets leveranse. 
Det er en del endringer fra fjorårets leveranse. Her er en oversikt over endringene:
* Fylkesveg i alt >5000 ÅDT endres til Fylkesveg i alt >4000 ÅDT.
* Fylkesveg uten fast dekke >5000 ÅDT fjernes fra KOSTRA-uttrekket.
* Fylkesveg med dårlig eller svært dårlig dekketilstand endres til å benytte objekttypen "Tilstandsindikator, dekketilstand" i NVDB.
* Følgende variabler legges til i uttrekket.
    * Fylkesvei med tillatt kjøretøylengde 25.25 meter
    * Fylkesveiferjekaier på fylkesvei
    * Undersjøiske tunneler på fylkesvei

# Nedlasting

Årets leveranse publiseres på github på adressen [https://github.com/nvdb-vegdata/kostra](https://github.com/nvdb-vegdata/kostra). På github kan du lettvint laste ned data med den grønne knappen _"Code" -> "Download ZIP"_ , plassert oppe til høyre.

Eller bruk [denne lenken](https://github.com/nvdb-vegdata/kostra/archive/refs/heads/master.zip)

Nedlasting av enkeltrapporter er ørlite grann mer plundrete, og krever at du navigerer deg fram til riktig rapport, klikker på den og så kan du laste ned:

* Gå til mappen [rapporter_2026](https://github.com/nvdb-vegdata/kostra/tree/main/rapporter_2026)
* Klikk på en fil, for eksempel [Kostra 16 - Fylkesveg tunnel høyde under 4m.xlsx](https://github.com/nvdb-vegdata/kostra/blob/main/rapporter_2026/Kostra%2016%20-%20Fylkesveg%20tunnel%20h%C3%B8yde%20under%204m.xlsx)
* Klikk på _Download_ - knappen 

### Filstruktur

Årets leveranse ligger i undermappen [`rapporter_2026`](https://github.com/nvdb-vegdata/kostra/tree/main/rapporter_2026). Øvrige mapper inneholder kode og dokumentasjon.

| Navn formell bestilling                                              |  Nummerering | Filnavn                                                    |
|--------------------------------------------------------------------------------|----|------------------------------------------------------------|
| Riks-, fylkes-, kommune-, privat- og skogsbilveg                               |  1 | Kostra 01 - Vegnett hele landet.xlsx                       |
|                                                                                |  2 | Kostra 02 - Fylkesveg med motor- og motortrafikkveg.xlsx   |
| Fylkesveg uten fast dekke                                                      |  3 | Kostra 03 - Fylkesveg uten fast dekke.xlsx                 |
| Fylkesveg med 4 felt                                                           |  4 | Kostra 04 - Fylkesveg med 4 felt.xlsx                      |
| Fylkesvei med tillatt aksellast <10 tonn                                       |  5 | Kostra 05 - Fylkesveg aksellast u 10t.xlsx                 |
| Fylkesvei med begrensning på totalvekt <50 tonn                                |  6 | Kostra 06 - Fylkesveg totalvekt u 50t.xlsx                 |
| Fylkesveg med fartsgrense 50 eller lavere                                      |  7 | Kostra 07 - Fylkesveg fartsgrense maks 50kmt.xlsx          |
| Fylkesvei med begrensning på kj.t.lengde <19,5m                                |  8 | Kostra 08 - Fylkesveg maks vogntoglengde under 19.5m,.xlsx |
| Underganger på fylkesveg med høydebegrensning lavere enn 4 m                   |  9 | Kostra 09 - Undergang lavere enn 4m.xlsx                   |
| Fylkesveg med dårlig eller svært dårlig dekketilstand                          | 10 |  - _(leveres fra eget fagsystem dekkeforvaltning)_         |
| Fylkesveg uten fast dekke >5000 ÅDT                                            |    |  - _(Fjernet fra KOSTRA-uttrekket)_                        |
| Fylkesveg i alt >4000 ÅDT                                                      | 12 | Kostra 12 - Fylkesveg ÅDT over 4000.xlsx                   |
| Tunneler på fylkesveg. Lengde                                                  | 13 | Kostra 13 - Fylkesveg lengde tunnel.xlsx                   |
| Tunneler på fylkesveg. Antall                                                  | 14 | Kostra 14 - Fylkesveg antall tunnel.xlsx                   |
| Tunneler på fylkesveg med lengde 500 m og over                                 | 15 | Kostra 15 - Fylkesveg tunnel lengde enn 500m.xlsx          |
| Tunneler på fylkesveg med høydebegrensning <4m                                 | 16 | Kostra 16 - Fylkesveg tunnel høyde under 4m.xlsx           |
| Vegbruer på fylkesveg                                                          | 17 | Kostra 17 - Bruer fylkesveg.xlsx                           |
| Bruer på fylkesvei med tillatt aksellast <10 tonn                              | 18 | Kostra 18 - Bruer under 10t.xlsx                           |
| Bruer på fylkesvei med høydebegrensning <4m                                    | 19 | Kostra 19 - Bruer høydebegrensning under 4m.xlsx           |
| Midtrekkverk på to og trefelts fylkesveger                                     | 20 | Kostra 20 - Fylkesveg to- og trefelt midtrekkverk.xlsx     |
| Gang- og sykkelveger (statlig eller fylkeskommunalt ansvar) langs fylkesveg    | 21 | Kostra 21 - Fylkesveg gang- og sykkelveg.xlsx              |
| Gang- og sykkelveger, alle vegkategorier                                       |    | Kostra 21 - EKSTRA alle gang- og sykkelveg.xlsx            |
| Gang- og sykkelveg i byer/tettsteder >5000 innbyggere (~~SOSI~~ geojsonformat) | 22 | Kostra 22 - Fylkesveg gang- og sykkelveg.zip               |
| Forsterket midtoppmerking (rumlefelt), på fylkesveg                            | 23 | Kostra 23 - Fylkesveg med forsterket midtoppmerking.xlsx   |
| Støyskjermer og voller langs fylkesvei                                         | 24 | Kostra 24 - Fylkesveg med støyskjerm og voll.xlsx          |
| Kollektivfelt langs fylkesveg                                                  | 25 | Kostra 25 - Fylkesveg med kollektivfelt.xlsx               |
| Ekstrarapport motorveger (alle veger, ikke bare fylkesveg)                     |    | Kostra 02 - EKSTRA alle motor- og motortrafikkveger.xlsx   |
| Fylkesvei med tillatt kjøretøylengde 25.25 meter (km)                          | 26 | Kostra 26 - Fylkesveg tillatt kjøretøylengde 25,25m.xlsx   |
| Bruer på fylkesvei (meter)                                                     | 17 | Kostra 17 - Bruer fylkesveg.xlsx                           |
| Fylkesvegferjekaier på fylkesvei (antall)                                      | 27 | Kostra 27 - Fylkesveg antall ferjekai.xlsx                 |
| Undersjøiske tunneler på fylkesvei (meter)                                     | 28 | Kostra 28 - Fylkesveg lengde undersjøisk tunnel.xlsx       |

# Merknader til de enkelte rapportene

Konnekteringslenker knytter sammen en sideveg og en hovedveg i et kryss, og utgjør typisk 5-15 meter mellom det punktet der sideveg møter hovedvegenes vegkant og senterlinja på hovedveg. Disse 5-15 metrene skal ikke regnes med når vi teller veglenger. De utgjør i snitt mindre enn 0.05% av vegnettet, men de er ujevnt fordelt. Konnekteringslenker inngår ikke når vi teller lengder av vegnett, men noen av lengdene nedenfor er opptelling av såkalte _fagdata_, dvs NVDB objekttyper som er _"limt oppå"_ vegnettet i NVDB. For disse klarer vi p.t. ikke skille ut konnekterinngslenkene når vi jobber med fagdata.

### Kostra 01 - Vegnett hele landet

Rapport nummer 1, _"Vegnett hele landet"_, teller lengden av kjørbart vegnet i Norge. Merk at lengdene her oppgis i kilometer, til forskjell fra øvrige rapporter, som har meter som lengdeenhet.

Her teller vi ikke gang- og sykkelveger, kun trafikantgruppe K (kjørende). Av typeVeg så teller vi med verdiene _kanalisertVeg, enkelBilveg, rampe, rundkjøring_ og _gatetun_ Vi teller ikke med sideanlegg, strekninger med _adskilte løp=Mot_ og konnekteringslenker. Derimot teller vi alle kryssdeler.

### Kostra 02 - Fylkesveg med motorveg og motortrafikkveg

Her teller vi lengden av objektet _Motorveg (595)_ langs fylkesvegnettet. Det er såpass få (4 strekninger) at vi ramser dem opp per fylke og vegnummer. Vi teller med eventuelle kryssdeler, men ikke med sideanlegg eller strekninger med _adskilte løp=Mot_.

### Kostra 03 - Fylkesveg uten fast dekke

Her finner vi lengden av objekttypen _Vegdekke (241)_ langs fylkesveg med egenskapfilteret _massetype = Grus_, og skiller tall for vanlig bilveg (trafikantgruppe K) fra tall for gående og syklende (trafikantgruppe G) i egne faner. Vi teller ikke med sideanlegg og _adskilte løp = Mot_.

### Kostra 04 - Fylkesveg med 4 felt

Her teller vi lengden av vegnett som har fire eller flere felt. Vi regner ikke med kjørefelt av typene sykkelfelt, fergeoppstillingsplass og ekstra felt ved bomstasjoner. Vi teller heller ikke med kryssdeler, sideanlegg og konnekteringslenker, og heller ikke _adskilte løp = Mot_.

### Kostra 05 - Fylkesveg med maks aksellast under 10 tonn

Her finner vi lengden av objekttypen _Bruksklasse, normaltransport (904)_ med de egenskapverdiene som tilsier maks aksellast under 10 tonn, langs fylkesveg for trafikantgruppe _kjørende_. Vi tar ikke med data for sideanlegg og _adskilte løp = Mot_.

### Kostra 06 - Fylkesveg med maks totalvekt under 50 tonn

Her finner vi lengden av _Bruksklasse, normaltransport (904)_ langs fylkesveg med de egenskapverdiene som tilsier maks totalvekt under 50 tonn, for trafikantgruppe _kjørende_. Vi tar ikke med data for sideanlegg og _adskilte løp = Mot_.

### Kostra 07 - Fylkesveg med fartsgrense under 50 km/t

Her finner vi lengden av _Fartsgrense (105)_ langs fylkesveg med de egenskapverdiene som tilsier fartgrense 50 kilometer i timen eller lavere, for trafikantgruppe _kjørende_. Vi tar ikke med data for sideanlegg og _adskilte løp = Mot_.

### Kostra 08 - Fylkesveg med begrensing på kjøretøylengde mindre enn 19,5 meter

Her finner vi lengden av _Bruksklasse, normaltransport (904)_ langs fylkesveg med de egenskapverdiene som tilsier maks kjøretøylengde kortere enn 19.5 meter, for trafikantgruppe _kjørende_. Vi tar ikke med data for sideanlegg og _adskilte løp = Mot_.

### Kostra 09 - Undergang med høyde lavere enn 4 meter

Her teller vi antall av _Høydebegrensning (591)_ med egenskapsfilteret _Type Hinder = Undergang/bru_ og _Skilta høyde < 4_ langs fylkesveg.

### Kostra 10 - IKKE I DENNE LEVERANSEN (fylkesveg med dårlig dekketilstand)

_Disse dataene finnes ikke i nasjonal vegdatbank, men i eget system for forvaltning av vegdekke. Vi forstår at dette er en separat leveranse; denne leveransen har kun data fra NVDB._

### Kostra 12 - Fylkesveg i alt >5000 ÅDT

Her teller vi objekttypen _Trafikkmengde (540)_ med egenskapverdien _ÅDT, total_ større enn 5000 kjøretøy per døgn langs fylkesveger.

### Kostra 13 - Tunneller på fylkesveg, lengde

Her teller vi samlet lengde for tunneler på fylkesveg. Analysen er en sammenstilling av objekttypene _Tunnelløp (67)_ og _Tunnel (581)_. Hvis _tunnel_ - objektet har egenskapen _Lengde, offisiell_ så bruker vi denne for å regne ut lengdene. Hvis ikke henter vi lengden fra tunnelløpet, enten fra tunnelløpets egenskap _Lengde_ eller fra tunnelløpets utstrekning langs vegnettet.

### Kostra 14 - Tunneller på fylkesveg, antall

Her teller vi antall tunneler på fylkesveg. Analysen ser på vegobjekttypen _Tunnel (581)_. 

### Kostra 15 - Tunneller lengre enn 500 meter på fylkesveg

Samme metodikk som for kostra 13 og 14, men nå teller vi kun antall og lengde for de tunnellene som er lengre enn 500 meter.

### Kostra 16 - Tunneller på fylkesveg med høyde under 4 meter

Her finner vi objekttypene _Tunnel (581)_ og _Tunnelløp (67)_ som overlapper med objekttypen _Høydebegrensning (591)_ som har egenskapverdi _Skilta høyde_ lavere enn 4 meter. For å finne lengden av tunneller bruker vi samme metode som Kostra 13, 14 og 15.

### Kostra 17 - Bruer langs fylkesveg

Her finner vi antall og lengde av objekttypen _Bru (60)_ som har egenskap _Brukategori = Vegbru_ eller  _Bru i fylling_.

### Kostra 18 - Bruer under 10t langs fylkesveg

Her finner vi antall og lengde langs fylkesveg av objekttypen _Bru (60)_ som har egenskap _Brukategori = Vegbru_ og overlapper med objekttypen _Brukslasse, normaltransport (904)_ med egenskapverdier som angir tillatt aksellast lavere enn 10 tonn.

### Kostra 19 - Bruer med høydebegrensning lavere enn 4 meter

Her finner vi antall og lengde langs fylkesveg av objekttypen _Bru (60)_ som har egenskap _Brukategori = Vegbru_ og overlapper med objekttypen _Høydebegrensning (591)_ med egenskapverdi _Skilta høyde_ lavere enn 4 meter.

### Kostra 20 - Midtrekkverk på to og trefelts fylkesveger

Objekttypen _Rekkverk (5)_ med egenskapen _Bruksområde = Midtrekkverk_ eller _Midtdeler_  langs fylkesveger der vi har to eller tre kjørefelt. Her er analysen simplifisert fra tidligere leveranser. Nå gjør vi en overlappsspørring med objekttypen _Feltstrekning (616)_ med egenskapen _Type = 2-feltsveg envegskjørt, 2-feltsveg, Del av 2-feltsveg, 3-feltsveg envegskjørt, 3-feltsveg_ eller _Del av 3-feltsveg_.
Ettersom datagrunnlaget for midtrekkverk i NVDB inneholder en god del feil, har det i forbindelse med årets leveranse blitt gjort en jobb med å gå gjennom midtrekkverkene i NVDB og filtrere bort feilklassifiserte midtrekkvert fra rapporten. Eksakt hvilke rekkverk-objekter som er filtrert bort står tydelig i Python-koden.

### Kostra 21 - gang og sykkelveg for fylkesveger

Her henter vi vegnett for vegkategorien "Fylkesveg" og  trafikantgruppe "G" (gående og syklende).

### Kostra 21 - EKSTRA gang og sykkelveg for alle vegkategorier

Dette er ikke en del av KOSTRA-rapporteringen, men lengde vegnett for gående og syklende er etterspurt for alle vegkategorier. Så her henter vi vegnett for trafikantgruppe "G" (gående og syklende), alle vegkategorier.

### Kostra 22 - Gang og sykkelveg langs fylkesveg i tettsteder med mer enn 5000 innbyggere

Dette er samme datagrunnlag som rapport 21, men i stedet for å oppsummere lengder per fylke så lagrer vi dataene på et GIS-vennlig format. Strengt tatt er vi forpliktet til å levere på SOSI-format for denen typen datautveksling. Dessverre er vi pga tidsnød ikke i stand til å løse gjenværende hindringer for lettvint produksjon av sosifiler med vegnett på det nye vegreferansesystemet. I stedet mener vi geojson er et greit alternativ. Vi kan også levere på andre formater - også sosi, gitt mere tid - bare si ifra.

Den opprinnelige bestillingen er _"gang- og sykkelveger innenfor tettsteder med mer enn 5000 innbyggere"_. Ettersom tettsteder er et datasett som ajourholdes av SSB ser vi det som mest hensiktsmessig at SSB selv gjør analysen med å finne hvor stor del av gang- og sykkelvegene som er innafor disse tettstedene. Dette er en triviell geografisk analyse. Hvis dette ikke er tilfredsstillende så ta kontakt, så skal vi ordne det.

### Kostra 23 - Fylkesveg med forsterket midtoppmerking

Dette er telling av objekttypen "Vegoppmerking, forsterket (836)" med egenskapsfilteret _Type = Forsterket midtoppmerking_ langs fylkesveg.

### Kostra 24 - Fylkesveg med støyskjerm og voll

Dette er telling av objekttypene _Skjerm (3)_ med  egenskapen _Bruksområde = Stæyskjerm_ og _Voll (234)_ med egenskapen  _Bruksområde = Støyskjerming_ langs fylkesveg.

### Kostra 25 - Fylkesveg med kollektivfelt

Her teller vi lengde av vegnettet for kjørende, slik som i rapporten Kostra 01 vegnett, men i denne rapporten teller vi vi kun med de strekningene der det finnes kollektivfelt.  

Vi ser at de eldre versjonene av Rapport nummer 25, _"Fylkesveg med kollektivfelt"_, så er det telt to ganger veglengden der kollektivfelt finnes på begge sider av vegen. I årets rapport vil lengden tilsvare _"Lengde per kollektivfelt"_. Altså strekninger der kollektivfelt finnes på begge sider vil telles to ganger i rapporten.

### Ekstrarapport motorveger

Dette er en modifisering av datauttaket for motorveg og motortrafikkveg fylkesveger (rapport 02), men for alle veger. Underveis fant vi at det riktigste bildet er å ingnorere kryssdeler og ramper (fra før har vi filtrert ut _adskilte løp=MOT_ og sideanlegg). 

### Kostra 26 - Fylkesvei med tillatt kjøretøylengde 25.25 meter

Her finner vi lengden av _Bruksklasse, tømmertransport (900)_ med egenskapsverdi _Tillatt for modulvogntog 1 og 2 med sporingskrav_ = _Ja_ langs fylkesveg, for trafikantgruppe _kjørende_. Vi tar ikke med data for sideanlegg og _adskilte løp = Mot_.

### Kostra 27 - Fylkesveiferjekaier på fylkesvei

Dette er en opptelling av objekttypen _Ferjekai (64)_ med egenskapen _Driftsstatus_ = _Trafikkeres_ langs fylkesveg. I tillegg filtrerer vi på ferjekaier med _Vedlikeholdsansvarlig_ = _Fylkeskommune_. Dersom _Vedlikeholdsansvarlig_ ikke har verdi filtrerer vi på _Eier_ = _Fylkeskommune_. Ferjekaier der både _Eier_ og _Vedlikeholdsansvarlig_ mangler verdi vil også tas med i uttrekket.

### Kostra 28 - Undersjøiske tunneler på fylkesvei

Her teller vi samlet lengde for undersjøiske tunneler på fylkesveg. Analysen er en sammenstilling av objekttypene _Tunnelløp (67)_ og _Tunnel (581)_ med egenskapen _Undersjøisk_ = _Ja_. Hvis _tunnel_ - objektet har egenskapen _Lengde, offisiell_ så bruker vi denne for å regne ut lengdene. Hvis ikke henter vi lengden fra tunnelløpet, enten fra tunnelløpets egenskap _Lengde_ eller fra tunnelløpets utstrekning langs vegnettet.