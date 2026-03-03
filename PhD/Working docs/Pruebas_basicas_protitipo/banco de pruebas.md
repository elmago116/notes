SELECT DISTINCT ?type (COUNT(?node) AS ?count) 

WHERE { 

  ?node <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ?type . 

} 

GROUP BY ?type 

ORDER BY DESC(?count) 

LIMIT 20 

---

## Ver **tus** tipos (tu grafo UBXAT / Neo4j)

La consulta de arriba contra **Wikidata** devuelve tipos de Wikidata. Para ver **los tipos de tu propio grafo** (personas, publicaciones, fosas, etc.) hay que lanzarla contra **tu endpoint**.

**UBXAT (POST + JSON; sustituye `USER` y `PASSWORD` por tus credenciales):**

```bash
curl -u 'ubxat:BLI-u24KH%36xM9gQ9PzX' \
  -X POST 'https://ubxat.peninsula.co/api/v1/sparql' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{
    "query": "SELECT DISTINCT ?type (COUNT(?node) AS ?count) WHERE { ?node <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ?type . } GROUP BY ?type ORDER BY DESC(?count) LIMIT 20",
    "format": "json"
  }'
```

Si tu API traduce SPARQL a Cypher y no expone `rdf:type`, puede que sigas obteniendo 0. En ese caso prueba en **Cypher** (lo que acepta UBXAT) para listar etiquetas y conteos:

```bash
curl -u 'USER:PASSWORD' \
  -X POST 'https://ubxat.peninsula.co/api/v1/sparql' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{
    "query": "MATCH (n) UNWIND labels(n) AS type RETURN type, count(n) AS count ORDER BY count DESC LIMIT 20",
    "format": "json"
  }'
```

Esa segunda petición devuelve **tus** etiquetas de nodo (p. ej. `Publication`, `Person`, etc.) y cuántos nodos hay de cada una.

---

## Probar con curl (Wikidata y genérico)

**1. Contra Wikidata (comprobar que la consulta es válida y devuelve datos):**

```bash
curl -G "https://query.wikidata.org/sparql" \
  --data-urlencode "query=SELECT DISTINCT ?type (COUNT(?node) AS ?count) WHERE { ?node <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ?type . } GROUP BY ?type ORDER BY DESC(?count) LIMIT 20" \
  -H "Accept: application/sparql-results+json"
```

**2. Contra tu endpoint Neo4j / UBXAT (sustituye `ENDPOINT_URL` por la URL real):**

```bash
curl -G "ENDPOINT_URL" \
  --data-urlencode "query=SELECT DISTINCT ?type (COUNT(?node) AS ?count) WHERE { ?node <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ?type . } GROUP BY ?type ORDER BY DESC(?count) LIMIT 20" \
  -H "Accept: application/sparql-results+json"
```

Si el endpoint exige POST en lugar de GET, usa:

```bash
curl -X POST "ENDPOINT_URL" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "Accept: application/sparql-results+json" \
  --data-urlencode "query=SELECT DISTINCT ?type (COUNT(?node) AS ?count) WHERE { ?node <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ?type . } GROUP BY ?type ORDER BY DESC(?count) LIMIT 20"
```