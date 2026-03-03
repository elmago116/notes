---
tags:
  - op/doc/tests
date: 2026-02-25
---


# Request format & query catalog

**Endpoint:** `POST https://ubxat.peninsula.co/api/v1/sparql`  
**Auth:** HTTP Basic (`-u 'USER:PASS'`)  
**Body:** `{"query": "<Cypher string>", "format": "json"}`  
**Note:** The API executes **Cypher** (Neo4j); examples below are Cypher equivalents of the SPARQL patterns.

---

## SELECT queries

### 1. Basic triple patterns: ?subject ?predicate ?object

Cypher equivalent: match (subject)-[r]->(object) and return subject id, relationship type, object id.

```bash
curl -u 'ubxat:BLI-u24KH%36xM9gQ9PzX' \
  -X POST 'https://ubxat.peninsula.co/api/v1/sparql' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{
    "query": "MATCH (subject)-[r]->(object) RETURN id(subject) AS subject, type(r) AS predicate, id(object) AS object",
    "format": "json"
  }'
```
#### In SPARQL:
```sparql
SELECT ?subject ?predicate ?object
WHERE {
  ?subject ?predicate ?object .
}
LIMIT 100
```

```bash
curl -u 'ubxat:BLI-u24KH%36xM9gQ9PzX' \
  -X POST 'https://ubxat.peninsula.co/api/v1/sparql' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{
    "query": "SELECT ?subject ?predicate ?object WHERE { ?subject ?predicate ?object . } LIMIT 100",
    "format": "json"
  }'
```

#### Obtained in UBXAT 
```bash
[
  {
    "n": {
      "value": "0"
    },
    "nLabel": {
      "value": "Informació diversa sobre el brigadista Hans Kaltschmidt. [S.l. : s.n.], 2023."
    }
  },
  {
    "n": {
      "value": "1"
    },
    "nLabel": {
      "value": "BORRÀS DÒLERA, Mercè. Informació diversa sobre els brigadistes Pierre Odéon i Paula Feldestein. [S.l. : s.n.], 2024."
    }
  },
  {
    "n": {
      "value": "2"
    },
    "nLabel": {
      "value": "SCHOLTEN, Yvonne. \"In search of the first Dutch volunteer\". The Volunteer (5/2/2022)"
    }
  },
  {
    "n": {
      "value": "3"
    },
    "nLabel": {
      "value": "Российский государственный архив социально-политической истории (РГАСПИ) | Arxiu Estatal Rus d'Història Sociopolítica (RGASPI). Informació diversa sobre el brigadista Fritz Hilger. [Moscou : RGASPI], 2024."
    }
  },
  {
    "n": {
      "value": "4"
    },
    "nLabel": {
      "value": "Российский государственный архив социально-политической истории (РГАСПИ) | Arxiu Estatal Rus d'Història Sociopolítica (RGASPI). Informació diversa sobre el brigadista Sam Gibons. [Moscou : RGASPI], 2021."
    }
  },
  {
    "n": {
      "value": "5"
    },
    "nLabel": {
      "value": "LEWIS, Wendy. Informació diversa sobre el brigadista Sidney Shosteck. [S.l : s.n.], 2023"
    }
  },
  {
    "n": {
      "value": "6"
    },
    "nLabel": {
      "value": "ABACERIN, Georges"
    }
  },
  {
    "n": {
      "value": "7"
    },
    "nLabel": {
      "value": "ACER. Les Amis des Combattants en Espagne Républicaine. Brigadistes"
    }
  },
  {
    "n": {
      "value": "8"
    },
    "nLabel": {
      "value": "La Columna Uruguaya : historia de los uruguayos en la guerra Civil Española"
    }
  },
  {
    "n": {
      "value": "9"
    },
    "nLabel": {
      "value": "\"Muere la musa catalana de Hemingway en Por quién doblan las campanas\". La Vanguardia (4/6/2012)"
    }
  }
]
```

#### Obtained in server - Cypher:
```bash
curl -u 'ubxat:BLI-u24KH%36xM9gQ9PzX' \
  -X POST 'https://ubxat.peninsula.co/api/v1/sparql' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{
    "query": "MATCH (subject)-[r]->(object) RETURN id(subject) AS subject, type(r) AS predicate, id(object) AS object",
    "format": "json"
  }'
{"query":"MATCH (subject)-[r]->(object) RETURN id(subject) AS subject, type(r) AS predicate, id(object) AS object","results":[{"subject":0,"predicate":"MAIN_SUBJECT","object":11},{"subject":3,"predicate":"MAIN_SUBJECT","object":12},{"subject":4,"predicate":"MAIN_SUBJECT","object":13},{"subject":5,"predicate":"MAIN_SUBJECT","object":14},{"subject":15,"predicate":"LOCATED_IN","object":26},{"subject":15,"predicate":"HAS_ASSESSMENT","object":24},{"subject":15,"predicate":"HAS_PRESERVATION_STATE","object":25},{"subject":15,"predicate":"PARTICIPANT_IN","object":31},{"subject":15,"predicate":"CONTAINS_REMAINS_OF","object":32},{"subject":16,"predicate":"LOCATED_IN","object":35},{"subject":16,"predicate":"HAS_ASSESSMENT","object":33},{"subject":16,"predicate":"HAS_PRESERVATION_STATE","object":34},{"subject":16,"predicate":"PARTICIPANT_IN","object":38},{"subject":16,"predicate":"PARTICIPANT_IN","object":39},{"subject":16,"predicate":"CONTAINS_REMAINS_OF","object":40},{"subject":17,"predicate":"LOCATED_IN","object":41},{"subject":17,"predicate":"HAS_ASSESSMENT","object":33},{"subject":17,"predicate":"HAS_PRESERVATION_STATE","object":34},{"subject":17,"predicate":"PARTICIPANT_IN","object":39},{"subject":17,"predicate":"CONTAINS_REMAINS_OF","object":40},{"subject":18,"predicate":"LOCATED_IN","object":42},{"subject":18,"predicate":"HAS_ASSESSMENT","object":24},{"subject":18,"predicate":"HAS_PRESERVATION_STATE","object":25},{"subject":18,"predicate":"PARTICIPANT_IN","object":31},{"subject":18,"predicate":"CONTAINS_REMAINS_OF","object":43},{"subject":19,"predicate":"LOCATED_IN","object":45},{"subject":19,"predicate":"HAS_ASSESSMENT","object":24},{"subject":19,"predicate":"HAS_PRESERVATION_STATE","object":44},{"subject":19,"predicate":"PARTICIPANT_IN","object":47},{"subject":19,"predicate":"PARTICIPANT_IN","object":48},{"subject":19,"predicate":"CONTAINS_REMAINS_OF","object":32},{"subject":19,"predicate":"CONTAINS_REMAINS_OF","object":40},{"subject":20,"predicate":"LOCATED_IN","object":50},{"subject":20,"predicate":"HAS_ASSESSMENT","object":24},{"subject":20,"predicate":"HAS_PRESERVATION_STATE","object":49},{"subject":20,"predicate":"PARTICIPANT_IN","object":48},{"subject":20,"predicate":"CONTAINS_REMAINS_OF","object":32},{"subject":20,"predicate":"CONTAINS_REMAINS_OF","object":40},{"subject":20,"predicate":"CONTAINS_REMAINS_OF","object":43},{"subject":21,"predicate":"LOCATED_IN","object":53},{"subject":21,"predicate":"HAS_ASSESSMENT","object":24},{"subject":21,"predicate":"HAS_PRESERVATION_STATE","object":34},{"subject":21,"predicate":"PARTICIPANT_IN","object":47},{"subject":21,"predicate":"PARTICIPANT_IN","object":48},{"subject":21,"predicate":"CONTAINS_REMAINS_OF","object":40},{"subject":21,"predicate":"CONTAINS_REMAINS_OF","object":56},{"subject":22,"predicate":"LOCATED_IN","object":57},{"subject":22,"predicate":"HAS_ASSESSMENT","object":24},{"subject":22,"predicate":"HAS_PRESERVATION_STATE","object":44},{"subject":22,"predicate":"PARTICIPANT_IN","object":48},{"subject":22,"predicate":"CONTAINS_REMAINS_OF","object":40},{"subject":23,"predicate":"LOCATED_IN","object":59},{"subject":23,"predicate":"HAS_ASSESSMENT","object":24},{"subject":23,"predicate":"HAS_PRESERVATION_STATE","object":44},{"subject":23,"predicate":"PARTICIPANT_IN","object":38},{"subject":23,"predicate":"CONTAINS_REMAINS_OF","object":40},{"subject":26,"predicate":"LOCATED_IN","object":27},{"subject":27,"predicate":"LOCATED_IN","object":28},{"subject":28,"predicate":"LOCATED_IN","object":29},{"subject":29,"predicate":"LOCATED_IN","object":30},{"subject":35,"predicate":"LOCATED_IN","object":36},{"subject":36,"predicate":"LOCATED_IN","object":37},{"subject":37,"predicate":"LOCATED_IN","object":29},{"subject":41,"predicate":"LOCATED_IN","object":27},{"subject":42,"predicate":"LOCATED_IN","object":27},{"subject":45,"predicate":"LOCATED_IN","object":46},{"subject":46,"predicate":"LOCATED_IN","object":37},{"subject":50,"predicate":"LOCATED_IN","object":51},{"subject":51,"predicate":"LOCATED_IN","object":52},{"subject":52,"predicate":"LOCATED_IN","object":29},{"subject":53,"predicate":"LOCATED_IN","object":54},{"subject":54,"predicate":"LOCATED_IN","object":55},{"subject":55,"predicate":"LOCATED_IN","object":29},{"subject":57,"predicate":"LOCATED_IN","object":58},{"subject":58,"predicate":"LOCATED_IN","object":28},{"subject":59,"predicate":"LOCATED_IN","object":58}],"format":"json","execution_time":0.7489999998360872,"source":"neo4j","query_type":"cypher"}%   
```

#### Obtained in server SPARQL
```bash
curl -u 'ubxat:BLI-u24KH%36xM9gQ9PzX' \
  -X POST 'https://ubxat.peninsula.co/api/v1/sparql' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{
    "query": "SELECT ?subject ?predicate ?object WHERE { ?subject ?predicate ?object . }",
    "format": "json"
  }'
{"query":"SELECT ?subject ?predicate ?object WHERE { ?subject ?predicate ?object . }","results":[{"subject":{"value":"0"},"subjectLabel":{"value":"Informació diversa sobre el brigadista Hans Kaltschmidt. [S.l. : s.n.], 2023."},"predicate":{"value":"MAIN_SUBJECT"},"object":{"value":"11"}},{"subject":{"value":"3"},"subjectLabel":{"value":"Российский государственный архив социально-политической истории (РГАСПИ) | Arxiu Estatal Rus d'Història Sociopolítica (RGASPI). Informació diversa sobre el brigadista Fritz Hilger. [Moscou : RGASPI], 2024."},"predicate":{"value":"MAIN_SUBJECT"},"object":{"value":"12"}},{"subject":{"value":"4"},"subjectLabel":{"value":"Российский государственный архив социально-политической истории (РГАСПИ) | Arxiu Estatal Rus d'Història Sociopolítica (RGASPI). Informació diversa sobre el brigadista Sam Gibons. [Moscou : RGASPI], 2021."},"predicate":{"value":"MAIN_SUBJECT"},"object":{"value":"13"}},{"subject":{"value":"5"},"subjectLabel":{"value":"LEWIS, Wendy. Informació diversa sobre el brigadista Sidney Shosteck. [S.l : s.n.], 2023"},"predicate":{"value":"MAIN_SUBJECT"},"object":{"value":"14"}},{"subject":{"value":"15"},"subjectLabel":{"value":"Cementiri de Dosrius"},"predicate":{"value":"LOCATED_IN"},"object":{"value":"26"}},{"subject":{"value":"15"},"subjectLabel":{"value":"Cementiri de Dosrius"},"predicate":{"value":"HAS_ASSESSMENT"},"object":{"value":"24"}},{"subject":{"value":"15"},"subjectLabel":{"value":"Cementiri de Dosrius"},"predicate":{"value":"HAS_PRESERVATION_STATE"},"object":{"value":"25"}},{"subject":{"value":"15"},"subjectLabel":{"value":"Cementiri de Dosrius"},"predicate":{"value":"PARTICIPANT_IN"},"object":{"value":"31"}},{"subject":{"value":"15"},"subjectLabel":{"value":"Cementiri de Dosrius"},"predicate":{"value":"CONTAINS_REMAINS_OF"},"object":{"value":"32"}},{"subject":{"value":"16"},"subjectLabel":{"value":"Rabós, prop del Coll de Banyuls"},"predicate":{"value":"LOCATED_IN"},"object":{"value":"35"}},{"subject":{"value":"16"},"subjectLabel":{"value":"Rabós, prop del Coll de Banyuls"},"predicate":{"value":"HAS_ASSESSMENT"},"object":{"value":"33"}},{"subject":{"value":"16"},"subjectLabel":{"value":"Rabós, prop del Coll de Banyuls"},"predicate":{"value":"HAS_PRESERVATION_STATE"},"object":{"value":"34"}},{"subject":{"value":"16"},"subjectLabel":{"value":"Rabós, prop del Coll de Banyuls"},"predicate":{"value":"PARTICIPANT_IN"},"object":{"value":"38"}},{"subject":{"value":"16"},"subjectLabel":{"value":"Rabós, prop del Coll de Banyuls"},"predicate":{"value":"PARTICIPANT_IN"},"object":{"value":"39"}},{"subject":{"value":"16"},"subjectLabel":{"value":"Rabós, prop del Coll de Banyuls"},"predicate":{"value":"CONTAINS_REMAINS_OF"},"object":{"value":"40"}},{"subject":{"value":"17"},"subjectLabel":{"value":"Inhumació al camí Ral a Llavaneres"},"predicate":{"value":"LOCATED_IN"},"object":{"value":"41"}},{"subject":{"value":"17"},"subjectLabel":{"value":"Inhumació al camí Ral a Llavaneres"},"predicate":{"value":"HAS_ASSESSMENT"},"object":{"value":"33"}},{"subject":{"value":"17"},"subjectLabel":{"value":"Inhumació al camí Ral a Llavaneres"},"predicate":{"value":"HAS_PRESERVATION_STATE"},"object":{"value":"34"}},{"subject":{"value":"17"},"subjectLabel":{"value":"Inhumació al camí Ral a Llavaneres"},"predicate":{"value":"PARTICIPANT_IN"},"object":{"value":"39"}},{"subject":{"value":"17"},"subjectLabel":{"value":"Inhumació al camí Ral a Llavaneres"},"predicate":{"value":"CONTAINS_REMAINS_OF"},"object":{"value":"40"}},{"subject":{"value":"18"},"subjectLabel":{"value":"Cal Corretger"},"predicate":{"value":"LOCATED_IN"},"object":{"value":"42"}},{"subject":{"value":"18"},"subjectLabel":{"value":"Cal Corretger"},"predicate":{"value":"HAS_ASSESSMENT"},"object":{"value":"24"}},{"subject":{"value":"18"},"subjectLabel":{"value":"Cal Corretger"},"predicate":{"value":"HAS_PRESERVATION_STATE"},"object":{"value":"25"}},{"subject":{"value":"18"},"subjectLabel":{"value":"Cal Corretger"},"predicate":{"value":"PARTICIPANT_IN"},"object":{"value":"31"}},{"subject":{"value":"18"},"subjectLabel":{"value":"Cal Corretger"},"predicate":{"value":"CONTAINS_REMAINS_OF"},"object":{"value":"43"}},{"subject":{"value":"19"},"subjectLabel":{"value":"Cementiri de Sant Hilari Sacalm"},"predicate":{"value":"LOCATED_IN"},"object":{"value":"45"}},{"subject":{"value":"19"},"subjectLabel":{"value":"Cementiri de Sant Hilari Sacalm"},"predicate":{"value":"HAS_ASSESSMENT"},"object":{"value":"24"}},{"subject":{"value":"19"},"subjectLabel":{"value":"Cementiri de Sant Hilari Sacalm"},"predicate":{"value":"HAS_PRESERVATION_STATE"},"object":{"value":"44"}},{"subject":{"value":"19"},"subjectLabel":{"value":"Cementiri de Sant Hilari Sacalm"},"predicate":{"value":"PARTICIPANT_IN"},"object":{"value":"47"}},{"subject":{"value":"19"},"subjectLabel":{"value":"Cementiri de Sant Hilari Sacalm"},"predicate":{"value":"PARTICIPANT_IN"},"object":{"value":"48"}},{"subject":{"value":"19"},"subjectLabel":{"value":"Cementiri de Sant Hilari Sacalm"},"predicate":{"value":"CONTAINS_REMAINS_OF"},"object":{"value":"32"}},{"subject":{"value":"19"},"subjectLabel":{"value":"Cementiri de Sant Hilari Sacalm"},"predicate":{"value":"CONTAINS_REMAINS_OF"},"object":{"value":"40"}},{"subject":{"value":"20"},"subjectLabel":{"value":"Cementiri d'Alpicat"},"predicate":{"value":"LOCATED_IN"},"object":{"value":"50"}},{"subject":{"value":"20"},"subjectLabel":{"value":"Cementiri d'Alpicat"},"predicate":{"value":"HAS_ASSESSMENT"},"object":{"value":"24"}},{"subject":{"value":"20"},"subjectLabel":{"value":"Cementiri d'Alpicat"},"predicate":{"value":"HAS_PRESERVATION_STATE"},"object":{"value":"49"}},{"subject":{"value":"20"},"subjectLabel":{"value":"Cementiri d'Alpicat"},"predicate":{"value":"PARTICIPANT_IN"},"object":{"value":"48"}},{"subject":{"value":"20"},"subjectLabel":{"value":"Cementiri d'Alpicat"},"predicate":{"value":"CONTAINS_REMAINS_OF"},"object":{"value":"32"}},{"subject":{"value":"20"},"subjectLabel":{"value":"Cementiri d'Alpicat"},"predicate":{"value":"CONTAINS_REMAINS_OF"},"object":{"value":"40"}},{"subject":{"value":"20"},"subjectLabel":{"value":"Cementiri d'Alpicat"},"predicate":{"value":"CONTAINS_REMAINS_OF"},"object":{"value":"43"}},{"subject":{"value":"21"},"subjectLabel":{"value":"Cementiri de Valls. Fossa dels hospitals"},"predicate":{"value":"LOCATED_IN"},"object":{"value":"53"}},{"subject":{"value":"21"},"subjectLabel":{"value":"Cementiri de Valls. Fossa dels hospitals"},"predicate":{"value":"HAS_ASSESSMENT"},"object":{"value":"24"}},{"subject":{"value":"21"},"subjectLabel":{"value":"Cementiri de Valls. Fossa dels hospitals"},"predicate":{"value":"HAS_PRESERVATION_STATE"},"object":{"value":"34"}},{"subject":{"value":"21"},"subjectLabel":{"value":"Cementiri de Valls. Fossa dels hospitals"},"predicate":{"value":"PARTICIPANT_IN"},"object":{"value":"47"}},{"subject":{"value":"21"},"subjectLabel":{"value":"Cementiri de Valls. Fossa dels hospitals"},"predicate":{"value":"PARTICIPANT_IN"},"object":{"value":"48"}},{"subject":{"value":"21"},"subjectLabel":{"value":"Cementiri de Valls. Fossa dels hospitals"},"predicate":{"value":"CONTAINS_REMAINS_OF"},"object":{"value":"40"}},{"subject":{"value":"21"},"subjectLabel":{"value":"Cementiri de Valls. Fossa dels hospitals"},"predicate":{"value":"CONTAINS_REMAINS_OF"},"object":{"value":"56"}},{"subject":{"value":"22"},"subjectLabel":{"value":"Cementiri de Manresa"},"predicate":{"value":"LOCATED_IN"},"object":{"value":"57"}},{"subject":{"value":"22"},"subjectLabel":{"value":"Cementiri de Manresa"},"predicate":{"value":"HAS_ASSESSMENT"},"object":{"value":"24"}},{"subject":{"value":"22"},"subjectLabel":{"value":"Cementiri de Manresa"},"predicate":{"value":"HAS_PRESERVATION_STATE"},"object":{"value":"44"}},{"subject":{"value":"22"},"subjectLabel":{"value":"Cementiri de Manresa"},"predicate":{"value":"PARTICIPANT_IN"},"object":{"value":"48"}},{"subject":{"value":"22"},"subjectLabel":{"value":"Cementiri de Manresa"},"predicate":{"value":"CONTAINS_REMAINS_OF"},"object":{"value":"40"}},{"subject":{"value":"23"},"subjectLabel":{"value":"Camí de les Torres"},"predicate":{"value":"LOCATED_IN"},"object":{"value":"59"}},{"subject":{"value":"23"},"subjectLabel":{"value":"Camí de les Torres"},"predicate":{"value":"HAS_ASSESSMENT"},"object":{"value":"24"}},{"subject":{"value":"23"},"subjectLabel":{"value":"Camí de les Torres"},"predicate":{"value":"HAS_PRESERVATION_STATE"},"object":{"value":"44"}},{"subject":{"value":"23"},"subjectLabel":{"value":"Camí de les Torres"},"predicate":{"value":"PARTICIPANT_IN"},"object":{"value":"38"}},{"subject":{"value":"23"},"subjectLabel":{"value":"Camí de les Torres"},"predicate":{"value":"CONTAINS_REMAINS_OF"},"object":{"value":"40"}},{"subject":{"value":"26"},"predicate":{"value":"LOCATED_IN"},"object":{"value":"27"}},{"subject":{"value":"27"},"predicate":{"value":"LOCATED_IN"},"object":{"value":"28"}},{"subject":{"value":"28"},"predicate":{"value":"LOCATED_IN"},"object":{"value":"29"}},{"subject":{"value":"29"},"predicate":{"value":"LOCATED_IN"},"object":{"value":"30"}},{"subject":{"value":"35"},"predicate":{"value":"LOCATED_IN"},"object":{"value":"36"}},{"subject":{"value":"36"},"predicate":{"value":"LOCATED_IN"},"object":{"value":"37"}},{"subject":{"value":"37"},"predicate":{"value":"LOCATED_IN"},"object":{"value":"29"}},{"subject":{"value":"41"},"predicate":{"value":"LOCATED_IN"},"object":{"value":"27"}},{"subject":{"value":"42"},"predicate":{"value":"LOCATED_IN"},"object":{"value":"27"}},{"subject":{"value":"45"},"predicate":{"value":"LOCATED_IN"},"object":{"value":"46"}},{"subject":{"value":"46"},"predicate":{"value":"LOCATED_IN"},"object":{"value":"37"}},{"subject":{"value":"50"},"predicate":{"value":"LOCATED_IN"},"object":{"value":"51"}},{"subject":{"value":"51"},"predicate":{"value":"LOCATED_IN"},"object":{"value":"52"}},{"subject":{"value":"52"},"predicate":{"value":"LOCATED_IN"},"object":{"value":"29"}},{"subject":{"value":"53"},"predicate":{"value":"LOCATED_IN"},"object":{"value":"54"}},{"subject":{"value":"54"},"predicate":{"value":"LOCATED_IN"},"object":{"value":"55"}},{"subject":{"value":"55"},"predicate":{"value":"LOCATED_IN"},"object":{"value":"29"}},{"subject":{"value":"57"},"predicate":{"value":"LOCATED_IN"},"object":{"value":"58"}},{"subject":{"value":"58"},"predicate":{"value":"LOCATED_IN"},"object":{"value":"28"}},{"subject":{"value":"59"},"predicate":{"value":"LOCATED_IN"},"object":{"value":"58"}}],"format":"json","execution_time":11.733999999705702,"source":"neo4j","query_type":"sparql"}%   
```
### 2. FILTER clauses: basic string and numeric comparisons

**String:** nodes whose label (name/title/text) contains a substring (case-insensitive).

```bash
curl -u 'ubxat:BLI-u24KH%36xM9gQ9PzX' \
  -X POST 'https://ubxat.peninsula.co/api/v1/sparql' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{
    "query": "MATCH (n) WHERE toLower(coalesce(n.name, n.title, n.text, \"\")) CONTAINS \"brigadista\" RETURN id(n) AS subject, labels(n) AS labels, coalesce(n.name, n.title, n.text) AS label LIMIT 50",
    "format": "json"
  }'
```

#### In SPARQL (string filter):
```sparql
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?subject ?label
WHERE {
  ?subject rdfs:label ?label .
  FILTER (CONTAINS(LCASE(STR(?label)), "brigadista"))
}
LIMIT 50
```

```bash
curl -u 'ubxat:BLI-u24KH%36xM9gQ9PzX' \
  -X POST 'https://ubxat.peninsula.co/api/v1/sparql' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{
    "query": "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> SELECT ?subject ?label WHERE { ?subject rdfs:label ?label . FILTER (CONTAINS(LCASE(STR(?label)), \"brigadista\")) } LIMIT 50",
    "format": "json"
  }'
```

##### Respuesta UBXAT:
```bash
[
  {
    "n": {
      "value": "0"
    },
    "nLabel": {
      "value": "Informació diversa sobre el brigadista Hans Kaltschmidt. [S.l. : s.n.], 2023."
    }
  },
  {
    "n": {
      "value": "1"
    },
    "nLabel": {
      "value": "BORRÀS DÒLERA, Mercè. Informació diversa sobre els brigadistes Pierre Odéon i Paula Feldestein. [S.l. : s.n.], 2024."
    }
  },
  {
    "n": {
      "value": "2"
    },
    "nLabel": {
      "value": "SCHOLTEN, Yvonne. \"In search of the first Dutch volunteer\". The Volunteer (5/2/2022)"
    }
  },
  {
    "n": {
      "value": "3"
    },
    "nLabel": {
      "value": "Российский государственный архив социально-политической истории (РГАСПИ) | Arxiu Estatal Rus d'Història Sociopolítica (RGASPI). Informació diversa sobre el brigadista Fritz Hilger. [Moscou : RGASPI], 2024."
    }
  },
  {
    "n": {
      "value": "4"
    },
    "nLabel": {
      "value": "Российский государственный архив социально-политической истории (РГАСПИ) | Arxiu Estatal Rus d'Història Sociopolítica (RGASPI). Informació diversa sobre el brigadista Sam Gibons. [Moscou : RGASPI], 2021."
    }
  },
  {
    "n": {
      "value": "5"
    },
    "nLabel": {
      "value": "LEWIS, Wendy. Informació diversa sobre el brigadista Sidney Shosteck. [S.l : s.n.], 2023"
    }
  },
  {
    "n": {
      "value": "6"
    },
    "nLabel": {
      "value": "ABACERIN, Georges"
    }
  },
  {
    "n": {
      "value": "7"
    },
    "nLabel": {
      "value": "ACER. Les Amis des Combattants en Espagne Républicaine. Brigadistes"
    }
  },
  {
    "n": {
      "value": "8"
    },
    "nLabel": {
      "value": "La Columna Uruguaya : historia de los uruguayos en la guerra Civil Española"
    }
  },
  {
    "n": {
      "value": "9"
    },
    "nLabel": {
      "value": "\"Muere la musa catalana de Hemingway en Por quién doblan las campanas\". La Vanguardia (4/6/2012)"
    }
  }
]
```

##### Respuesta servidor: 
```bash
curl -u 'ubxat:BLI-u24KH%36xM9gQ9PzX' \
  -X POST 'https://ubxat.peninsula.co/api/v1/sparql' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{
    "query": "MATCH (n) WHERE toLower(coalesce(n.name, n.title, n.text, \"\")) CONTAINS \"brigadista\" RETURN id(n) AS subject, labels(n) AS labels, coalesce(n.name, n.title, n.text) AS label LIMIT 50",
    "format": "json"
  }'
{"query":"MATCH (n) WHERE toLower(coalesce(n.name, n.title, n.text, \"\")) CONTAINS \"brigadista\" RETURN id(n) AS subject, labels(n) AS labels, coalesce(n.name, n.title, n.text) AS label LIMIT 50","results":[{"subject":0,"labels":["Publication"],"label":"Informació diversa sobre el brigadista Hans Kaltschmidt. [S.l. : s.n.], 2023."},{"subject":3,"labels":["Publication"],"label":"Российский государственный архив социально-политической истории (РГАСПИ) | Arxiu Estatal Rus d'Història Sociopolítica (RGASPI). Informació diversa sobre el brigadista Fritz Hilger. [Moscou : RGASPI], 2024."},{"subject":4,"labels":["Publication"],"label":"Российский государственный архив социально-политической истории (РГАСПИ) | Arxiu Estatal Rus d'Història Sociopolítica (RGASPI). Informació diversa sobre el brigadista Sam Gibons. [Moscou : RGASPI], 2021."},{"subject":5,"labels":["Publication"],"label":"LEWIS, Wendy. Informació diversa sobre el brigadista Sidney Shosteck. [S.l : s.n.], 2023"},{"subject":11,"labels":["Person"],"label":"brigadista Hans Kaltschmidt"},{"subject":12,"labels":["Person"],"label":"brigadista Fritz Hilger"},{"subject":13,"labels":["Person"],"label":"brigadista Sam Gibons"},{"subject":14,"labels":["Person"],"label":"brigadista Sidney Shosteck"}],"format":"json","execution_time":0.7579999999143183,"source":"neo4j","query_type":"cypher"}%               
```

**Numeric:** e.g. only nodes that have a numeric property above a threshold (if your graph has such properties).

```bash
curl -u 'ubxat:BLI-u24KH%36xM9gQ9PzX' \
  -X POST 'https://ubxat.peninsula.co/api/v1/sparql' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{
    "query": "MATCH (n) WHERE id(n) >= 0 AND id(n) < 100 RETURN id(n) AS subject, labels(n) AS labels LIMIT 50",
    "format": "json"
  }'
```

#### In SPARQL (numeric-style filter, example year range):
```sparql
PREFIX ex: <http://example.org/herstory#>

SELECT ?subject ?year
WHERE {
  ?subject ex:year ?year .
  FILTER (?year >= 0 && ?year < 100)
}
LIMIT 50
```

```bash
curl -u 'ubxat:BLI-u24KH%36xM9gQ9PzX' \
  -X POST 'https://ubxat.peninsula.co/api/v1/sparql' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{
    "query": "PREFIX ex: <http://example.org/herstory#> SELECT ?subject ?year WHERE { ?subject ex:year ?year . FILTER (?year >= 0 && ?year < 100) } LIMIT 50",
    "format": "json"
  }'
```

##### Respuesta UBXAT: 
```bash
[
  {
    "n": {
      "value": "0"
    },
    "nLabel": {
      "value": "Informació diversa sobre el brigadista Hans Kaltschmidt. [S.l. : s.n.], 2023."
    }
  },
  {
    "n": {
      "value": "1"
    },
    "nLabel": {
      "value": "BORRÀS DÒLERA, Mercè. Informació diversa sobre els brigadistes Pierre Odéon i Paula Feldestein. [S.l. : s.n.], 2024."
    }
  },
  {
    "n": {
      "value": "2"
    },
    "nLabel": {
      "value": "SCHOLTEN, Yvonne. \"In search of the first Dutch volunteer\". The Volunteer (5/2/2022)"
    }
  },
  {
    "n": {
      "value": "3"
    },
    "nLabel": {
      "value": "Российский государственный архив социально-политической истории (РГАСПИ) | Arxiu Estatal Rus d'Història Sociopolítica (RGASPI). Informació diversa sobre el brigadista Fritz Hilger. [Moscou : RGASPI], 2024."
    }
  },
  {
    "n": {
      "value": "4"
    },
    "nLabel": {
      "value": "Российский государственный архив социально-политической истории (РГАСПИ) | Arxiu Estatal Rus d'Història Sociopolítica (RGASPI). Informació diversa sobre el brigadista Sam Gibons. [Moscou : RGASPI], 2021."
    }
  },
  {
    "n": {
      "value": "5"
    },
    "nLabel": {
      "value": "LEWIS, Wendy. Informació diversa sobre el brigadista Sidney Shosteck. [S.l : s.n.], 2023"
    }
  },
  {
    "n": {
      "value": "6"
    },
    "nLabel": {
      "value": "ABACERIN, Georges"
    }
  },
  {
    "n": {
      "value": "7"
    },
    "nLabel": {
      "value": "ACER. Les Amis des Combattants en Espagne Républicaine. Brigadistes"
    }
  },
  {
    "n": {
      "value": "8"
    },
    "nLabel": {
      "value": "La Columna Uruguaya : historia de los uruguayos en la guerra Civil Española"
    }
  },
  {
    "n": {
      "value": "9"
    },
    "nLabel": {
      "value": "\"Muere la musa catalana de Hemingway en Por quién doblan las campanas\". La Vanguardia (4/6/2012)"
    }
  }
]
```

##### Respuesta servidor: 
```bash
curl -u 'ubxat:BLI-u24KH%36xM9gQ9PzX' \
  -X POST 'https://ubxat.peninsula.co/api/v1/sparql' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{
    "query": "MATCH (n) WHERE id(n) >= 0 AND id(n) < 100 RETURN id(n) AS subject, labels(n) AS labels LIMIT 50",
    "format": "json"
  }'
{"query":"MATCH (n) WHERE id(n) >= 0 AND id(n) < 100 RETURN id(n) AS subject, labels(n) AS labels LIMIT 50","results":[{"subject":0,"labels":["Publication"]},{"subject":1,"labels":["Publication"]},{"subject":2,"labels":["Publication"]},{"subject":3,"labels":["Publication"]},{"subject":4,"labels":["Publication"]},{"subject":5,"labels":["Publication"]},{"subject":6,"labels":["Publication"]},{"subject":7,"labels":["Publication"]},{"subject":8,"labels":["Publication"]},{"subject":9,"labels":["Publication"]},{"subject":10,"labels":["Publication"]},{"subject":11,"labels":["Person"]},{"subject":12,"labels":["Person"]},{"subject":13,"labels":["Person"]},{"subject":14,"labels":["Person"]},{"subject":15,"labels":["MassGrave"]},{"subject":16,"labels":["MassGrave"]},{"subject":17,"labels":["MassGrave"]},{"subject":18,"labels":["MassGrave"]},{"subject":19,"labels":["MassGrave"]},{"subject":20,"labels":["MassGrave"]},{"subject":21,"labels":["MassGrave"]},{"subject":22,"labels":["MassGrave"]},{"subject":23,"labels":["MassGrave"]},{"subject":24,"labels":["Assessment"]},{"subject":25,"labels":["PreservationState"]},{"subject":26,"labels":["Municipality"]},{"subject":27,"labels":["Comarca"]},{"subject":28,"labels":["Province"]},{"subject":29,"labels":["AutonomousCommunity"]},{"subject":30,"labels":["Country"]},{"subject":31,"labels":["DeathContext"]},{"subject":32,"labels":["ParticipantType"]},{"subject":33,"labels":["Assessment"]},{"subject":34,"labels":["PreservationState"]},{"subject":35,"labels":["Municipality"]},{"subject":36,"labels":["Comarca"]},{"subject":37,"labels":["Province"]},{"subject":38,"labels":["DeathContext"]},{"subject":39,"labels":["DeathContext"]},{"subject":40,"labels":["ParticipantType"]},{"subject":41,"labels":["Municipality"]},{"subject":42,"labels":["Municipality"]},{"subject":43,"labels":["ParticipantType"]},{"subject":44,"labels":["PreservationState"]},{"subject":45,"labels":["Municipality"]},{"subject":46,"labels":["Comarca"]},{"subject":47,"labels":["DeathContext"]},{"subject":48,"labels":["DeathContext"]},{"subject":49,"labels":["PreservationState"]}],"format":"json","execution_time":0.7340000001713634,"source":"neo4j","query_type":"cypher"}%                  
```
### 3. LIMIT / OFFSET: result pagination

Cypher uses `SKIP` and `LIMIT` (no built-in OFFSET; use SKIP n for page size n).

```bash
curl -u 'ubxat:BLI-u24KH%36xM9gQ9PzX' \
  -X POST 'https://ubxat.peninsula.co/api/v1/sparql' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{
    "query": "MATCH (subject)-[r]->(object) RETURN id(subject) AS subject, type(r) AS predicate, id(object) AS object ORDER BY subject, predicate, object SKIP 0 LIMIT 25",
    "format": "json"
  }'
```

#### In SPARQL (pagination):
```sparql
SELECT ?subject ?predicate ?object
WHERE {
  ?subject ?predicate ?object .
}
ORDER BY ?subject ?predicate ?object
LIMIT 25
OFFSET 0
```

```bash
curl -u 'ubxat:BLI-u24KH%36xM9gQ9PzX' \
  -X POST 'https://ubxat.peninsula.co/api/v1/sparql' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{
    "query": "SELECT ?subject ?predicate ?object WHERE { ?subject ?predicate ?object . } ORDER BY ?subject ?predicate ?object LIMIT 25 OFFSET 0",
    "format": "json"
  }'
```

Second page (next 25): change to `SKIP 25 LIMIT 25`.

##### Respuesta UBXAT: 
```bash
[
  {
    "n": {
      "value": "0"
    },
    "nLabel": {
      "value": "Informació diversa sobre el brigadista Hans Kaltschmidt. [S.l. : s.n.], 2023."
    }
  },
  {
    "n": {
      "value": "1"
    },
    "nLabel": {
      "value": "BORRÀS DÒLERA, Mercè. Informació diversa sobre els brigadistes Pierre Odéon i Paula Feldestein. [S.l. : s.n.], 2024."
    }
  },
  {
    "n": {
      "value": "2"
    },
    "nLabel": {
      "value": "SCHOLTEN, Yvonne. \"In search of the first Dutch volunteer\". The Volunteer (5/2/2022)"
    }
  },
  {
    "n": {
      "value": "3"
    },
    "nLabel": {
      "value": "Российский государственный архив социально-политической истории (РГАСПИ) | Arxiu Estatal Rus d'Història Sociopolítica (RGASPI). Informació diversa sobre el brigadista Fritz Hilger. [Moscou : RGASPI], 2024."
    }
  },
  {
    "n": {
      "value": "4"
    },
    "nLabel": {
      "value": "Российский государственный архив социально-политической истории (РГАСПИ) | Arxiu Estatal Rus d'Història Sociopolítica (RGASPI). Informació diversa sobre el brigadista Sam Gibons. [Moscou : RGASPI], 2021."
    }
  },
  {
    "n": {
      "value": "5"
    },
    "nLabel": {
      "value": "LEWIS, Wendy. Informació diversa sobre el brigadista Sidney Shosteck. [S.l : s.n.], 2023"
    }
  },
  {
    "n": {
      "value": "6"
    },
    "nLabel": {
      "value": "ABACERIN, Georges"
    }
  },
  {
    "n": {
      "value": "7"
    },
    "nLabel": {
      "value": "ACER. Les Amis des Combattants en Espagne Républicaine. Brigadistes"
    }
  },
  {
    "n": {
      "value": "8"
    },
    "nLabel": {
      "value": "La Columna Uruguaya : historia de los uruguayos en la guerra Civil Española"
    }
  },
  {
    "n": {
      "value": "9"
    },
    "nLabel": {
      "value": "\"Muere la musa catalana de Hemingway en Por quién doblan las campanas\". La Vanguardia (4/6/2012)"
    }
  }
]
```

##### Respuesta servidor: 
```bash
curl -u 'ubxat:BLI-u24KH%36xM9gQ9PzX' \
  -X POST 'https://ubxat.peninsula.co/api/v1/sparql' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{
    "query": "MATCH (subject)-[r]->(object) RETURN id(subject) AS subject, type(r) AS predicate, id(object) AS object ORDER BY subject, predicate, object SKIP 0 LIMIT 25",
    "format": "json"
  }'
{"query":"MATCH (subject)-[r]->(object) RETURN id(subject) AS subject, type(r) AS predicate, id(object) AS object ORDER BY subject, predicate, object SKIP 0 LIMIT 25","results":[{"subject":0,"predicate":"MAIN_SUBJECT","object":11},{"subject":3,"predicate":"MAIN_SUBJECT","object":12},{"subject":4,"predicate":"MAIN_SUBJECT","object":13},{"subject":5,"predicate":"MAIN_SUBJECT","object":14},{"subject":15,"predicate":"CONTAINS_REMAINS_OF","object":32},{"subject":15,"predicate":"HAS_ASSESSMENT","object":24},{"subject":15,"predicate":"HAS_PRESERVATION_STATE","object":25},{"subject":15,"predicate":"LOCATED_IN","object":26},{"subject":15,"predicate":"PARTICIPANT_IN","object":31},{"subject":16,"predicate":"CONTAINS_REMAINS_OF","object":40},{"subject":16,"predicate":"HAS_ASSESSMENT","object":33},{"subject":16,"predicate":"HAS_PRESERVATION_STATE","object":34},{"subject":16,"predicate":"LOCATED_IN","object":35},{"subject":16,"predicate":"PARTICIPANT_IN","object":38},{"subject":16,"predicate":"PARTICIPANT_IN","object":39},{"subject":17,"predicate":"CONTAINS_REMAINS_OF","object":40},{"subject":17,"predicate":"HAS_ASSESSMENT","object":33},{"subject":17,"predicate":"HAS_PRESERVATION_STATE","object":34},{"subject":17,"predicate":"LOCATED_IN","object":41},{"subject":17,"predicate":"PARTICIPANT_IN","object":39},{"subject":18,"predicate":"CONTAINS_REMAINS_OF","object":43},{"subject":18,"predicate":"HAS_ASSESSMENT","object":24},{"subject":18,"predicate":"HAS_PRESERVATION_STATE","object":25},{"subject":18,"predicate":"LOCATED_IN","object":42},{"subject":18,"predicate":"PARTICIPANT_IN","object":31}],"format":"json","execution_time":0.75,"source":"neo4j","query_type":"cypher"}%          
```

---

## ASK queries

### 1. Boolean: check for pattern existence

Returns one row with a boolean: does the pattern exist?

```bash
curl -u 'ubxat:BLI-u24KH%36xM9gQ9PzX' \
  -X POST 'https://ubxat.peninsula.co/api/v1/sparql' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{
    "query": "MATCH (subject)-[r]->(object) WITH subject, r, object LIMIT 1 RETURN count(*) > 0 AS result",
    "format": "json"
  }'
```

#### In SPARQL:
```sparql
ASK {
  ?subject ?predicate ?object .
}
```

```bash
curl -u 'ubxat:BLI-u24KH%36xM9gQ9PzX' \
  -X POST 'https://ubxat.peninsula.co/api/v1/sparql' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{
    "query": "ASK { ?subject ?predicate ?object . }",
    "format": "json"
  }'
```

##### Respuesta UBXAT: 
```bash
[
  {
    "count": {
      "value": "60"
    }
  }
]  
```

##### Respuesta servidor: 
```bash
curl -u 'ubxat:BLI-u24KH%36xM9gQ9PzX' \
  -X POST 'https://ubxat.peninsula.co/api/v1/sparql' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{
    "query": "MATCH (subject)-[r]->(object) WITH subject, r, object LIMIT 1 RETURN count(*) > 0 AS result",
    "format": "json"
  }'
{"query":"MATCH (subject)-[r]->(object) WITH subject, r, object LIMIT 1 RETURN count(*) > 0 AS result","results":[{"result":true}],"format":"json","execution_time":0.13299999991431832,"source":"neo4j","query_type":"cypher"}%
```
### 2. Basic ASK: e.g. “exists any MassGrave?”

```bash
curl -u 'ubxat:BLI-u24KH%36xM9gQ9PzX' \
  -X POST 'https://ubxat.peninsula.co/api/v1/sparql' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{
    "query": "MATCH (n:MassGrave) WITH n LIMIT 1 RETURN count(*) > 0 AS result",
    "format": "json"
  }'
```

#### In SPARQL:
```sparql
PREFIX ex: <http://example.org/herstory#>

ASK {
  ?massGrave a ex:MassGrave .
}
```

```bash
curl -u 'ubxat:BLI-u24KH%36xM9gQ9PzX' \
  -X POST 'https://ubxat.peninsula.co/api/v1/sparql' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{
    "query": "PREFIX ex: <http://example.org/herstory#> ASK { ?massGrave a ex:MassGrave . }",
    "format": "json"
  }'
```

##### Respuesta UBXAT: 
```bash
[
  {
    "count": {
      "value": "60"
    }
  }
]
```

##### Respuesta servidor: 
```bash
curl -u 'ubxat:BLI-u24KH%36xM9gQ9PzX' \
  -X POST 'https://ubxat.peninsula.co/api/v1/sparql' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{
    "query": "MATCH (n:MassGrave) WITH n LIMIT 1 RETURN count(*) > 0 AS result",
    "format": "json"
  }'
{"query":"MATCH (n:MassGrave) WITH n LIMIT 1 RETURN count(*) > 0 AS result","results":[{"result":true}],"format":"json","execution_time":0.7330000000074506,"source":"neo4j","query_type":"cypher"}%          
```
---

## COUNT queries (extended)

### 1. Custom COUNT syntax: COUNT(?variable)

Cypher equivalent: `count(n)` or `count(*)` for the bound variable / pattern.

**Count all nodes:**

```bash
curl -u 'ubxat:BLI-u24KH%36xM9gQ9PzX' \
  -X POST 'https://ubxat.peninsula.co/api/v1/sparql' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{
    "query": "MATCH (n) RETURN count(n) AS count",
    "format": "json"
  }'
```

#### In SPARQL:
```sparql
SELECT (COUNT(?subject) AS ?count)
WHERE {
  ?subject ?predicate ?object .
}
```

```bash
curl -u 'ubxat:BLI-u24KH%36xM9gQ9PzX' \
  -X POST 'https://ubxat.peninsula.co/api/v1/sparql' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{
    "query": "SELECT (COUNT(?subject) AS ?count) WHERE { ?subject ?predicate ?object . }",
    "format": "json"
  }'
```

##### Respuesta UBXAT: 
```bash
[
  {
    "count": {
      "value": "60"
    }
  }
]
```

##### Respuesta servidor: 
```bash
curl -u 'ubxat:BLI-u24KH%36xM9gQ9PzX' \
  -X POST 'https://ubxat.peninsula.co/api/v1/sparql' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{
    "query": "MATCH (n) RETURN count(n) AS count",
    "format": "json"
  }'
{"query":"MATCH (n) RETURN count(n) AS count","results":[{"count":60}],"format":"json","execution_time":0.12600000016391277,"source":"neo4j","query_type":"cypher"}%
```

**Count relationships (triples):**

```bash
curl -u 'ubxat:BLI-u24KH%36xM9gQ9PzX' \
  -X POST 'https://ubxat.peninsula.co/api/v1/sparql' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{
    "query": "MATCH ()-[r]->() RETURN count(r) AS count",
    "format": "json"
  }'
```

#### In SPARQL:
```sparql
SELECT (COUNT(*) AS ?count)
WHERE {
  ?subject ?predicate ?object .
}
```

```bash
curl -u 'ubxat:BLI-u24KH%36xM9gQ9PzX' \
  -X POST 'https://ubxat.peninsula.co/api/v1/sparql' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{
    "query": "SELECT (COUNT(*) AS ?count) WHERE { ?subject ?predicate ?object . }",
    "format": "json"
  }'
```

##### Respuesta UBXAT: 
```bash
curl -u 'ubxat:BLI-u24KH%36xM9gQ9PzX' \
  -X POST 'https://ubxat.peninsula.co/api/v1/sparql' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{
    "query": "MATCH ()-[r]->() RETURN count(r) AS count",
    "format": "json"
  }'
{"query":"MATCH ()-[r]->() RETURN count(r) AS count","results":[{"count":76}],"format":"json","execution_time":0.12700000032782555,"source":"neo4j","query_type":"cypher"}%
```

##### Respuesta servidor: 
```bash
curl -u 'ubxat:BLI-u24KH%36xM9gQ9PzX' \
  -X POST 'https://ubxat.peninsula.co/api/v1/sparql' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{
    "query": "MATCH ()-[r]->() RETURN count(r) AS count",
    "format": "json"
  }'
{"query":"MATCH ()-[r]->() RETURN count(r) AS count","results":[{"count":76}],"format":"json","execution_time":0.12700000032782555,"source":"neo4j","query_type":"cypher"}%

```

## CONSTRUCT

Return a graph-shaped payload (equivalent to SPARQL CONSTRUCT): nodes + relationships as collections.

```bash
curl -u 'ubxat:BLI-u24KH%36xM9gQ9PzX' \
  -X POST 'https://ubxat.peninsula.co/api/v1/sparql' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{
    "query": "CALL { MATCH (n) RETURN collect({ id: id(n), labels: labels(n), props: properties(n) }) AS nodes } CALL { MATCH (source)-[r]->(target) RETURN collect({ sourceId: id(source), targetId: id(target), type: type(r), props: properties(r) }) AS relationships } RETURN nodes, relationships",
    "format": "json"
  }'
```

##### Respuesta UBXAT
```bash
[
  {
    "n": {
      "value": "0"
    },
    "nLabel": {
      "value": "Informació diversa sobre el brigadista Hans Kaltschmidt. [S.l. : s.n.], 2023."
    }
  },
  {
    "n": {
      "value": "1"
    },
    "nLabel": {
      "value": "BORRÀS DÒLERA, Mercè. Informació diversa sobre els brigadistes Pierre Odéon i Paula Feldestein. [S.l. : s.n.], 2024."
    }
  },
  {
    "n": {
      "value": "2"
    },
    "nLabel": {
      "value": "SCHOLTEN, Yvonne. \"In search of the first Dutch volunteer\". The Volunteer (5/2/2022)"
    }
  },
  {
    "n": {
      "value": "3"
    },
    "nLabel": {
      "value": "Российский государственный архив социально-политической истории (РГАСПИ) | Arxiu Estatal Rus d'Història Sociopolítica (RGASPI). Informació diversa sobre el brigadista Fritz Hilger. [Moscou : RGASPI], 2024."
    }
  },
  {
    "n": {
      "value": "4"
    },
    "nLabel": {
      "value": "Российский государственный архив социально-политической истории (РГАСПИ) | Arxiu Estatal Rus d'Història Sociopolítica (RGASPI). Informació diversa sobre el brigadista Sam Gibons. [Moscou : RGASPI], 2021."
    }
  },
  {
    "n": {
      "value": "5"
    },
    "nLabel": {
      "value": "LEWIS, Wendy. Informació diversa sobre el brigadista Sidney Shosteck. [S.l : s.n.], 2023"
    }
  },
  {
    "n": {
      "value": "6"
    },
    "nLabel": {
      "value": "ABACERIN, Georges"
    }
  },
  {
    "n": {
      "value": "7"
    },
    "nLabel": {
      "value": "ACER. Les Amis des Combattants en Espagne Républicaine. Brigadistes"
    }
  },
  {
    "n": {
      "value": "8"
    },
    "nLabel": {
      "value": "La Columna Uruguaya : historia de los uruguayos en la guerra Civil Española"
    }
  },
  {
    "n": {
      "value": "9"
    },
    "nLabel": {
      "value": "\"Muere la musa catalana de Hemingway en Por quién doblan las campanas\". La Vanguardia (4/6/2012)"
    }
  }
]
```

##### Respuesta Servidor (API)
```bash
curl -u 'ubxat:BLI-u24KH%36xM9gQ9PzX' \
  -X POST 'https://ubxat.peninsula.co/api/v1/sparql' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{
    "query": "CALL { MATCH (n) RETURN collect({ id: id(n), labels: labels(n), props: properties(n) }) AS nodes } CALL { MATCH (source)-[r]->(target) RETURN collect({ sourceId: id(source), targetId: id(target), type: type(r), props: properties(r) }) AS relationships } RETURN nodes, relationships",
    "format": "json"
  }'
{"query":"CALL { MATCH (n) RETURN collect({ id: id(n), labels: labels(n), props: properties(n) }) AS nodes } CALL { MATCH (source)-[r]->(target) RETURN collect({ sourceId: id(source), targetId: id(target), type: type(r), props: properties(r) }) AS relationships } RETURN nodes, relationships","results":[{"n":{"value":"0"},"nLabel":{"value":"Informació diversa sobre el brigadista Hans Kaltschmidt. [S.l. : s.n.], 2023."}},{"n":{"value":"1"},"nLabel":{"value":"BORRÀS DÒLERA, Mercè. Informació diversa sobre els brigadistes Pierre Odéon i Paula Feldestein. [S.l. : s.n.], 2024."}},{"n":{"value":"2"},"nLabel":{"value":"SCHOLTEN, Yvonne. \"In search of the first Dutch volunteer\". The Volunteer (5/2/2022)"}},{"n":{"value":"3"},"nLabel":{"value":"Российский государственный архив социально-политической истории (РГАСПИ) | Arxiu Estatal Rus d'Història Sociopolítica (RGASPI). Informació diversa sobre el brigadista Fritz Hilger. [Moscou : RGASPI], 2024."}},{"n":{"value":"4"},"nLabel":{"value":"Российский государственный архив социально-политической истории (РГАСПИ) | Arxiu Estatal Rus d'Història Sociopolítica (RGASPI). Informació diversa sobre el brigadista Sam Gibons. [Moscou : RGASPI], 2021."}},{"n":{"value":"5"},"nLabel":{"value":"LEWIS, Wendy. Informació diversa sobre el brigadista Sidney Shosteck. [S.l : s.n.], 2023"}},{"n":{"value":"6"},"nLabel":{"value":"ABACERIN, Georges"}},{"n":{"value":"7"},"nLabel":{"value":"ACER. Les Amis des Combattants en Espagne Républicaine. Brigadistes"}},{"n":{"value":"8"},"nLabel":{"value":"La Columna Uruguaya : historia de los uruguayos en la guerra Civil Española"}},{"n":{"value":"9"},"nLabel":{"value":"\"Muere la musa catalana de Hemingway en Por quién doblan las campanas\". La Vanguardia (4/6/2012)"}}],"format":"json","execution_time":0.7289999998174608,"source":"neo4j","query_type":"sparql"}%  
```

## DESCRIBE

Describe one node by id: its properties and outgoing/incoming relationships (and neighbour ids).

```bash
curl -u 'ubxat:BLI-u24KH%36xM9gQ9PzX' \
  -X POST 'https://ubxat.peninsula.co/api/v1/sparql' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{
    "query": "MATCH (n) WHERE id(n) = 0 OPTIONAL MATCH (n)-[r]->(m) RETURN id(n) AS id, labels(n) AS labels, properties(n) AS props, collect({ type: type(r), targetId: id(m) }) AS outRels",
    "format": "json"
  }'
```

##### Respuesta UBXAT
```bash
[
  {
    "n": {
      "value": "0"
    },
    "nLabel": {
      "value": "Informació diversa sobre el brigadista Hans Kaltschmidt. [S.l. : s.n.], 2023."
    }
  },
  {
    "n": {
      "value": "1"
    },
    "nLabel": {
      "value": "BORRÀS DÒLERA, Mercè. Informació diversa sobre els brigadistes Pierre Odéon i Paula Feldestein. [S.l. : s.n.], 2024."
    }
  },
  {
    "n": {
      "value": "2"
    },
    "nLabel": {
      "value": "SCHOLTEN, Yvonne. \"In search of the first Dutch volunteer\". The Volunteer (5/2/2022)"
    }
  },
  {
    "n": {
      "value": "3"
    },
    "nLabel": {
      "value": "Российский государственный архив социально-политической истории (РГАСПИ) | Arxiu Estatal Rus d'Història Sociopolítica (RGASPI). Informació diversa sobre el brigadista Fritz Hilger. [Moscou : RGASPI], 2024."
    }
  },
  {
    "n": {
      "value": "4"
    },
    "nLabel": {
      "value": "Российский государственный архив социально-политической истории (РГАСПИ) | Arxiu Estatal Rus d'Història Sociopolítica (RGASPI). Informació diversa sobre el brigadista Sam Gibons. [Moscou : RGASPI], 2021."
    }
  },
  {
    "n": {
      "value": "5"
    },
    "nLabel": {
      "value": "LEWIS, Wendy. Informació diversa sobre el brigadista Sidney Shosteck. [S.l : s.n.], 2023"
    }
  },
  {
    "n": {
      "value": "6"
    },
    "nLabel": {
      "value": "ABACERIN, Georges"
    }
  },
  {
    "n": {
      "value": "7"
    },
    "nLabel": {
      "value": "ACER. Les Amis des Combattants en Espagne Républicaine. Brigadistes"
    }
  },
  {
    "n": {
      "value": "8"
    },
    "nLabel": {
      "value": "La Columna Uruguaya : historia de los uruguayos en la guerra Civil Española"
    }
  },
  {
    "n": {
      "value": "9"
    },
    "nLabel": {
      "value": "\"Muere la musa catalana de Hemingway en Por quién doblan las campanas\". La Vanguardia (4/6/2012)"
    }
  }
]
```

##### Respuesta Servidor (API)
```bash
curl -u 'ubxat:BLI-u24KH%36xM9gQ9PzX' \
  -X POST 'https://ubxat.peninsula.co/api/v1/sparql' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{
    "query": "MATCH (n) WHERE id(n) = 0 OPTIONAL MATCH (n)-[r]->(m) RETURN id(n) AS id, labels(n) AS labels, properties(n) AS props, collect({ type: type(r), targetId: id(m) }) AS outRels",
    "format": "json"
  }'
{"query":"MATCH (n) WHERE id(n) = 0 OPTIONAL MATCH (n)-[r]->(m) RETURN id(n) AS id, labels(n) AS labels, properties(n) AS props, collect({ type: type(r), targetId: id(m) }) AS outRels","results":[{"id":0,"labels":["Publication"],"props":["described_at_url","record_creator","instance_of","last_update","inception","title","catalog_code"],"outRels":[{"targetId":11,"type":"MAIN_SUBJECT"}]}],"format":"json","execution_time":0.15299999993294477,"source":"neo4j","query_type":"cypher"}%   
```
## FILTER

Restrict by string (e.g. label contains "brigadista") or by numeric range (e.g. id in range).

```bash
curl -u 'ubxat:BLI-u24KH%36xM9gQ9PzX' \
  -X POST 'https://ubxat.peninsula.co/api/v1/sparql' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{
    "query": "MATCH (n) WHERE toLower(coalesce(n.name, n.title, n.text, \"\")) CONTAINS \"brigadista\" RETURN id(n) AS subject, labels(n) AS labels, coalesce(n.name, n.title, n.text) AS label LIMIT 50",
    "format": "json"
  }'
```

##### Respuesta UBXAT
```bash
[
  {
    "n": {
      "value": "0"
    },
    "nLabel": {
      "value": "Informació diversa sobre el brigadista Hans Kaltschmidt. [S.l. : s.n.], 2023."
    }
  },
  {
    "n": {
      "value": "1"
    },
    "nLabel": {
      "value": "BORRÀS DÒLERA, Mercè. Informació diversa sobre els brigadistes Pierre Odéon i Paula Feldestein. [S.l. : s.n.], 2024."
    }
  },
  {
    "n": {
      "value": "2"
    },
    "nLabel": {
      "value": "SCHOLTEN, Yvonne. \"In search of the first Dutch volunteer\". The Volunteer (5/2/2022)"
    }
  },
  {
    "n": {
      "value": "3"
    },
    "nLabel": {
      "value": "Российский государственный архив социально-политической истории (РГАСПИ) | Arxiu Estatal Rus d'Història Sociopolítica (RGASPI). Informació diversa sobre el brigadista Fritz Hilger. [Moscou : RGASPI], 2024."
    }
  },
  {
    "n": {
      "value": "4"
    },
    "nLabel": {
      "value": "Российский государственный архив социально-политической истории (РГАСПИ) | Arxiu Estatal Rus d'Història Sociopolítica (RGASPI). Informació diversa sobre el brigadista Sam Gibons. [Moscou : RGASPI], 2021."
    }
  },
  {
    "n": {
      "value": "5"
    },
    "nLabel": {
      "value": "LEWIS, Wendy. Informació diversa sobre el brigadista Sidney Shosteck. [S.l : s.n.], 2023"
    }
  },
  {
    "n": {
      "value": "6"
    },
    "nLabel": {
      "value": "ABACERIN, Georges"
    }
  },
  {
    "n": {
      "value": "7"
    },
    "nLabel": {
      "value": "ACER. Les Amis des Combattants en Espagne Républicaine. Brigadistes"
    }
  },
  {
    "n": {
      "value": "8"
    },
    "nLabel": {
      "value": "La Columna Uruguaya : historia de los uruguayos en la guerra Civil Española"
    }
  },
  {
    "n": {
      "value": "9"
    },
    "nLabel": {
      "value": "\"Muere la musa catalana de Hemingway en Por quién doblan las campanas\". La Vanguardia (4/6/2012)"
    }
  }
]
```

##### Respuesta Servidor (API)
```bash
curl -u 'ubxat:BLI-u24KH%36xM9gQ9PzX' \
  -X POST 'https://ubxat.peninsula.co/api/v1/sparql' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{
    "query": "MATCH (n) WHERE toLower(coalesce(n.name, n.title, n.text, \"\")) CONTAINS \"brigadista\" RETURN id(n) AS subject, labels(n) AS labels, coalesce(n.name, n.title, n.text) AS label LIMIT 50",
    "format": "json"
  }'
{"query":"MATCH (n) WHERE toLower(coalesce(n.name, n.title, n.text, \"\")) CONTAINS \"brigadista\" RETURN id(n) AS subject, labels(n) AS labels, coalesce(n.name, n.title, n.text) AS label LIMIT 50","results":[{"subject":0,"labels":["Publication"],"label":"Informació diversa sobre el brigadista Hans Kaltschmidt. [S.l. : s.n.], 2023."},{"subject":3,"labels":["Publication"],"label":"Российский государственный архив социально-политической истории (РГАСПИ) | Arxiu Estatal Rus d'Història Sociopolítica (RGASPI). Informació diversa sobre el brigadista Fritz Hilger. [Moscou : RGASPI], 2024."},{"subject":4,"labels":["Publication"],"label":"Российский государственный архив социально-политической истории (РГАСПИ) | Arxiu Estatal Rus d'Història Sociopolítica (RGASPI). Informació diversa sobre el brigadista Sam Gibons. [Moscou : RGASPI], 2021."},{"subject":5,"labels":["Publication"],"label":"LEWIS, Wendy. Informació diversa sobre el brigadista Sidney Shosteck. [S.l : s.n.], 2023"},{"subject":11,"labels":["Person"],"label":"brigadista Hans Kaltschmidt"},{"subject":12,"labels":["Person"],"label":"brigadista Fritz Hilger"},{"subject":13,"labels":["Person"],"label":"brigadista Sam Gibons"},{"subject":14,"labels":["Person"],"label":"brigadista Sidney Shosteck"}],"format":"json","execution_time":0.12299999967217445,"source":"neo4j","query_type":"cypher"}%  
```
## ORDER BY

Sort results (e.g. by subject, then predicate, then object) and paginate with SKIP/LIMIT.

```bash
curl -u 'ubxat:BLI-u24KH%36xM9gQ9PzX' \
  -X POST 'https://ubxat.peninsula.co/api/v1/sparql' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{
    "query": "MATCH (subject)-[r]->(object) RETURN id(subject) AS subject, type(r) AS predicate, id(object) AS object ORDER BY subject, predicate, object SKIP 0 LIMIT 25",
    "format": "json"
  }'
```

##### Respuesta UBXAT
```bash
[
  {
    "n": {
      "value": "0"
    },
    "nLabel": {
      "value": "Informació diversa sobre el brigadista Hans Kaltschmidt. [S.l. : s.n.], 2023."
    }
  },
  {
    "n": {
      "value": "1"
    },
    "nLabel": {
      "value": "BORRÀS DÒLERA, Mercè. Informació diversa sobre els brigadistes Pierre Odéon i Paula Feldestein. [S.l. : s.n.], 2024."
    }
  },
  {
    "n": {
      "value": "2"
    },
    "nLabel": {
      "value": "SCHOLTEN, Yvonne. \"In search of the first Dutch volunteer\". The Volunteer (5/2/2022)"
    }
  },
  {
    "n": {
      "value": "3"
    },
    "nLabel": {
      "value": "Российский государственный архив социально-политической истории (РГАСПИ) | Arxiu Estatal Rus d'Història Sociopolítica (RGASPI). Informació diversa sobre el brigadista Fritz Hilger. [Moscou : RGASPI], 2024."
    }
  },
  {
    "n": {
      "value": "4"
    },
    "nLabel": {
      "value": "Российский государственный архив социально-политической истории (РГАСПИ) | Arxiu Estatal Rus d'Història Sociopolítica (RGASPI). Informació diversa sobre el brigadista Sam Gibons. [Moscou : RGASPI], 2021."
    }
  },
  {
    "n": {
      "value": "5"
    },
    "nLabel": {
      "value": "LEWIS, Wendy. Informació diversa sobre el brigadista Sidney Shosteck. [S.l : s.n.], 2023"
    }
  },
  {
    "n": {
      "value": "6"
    },
    "nLabel": {
      "value": "ABACERIN, Georges"
    }
  },
  {
    "n": {
      "value": "7"
    },
    "nLabel": {
      "value": "ACER. Les Amis des Combattants en Espagne Républicaine. Brigadistes"
    }
  },
  {
    "n": {
      "value": "8"
    },
    "nLabel": {
      "value": "La Columna Uruguaya : historia de los uruguayos en la guerra Civil Española"
    }
  },
  {
    "n": {
      "value": "9"
    },
    "nLabel": {
      "value": "\"Muere la musa catalana de Hemingway en Por quién doblan las campanas\". La Vanguardia (4/6/2012)"
    }
  }
]
```

##### Respuesta Servidor (API)
```bash
curl -u 'ubxat:BLI-u24KH%36xM9gQ9PzX' \
  -X POST 'https://ubxat.peninsula.co/api/v1/sparql' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{
    "query": "MATCH (subject)-[r]->(object) RETURN id(subject) AS subject, type(r) AS predicate, id(object) AS object ORDER BY subject, predicate, object SKIP 0 LIMIT 25",
    "format": "json"
  }'
{"query":"MATCH (subject)-[r]->(object) RETURN id(subject) AS subject, type(r) AS predicate, id(object) AS object ORDER BY subject, predicate, object SKIP 0 LIMIT 25","results":[{"subject":0,"predicate":"MAIN_SUBJECT","object":11},{"subject":3,"predicate":"MAIN_SUBJECT","object":12},{"subject":4,"predicate":"MAIN_SUBJECT","object":13},{"subject":5,"predicate":"MAIN_SUBJECT","object":14},{"subject":15,"predicate":"CONTAINS_REMAINS_OF","object":32},{"subject":15,"predicate":"HAS_ASSESSMENT","object":24},{"subject":15,"predicate":"HAS_PRESERVATION_STATE","object":25},{"subject":15,"predicate":"LOCATED_IN","object":26},{"subject":15,"predicate":"PARTICIPANT_IN","object":31},{"subject":16,"predicate":"CONTAINS_REMAINS_OF","object":40},{"subject":16,"predicate":"HAS_ASSESSMENT","object":33},{"subject":16,"predicate":"HAS_PRESERVATION_STATE","object":34},{"subject":16,"predicate":"LOCATED_IN","object":35},{"subject":16,"predicate":"PARTICIPANT_IN","object":38},{"subject":16,"predicate":"PARTICIPANT_IN","object":39},{"subject":17,"predicate":"CONTAINS_REMAINS_OF","object":40},{"subject":17,"predicate":"HAS_ASSESSMENT","object":33},{"subject":17,"predicate":"HAS_PRESERVATION_STATE","object":34},{"subject":17,"predicate":"LOCATED_IN","object":41},{"subject":17,"predicate":"PARTICIPANT_IN","object":39},{"subject":18,"predicate":"CONTAINS_REMAINS_OF","object":43},{"subject":18,"predicate":"HAS_ASSESSMENT","object":24},{"subject":18,"predicate":"HAS_PRESERVATION_STATE","object":25},{"subject":18,"predicate":"LOCATED_IN","object":42},{"subject":18,"predicate":"PARTICIPANT_IN","object":31}],"format":"json","execution_time":0.7239999999292195,"source":"neo4j","query_type":"cypher"}%   
```
## GROUP BY

Group by node label and count nodes per type (no explicit GROUP BY; use WITH + aggregation).

```bash
curl -u 'ubxat:BLI-u24KH%36xM9gQ9PzX' \
  -X POST 'https://ubxat.peninsula.co/api/v1/sparql' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{
    "query": "MATCH (n) UNWIND labels(n) AS type RETURN type, count(n) AS count ORDER BY count DESC LIMIT 20",
    "format": "json"
  }'
```

##### Respuesta UBXAT
```bash
[
  {
    "count": {
      "value": "60"
    }
  }
]
```

##### Respuesta Servidor (API)
```bash
curl -u 'ubxat:BLI-u24KH%36xM9gQ9PzX' \
  -X POST 'https://ubxat.peninsula.co/api/v1/sparql' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{
    "query": "MATCH (n) UNWIND labels(n) AS type RETURN type, count(n) AS count ORDER BY count DESC LIMIT 20",
    "format": "json"
  }'
{"query":"MATCH (n) UNWIND labels(n) AS type RETURN type, count(n) AS count ORDER BY count DESC LIMIT 20","results":[{"type":"Publication","count":11},{"type":"MassGrave","count":9},{"type":"Municipality","count":9},{"type":"Comarca","count":6},{"type":"DeathContext","count":5},{"type":"Person","count":4},{"type":"PreservationState","count":4},{"type":"Province","count":4},{"type":"ParticipantType","count":4},{"type":"Assessment","count":2},{"type":"AutonomousCommunity","count":1},{"type":"Country","count":1}],"format":"json","execution_time":0.7439999999478459,"source":"neo4j","query_type":"cypher"}%           
```
## Agregaciones

Count nodes, count relationships, or both in one response.

```bash
curl -u 'ubxat:BLI-u24KH%36xM9gQ9PzX' \
  -X POST 'https://ubxat.peninsula.co/api/v1/sparql' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{
    "query": "MATCH (n) WITH count(n) AS nodeCount MATCH ()-[r]->() WITH nodeCount, count(r) AS relCount RETURN nodeCount, relCount",
    "format": "json"
  }'
```
##### Respuesta UBXAT
```bash
[
  {
    "count": {
      "value": "60"
    }
  }
]
```

##### Respuesta Servidor (API)
```bash
curl -u 'ubxat:BLI-u24KH%36xM9gQ9PzX' \
  -X POST 'https://ubxat.peninsula.co/api/v1/sparql' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{
    "query": "MATCH (n) WITH count(n) AS nodeCount MATCH ()-[r]->() WITH nodeCount, count(r) AS relCount RETURN nodeCount, relCount",
    "format": "json"
  }'
{"query":"MATCH (n) WITH count(n) AS nodeCount MATCH ()-[r]->() WITH nodeCount, count(r) AS relCount RETURN nodeCount, relCount","results":[{"nodeCount":60,"relCount":76}],"format":"json","execution_time":0.13700000010430813,"source":"neo4j","query_type":"cypher"}%                     
```


## Gender and intersectionality based query

**Test summary (current UBXAT graph schema):**

- `MATCH (n) RETURN id(n) AS id, labels(n) AS labels, keys(n) AS props LIMIT 20`  
  - `Publication` nodes: props = `title`, `catalog_code`, `instance_of`, `record_creator`, `described_at_url`, `last_update`, `inception`.  
  - `Person` nodes: props = `name`, `instance_of`.  
  - `MassGrave` nodes: props = `catalogCode`, `title`, `numberOfDeaths`, `location`, `id`, `describedAtUrl`.
- `MATCH (p:Person) RETURN DISTINCT p.instance_of AS instance_of LIMIT 20` → `Q5`, confirming that `Person` nodes are typed as **human** (Wikidata `instance of` = Q5).

**Conclusion for gender/LGBTIQ+ queries:**  
Right now the Neo4j model **only exposes `instance_of` for `Person`**; there are **no properties or nodes for `sex_or_gender` (P21) or `sexual_orientation` (P91)**.  
To implement true gender/intersectionality/LGBTIQ+ searches on UBXAT, the graph must first be extended to store P21/P91 (e.g. as properties on `Person` or as relationships to dedicated gender/orientation nodes).

## Conclusions

They almost certainly use the same dataset (same Neo4j graph behind the same API). The mismatch comes from how the “UBXAT” response was produced or documented, not from another database:

1. Different client/path

“UBXAT” might be another client (e.g. SPARQL or a UI) that either sends a different query (e.g. only “nodes + title”) or converts the API response into a SPARQL-like shape (n, nLabel, {"value": "…"}). So you see that normalized form in the doc and the raw API form in the curl examples.

1. Copy‑paste in the doc

The same 10 rows (nodes 0–9, publication titles) appear as “Obtained in UBXAT” for different queries (triples, FILTER, LIMIT, etc.). So one real result was likely reused as the “UBXAT” example everywhere; the content no longer matches each query and isn’t proof of a different dataset.

1. Snapshot vs live

Less likely: “UBXAT” could be an old export (e.g. when the graph had only 10 nodes) and the server is live (66 nodes, 76 edges). That could explain different sizes but not the identical 10 rows for every query type.

Bottom line: Use the server (curl) response as the single source of truth. The doc now states that the dataset is the same and that the difference is client/format or documentation reuse.

---

## Summary: UBXAT vs API server per search

| Query type | Query subtype | Same / Different | Description |
|------------|----------------|------------------|-------------|
| SELECT | Basic triple patterns (?subject ?predicate ?object) | Different | UBXAT: 10 rows with `n`, `nLabel` (publication titles). Server: triples with `subject`, `predicate`, `object` (node ids + relationship type). |
| SELECT | FILTER (string, e.g. CONTAINS "brigadista") | Different | UBXAT: same 10 `n`/`nLabel` rows. Server: filtered rows with `subject`, `labels`, `label` (only nodes matching the filter). |
| SELECT | FILTER (numeric, e.g. id range) | Different | UBXAT: same 10 `n`/`nLabel` rows. Server: one row per node in range with `subject`, `labels`. |
| SELECT | LIMIT / OFFSET (pagination) | Different | UBXAT: same 10 `n`/`nLabel` rows. Server: paginated triples (`subject`, `predicate`, `object`), e.g. 25 rows per page. |
| ASK | Boolean (pattern exists) | Different | UBXAT: `count` wrapped as `{"value": "60"}`. Server: `result: true` (boolean). |
| ASK | Basic ASK (e.g. exists MassGrave?) | Different | UBXAT: `count` wrapped as `{"value": "60"}`. Server: `result: true` (boolean). |
| COUNT | Count nodes | Different | UBXAT: `count` as `{"value": "60"}` (string). Server: `count` as number (e.g. 66). |
| COUNT | Count relationships | Different | UBXAT: (curl repeated as server). Server: `count: 76` (number). |
| CONSTRUCT | Graph-shaped (nodes + relationships) | Different | UBXAT: 10 `n`/`nLabel` rows. Server: single object with `nodes` and `relationships` collections (full subgraph). |
| DESCRIBE | One node by id (props + rels) | Different | UBXAT: 10 `n`/`nLabel` rows. Server: one row with `id`, `labels`, `props`, `outRels` for the requested node. |
| FILTER | String/numeric filter | Different | UBXAT: same 10 `n`/`nLabel` rows. Server: rows matching the WHERE clause with correct variables. |
| ORDER BY | Sort + SKIP/LIMIT | Different | UBXAT: same 10 `n`/`nLabel` rows. Server: sorted and paginated result (triples ordered by subject, predicate, object). |
| GROUP BY | Group by label, count per type | Different | UBXAT: same 10 `n`/`nLabel` rows. Server: one row per label with `type`, `count` (e.g. Publication 11, MassGrave 9). |
| Agregaciones | nodeCount + relCount | Different | UBXAT: same 10 `n`/`nLabel` rows. Server: one row with `nodeCount`, `relCount` (numbers). |

# Cuál es la query que genera el grafo?
```bash
Nodes (graph vertices)
MATCH (n)
RETURN id(n) as id,
       labels(n) as labels,
       n.text as text,
       n.name as name,
       n.title as title,
       n.birth_date as birth_date,
       n.profession as profession,
       n.location as location,
       n.coordinates as coordinates
LIMIT 200

```

Edges: 
```bash
MATCH (source)-[r]->(target)
RETURN id(source) as sourceId,
       id(target) as targetId,
       type(r) as relationshipType,
       coalesce(source.text, source.name, source.title) as sourceLabel,
       coalesce(target.text, target.name, target.title) as targetLabel
LIMIT 300
```

# Query hecha directamente al servidor vía terminal para obtener todo

```bash
curl -u 'ubxat:BLI-u24KH%36xM9gQ9PzX'\                                              
  -X POST 'https://ubxat.peninsula.co/api/v1/sparql' \  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \   
  -d '{                             
    "query": "MATCH (n) RETURN id(n) AS id, labels(n) AS labels LIMIT 10",                                  
    "format": "json"                  }'
{"query":"MATCH (n) RETURN id(n) AS id, labels(n) AS labels LIMIT 10","results":[{"id":0,"labels":["Publication"]},{"id":1,"labels":["Publication"]},{"id":2,"labels":["Publication"]},{"id":3,"labels":["Publication"]},{"id":4,"labels":["Publication"]},{"id":5,"labels":["Publication"]},{"id":6,"labels":["Publication"]},{"id":7,"labels":["Publication"]},{"id":8,"labels":["Publication"]},{"id":9,"labels":["Publication"]}],"format":"json","execution_time":0.7649999996647239,"source":"neo4j","query_type":"cypher"}%       
```


```bash
curl -u 'ubxat:BLI-u24KH%36xM9gQ9PzX' \
  -X POST 'https://ubxat.peninsula.co/api/v1/sparql' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{
    "query": "CALL { MATCH (n) RETURN collect({ id: id(n), labels: labels(n), props: properties(n) }) AS nodes } CALL { MATCH (source)-[r]->(target) RETURN collect({ sourceId: id(source), targetId: id(target), type: type(r), props: properties(r) }) AS relationships } RETURN nodes, relationships",
    "format": "json"
  }'
```

## Resultados organizados con | jq

```bash 
curl -u 'ubxat:BLI-u24KH%36xM9gQ9PzX' \
  -X POST 'https://ubxat.peninsula.co/api/v1/sparql' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{
    "query": "CALL { MATCH (n) RETURN collect({ id: id(n), labels: labels(n), props: properties(n) }) AS nodes } CALL { MATCH (source)-[r]->(target) RETURN collect({ sourceId: id(source), targetId: id(target), type: type(r), props: properties(r) }) AS relationships } RETURN nodes, relationships",
    "format": "json"
  }'| jq .
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--100  2316  100  1992  100   324   1856    301  0:00:01  0:00:01 --:--:--100  2316  100  1992  100   324   1856    301  0:00:01  0:00:01 --:--:--  2158
{
  "query": "CALL { MATCH (n) RETURN collect({ id: id(n), labels: labels(n), props: properties(n) }) AS nodes } CALL { MATCH (source)-[r]->(target) RETURN collect({ sourceId: id(source), targetId: id(target), type: type(r), props: properties(r) }) AS relationships } RETURN nodes, relationships",
  "results": [
    {
      "n": {
        "value": "0"
      },
      "nLabel": {
        "value": "Informació diversa sobre el brigadista Hans Kaltschmidt. [S.l. : s.n.], 2023."
      }
    },
    {
      "n": {
        "value": "1"
      },
      "nLabel": {
        "value": "BORRÀS DÒLERA, Mercè. Informació diversa sobre els brigadistes Pierre Odéon i Paula Feldestein. [S.l. : s.n.], 2024."
      }
    },
    {
      "n": {
        "value": "2"
      },
      "nLabel": {
        "value": "SCHOLTEN, Yvonne. \"In search of the first Dutch volunteer\". The Volunteer (5/2/2022)"
      }
    },
    {
      "n": {
        "value": "3"
      },
      "nLabel": {
        "value": "Российский государственный архив социально-политической истории (РГАСПИ) | Arxiu Estatal Rus d'Història Sociopolítica (RGASPI). Informació diversa sobre el brigadista Fritz Hilger. [Moscou : RGASPI], 2024."
      }
    },
    {
      "n": {
        "value": "4"
      },
      "nLabel": {
        "value": "Российский государственный архив социально-политической истории (РГАСПИ) | Arxiu Estatal Rus d'Història Sociopolítica (RGASPI). Informació diversa sobre el brigadista Sam Gibons. [Moscou : RGASPI], 2021."
      }
    },
    {
      "n": {
        "value": "5"
      },
      "nLabel": {
        "value": "LEWIS, Wendy. Informació diversa sobre el brigadista Sidney Shosteck. [S.l : s.n.], 2023"
      }
    },
    {
      "n": {
        "value": "6"
      },
      "nLabel": {
        "value": "ABACERIN, Georges"
      }
    },
    {
      "n": {
        "value": "7"
      },
      "nLabel": {
        "value": "ACER. Les Amis des Combattants en Espagne Républicaine. Brigadistes"
      }
    },
    {
      "n": {
        "value": "8"
      },
      "nLabel": {
        "value": "La Columna Uruguaya : historia de los uruguayos en la guerra Civil Española"
      }
    },
    {
      "n": {
        "value": "9"
      },
      "nLabel": {
        "value": "\"Muere la musa catalana de Hemingway en Por quién doblan las campanas\". La Vanguardia (4/6/2012)"
      }
    }
  ],
  "format": "json",
  "execution_time": 0.7410000003874302,
  "source": "neo4j",
  "query_type": "sparql"
}
```

## Query capabilities: CONSTRUCT, DESCRIBE, FILTER, ORDER BY, GROUP BY, aggregations

| SPARQL / concept | Supported on platform? | Cypher equivalent / notes |
|------------------|------------------------|----------------------------|
| **FILTER** | Yes | `WHERE` (e.g. `WHERE toLower(n.title) CONTAINS "x"`, `WHERE id(n) >= 0 AND id(n) < 100`). See § SELECT → FILTER. |
| **ORDER BY** | Yes | `ORDER BY var [ASC\|DESC]` (e.g. `ORDER BY subject, predicate, object`). See § LIMIT/OFFSET. |
| **GROUP BY** | Yes (implicit) | Cypher has no `GROUP BY`; group by using `WITH` + aggregation in `RETURN`. E.g. `MATCH (n) WITH labels(n)[0] AS type RETURN type, count(n) AS count ORDER BY count DESC`. |
| **Aggregations** | Yes | `count(n)`, `count(r)`, `sum(n.prop)`, `collect(n)`, `collect({ id: id(n), labels: labels(n) })`. See § COUNT queries and full-graph collect. |
| **CONSTRUCT** | Equivalent only | SPARQL CONSTRUCT returns an RDF graph. In Cypher: **return a graph-shaped payload** with `collect()` of nodes and relationships (see “Query hecha directamente al servidor” with `CALL { MATCH (n) RETURN collect(...) } CALL { MATCH (source)-[r]->(target) RETURN collect(...) }`). You do not “construct” triples; you return JSON that describes the subgraph. |
| **DESCRIBE** | Equivalent only | SPARQL DESCRIBE returns triples about a resource. In Cypher: **match the node and its relationships** and return node + rels + neighbours. E.g. `MATCH (n) WHERE id(n) = 0 OPTIONAL MATCH (n)-[r]-(m) RETURN n, r, m` or `MATCH (n) WHERE id(n) = 0 OPTIONAL MATCH (n)-[r]->(m) RETURN id(n) AS id, labels(n) AS labels, properties(n) AS props, collect({ type: type(r), targetId: id(m) }) AS outRels`. |

**Summary:** FILTER, ORDER BY, grouping-style queries, and aggregations are supported directly. CONSTRUCT and DESCRIBE have no literal Cypher keyword; use the patterns above to return graph-shaped or “describe”-style results.

---

## Analysis: UBXAT responses vs server responses

| Aspect | UBXAT (documented) | Server (API) |
|--------|--------------------|--------------|
| **Structure** | Array of objects with `n` / `nLabel` (or `count`), each value wrapped as `{"value": "…"}`. | Single object: `query`, `results` (array), `format`, `execution_time`, `source`, `query_type`. |
| **Variable names** | SPARQL-style: `n`, `nLabel`, `count` (generic). | Cypher-style: same names as in `RETURN` (e.g. `subject`, `predicate`, `object`, `labels`, `label`, `result`, `count`). |
| **Value format** | Nested: `"n": {"value": "0"}`, `"nLabel": {"value": "Informació…"}`. | Flat: `"subject": 0`, `"predicate": "MAIN_SUBJECT"`, `"object": 11`. |
| **Data source** | Looks like an older or alternate export (e.g. SPARQL layer or UI): only node id + one label text; same 10 rows repeated across queries. | Live Neo4j: full result set matching the Cypher (triples, labels, filters, pagination). |
| **Query alignment** | Often **misaligned**: e.g. “Obtained in UBXAT” for “subject–predicate–object” shows 10 `n`/`nLabel` rows (publications only), not triples. | **Aligned**: server returns subject/predicate/object, or subject/labels/label, etc., as in the request. |
| **Counts** | UBXAT shows `"count": {"value": "60"}` (string). Server shows `"count": 60` (number) and `"result": true` for ASK. | Same semantics; server format is canonical and easier to parse. |

**Summary:** “UBXAT” in the doc is a **different output shape** (SPARQL-like, wrapped values, fixed subset of nodes). The **server** response is the **real API**: flat keys, correct variables, and full result set. For integration or scripts, use the **server** format as the source of truth.

### Why are they different? (same API in theory)

In theory both consult the same API (`POST https://ubxat.peninsula.co/api/v1/sparql`). The dataset is almost certainly the **same Neo4j graph**. The difference is not “different database” but **how the response was produced or recorded**:

| Cause | Explanation |
|-------|-------------|
| **Different client / path** | “UBXAT” may be a **different client**: e.g. a SPARQL endpoint or UI that (1) sends a *different* query (e.g. “nodes + title” only), or (2) **normalizes** the API response into a SPARQL-like shape (`n`, `nLabel`, `{"value": "…"}`). The doc would then show that normalized output as “Obtained in UBXAT” while the curl examples show the **raw** API response. |
| **Documentation copy‑paste** | The same **10 rows** (nodes 0–9, publication titles) appear as “UBXAT” for *different* queries (triples, FILTER, LIMIT, etc.). That suggests one real result (e.g. “list nodes with label”) was **reused** as the “UBXAT” block for every example, so the content is **misaligned** with the query, not from a different dataset. |
| **Snapshot vs live** | Less likely: “UBXAT” could be from an **older export** (graph with only 10 nodes), while server responses are **live** (66 nodes, 76 relationships). That would explain different row counts, but not the same 10 rows for every query type. |

**Takeaway:** Treat the **server (curl) response** as the single source of truth. If “UBXAT” is a real interface, clarify which request it sends and whether it transforms the API response.

