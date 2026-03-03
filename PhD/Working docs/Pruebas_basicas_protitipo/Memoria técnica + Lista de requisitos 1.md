---
date: 2026-01-30
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

Comprovació dels requisits de la memòria tècnica respecte al que està documentat en: notes amb tag `op/projects/peninsula` ([[PDF/Peninsula/Peninsula.base]]), [[ONTOLOGY_GUIDE]] i [[GROUND_TRUTH_AND_PROMPT_GUIDE]]. Llegenda: **Present** = documentat o clarament implícit en aquestes fonts; **No present** = no documentat.

### 1. Col·laboració i equips

- [x] Definir composició dels equips (Peninsula i UB) i responsabilitats per fase — *No documentat als guides*
- [x] Peninsula: PM, arquitecte, desenvolupadors (NLP, ML, grafs), expert dades, expert UI/accessibilitat — *No documentat*
- [x] UB: IP, requisits funcionals, selecció de dades, model de dades, avaluació i validació — *No documentat*
- [x] Integrar estudiant de doctorat — *No documentat*
- [x] Canals de comunicació, reunions, eines, metodologia (Gantt, riscos, comitè) — *No documentat*
- [x] Transferència de coneixement, documentació, repositori — *No documentat*

### 2. Dades

- [x] Selecció de dades obertes (rellevància, qualitat, formats, llicències) — *ONTOLOGY_GUIDE: fonts CSV, RDF, SQL; qualitat via validació*
- [x] Fonts: dades estructurades (CSV, JSON, RDF) i no estructurades — *Guides: CSV, RDF, SQL; text via LLM*
- [x] Processament: neteja, transformació, integració; NER/relacions; record linking, schema mapping — *GROUND_TRUTH: TYPE_ALIAS_MAP, ONTOLOGICAL_PROPERTY_MAP, RELATIONSHIP_RULES, integració al graf*

### 3. Programari i tecnologies

- [x] Grafs de coneixement: Neo4j (representació, consultes, raonament) — *ONTOLOGY_GUIDE, GROUND_TRUTH: Neo4j, Cypher/SPARQL, RAG*
- [x] **IA/LLM**: Langchain (MLE externs, pipelines, agents); Node.js informes/panells — *Gemini + RAG documentat; Langchain/Node no citats*
- [x] Python; pipelines de text (extraction + QA) — *Guides: Python, prompts, graph_rag*
- [ ] PyTorch, TensorFlow — *No documentat (embeddings/Gemini sense detall de llibreria)*
- [ ] PostgreSQL (dades no graf, geo, vectors) — *No documentat*
- [ ] Stack codi obert memòria (Transformers, RDFlib, NetworkX, React/Vue, Docker) — *No documentat als guides*
- [ ] Integració: Flask/FastAPI, RabbitMQ/Kafka, NiFi/Airflow, Docker/Kubernetes — *endpoint.py (SPARQL) citat; la resta no*

### 4. Llicències i drets d’ús

- [ ] Dades: CC BY/BY-SA, Open Data Commons; no ús sense llicència — *No documentat*
- [ ] Programari: MIT/Apache/BSD/GPL; README amb llicències; control UB — *No documentat*

### 5. Accessibilitat i documentació

- [x] Organitzar dades i codi; documentar — *Guides: estructura constants.py, prompts, mòduls*
- [ ] Dades: estructura jeràrquica, metadades en JSON, esquema del graf documentat — *Parcial: esquema implícit a CELIRU; metadades JSON no*
- [ ] Codi: mòduls (NLP, graf, UI, dades), Git, README, manual, desplegament — *Guides: mòduls backend; README/manual no*

### 6. Requisits funcionals i de disseny

#### 6.1 Interfície d’usuari

- [x] Interfície neta, minimalista, accessible (WCAG), paleta, tipografia — *No documentat*
- [ ] Responsive (escriptori, mòbil, tauleta) — *No documentat*
- [ ] Cerca intel·ligent, navegació, menús, formularis — *RAG/consulta en llenguatge natural documentada; UI no*
- [ ] Accessibilitat: contrastos, text alternatiu, teclat, mida de text, personalització — *No documentat*

#### 6.2 NLP

- [x] Anàlisi semàntica, entitats, relacions, desambiguació — *EXTRACTION_PROMPT + validació simbòlica*
- [x] NER i RE — *Guides: extracció d’entitats i relacions via LLM + ground truth*
- [ ] Topic modeling — *No documentat*
- [x] Generació de respostes: LLM, coherència amb context — *QA_TEMPLATE, RAG*
- [ ] Fine-tuning, aprenentatge per reforç, feedback d’usuaris — *No documentat*
- [ ] Monitoratge de rendiment i errors — *Langfuse citat (observabilitat); detecció d’errors no detallada*

#### 6.3 Raonament simbòlic

- [x] Inferència sobre el graf; consultes tipus SPARQL; relacions implícites — *ONTOLOGY_GUIDE: SPARQL export, Cypher; inverses via ONTOLOGICAL_INFERENCE_RULES*
- [x] Raonament basat en regles — *GROUND_TRUTH: RELATIONSHIP_RULES, inferència inversa, jerarquia administrativa*
- [x] Ontologies (classes, propietats, relacions); vocabulari controlat — *CELIRU + Wikidata als guides*
- [ ] Ontologies OWL formals; LOV; ontologies gènere/interseccionalitats — *CELIRU domain ontology; OWL/LOV no explícits*
- [x] Integració amb LLM: graph embeddings, prompt engineering — *RAG, embeddings, EXTRACTION_PROMPT / QA_TEMPLATE*
- [x] Motor Neo4j; avaluació del raonament — *Neo4j; validació multi-etapa documentada*

#### 6.4 Integració

- [ ] APIs REST (HTTP, JSON) documentades i exemples — *endpoint SPARQL citat; REST no*
- [ ] Missatgeria (RabbitMQ, Kafka), logs, alertes — *No documentat*
- [x] ETL / connectors (SQL, CSV, web); mapatge al graf — *Guides: loader, CSV/RDF/SQL, validació, Neo4j*
- [ ] Microserveis, APIs, escalabilitat — *No documentat*

### 7. Inclusió i diversitat

- [ ] Criteris de selecció de dades (gènere, interseccionalitats), revisió de biaixos — *No documentat*
- [ ] Representació (cis/trans/no binari, ètnia, orientació) — *No documentat*
- [ ] Augmentació/dades sintètiques identificades — *No documentat*
- [ ] Entrenament: desbiaixament, supervisió per equitat — *No documentat*

### 8. Impacte social i mediambiental

- [ ] Impacte social (democratització, memòria democràtica, recerca) — *No documentat*
- [ ] Medi ambient: models eficients, optimització, carbon neutral — *No documentat*

### 9. Responsabilitat ètica i qualitat

- [ ] Proves unitàries, integració, rendiment, usabilitat, acceptació UB — *No documentat als guides*
- [x] Explicabilitat / traçabilitat (context en respostes, font al graf) — *RAG: respostes només amb context; Langfuse*
- [ ] Privacitat: anonimització, consentiment, dades públiques, seguretat — *No documentat*
- [ ] Biaixos: monitoratge, auditoria, feedback i correcció — *No documentat*


