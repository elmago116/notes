# Acta de la reunió entre l'equip de Península i l'equip de recerca de HerStory

**Data:** 2 de juliol de 2025

---

[[HerStory_reunió_20250702_acta.pdf]]
## Participants

### Equip de Península
- **Victor Piles** (organitzador)
- **Thomas Gómez** 
- **Andrés Manso**

### Equip de HerStory
- **Marina Salse**
- **Miquel Centelles**

---

## Desenvolupament i Acords

### Incorporació de nou membre

Per part de l'equip de Península, s'hi incorpora el desenvolupador **Thomas Gómez** (thomas.gomez@peninsula.co).

### Revisió del Document Sistema General

Es revisa el document **Sistema General**, on s'exposa el sistema d'extracció de dades RDF a partir de formats relacionals, i la generació del sistema d'IAG per a l'explotació del graf de coneixement.

A partir de la revisió, s'incorporen les següents modificacions:

---

## Modificacions Acordades

### 1. Apartat "2. Análisis Estructural Previo"

S'incorpora **SQL** com a format d'ingesta i anàlisi estructural juntament amb els dos ja previstos: **CSV** i **RDF**.

### 2. Apartat "3. Extracción de Entidades y Relaciones"

Península realitzarà **dos mapatges** a partir de la informació facilitada per l'equip de recerca:

#### 2a. Primer mapatge
Un mapatge entre les **regles d'extracció d'entitats i relacions** dels fitxers font i les **regles de transformació de l'esquema ER a Ontologia**.

#### 2b. Segon mapatge  
Un mapatge entre les **entitats i relacions extretes de forma automàtica**, i les **classes i propietats de l'ontologia** desenvolupada per l'equip de recerca sobre la base de Wikidata. 

Aquest mapatge tindrà la forma de taula amb **tres columnes**:
- **Columna 1**: Entitats i relacions procedents de l'extracció automàtica (origen)
- **Columna 2**: Correspondència amb classes i propietats de l'ontologia de HerStory (destinació)  
- **Columna 3**: Noves designacions de les classes i propietats identificades durant la fase d'extracció automàtica

### 3. Apartat "4. Almacenamiento en Neo4j"

#### 3a. Model de graf de propietats
L'equip de Península confirma que l'ús del **model de graf de propietats Neo4j** facilita la conversió en origen a RDF, de forma que no es dificulta (ni es ralentitza) la generació de respostes RDF a consultes i a consum de dades a través d'**SPARQL**.

#### 3b. Restriccions semàntiques
A través de l'ontologia de HerStory, s'aplicaran **restriccions semàntiques (axiomes)** en les dades RDF del graf. Per exemple, les restriccions de domini i de rang en les propietats. 

> **Nota important**: La incorporació de restriccions semàntiques (axiomes) és una tasca específicament desenvolupada per un estudiant de doctorat vinculat al projecte (**Matheus Jerevain**).

### 4. Apartat "Motor de Consultas"

> **Valoració especialment adreçada a Elena Gómez, i al seu pla de recerca.**

L'equip de Península explica com és el **workflow de cerca semàntica** a partir de la consulta (prompt) d'un usuari. Inclou **cinc processos**:

1. Converteix la pregunta en embedding vectorial
2. Busca chunks similars en l'índex vectorial  
3. Identifica entitats relevants en aquests chunks
4. Expandeix el context seguint relacions en el graf
5. Genera resposta utilitzant el context expandit

#### Personalització de respostes

De forma nativa, el sistema té en compte **preguntes anteriors del mateix usuari**, en la mateixa sessió de consulta, per a ponderar i "personalitzar" la resposta. Aquest efecte es produeix durant el **procés número 4**. Això és el que permet **Google Generative AI (Gemini)**. 

La incorporació de dades externes sobre les necessitats i preferències de l'usuari, més enllà de les dades de la sessió, exigirà un **desenvolupament (evolutiu) addicional**. 

> **Important**: Treballar sobre aquest punt en comunicació amb l'equip de Península per tal d'alinear els desenvolupaments.

---

## Calendari de Seguiment

### 📅 **Divendres, 4 de juliol**
L'equip de Península enviarà a **Miquel Centelles** la revisió dels processos de l'Sprint actual per tal de reajustar-los a les **modificacions 1 i 2(a i b)**.

### 📅 **Dilluns, 7 de juliol**  
**Miquel Centelles** confirmarà, si escau, la revisió dels processos de l'Sprint.

---

*Acta redactada el 2 de juliol de 2025*
*Projecte HerStory - Col·laboració Península* 