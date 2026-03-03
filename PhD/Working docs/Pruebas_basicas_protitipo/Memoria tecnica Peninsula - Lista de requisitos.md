---
date: 2026-02-02
tags:
  - op/doc/reporte
  - op/projects/peninsula
  - design/requirements
source: "[[Memoria tecnica - planteamiento incial del proyecto]]"
---

# Memoria técnica Peninsula – Lista de requisitos

Requisitos extraïts del document [[Memoria tecnica - planteamiento incial del proyecto]] (PDF: `PDF/Peninsula/Memoria tecnica - planteamiento incial del proyecto.pdf`), segons el text recollit al fitxer .md de clippings.

---

## 1. Col·laboració i equips

- Definir composició dels equips (Peninsula i UB) i responsabilitats per fase.
- Peninsula: Project Manager, arquitecte de solucions, desenvolupadors (NLP, ML, grafs de coneixement), expert en gestió de dades, expert en interfícies d’usuari (accessibilitat, inclusió, diversitat).
- UB: investigador principal, definició d’objectius i **requisits funcionals** del prototip; selecció i interpretació de dades obertes; definició del model de dades i construcció del graf; **avaluació i validació** del prototip (==criteris acadèmics, qualitat i fiabilitat de les respostes, dimensió ètica i social==). #design/evaluation 
- Integrar un estudiant de doctorat a l’equip Peninsula (tesi doctoral).
- Canals de comunicació fluids: reunions regulars, eines de gestió de projectes, plataformes col·laboratives.
- Metodologia: planificació, transparència, comunicació oberta, responsabilitat compartida; descomposició en fases i tasques; Gantt; fites i punts de control; registre de riscos; comunicació asíncrona i sincrona; control de versions; procés formal de gestió de canvis (comitè); actes de reunions.
- Reunions de seguiment setmanals (1 h); reunions puntuals per temes específics (requisits funcionals, tecnologies, tècnics); reunions de planificació de sprints cada 3 setmanes.
- Transferència de coneixement: formació pràctica (“aprendre fent”), sessions sobre reentrenament de models; col·laboració activa de la UB en totes les fases; documentació exhaustiva (disseny, arquitectura, codi, BD, funcionament); lliurament de codi font, dades, eines de configuració i documentació d’implementació i dependències; repositori de control de versions.

---

## 2. Dades

- **Selecció de dades obertes**: rellevància per al projecte (memòria democràtica, interseccionalitats de gènere), qualitat, disponibilitat, idoneïtat per al modelatge del graf; precisió, completesa i actualització; formats adequats; llicències apropiades.
- **Fonts**: repositoris UE, organismes governamentals, acadèmics, sense ànim de lucre; bases dades sobre història, sociologia, política, gènere, memòria democràtica; dades estructurades (CSV, JSON, RDF) i no estructurades (text, imatges, vídeo, àudio).
- **Processament**: neteja (duplicats, valors perduts, errors de format, inconsistències); transformació (format uniforme, normalització, etiquetatge d’entitats, relacions); per a no estructurades: extracció d’entitats, classificació de text, anàlisi de sentiments; integració (record linking, schema mapping); revisió final de qualitat i coherència.

---

## 3. Programari i tecnologies

- **Grafs de coneixement**: Neo4j (representació, consultes, raonament, escalabilitat).
- **IA/LLM**: Langchain (connexió amb MLE externs, pipelines de text, agents de diàleg); Python; llibreries actuals (PyTorch, TensorFlow); Node.js per informes i panells.
- **Dades no graf**: PostgreSQL #op/acc/question  (dades relacionales, extensions geoespacials, vectors).
- **Codi obert (memòria)**: Hugging Face Transformers (NLP, espanyol/català); PyTorch o TensorFlow; RDFlib (RDF, raonament simbòlic); NetworkX (visualització/anàlisi de grafs); Matplotlib/Seaborn; React o Vue.js (UI); Docker (desplegament).
- **Integració (memòria)**: Flask, FastAPI o Django (APIs); RabbitMQ o Kafka (missatgeria); Apache NiFi o Apache Airflow (ETL); Docker i Kubernetes (microserveis).

---

## 4. Llicències i drets d’ús

- Dades: llicències que permetin ús, modificació i redistribució; preferència CC BY, CC BY-SA; Open Data Commons i governamentals si compleixen criteris; consulta als titulars en dubtes; no utilitzar dades sense llicència clara o compatible.
- Programari: prioritat MIT, Apache 2.0, BSD 3 clàusules, GNU GPLv3; compatibilitat de les biblioteques amb la distribució del prototip; README amb tipus de llicència de cada component; models d’IA en codi obert i llicències permissives quan sigui possible; control total de la UB sobre el prototip i el codi font.

---

## 5. Accessibilitat i documentació

- Organitzar dades i codi de manera estructurada i documentar exhaustivament.
- **Dades**: estructura jeràrquica per temàtica/font; subcarpetes per format (CSV, JSON, RDF); noms descriptius; fitxers de metadades (font, llicència, format, dates, criteris) en JSON; documentar esquema del graf a Neo4j.
- **Codi**: estructura modular (mòduls per NLP, graf, UI, gestió de dades); convencions de codificació i comentaris; Git/GitHub; README amb estructura, objectiu dels fitxers, manual d’inici, instal·lació, ús, dependències, desplegament i generació de models personalitzats.

---

## 6. Requisits funcionals i de disseny (Proposta de millores)

### 6.1 Interfície d’usuari

- Interfície neta i minimalista; claredat i facilitat d’ús; disseny consistent; paleta de colors suau; tipografia clara, llegible, mida adequada, estàndards d’accessibilitat web.
- Disseny responsive (escriptori, portàtil, tauleta, mòbil).
- Informació jeràrquica i lògica; barra de navegació clara; menús desplegables, botons, formularis; funció de cerca intel·ligent (paraules clau o frases, resultats ordenats per coincidència).
- **Accessibilitat**: contrastos adequats; text alternatiu per imatges; navegació per teclat i focus visible; control de mida de text; compliment WCAG; opcions de personalització (colors, mida de font, tema); feedback i iteracions de millora.

### 6.2 Processament del llenguatge natural (NLP)

- Anàlisi semàntica (més enllaç de la sintaxi): significat en context, entitats, conceptes i relacions; desambiguació lèxica; anàlisi de dependències; word embeddings per a coneixement contextual.
- NER (reconeixement d’entitats nombrades) i RE (relació entre entitats); topic modeling per a temàtiques i indexació.
- Generació de respostes: LLM pre-entrenats adaptables; coherència amb el context; aprenentatge per reforç; resum; classificació de text per rellevància.
- Aprenentatge i adaptació: feedback d’usuaris per entrenar models; fine-tuning; monitoratge de rendiment i detecció d’errors/inconsistències.

### 6.3 Raonament simbòlic

- Inferència lògica sobre el graf; consultes en llenguatges basats en lògica descriptiva (SPARQL); deducció de relacions implícites; raonament basat en regles (rule-based reasoning).
- Ontologies formals (OWL) per a classes, propietats i relacions; vocabulari controlat (Linked Open Vocabularies); ontologies per a diversitat de gènere i interseccionalitats (interpretació inclusiva i equitativa).
- Integració amb el model de llenguatge: graph embeddings; prompt engineering (Langchain) #op/acc/question per guiar respostes amb informació del graf; rule induction a partir del graf.
- Motor de raonament Neo4j; tècniques d’avaluació per mesurar eficàcia del raonament simbòlic i qualitat de les respostes #op/acc/question .

### 6.4 Integració

- APIs REST (HTTP, JSON) per consultar el graf, enviar consultes en llenguatge natural i rebre respostes estructurades; documentació detallada i exemples.
- Missatgeria asíncrona (p. ex. RabbitMQ, Kafka) per a sistemes heterogenis, monitoratge, logs i alertes.
- Mecanismes ETL per a importació automatitzada (connectors a SQL, CSV, serveis web); mapatge de dades al graf.
- Arquitectura basada en microserveis; comunicació via APIs; escalabilitat i substitució de components.

---

## 7. Inclusió i diversitat

- Criteris de selecció de dades: prioritat a dades que reflecteixin diversitat de gènere i interseccionalitats; evitar biaixos o estereotips; revisió manual per identificar biaixos.
- Representació: dades sobre persones cisgènere, transgènere i no binàries; diferents orígens ètnics, cultures, orientacions sexuals i identitats de gènere.
- Augmentació de dades / dades sintètiques només si cal i identificades com a tals; preferència per dades reals.
- Entrenament: regularització i desbiaixament; supervisió del rendiment per a equitat i imparcialitat; classificació de dades per gènere, ètnia, orientació sexual, etc., per a anàlisi d’impacte per grups.

---

## 8. Impacte social i mediambiental

- **Impacte social positiu**: democratitzar l’accés a la informació; llenguatge natural per evitar llenguatges de consulta complexos; promoció de la memòria democràtica i divulgació de la història (repressió franquista); eina per a recerca acadèmica (història, sociologia, ciència política, etc.); exemples d’ús (familiars de víctimes, persones interessades en la història, investigadors).
- **Medi ambient**: selecció de models eficients en consum energètic; prioritat a models pre-entrenats i codi obert; optimització del codi (vectorització, compressió, quantificació); indexació i cache; compressió de dades; cloud amb energies renovables i alta eficiència (carbon neutral); escalabilitat i serverless on sigui possible.

---

## 9. Responsabilitat ètica i qualitat

- **Avaluació i qualitat**: proves unitàries; proves d’integració; proves de rendiment (càrrega alta, colls d’ampolla, escalabilitat); proves d’usabilitat amb usuaris reals; proves d’acceptació realitzades per la UB; documentació dels resultats i millora contínua; procés de gestió de canvis i d’errors.
- **Transparència**: tècniques d’explicabilitat (paraules/frases rellevants en NLP; visualització de relacions en grafs); interpretability en llenguatge natural per a usuaris no experts.
- **Privacitat**: anonimització de dades; no recollir ni emmagatzemar dades personals sense consentiment; dades externes d’accés públic i sense restriccions incompatibles; mesures de seguretat contra accessos no autoritzats.
- **Biaixos**: monitoratge continu per detectar tendències discriminatoris; auditoria algorítmica; mecanisme de feedback per respostes inadequades i correcció de biaixos/estereotips.

---

## Resum per categories

| Categoria              | Requisits principals                                                                                                         |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **Col·laboració**      | Equips definits, UB responsable de requisits funcionals i validació, metodologia amb reunions i transferència de coneixement |
| **Dades**              | Dades obertes rellevants (memòria democràtica, gènere), qualitat, processament (neteja, transformació, integració)           |
| **Programari**         | Neo4j, Langchain, Python, PostgreSQL, stack codi obert (Transformers, RDFlib, React/Vue, Docker, etc.)                       |
| **Llicències**         | CC BY/BY-SA per dades; MIT/Apache/BSD/GPL per programari; control UB del prototip                                            |
| **Documentació**       | Estructura de dades i codi, metadades, Git, README i manual d’ús i desplegament                                              |
| **UI**                 | Minimalista, accessible (WCAG), responsive, cerca intel·ligent, personalització                                              |
| **NLP**                | Anàlisi semàntica, NER/RE, topic modeling, LLM, fine-tuning, monitoratge                                                     |
| **Raonament simbòlic** | SPARQL, regles, ontologies OWL, graph embeddings, Neo4j, avaluació                                                           |
| **Integració**         | APIs REST, missatgeria, ETL, microserveis                                                                                    |
| **Ètica i qualitat**   | Proves unitàries/integració/rendiment/usabilitat/acceptació, explicabilitat, privacitat, monitoratge de biaixos              |

---

## Existence checklist

Comprovació **només** amb les fonts: [[Informe de Sprint_ 7 de julio - 18 de julio de 2024]] ([[PDF/Peninsula/Informe de Sprint_ 7 de julio - 18 de julio de 2024.pdf]], versió sync-conflict) i [[Memoria tecnica - planteamiento incial del proyecto]] ([[PDF/Peninsula/Memoria tecnica - planteamiento incial del proyecto.pdf]]). **Present** = documentat o clarament implícit en una d’aquestes dues fonts; **No present** = no apareix en cap de les dues.

### 1. Col·laboració i equips

- [x] Definir composició dels equips (Peninsula i UB) i responsabilitats per fase — *Memoria: Pla col·laboració, descripció i responsabilitats dels equips*
- [x] Peninsula: PM, arquitecte, desenvolupadors (NLP, ML, grafs), expert dades, expert UI/accessibilitat — *Memoria: equip Peninsula (PM, arquitecte, desenvolupadors, expert gestió dades, expert interfícies)*
- [x] UB: IP, requisits funcionals, selecció de dades, model de dades, avaluació i validació — *Memoria: equip UB (IP, objectius, requisits funcionals, dades, model de dades, avaluació i validació)*
- [x] Integrar estudiant de doctorat — *Memoria: estudiant de doctorat integrat a l’equip Peninsula*
- [x] Canals de comunicació, reunions, eines, metodologia (Gantt, riscos, comitè) — *Memoria: canals, reunions, Gantt, fites, registre de riscos, comitè de canvis*
- [x] Transferència de coneixement, documentació, repositori — *Memoria: transferència de coneixement, documentació exhaustiva, lliurament codi, repositori*

### 2. Dades

- [x] Selecció de dades obertes (rellevància, qualitat, formats, llicències) — *Memoria: Selecció de dades obertes (rellevància, qualitat, disponibilitat, formats, llicències)*
- [x] Fonts: dades estructurades (CSV, JSON, RDF) i no estructurades — *Memoria: fonts estructurades (CSV, JSON, RDF) i no estructurades (text, imatges, vídeo, àudio)*
- [x] Processament: neteja, transformació, integració; NER/relacions; record linking, schema mapping — *Memoria: neteja, transformació, etiquetatge entitats, relacions; extracció entitats, classificació text; record linking, schema mapping. Sprint: ingesta SQL al graf, mapeig nodos/relaciones*

### 3. Programari i tecnologies

- [x] Grafs de coneixement: Neo4j (representació, consultes, raonament) — *Memoria: Neo4j (representació, consultes, raonament). Sprint: grafo de conocimiento, endpoint SPARQL*
- [x] **IA/LLM**: Langchain (MLE externs, pipelines, agents); Node.js informes/panells — *Memoria: Langchain (MLE externs, pipelines de text, agents de diàleg); Node.js informes i panells*
- [x] Python; PyTorch, TensorFlow — *Memoria: Python; llibreries Pytorch i Tensorflow*
- [x] PostgreSQL (dades no graf, geo, vectors) — *Memoria: PostgreSQL, dades relacionales, extensions geoespacials, indexació de vectors*
- [x] Stack codi obert memòria (Transformers, RDFlib, NetworkX, React/Vue, Docker) — *Memoria: Hugging Face Transformers, PyTorch/TensorFlow, RDFlib, NetworkX, Matplotlib/Seaborn, React o Vue.js, Docker*
- [x] Integració: Flask/FastAPI, RabbitMQ/Kafka, NiFi/Airflow, Docker/Kubernetes — *Memoria: Flask/FastAPI/Django, RabbitMQ/Kafka, Apache NiFi/Airflow, Docker i Kubernetes. Sprint: endpoint SPARQL, redeploy*

### 4. Llicències i drets d’ús

- [x] Dades: CC BY/BY-SA, Open Data Commons; no ús sense llicència — *Memoria: Llicències i drets d’ús; CC BY, CC BY-SA; Open Data Commons; no utilitzar dades sense llicència clara*
- [x] Programari: MIT/Apache/BSD/GPL; README amb llicències; control UB — *Memoria: prioritat MIT, Apache 2.0, BSD 3 clàusules, GNU GPLv3; README amb tipus de llicència; control total UB sobre prototip i codi*

### 5. Accessibilitat i documentació

- [x] Organitzar dades i codi; documentar — *Memoria: Accessibilitat i documentació; organitzar dades i codi de manera estructurada i documentar exhaustivament*
- [x] Dades: estructura jeràrquica, metadades en JSON, esquema del graf documentat — *Memoria: estructura jeràrquica per temàtica/font, subcarpetes per format (CSV, JSON, RDF), fitxers de metadades en JSON; documentar esquema del graf a Neo4j*
- [x] Codi: mòduls (NLP, graf, UI, dades), Git, README, manual, desplegament — *Memoria: mòduls (NLP, graf, UI, gestió dades), Git/GitHub, README (estructura, manual d’inici, instal·lació, ús, dependències, desplegament). Sprint: document de mapeo, criteris d’acceptació*

### 6. Requisits funcionals i de disseny

#### 6.1 Interfície d’usuari

- [ ] Interfície neta, minimalista, accessible (WCAG), paleta, tipografia — *Memoria: Interfície d'usuari; neta i minimalista; paleta de colors suau; tipografia clara, estàndards d'accessibilitat web*
- [ ] Responsive (escriptori, mòbil, tauleta) — *Memoria: disseny responsive (escriptori, portàtil, tauleta, mòbil)*
- [ ] Cerca intel·ligent, navegació, menús, formularis — *Memoria: barra de navegació, menús desplegables, botons, formularis; funció de cerca intel·ligent (paraules clau o frases, resultats per coincidència)*
- [ ] Accessibilitat: contrastos, text alternatiu, teclat, mida de text, personalització — *Memoria: contrastos adequats; text alternatiu; navegació per teclat i focus visible; control de mida de text; WCAG; opcions de personalització (colors, mida de font, tema)*

#### 6.2 NLP

- [ ] Anàlisi semàntica, entitats, relacions, desambiguació — *Memoria: NPL; anàlisi semàntica, entitats, conceptes i relacions; desambiguació lèxica; anàlisi de dependències; word embeddings*
- [ ] NER i RE — *Memoria: NER (reconeixement d’entitats nombrades) i RE (relació entre entitats)*
- [ ] Topic modeling — *Memoria: topic modeling per a temàtiques i indexació*
- [ ] Generació de respostes: LLM, coherència amb context — *Memoria: generació de respostes amb LLM pre-entrenats; coherència amb el context; aprenentatge per reforç; resum; classificació per rellevància*
- [ ] Fine-tuning, feedback d’usuaris, monitoratge — *Memoria: feedback d’usuaris per entrenar models; fine-tuning; monitoratge de rendiment i detecció d’errors/inconsistències*
- [ ] Monitoratge de rendiment i errors — *Memoria: monitoratge de rendiment i detecció d’errors/inconsistències*

#### 6.3 Raonament simbòlic

- [ ] Inferència sobre el graf; consultes tipus SPARQL; relacions implícites — *Memoria: inferència lògica sobre el graf; consultes SPARQL; deducció de relacions implícites. Sprint: endpoint SPARQL, consultes al grafo*
- [ ] Raonament basat en regles — *Memoria: raonament basat en regles (rule-based reasoning). Sprint: regles segons document de Miquet, restriccions i validacions*
- [ ] Ontologies (classes, propietats, relacions); vocabulari controlat; OWL; ontologies gènere — *Memoria: ontologies formals (OWL); vocabulari controlat (LOV); ontologies per a diversitat de gènere i interseccionalitats*
- [ ] Integració amb LLM: graph embeddings, prompt engineering — *Memoria: graph embeddings; prompt engineering (Langchain) per guiar respostes amb informació del graf; rule induction*
- [ ] Motor Neo4j; avaluació del raonament — *Memoria: motor de raonament Neo4j; tècniques d’avaluació per mesurar eficàcia del raonament i qualitat de les respostes. Sprint: tasques sobre mapeo, regles, endpoint SPARQL, testing*

#### 6.4 Integració

- [ ] APIs REST (HTTP, JSON) documentades i exemples — *Memoria: APIs REST (HTTP, JSON) per consultar el graf, consultes en llenguatge natural, respostes estructurades; documentació detallada i exemples*
- [ ] Missatgeria (RabbitMQ, Kafka), logs, alertes — *Memoria: missatgeria asíncrona (RabbitMQ, Kafka) per sistemes heterogenis, monitoratge, logs i alertes*
- [ ] ETL / connectors (SQL, CSV, web); mapatge al graf — *Memoria: mecanismes ETL, connectors (SQL, CSV, serveis web), mapatge de dades al graf. Sprint: ingesta SQL al graf, mapeo nodos/relaciones a Wikidata*
- [ ] Microserveis, APIs, escalabilitat — *Memoria: arquitectura basada en microserveis; comunicació via APIs; escalabilitat i substitució de components*

### 7. Inclusió i diversitat

- [ ] Criteris de selecció de dades (gènere, interseccionalitats), revisió de biaixos — *Memoria: Inclusió i diversitat; prioritat a dades que reflecteixin diversitat de gènere i interseccionalitats; evitar biaixos; revisió manual per identificar biaixos*
- [ ] Representació (cis/trans/no binari, ètnia, orientació) — *Memoria: dades sobre persones cisgènere, transgènere i no binàries; orígens ètnics, cultures, orientacions sexuals i identitats de gènere*
- [ ] Augmentació/dades sintètiques identificades — *Memoria: augmentació de dades / dades sintètiques només si cal i identificades com a tals; preferència per dades reals*
- [ ] Entrenament: desbiaixament, supervisió per equitat — *Memoria: regularització i desbiaixament; supervisió del rendiment per a equitat i imparcialitat; classificació de dades per gènere, ètnia, etc.*

### 8. Impacte social i mediambiental

- [x] Impacte social (democratització, memòria democràtica, recerca) — *Memoria: Impacte social positiu; democratitzar l’accés; llenguatge natural; memòria democràtica i repressió franquista; eina per a recerca acadèmica; exemples d’ús*
- [x] Medi ambient: models eficients, optimització, carbon neutral — *Memoria: Consideracions mediambientals; models eficients; models pre-entrenats i codi obert; optimització (vectorització, compressió, quantificació); indexació i cache; cloud carbon neutral; escalabilitat i serverless*

### 9. Responsabilitat ètica i qualitat

- [ ] Proves unitàries, integració, rendiment, usabilitat, acceptació UB — *Memoria: proves unitàries; proves d’integració; proves de rendiment; proves d’usabilitat amb usuaris reals; proves d’acceptació per la UB; gestió de canvis i d’errors. Sprint ([[Informe de Sprint_ 7 de julio - 18 de julio de 2024]]): proves unitàries per a les regles (Tarea 4); testing ingesta SQL (Tarea 6); testing endpoint SPARQL (Tarea 7); smoke test post-despliegue (Tarea 8); demo i revisió (Tarea 9)*
- [ ] Explicabilitat / transparència — *Memoria: tècniques d’explicabilitat (paraules/frases rellevants; visualització de relacions en grafs); interpretability en llenguatge natural*
- [ ] Privacitat: anonimització, consentiment, dades públiques, seguretat — *Memoria: Privacitat; anonimització; no recollir dades personals sense consentiment; dades externes d’accés públic; mesures de seguretat*
- [ ] Biaixos: monitoratge, auditoria, feedback i correcció — *Memoria: monitoratge continu per detectar tendències discriminatoris; auditoria algorítmica; mecanisme de feedback per respostes inadequades i correcció de biaixos/estereotips*


