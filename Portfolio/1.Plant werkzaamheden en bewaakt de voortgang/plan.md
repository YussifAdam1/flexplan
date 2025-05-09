# Opdracht 1: Plant werkzaamheden en bewaakt de voortgang

## 1. Projectomschrijving (Criterium 1.1)

### Samenvatting
FlexPlan is een softwareoplossing waarmee bedrijven hun personeelsroosters efficiënt kunnen beheren. Het doel is om tijd te besparen, chaos door last-minute wijzigingen te verminderen, en medewerkers en managers meer controle te geven over de planning.

### Fictieve Opdrachtgever
We nemen als opdrachtgever een **middelgroot horecabedrijf met 50 medewerkers** dat worstelt met de planning.

#### Problemen die zij ervaren:
- Handmatige roosters maken kost veel tijd.
- Last-minute wijzigingen zorgen voor chaos.
- Medewerkers vergeten hun shifts.
- Managers willen inzicht in de personeelskosten.

### Doelgroep:
- **Horecabedrijven** (restaurants, cafés, hotels).
- **Retail** (supermarkten, kledingwinkels).
- **Gezondheidszorg** (verpleegtehuizen, ziekenhuizen).
- **Evenementensector** (beveiliging, catering).

### Functionaliteiten:
✅ **Automatische roosterplanning** – Maakt roosters op basis van beschikbaarheid.  
✅ **Verlof- en afwezigheidsbeheer** – Medewerkers kunnen vrij vragen en ziekmelden.  
✅ **Notificaties en meldingen** – Medewerkers ontvangen updates bij roosterwijzigingen.  
✅ **Externe koppelingen** – Rooster synchroniseren met telefoonagenda.  
✅ **Inloggen voor werknemer & werkgever** – Verschillende rechten per rol.  
✅ **Beschikbaarheid doorgeven** – Werknemers kunnen aangeven wanneer ze kunnen werken.  
✅ **Roosterweergave & collega's inzien** – Medewerkers kunnen hun rooster en teamleden zien.  
✅ **Werkgever kan beschikbaarheid goedkeuren** – Werkgever kan de opgegeven beschikbaarheid van werknemers goedkeuren.  
✅ **Werkgever kan verlof goedkeuren** – Werkgever kan verlofaanvragen goedkeuren.  
✅ **Werkgever kan roosters publiceren** – Werkgever kan het rooster uploaden en beschikbaar stellen aan medewerkers.  
✅ **Email & pushnotificaties** – Updates bij roosterwijzigingen of publicatie.

---

## 2. Backlog met User Stories (Criterium 1.1 & 1.2)

Hieronder een lijst met **user stories** geprioriteerd met de **MoSCoW-methode**.

### 🔹 Must-have Stories (Essentieel voor MVP)

1️⃣ **Als werknemer wil ik mijn werkrooster kunnen inzien, zodat ik weet wanneer ik moet werken.**  
   - **Definition of Done (DoD):**
     - Rooster is overzichtelijk en interactief.
     - Data komt uit een database.
   - **Acceptatiecriteria:**
     - Rooster toont shifts per dag en week.
     - Gebruiker kan filteren op datum.

2️⃣ **Als werknemer wil ik verlof kunnen aanvragen en afwezigheid doorgeven, zodat ik vrij kan nemen wanneer nodig.**  
   - **DoD:**
     - Formulier voor verlof- en afwezigheidsaanvragen.
     - Manager kan aanvraag goedkeuren of afwijzen.
   - **Acceptatiecriteria:**
     - Gebruiker kan een verlofaanvraag indienen met een reden en datum.
     - Manager ontvangt een melding voor goedkeuring.

3️⃣ **Als werknemer wil ik mijn beschikbaarheid kunnen doorgeven, zodat de planning hiermee rekening kan houden.**  
   - **DoD:**
     - Formulier om beschikbaarheid in te voeren en te wijzigen.
   - **Acceptatiecriteria:**
     - Gebruiker kan dagen en tijden selecteren waarop ze beschikbaar zijn.
     - Beschikbaarheid wordt opgeslagen in de database.

4️⃣ **Als werkgever wil ik de beschikbaarheid van werknemers kunnen goedkeuren, zodat ik efficiënte roosters kan maken.**  
   - **DoD:**
     - Overzicht van medewerkers en hun beschikbaarheid.
     - Mogelijkheid om goed- of af te keuren.
   - **Acceptatiecriteria:**
     - Manager ziet een lijst met beschikbaarheidsverzoeken.
     - Manager kan verzoeken goedkeuren of afwijzen.

5️⃣ **Als werknemer wil ik meldingen ontvangen bij roosterwijzigingen, zodat ik altijd op de hoogte ben.**  
   - **DoD:**
     - Pushnotificaties en e-mails bij veranderingen.
     - Gebruikers kunnen meldingen beheren.
   - **Acceptatiecriteria:**
     - Gebruiker ontvangt een melding bij wijzigingen in het rooster.
     - Gebruiker kan meldingen uitschakelen in de instellingen.

6️⃣ **Als werkgever wil ik roosters kunnen uploaden en publiceren, zodat werknemers hun werktijden kunnen inzien.**  
   - **DoD:**
     - Uploadfunctionaliteit voor roosters.
     - Mogelijkheid om een rooster te publiceren.
   - **Acceptatiecriteria:**
     - Manager kan een Excel-bestand uploaden.
     - Rooster wordt gepubliceerd en zichtbaar voor werknemers.

### 🟡 Should-have Stories (Belangrijk, maar kan later toegevoegd worden)

7️⃣ **Als werknemer wil ik mijn rooster kunnen exporteren naar mijn telefoonagenda, zodat ik altijd up-to-date ben.**  
   - **DoD:**
     - Koppeling met externe agenda’s.
   - **Acceptatiecriteria:**
     - Gebruiker kan rooster exporteren naar Google Calendar of Apple Calendar.

8️⃣ **Als werknemer wil ik kunnen zien met wie ik werk, zodat ik weet wie mijn collega's zijn tijdens mijn shift.**  
   - **DoD:**
     - Rooster toont collega’s per shift.
   - **Acceptatiecriteria:**
     - Gebruiker ziet namen en functies van collega’s per shift.

### 🔹 Could-have Stories (Nice to have, maar niet noodzakelijk)

9️⃣ **Als bedrijf wil ik statistieken kunnen inzien over verlof en werkuren, zodat ik de bezetting kan optimaliseren.**  
   - **DoD:**
     - Grafieken en dashboards over verlofpercentages.
   - **Acceptatiecriteria:**
     - Manager ziet een overzicht van verlofuren per medewerker.

---

## 3. Planning (Criterium 1.3)

Hieronder een overzicht van de sprintplanning, waarin de user stories worden verwerkt in wekelijkse taken.

| **Week** | **Taken** | **User Stories** |
|----------|----------|------------------|
| **Week 1** | Onderzoek & Ontwerp | Wireframes, database setup, API-structuur |
| **Week 2** | Backend Development | Authenticatie, roosterbeheer & verlof API |
| **Week 3** | Frontend Development | UI voor mobiele app & webversie |
| **Week 4** | Testen & Lancering | Bugs fixen, meldingen & livegang |

### Time Estimation per Story:
- **Roosterweergave:** 8 uur  
- **Verlof aanvragen:** 6 uur  
- **Beschikbaarheid doorgeven:** 5 uur  
- **Goedkeuring verlof en beschikbaarheid:** 6 uur  
- **Pushmeldingen en e-mails:** 5 uur  
- **Externe agenda-koppeling:** 6 uur  

---

## 4. Voortgangsbewaking (Criterium 1.4)

Tijdens het project houd ik de voortgang bij en pas ik de planning aan indien nodig.

### Week 1: Onderzoek & Ontwerp
✅ **Opgezet**: Wireframes en database-ontwerp.  
✅ **Afgerond**: API-strategie en keuze van technologieën.  
⚠️ **Uitdaging**: Hoe omgaan met verschillende tijdzones bij medewerkers?

### Week 2: Backend Development
✅ **Opgezet**: PHP backend met MySQL voor roosterbeheer.  
✅ **Afgerond**: API voor roosterbeheer en verlofaanvragen.  
🔄 **Keuze**: E-mailnotificaties toegevoegd voor wijzigingen.

### Week 3: Frontend Development
✅ **Opgezet**: HTML, CSS, JavaScript voor de interface.  
✅ **Afgerond**: Basisinterface voor roosters en verlofaanvragen.  
🔄 **Extra**: Toegevoegd een lichte/donkere modus.

### Week 4: Testen & Lancering
✅ **Opgezet**: Testen van functionaliteit en bugs oplossen.  
✅ **Afgerond**: Oplossen van bugs en verbeteren van UX.  
🚀 **Livegang**: MVP-versie beschikbaar gesteld voor testgebruikers.

---

## 5. Bewijs van Voortgang
- **Screenshots van mijn backlog (Jira, Trello of Notion).**
- **Dagelijkse updates in Markdown met wat is afgerond en waar nog uitdagingen liggen.**
- **Afwegingen die ik maak als iets langer duurt dan gepland.**

---

## 6. Resultaat
🔗 **Repository:** [Mijn GitHub Repo](https://github.com/jouw-github-repo)

---

### Technologieën die gebruikt gaan worden:
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** PHP, MySQL
- **Notificaties:** E-mailnotificaties via PHP mailer of een externe service
- **Roosterbeheer:** Interactief rooster via de front-end (HTML/CSS) en backend (PHP/MySQL)

---
