# Inventario de transformaciones SIDBRINT

## Inventario de transformaciones (Nivel columna)

| Tabla | Atributo | Tipo de atributo | Regla de transformación | Cómo se aplica | Ejemplo Turtle (TTL) |
|-------|----------|------------------|------------------------|----------------|----------------------|
| BRIGADISTES | IdBrigadista | Clave primaria | Regla 1 | Se usa como identificador de la clase :Brigadistes. | :Brigadistes a owl:Class . |
| BRIGADISTES | Nom | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :nom a owl:DatatypeProperty ; rdfs:domain :Brigadistes ; rdfs:range xsd:string . |
| BRIGADISTES | Alies del brigadista | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :aliesDelBrigadista a owl:DatatypeProperty ; rdfs:domain :Brigadistes ; rdfs:range xsd:string . |
| BRIGADISTES | PaisNaixement/Procedencia | Clave foránea | Regla 3 | Se transforma en owl:ObjectProperty. | :paisnaixementProcedencia a owl:ObjectProperty ; rdfs:domain :Brigadistes ; rdfs:range :Països . |
| BRIGADISTES | LlocNaixement | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :llocnaixement a owl:DatatypeProperty ; rdfs:domain :Brigadistes ; rdfs:range xsd:string . |
| BRIGADISTES | Data de Naixement | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :dataDeNaixement a owl:DatatypeProperty ; rdfs:domain :Brigadistes ; rdfs:range xsd:string . |
| BRIGADISTES | Data de defunció | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :dataDeDefunció a owl:DatatypeProperty ; rdfs:domain :Brigadistes ; rdfs:range xsd:string . |
| BRIGADISTES | LlocDefuncio | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :llocdefuncio a owl:DatatypeProperty ; rdfs:domain :Brigadistes ; rdfs:range xsd:string . |
| BRIGADISTES | Dades segons la font | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :dadesSegonsLaFont a owl:DatatypeProperty ; rdfs:domain :Brigadistes ; rdfs:range xsd:string . |
| BRIGADISTES | geologcalitzacioNaixement | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :geologcalitzacioNaixement a owl:DatatypeProperty ; rdfs:domain :Brigadistes ; rdfs:range xsd:string . |
| BRIGADISTES | geologcalitzacioMort | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :geologcalitzacioMort a owl:DatatypeProperty ; rdfs:domain :Brigadistes ; rdfs:range xsd:string . |
| PROFESSIONS | idProfessió | Clave primaria | Regla 1 | Se usa como identificador de la clase :Professions. | :Professions a owl:Class . |
| PROFESSIONS | nomProfessio | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :nomprofessio a owl:DatatypeProperty ; rdfs:domain :Professions ; rdfs:range xsd:string . |
| BRIGADISTES_PROFESSIONS | - | Tabla asociativa | Regla 2 | Se transforma en owl:ObjectProperty inversa. | ... |
| PAÏSOS | idPais | Clave primaria | Regla 1 | Se usa como identificador de la clase :Països. | :Països a owl:Class . |
| PAÏSOS | nomPais | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :nompais a owl:DatatypeProperty ; rdfs:domain :Països ; rdfs:range xsd:string . |
| PROCEDÈNCIA, RELIGIÓ, ÈTNIA | idCaracterística | Clave primaria | Regla 1 | Se usa como identificador de la clase :ProcedènciaReligióÈtnia. | :ProcedènciaReligióÈtnia a owl:Class . |
| PROCEDÈNCIA, RELIGIÓ, ÈTNIA | nomCaracterística | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :nomcaracterística a owl:DatatypeProperty ; rdfs:domain :ProcedènciaReligióÈtnia ; rdfs:range xsd:string . |
| PROCEDÈNCIA, RELIGIÓ, ÈTNIA | fkTipusCaracterística | Clave foránea | Regla 3 | Se transforma en owl:ObjectProperty. | :fktipuscaracterística a owl:ObjectProperty ; rdfs:domain :ProcedènciaReligióÈtnia ; rdfs:range :Tipuscaracteristica . |
| BRIGADISTES_ETNIA_RELIGIO | - | Tabla asociativa | Regla 2 | Se transforma en owl:ObjectProperty inversa. | ... |
| TipusCaracteristica | idCaracterística | Clave primaria | Regla 1 | Se usa como identificador de la clase :Tipuscaracteristica. | :Tipuscaracteristica a owl:Class . |
| TipusCaracteristica | nomCaracterística | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :nomcaracterística a owl:DatatypeProperty ; rdfs:domain :Tipuscaracteristica ; rdfs:range xsd:string . |
| IDEOLOGIES POLÍTIQUES | idideologia | Clave primaria | Regla 1 | Se usa como identificador de la clase :IdeologiesPolítiques. | :IdeologiesPolítiques a owl:Class . |
| IDEOLOGIES POLÍTIQUES | nomIdeologia | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :nomideologia a owl:DatatypeProperty ; rdfs:domain :IdeologiesPolítiques ; rdfs:range xsd:string . |
| BRIGADISTES_IDEOLOGIA | - | Tabla asociativa | Regla 2 | Se transforma en owl:ObjectProperty inversa. | ... |
| ORGANITZACIONS | idOrganitzacio | Clave primaria | Regla 1 | Se usa como identificador de la clase :Organitzacions. | :Organitzacions a owl:Class . |
| ORGANITZACIONS | nomOrganitzacio | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :nomorganitzacio a owl:DatatypeProperty ; rdfs:domain :Organitzacions ; rdfs:range xsd:string . |
| BRIGADISTES_ORGANITZACIONS | - | Tabla asociativa | Regla 2 | Se transforma en owl:ObjectProperty inversa. | ... |
| BATALLES_FRONTS | idBatallesFronts | Clave primaria | Regla 1 | Se usa como identificador de la clase :BatallesFronts. | :BatallesFronts a owl:Class . |
| BATALLES_FRONTS | nomEscenari | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :nomescenari a owl:DatatypeProperty ; rdfs:domain :BatallesFronts ; rdfs:range xsd:string . |
| BATALLES_FRONTS | fkTipusEscenari | Clave foránea | Regla 3 | Se transforma en owl:ObjectProperty. | :fktipusescenari a owl:ObjectProperty ; rdfs:domain :BatallesFronts ; rdfs:range :TipusEscenaris . |
| BATALLES_FRONTS | Dates | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :dates a owl:DatatypeProperty ; rdfs:domain :BatallesFronts ; rdfs:range xsd:string . |
| BATALLES_FRONTS | DataInici | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :datainici a owl:DatatypeProperty ; rdfs:domain :BatallesFronts ; rdfs:range xsd:string . |
| BATALLES_FRONTS | DataFi | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :datafi a owl:DatatypeProperty ; rdfs:domain :BatallesFronts ; rdfs:range xsd:string . |
| BATALLES_FRONTS | Informacio addicional. | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :informacioAddicional a owl:DatatypeProperty ; rdfs:domain :BatallesFronts ; rdfs:range xsd:string . |
| BATALLES_FRONTS | geolocalització | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :geolocalització a owl:DatatypeProperty ; rdfs:domain :BatallesFronts ; rdfs:range xsd:string . |
| ESCENARIS_BELICS | idEscenari | Clave primaria | Regla 1 | Se usa como identificador de la clase :EscenarisBelics. | :EscenarisBelics a owl:Class . |
| ESCENARIS_BELICS | tipusEscenari | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :tipusescenari a owl:DatatypeProperty ; rdfs:domain :EscenarisBelics ; rdfs:range xsd:string . |
| BATALLES_FRONTS_RELACIONATS | idBatallesFrontsRelacionats | Clave primaria | Regla 1 | Se usa como identificador de la clase :BatallesFrontsRelacionats. | :BatallesFrontsRelacionats a owl:Class . |
| BRIGADISTES_ESCENARIS_BEL.LICS | idBrigadistesEscenarisBelics | Clave primaria | Regla 1 | Se usa como identificador de la clase :BrigadistesEscenarisBellics. | :BrigadistesEscenarisBellics a owl:Class . |
| BRIGADISTES_ESCENARIS_BEL.LICS | idEscenariBelic | Clave foránea | Regla 3 | Se transforma en owl:ObjectProperty. | :idescenaribelic a owl:ObjectProperty ; rdfs:domain :BrigadistesEscenarisBellics ; rdfs:range :TipusEscenaris . |
| BRIGADISTES_ESCENARIS_BEL.LICS | fk_idBrigadista | Clave foránea | Regla 3 | Se transforma en owl:ObjectProperty. | :fkIdbrigadista a owl:ObjectProperty ; rdfs:domain :BrigadistesEscenarisBellics ; rdfs:range :Brigadistes . |
| BRIGADISTES_ESCENARIS_BEL.LICS | Data_inici | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :dataInici a owl:DatatypeProperty ; rdfs:domain :BrigadistesEscenarisBellics ; rdfs:range xsd:string . |
| BRIGADISTES_ESCENARIS_BEL.LICS | Data_fi | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :dataFi a owl:DatatypeProperty ; rdfs:domain :BrigadistesEscenarisBellics ; rdfs:range xsd:string . |
| TIPUS_ESCENARIS | idEscenari | Clave primaria | Regla 1 | Se usa como identificador de la clase :TipusEscenaris. | :TipusEscenaris a owl:Class . |
| TIPUS_ESCENARIS | tipusEscenari | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :tipusescenari a owl:DatatypeProperty ; rdfs:domain :TipusEscenaris ; rdfs:range xsd:string . |
| ESDEVENIMENTS | idEsdeveniment | Clave primaria | Regla 1 | Se usa como identificador de la clase :Esdeveniments. | :Esdeveniments a owl:Class . |
| ESDEVENIMENTS | descripcióEsdeveniment | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :descripcióesdeveniment a owl:DatatypeProperty ; rdfs:domain :Esdeveniments ; rdfs:range xsd:string . |
| ESDEVENIMENTS | fkTipusEsdeveniment | Clave foránea | Regla 3 | Se transforma en owl:ObjectProperty. | :fktipusesdeveniment a owl:ObjectProperty ; rdfs:domain :Esdeveniments ; rdfs:range :Esdeveniments . |
| BRIGADISTES_ESDEVENIMENTS | idBrigadistesEsdeveniments | Clave primaria | Regla 1 | Se usa como identificador de la clase :BrigadistesEsdeveniments. | :BrigadistesEsdeveniments a owl:Class . |
| BRIGADISTES_ESDEVENIMENTS | idEsdeveniments | Clave foránea | Regla 3 | Se transforma en owl:ObjectProperty. | :idesdeveniments a owl:ObjectProperty ; rdfs:domain :BrigadistesEsdeveniments ; rdfs:range :TipusEsdeveniments . |
| BRIGADISTES_ESDEVENIMENTS | fk_idBrigadista | Clave foránea | Regla 3 | Se transforma en owl:ObjectProperty. | :fkIdbrigadista a owl:ObjectProperty ; rdfs:domain :BrigadistesEsdeveniments ; rdfs:range :Brigadistes . |
| BRIGADISTES_ESDEVENIMENTS | Data_inici | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :dataInici a owl:DatatypeProperty ; rdfs:domain :BrigadistesEsdeveniments ; rdfs:range xsd:string . |
| BRIGADISTES_ESDEVENIMENTS | Data_fi | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :dataFi a owl:DatatypeProperty ; rdfs:domain :BrigadistesEsdeveniments ; rdfs:range xsd:string . |
| TIPUS_ESDEVENIMENTS | idEsdeveniments | Clave primaria | Regla 1 | Se usa como identificador de la clase :TipusEsdeveniments. | :TipusEsdeveniments a owl:Class . |
| TIPUS_ESDEVENIMENTS | tipusEscenari | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :tipusescenari a owl:DatatypeProperty ; rdfs:domain :TipusEsdeveniments ; rdfs:range xsd:string . |
| BATALLES_FRONTS_RELACIONATS | idBatallesFrontsRelacionats | Clave primaria | Regla 1 | Se usa como identificador de la clase :BatallesFrontsRelacionats. | :BatallesFrontsRelacionats a owl:Class . |
| BATALLES_FRONTS_RELACIONATS | idBatallesFronts | Clave foránea | Regla 3 | Se transforma en owl:ObjectProperty. | :idbatallesfronts a owl:ObjectProperty ; rdfs:domain :BatallesFrontsRelacionats ; rdfs:range :BatallesFronts . |
| BATALLES_FRONTS_RELACIONATS | idBatallesFrontsRelacionat | Clave foránea | Regla 3 | Se transforma en owl:ObjectProperty. | :idbatallesfrontsrelacionat a owl:ObjectProperty ; rdfs:domain :BatallesFrontsRelacionats ; rdfs:range :BatallesFronts . |
| BATALLES_FRONTS_RELACIONATS | DataRelacio | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :datarelacio a owl:DatatypeProperty ; rdfs:domain :BatallesFrontsRelacionats ; rdfs:range xsd:string . |
| ESTRUCTURES MILITARS | idEstructuraMilitar | Clave primaria | Regla 1 | Se usa como identificador de la clase :EstructuresMilitars. | :EstructuresMilitars a owl:Class . |
| ESTRUCTURES MILITARS | nomEstructura | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :nomestructura a owl:DatatypeProperty ; rdfs:domain :EstructuresMilitars ; rdfs:range xsd:string . |
| ESTRUCTURES MILITARS | fkTipusEstructura | Clave foránea | Regla 3 | Se transforma en owl:ObjectProperty. | :fktipusestructura a owl:ObjectProperty ; rdfs:domain :EstructuresMilitars ; rdfs:range :TipusEstructures . |
| ESTRUCTURES MILITARS | Descripció Estructura i actuacións | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :descripcióEstructuraIActuacións a owl:DatatypeProperty ; rdfs:domain :EstructuresMilitars ; rdfs:range xsd:string . |
| TIPUS_ESTRUCTURES | idEstructura | Clave primaria | Regla 1 | Se usa como identificador de la clase :TipusEstructures. | :TipusEstructures a owl:Class . |
| TIPUS_ESTRUCTURES | nomEstructura | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :nomestructura a owl:DatatypeProperty ; rdfs:domain :TipusEstructures ; rdfs:range xsd:string . |
| BRIGADISTES_ESTRUCTURES | idBrigadistesEstructures | Clave primaria | Regla 1 | Se usa como identificador de la clase :BrigadistesEstructures. | :BrigadistesEstructures a owl:Class . |
| BRIGADISTES_ESTRUCTURES | id Estructura_Militar | Clave foránea | Regla 3 | Se transforma en owl:ObjectProperty. | :idEstructuraMilitar a owl:ObjectProperty ; rdfs:domain :BrigadistesEstructures ; rdfs:range :EstructuresMilitars . |
| BRIGADISTES_ESTRUCTURES | fk_idBrigadista | Clave foránea | Regla 3 | Se transforma en owl:ObjectProperty. | :fkIdbrigadista a owl:ObjectProperty ; rdfs:domain :BrigadistesEstructures ; rdfs:range :Brigadistes . |
| BRIGADISTES_ESTRUCTURES | Data_inici | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :dataInici a owl:DatatypeProperty ; rdfs:domain :BrigadistesEstructures ; rdfs:range xsd:string . |
| BRIGADISTES_ESTRUCTURES | Data_fi | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :dataFi a owl:DatatypeProperty ; rdfs:domain :BrigadistesEstructures ; rdfs:range xsd:string . |
| LLOCS | idLloc | Clave primaria | Regla 1 | Se usa como identificador de la clase :Llocs. | :Llocs a owl:Class . |
| LLOCS | nomLloc | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :nomlloc a owl:DatatypeProperty ; rdfs:domain :Llocs ; rdfs:range xsd:string . |
| LLOCS | comarca | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :comarca a owl:DatatypeProperty ; rdfs:domain :Llocs ; rdfs:range xsd:string . |
| LLOCS | provincia | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :provincia a owl:DatatypeProperty ; rdfs:domain :Llocs ; rdfs:range xsd:string . |
| LLOCS | regió | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :regió a owl:DatatypeProperty ; rdfs:domain :Llocs ; rdfs:range xsd:string . |
| LLOCS | coordenades | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :coordenades a owl:DatatypeProperty ; rdfs:domain :Llocs ; rdfs:range xsd:string . |
| LLOCS | idPais | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :idpais a owl:DatatypeProperty ; rdfs:domain :Llocs ; rdfs:range xsd:string . |
| LLOCS - ESCENARIS | - | Tabla asociativa | Regla 2 | Se transforma en owl:ObjectProperty inversa. | ... |
| FONTS DOCUMENTALS | idFontDocumental | Clave primaria | Regla 1 | Se usa como identificador de la clase :FontsDocumentals. | :FontsDocumentals a owl:Class . |
| FONTS DOCUMENTALS | Titol | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :titol a owl:DatatypeProperty ; rdfs:domain :FontsDocumentals ; rdfs:range xsd:string . |
| FONTS DOCUMENTALS | Autor | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :autor a owl:DatatypeProperty ; rdfs:domain :FontsDocumentals ; rdfs:range xsd:string . |
| FONTS DOCUMENTALS | Referencia completa | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :referenciaCompleta a owl:DatatypeProperty ; rdfs:domain :FontsDocumentals ; rdfs:range xsd:string . |
| FONTS DOCUMENTALS | Any d'Edició | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :anyD'Edició a owl:DatatypeProperty ; rdfs:domain :FontsDocumentals ; rdfs:range xsd:string . |
| FONTS DOCUMENTALS | Lloc d'edició | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :llocD'Edició a owl:DatatypeProperty ; rdfs:domain :FontsDocumentals ; rdfs:range xsd:string . |
| FONTS_BRIGADISTES | - | Tabla asociativa | Regla 2 | Se transforma en owl:ObjectProperty inversa. | ... |
| FONTS_FONTS | - | Tabla asociativa | Regla 2 | Se transforma en owl:ObjectProperty inversa. | ... |
| IDIOMES | idIdioma | Clave primaria | Regla 1 | Se usa como identificador de la clase :Idiomes. | :Idiomes a owl:Class . |
| IDIOMES | nomIdioma | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :nomidioma a owl:DatatypeProperty ; rdfs:domain :Idiomes ; rdfs:range xsd:string . |
| FONTS_IDIOMES | - | Tabla asociativa | Regla 2 | Se transforma en owl:ObjectProperty inversa. | ... |
| ENFOCAMENTS | idEnfocament | Clave primaria | Regla 1 | Se usa como identificador de la clase :Enfocaments. | :Enfocaments a owl:Class . |
| ENFOCAMENTS | nomEnfocament | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :nomenfocament a owl:DatatypeProperty ; rdfs:domain :Enfocaments ; rdfs:range xsd:string . |
| FONTS_ENFOCAMENTS | - | Tabla asociativa | Regla 2 | Se transforma en owl:ObjectProperty inversa. | ... |
| LITERATURA_MITJANS_COMUNICACIO | idLiteraturaMitjans | Clave primaria | Regla 1 | Se usa como identificador de la clase :LiteraturaMitjansComunicacio. | :LiteraturaMitjansComunicacio a owl:Class . |
| LITERATURA_MITJANS_COMUNICACIO | nomLiteraturaMitjans | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :nomliteraturamitjans a owl:DatatypeProperty ; rdfs:domain :LiteraturaMitjansComunicacio ; rdfs:range xsd:string . |
| FONTS_LITERATURA_MITJANS | - | Tabla asociativa | Regla 2 | Se transforma en owl:ObjectProperty inversa. | ... |
| CULTURA | idCultura | Clave primaria | Regla 1 | Se usa como identificador de la clase :Cultura. | :Cultura a owl:Class . |
| CULTURA | nomCultura | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :nomcultura a owl:DatatypeProperty ; rdfs:domain :Cultura ; rdfs:range xsd:string . |
| FONTS_ CULTURA | - | Tabla asociativa | Regla 2 | Se transforma en owl:ObjectProperty inversa. | ... |
| TIPUS_DOCUMENTAL | idTipusDocumental | Clave primaria | Regla 1 | Se usa como identificador de la clase :TipusDocumental. | :TipusDocumental a owl:Class . |
| TIPUS_DOCUMENTAL | nomTipusDocumental | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :nomtipusdocumental a owl:DatatypeProperty ; rdfs:domain :TipusDocumental ; rdfs:range xsd:string . |
| FONTS_TIPUS_DOCUMENTAL | - | Tabla asociativa | Regla 2 | Se transforma en owl:ObjectProperty inversa. | ... |
| FONTS_PAIS_EDICIO | - | Tabla asociativa | Regla 2 | Se transforma en owl:ObjectProperty inversa. | ... |
| MOVIMENTS | idMoviment | Clave primaria | Regla 1 | Se usa como identificador de la clase :Moviments. | :Moviments a owl:Class . |
| MOVIMENTS | nomMoviment | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :nommoviment a owl:DatatypeProperty ; rdfs:domain :Moviments ; rdfs:range xsd:string . |
| BRIGADISTES_MOVIMENTS | - | Tabla asociativa | Regla 2 | Se transforma en owl:ObjectProperty inversa. | ... |
| PRESONS_CAMPS | idPresonsCamps | Clave primaria | Regla 1 | Se usa como identificador de la clase :PresonsCamps. | :PresonsCamps a owl:Class . |
| PRESONS_CAMPS | nomPresoCamp | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :nompresoccamp a owl:DatatypeProperty ; rdfs:domain :PresonsCamps ; rdfs:range xsd:string . |
| PRESONS_CAMPS | fkTipusEscenari | Clave foránea | Regla 3 | Se transforma en owl:ObjectProperty. | :fktipusescenari a owl:ObjectProperty ; rdfs:domain :PresonsCamps ; rdfs:range :TipusEscenaris . |
| PRESONS_CAMPS | descripció | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :descripció a owl:DatatypeProperty ; rdfs:domain :PresonsCamps ; rdfs:range xsd:string . |
| PRESONS_CAMPS | geolocalitzacio | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :geolocalitzacio a owl:DatatypeProperty ; rdfs:domain :PresonsCamps ; rdfs:range xsd:string . |
| BRIGADISTES_PRESONS_CAMPS | idBrigadistes_Presons_Camps | Clave primaria | Regla 1 | Se usa como identificador de la clase :BrigadistesPresonsCamps. | :BrigadistesPresonsCamps a owl:Class . |
| BRIGADISTES_PRESONS_CAMPS | idPresonsCamps | Clave foránea | Regla 3 | Se transforma en owl:ObjectProperty. | :idpresonsccamps a owl:ObjectProperty ; rdfs:domain :BrigadistesPresonsCamps ; rdfs:range :PresonsCamps . |
| BRIGADISTES_PRESONS_CAMPS | fk_idBrigadista | Clave foránea | Regla 3 | Se transforma en owl:ObjectProperty. | :fkIdbrigadista a owl:ObjectProperty ; rdfs:domain :BrigadistesPresonsCamps ; rdfs:range :Brigadistes . |
| BRIGADISTES_PRESONS_CAMPS | Data_inici | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :dataInici a owl:DatatypeProperty ; rdfs:domain :BrigadistesPresonsCamps ; rdfs:range xsd:string . |
| BRIGADISTES_PRESONS_CAMPS | Data_fi | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :dataFi a owl:DatatypeProperty ; rdfs:domain :BrigadistesPresonsCamps ; rdfs:range xsd:string . |
| ESPAIS_SANITARIS | idEspaisSanitaris | Clave primaria | Regla 1 | Se usa como identificador de la clase :EspaisSanitaris. | :EspaisSanitaris a owl:Class . |
| ESPAIS_SANITARIS | nomEspaiSanitari | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :nomespaisanitari a owl:DatatypeProperty ; rdfs:domain :EspaisSanitaris ; rdfs:range xsd:string . |
| ESPAIS_SANITARIS | fkTipusEscenari | Clave foránea | Regla 3 | Se transforma en owl:ObjectProperty. | :fktipusescenari a owl:ObjectProperty ; rdfs:domain :EspaisSanitaris ; rdfs:range :TipusEscenaris . |
| ESPAIS_SANITARIS | descripció | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :descripció a owl:DatatypeProperty ; rdfs:domain :EspaisSanitaris ; rdfs:range xsd:string . |
| ESPAIS_SANITARIS | geolocalitzacio | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :geolocalitzacio a owl:DatatypeProperty ; rdfs:domain :EspaisSanitaris ; rdfs:range xsd:string . |
| BRIGADISTES_ESPAIS_SANITARIS | idBrigadistes_EspaisSanitaris | Clave primaria | Regla 1 | Se usa como identificador de la clase :BrigadistesEspaisSanitaris. | :BrigadistesEspaisSanitaris a owl:Class . |
| BRIGADISTES_ESPAIS_SANITARIS | idEspaisSanitaris | Clave foránea | Regla 3 | Se transforma en owl:ObjectProperty. | :idespaisanitaris a owl:ObjectProperty ; rdfs:domain :BrigadistesEspaisSanitaris ; rdfs:range :EspaisSanitaris . |
| BRIGADISTES_ESPAIS_SANITARIS | fk_idBrigadista | Clave foránea | Regla 3 | Se transforma en owl:ObjectProperty. | :fkIdbrigadista a owl:ObjectProperty ; rdfs:domain :BrigadistesEspaisSanitaris ; rdfs:range :Brigadistes . |
| BRIGADISTES_ESPAIS_SANITARIS | Data_inici | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :dataInici a owl:DatatypeProperty ; rdfs:domain :BrigadistesEspaisSanitaris ; rdfs:range xsd:string . |
| BRIGADISTES_ESPAIS_SANITARIS | Data_fi | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :dataFi a owl:DatatypeProperty ; rdfs:domain :BrigadistesEspaisSanitaris ; rdfs:range xsd:string . |

## Tabla 1: Clases

| Clase | Expresión Turtle |
| - | - |
| Brigadistes | :Brigadistes a owl:Class . |
| Professions | :Professions a owl:Class . |
| Països | :Països a owl:Class . |
| ProcedènciaReligióÈtnia | :ProcedènciaReligióÈtnia a owl:Class . |
| Tipuscaracteristica | :Tipuscaracteristica a owl:Class . |
| IdeologiesPolítiques | :IdeologiesPolítiques a owl:Class . |
| Organitzacions | :Organitzacions a owl:Class . |
| BatallesFronts | :BatallesFronts a owl:Class . |
| EscenarisBelics | :EscenarisBelics a owl:Class . |
| BatallesFrontsRelacionats | :BatallesFrontsRelacionats a owl:Class . |
| BrigadistesEscenarisBellics | :BrigadistesEscenarisBellics a owl:Class . |
| TipusEscenaris | :TipusEscenaris a owl:Class . |
| Esdeveniments | :Esdeveniments a owl:Class . |
| BrigadistesEsdeveniments | :BrigadistesEsdeveniments a owl:Class . |
| TipusEsdeveniments | :TipusEsdeveniments a owl:Class . |
| BatallesFrontsRelacionats | :BatallesFrontsRelacionats a owl:Class . |
| EstructuresMilitars | :EstructuresMilitars a owl:Class . |
| TipusEstructures | :TipusEstructures a owl:Class . |
| BrigadistesEstructures | :BrigadistesEstructures a owl:Class . |
| Llocs | :Llocs a owl:Class . |
| FontsDocumentals | :FontsDocumentals a owl:Class . |
| Idiomes | :Idiomes a owl:Class . |
| Enfocaments | :Enfocaments a owl:Class . |
| LiteraturaMitjansComunicacio | :LiteraturaMitjansComunicacio a owl:Class . |
| Cultura | :Cultura a owl:Class . |
| TipusDocumental | :TipusDocumental a owl:Class . |
| Moviments | :Moviments a owl:Class . |
| PresonsCamps | :PresonsCamps a owl:Class . |
| BrigadistesPresonsCamps | :BrigadistesPresonsCamps a owl:Class . |
| EspaisSanitaris | :EspaisSanitaris a owl:Class . |
| BrigadistesEspaisSanitaris | :BrigadistesEspaisSanitaris a owl:Class . |

## Tabla 2: owl:DatatypeProperty de cada clase

| Clase | DatatypeProperty | Expresión Turtle |
| - | - | - |
| Brigadistes | nom | :nom a owl:DatatypeProperty ; rdfs:domain :Brigadistes ; rdfs:range xsd:string . |
| Brigadistes | aliesDelBrigadista | :aliesDelBrigadista a owl:DatatypeProperty ; rdfs:domain :Brigadistes ; rdfs:range xsd:string . |
| Brigadistes | llocnaixement | :llocnaixement a owl:DatatypeProperty ; rdfs:domain :Brigadistes ; rdfs:range xsd:string . |
| Brigadistes | dataDeNaixement | :dataDeNaixement a owl:DatatypeProperty ; rdfs:domain :Brigadistes ; rdfs:range xsd:string . |
| Brigadistes | dataDeDefunció | :dataDeDefunció a owl:DatatypeProperty ; rdfs:domain :Brigadistes ; rdfs:range xsd:string . |
| Brigadistes | llocdefuncio | :llocdefuncio a owl:DatatypeProperty ; rdfs:domain :Brigadistes ; rdfs:range xsd:string . |
| Brigadistes | dadesSegonsLaFont | :dadesSegonsLaFont a owl:DatatypeProperty ; rdfs:domain :Brigadistes ; rdfs:range xsd:string . |
| Brigadistes | geologcalitzacioNaixement | :geologcalitzacioNaixement a owl:DatatypeProperty ; rdfs:domain :Brigadistes ; rdfs:range xsd:string . |
| Brigadistes | geologcalitzacioMort | :geologcalitzacioMort a owl:DatatypeProperty ; rdfs:domain :Brigadistes ; rdfs:range xsd:string . |
| Professions | nomprofessio | :nomprofessio a owl:DatatypeProperty ; rdfs:domain :Professions ; rdfs:range xsd:string . |
| Països | nompais | :nompais a owl:DatatypeProperty ; rdfs:domain :Països ; rdfs:range xsd:string . |
| ProcedènciaReligióÈtnia | nomcaracterística | :nomcaracterística a owl:DatatypeProperty ; rdfs:domain :ProcedènciaReligióÈtnia ; rdfs:range xsd:string . |
| Tipuscaracteristica | nomcaracterística | :nomcaracterística a owl:DatatypeProperty ; rdfs:domain :Tipuscaracteristica ; rdfs:range xsd:string . |
| IdeologiesPolítiques | nomideologia | :nomideologia a owl:DatatypeProperty ; rdfs:domain :IdeologiesPolítiques ; rdfs:range xsd:string . |
| Organitzacions | nomorganitzacio | :nomorganitzacio a owl:DatatypeProperty ; rdfs:domain :Organitzacions ; rdfs:range xsd:string . |
| BatallesFronts | nomescenari | :nomescenari a owl:DatatypeProperty ; rdfs:domain :BatallesFronts ; rdfs:range xsd:string . |
| BatallesFronts | dates | :dates a owl:DatatypeProperty ; rdfs:domain :BatallesFronts ; rdfs:range xsd:string . |
| BatallesFronts | datainici | :datainici a owl:DatatypeProperty ; rdfs:domain :BatallesFronts ; rdfs:range xsd:string . |
| BatallesFronts | datafi | :datafi a owl:DatatypeProperty ; rdfs:domain :BatallesFronts ; rdfs:range xsd:string . |
| BatallesFronts | informacioAddicional | :informacioAddicional a owl:DatatypeProperty ; rdfs:domain :BatallesFronts ; rdfs:range xsd:string . |
| BatallesFronts | geolocalització | :geolocalització a owl:DatatypeProperty ; rdfs:domain :BatallesFronts ; rdfs:range xsd:string . |
| EscenarisBelics | tipusescenari | :tipusescenari a owl:DatatypeProperty ; rdfs:domain :EscenarisBelics ; rdfs:range xsd:string . |
| BrigadistesEscenarisBellics | dataInici | :dataInici a owl:DatatypeProperty ; rdfs:domain :BrigadistesEscenarisBellics ; rdfs:range xsd:string . |
| BrigadistesEscenarisBellics | dataFi | :dataFi a owl:DatatypeProperty ; rdfs:domain :BrigadistesEscenarisBellics ; rdfs:range xsd:string . |
| TipusEscenaris | tipusescenari | :tipusescenari a owl:DatatypeProperty ; rdfs:domain :TipusEscenaris ; rdfs:range xsd:string . |
| Esdeveniments | descripcióesdeveniment | :descripcióesdeveniment a owl:DatatypeProperty ; rdfs:domain :Esdeveniments ; rdfs:range xsd:string . |
| BrigadistesEsdeveniments | dataInici | :dataInici a owl:DatatypeProperty ; rdfs:domain :BrigadistesEsdeveniments ; rdfs:range xsd:string . |
| BrigadistesEsdeveniments | dataFi | :dataFi a owl:DatatypeProperty ; rdfs:domain :BrigadistesEsdeveniments ; rdfs:range xsd:string . |
| TipusEsdeveniments | tipusescenari | :tipusescenari a owl:DatatypeProperty ; rdfs:domain :TipusEsdeveniments ; rdfs:range xsd:string . |
| BatallesFrontsRelacionats | datarelacio | :datarelacio a owl:DatatypeProperty ; rdfs:domain :BatallesFrontsRelacionats ; rdfs:range xsd:string . |
| EstructuresMilitars | nomestructura | :nomestructura a owl:DatatypeProperty ; rdfs:domain :EstructuresMilitars ; rdfs:range xsd:string . |
| EstructuresMilitars | descripcióEstructuraIActuacións | :descripcióEstructuraIActuacións a owl:DatatypeProperty ; rdfs:domain :EstructuresMilitars ; rdfs:range xsd:string . |
| TipusEstructures | nomestructura | :nomestructura a owl:DatatypeProperty ; rdfs:domain :TipusEstructures ; rdfs:range xsd:string . |
| BrigadistesEstructures | dataInici | :dataInici a owl:DatatypeProperty ; rdfs:domain :BrigadistesEstructures ; rdfs:range xsd:string . |
| BrigadistesEstructures | dataFi | :dataFi a owl:DatatypeProperty ; rdfs:domain :BrigadistesEstructures ; rdfs:range xsd:string . |
| Llocs | nomlloc | :nomlloc a owl:DatatypeProperty ; rdfs:domain :Llocs ; rdfs:range xsd:string . |
| Llocs | comarca | :comarca a owl:DatatypeProperty ; rdfs:domain :Llocs ; rdfs:range xsd:string . |
| Llocs | provincia | :provincia a owl:DatatypeProperty ; rdfs:domain :Llocs ; rdfs:range xsd:string . |
| Llocs | regió | :regió a owl:DatatypeProperty ; rdfs:domain :Llocs ; rdfs:range xsd:string . |
| Llocs | coordenades | :coordenades a owl:DatatypeProperty ; rdfs:domain :Llocs ; rdfs:range xsd:string . |
| Llocs | idpais | :idpais a owl:DatatypeProperty ; rdfs:domain :Llocs ; rdfs:range xsd:string . |
| FontsDocumentals | titol | :titol a owl:DatatypeProperty ; rdfs:domain :FontsDocumentals ; rdfs:range xsd:string . |
| FontsDocumentals | autor | :autor a owl:DatatypeProperty ; rdfs:domain :FontsDocumentals ; rdfs:range xsd:string . |
| FontsDocumentals | referenciaCompleta | :referenciaCompleta a owl:DatatypeProperty ; rdfs:domain :FontsDocumentals ; rdfs:range xsd:string . |
| FontsDocumentals | anyD'Edició | :anyD'Edició a owl:DatatypeProperty ; rdfs:domain :FontsDocumentals ; rdfs:range xsd:string . |
| FontsDocumentals | llocD'Edició | :llocD'Edició a owl:DatatypeProperty ; rdfs:domain :FontsDocumentals ; rdfs:range xsd:string . |
| Idiomes | nomidioma | :nomidioma a owl:DatatypeProperty ; rdfs:domain :Idiomes ; rdfs:range xsd:string . |
| Enfocaments | nomenfocament | :nomenfocament a owl:DatatypeProperty ; rdfs:domain :Enfocaments ; rdfs:range xsd:string . |
| LiteraturaMitjansComunicacio | nomliteraturamitjans | :nomliteraturamitjans a owl:DatatypeProperty ; rdfs:domain :LiteraturaMitjansComunicacio ; rdfs:range xsd:string . |
| Cultura | nomcultura | :nomcultura a owl:DatatypeProperty ; rdfs:domain :Cultura ; rdfs:range xsd:string . |
| TipusDocumental | nomtipusdocumental | :nomtipusdocumental a owl:DatatypeProperty ; rdfs:domain :TipusDocumental ; rdfs:range xsd:string . |
| Moviments | nommoviment | :nommoviment a owl:DatatypeProperty ; rdfs:domain :Moviments ; rdfs:range xsd:string . |
| PresonsCamps | nompresoccamp | :nompresoccamp a owl:DatatypeProperty ; rdfs:domain :PresonsCamps ; rdfs:range xsd:string . |
| PresonsCamps | descripció | :descripció a owl:DatatypeProperty ; rdfs:domain :PresonsCamps ; rdfs:range xsd:string . |
| PresonsCamps | geolocalitzacio | :geolocalitzacio a owl:DatatypeProperty ; rdfs:domain :PresonsCamps ; rdfs:range xsd:string . |
| BrigadistesPresonsCamps | dataInici | :dataInici a owl:DatatypeProperty ; rdfs:domain :BrigadistesPresonsCamps ; rdfs:range xsd:string . |
| BrigadistesPresonsCamps | dataFi | :dataFi a owl:DatatypeProperty ; rdfs:domain :BrigadistesPresonsCamps ; rdfs:range xsd:string . |
| EspaisSanitaris | nomespaisanitari | :nomespaisanitari a owl:DatatypeProperty ; rdfs:domain :EspaisSanitaris ; rdfs:range xsd:string . |
| EspaisSanitaris | descripció | :descripció a owl:DatatypeProperty ; rdfs:domain :EspaisSanitaris ; rdfs:range xsd:string . |
| EspaisSanitaris | geolocalitzacio | :geolocalitzacio a owl:DatatypeProperty ; rdfs:domain :EspaisSanitaris ; rdfs:range xsd:string . |
| BrigadistesEspaisSanitaris | dataInici | :dataInici a owl:DatatypeProperty ; rdfs:domain :BrigadistesEspaisSanitaris ; rdfs:range xsd:string . |
| BrigadistesEspaisSanitaris | dataFi | :dataFi a owl:DatatypeProperty ; rdfs:domain :BrigadistesEspaisSanitaris ; rdfs:range xsd:string . |

## Tabla de Relaciones (owl:ObjectProperty)

| Relación | Dominio | Rango | Es inversa de | Expresión Turtle |
| - | - | - | - | - |
| hasPaïsosProcedencia | Brigadistes | Països | isPaïsosProcedenciaOf | :hasPaïsosProcedencia a owl:ObjectProperty ; rdfs:domain :Brigadistes ; rdfs:range :Països . |
| isPaïsosProcedenciaOf | Països | Brigadistes | hasPaïsosProcedencia | :isPaïsosProcedenciaOf a owl:ObjectProperty ; rdfs:domain :Països ; rdfs:range :Brigadistes . |
| hasTipuscaracteristica | ProcedènciaReligióÈtnia | Tipuscaracteristica | isTipuscaracteristicaOf | :hasTipuscaracteristica a owl:ObjectProperty ; rdfs:domain :ProcedènciaReligióÈtnia ; rdfs:range :Tipuscaracteristica . |
| isTipuscaracteristicaOf | Tipuscaracteristica | ProcedènciaReligióÈtnia | hasTipuscaracteristica | :isTipuscaracteristicaOf a owl:ObjectProperty ; rdfs:domain :Tipuscaracteristica ; rdfs:range :ProcedènciaReligióÈtnia . |
| hasTipusEscenaris | Llocs | TipusEscenaris | hasLlocs | :hasTipusEscenaris a owl:ObjectProperty ; rdfs:domain :Llocs ; rdfs:range :TipusEscenaris . |
| hasBatallesFronts | BatallesFrontsRelacionats | BatallesFronts | isBatallesFrontsOf | :hasBatallesFronts a owl:ObjectProperty ; rdfs:domain :BatallesFrontsRelacionats ; rdfs:range :BatallesFronts . |
| isBatallesFrontsOf | BatallesFronts | BatallesFrontsRelacionats | hasBatallesFronts | :isBatallesFrontsOf a owl:ObjectProperty ; rdfs:domain :BatallesFronts ; rdfs:range :BatallesFrontsRelacionats . |
| hasBrigadistes | Moviments | Brigadistes | hasMoviments | :hasBrigadistes a owl:ObjectProperty ; rdfs:domain :Moviments ; rdfs:range :Brigadistes . |
| isBrigadistesOf | Brigadistes | BrigadistesEstructures | hasBrigadistes | :isBrigadistesOf a owl:ObjectProperty ; rdfs:domain :Brigadistes ; rdfs:range :BrigadistesEstructures . |
| hasEsdeveniments | Esdeveniments | Esdeveniments | isEsdevenimentsOf | :hasEsdeveniments a owl:ObjectProperty ; rdfs:domain :Esdeveniments ; rdfs:range :Esdeveniments . |
| isEsdevenimentsOf | Esdeveniments | Esdeveniments | hasEsdeveniments | :isEsdevenimentsOf a owl:ObjectProperty ; rdfs:domain :Esdeveniments ; rdfs:range :Esdeveniments . |
| hasTipusEsdeveniments | BrigadistesEsdeveniments | TipusEsdeveniments | isTipusEsdevenimentsOf | :hasTipusEsdeveniments a owl:ObjectProperty ; rdfs:domain :BrigadistesEsdeveniments ; rdfs:range :TipusEsdeveniments . |
| isTipusEsdevenimentsOf | TipusEsdeveniments | BrigadistesEsdeveniments | hasTipusEsdeveniments | :isTipusEsdevenimentsOf a owl:ObjectProperty ; rdfs:domain :TipusEsdeveniments ; rdfs:range :BrigadistesEsdeveniments . |
| hasTipusEstructures | EstructuresMilitars | TipusEstructures | isTipusEstructuresOf | :hasTipusEstructures a owl:ObjectProperty ; rdfs:domain :EstructuresMilitars ; rdfs:range :TipusEstructures . |
| isTipusEstructuresOf | TipusEstructures | EstructuresMilitars | hasTipusEstructures | :isTipusEstructuresOf a owl:ObjectProperty ; rdfs:domain :TipusEstructures ; rdfs:range :EstructuresMilitars . |
| hasEstructuresMilitars | BrigadistesEstructures | EstructuresMilitars | isEstructuresMilitarsOf | :hasEstructuresMilitars a owl:ObjectProperty ; rdfs:domain :BrigadistesEstructures ; rdfs:range :EstructuresMilitars . |
| isEstructuresMilitarsOf | EstructuresMilitars | BrigadistesEstructures | hasEstructuresMilitars | :isEstructuresMilitarsOf a owl:ObjectProperty ; rdfs:domain :EstructuresMilitars ; rdfs:range :BrigadistesEstructures . |
| hasIdeologiesPolítiques | Brigadistes | IdeologiesPolítiques | hasBrigadistes | :hasIdeologiesPolítiques a owl:ObjectProperty ; rdfs:domain :Brigadistes ; rdfs:range :IdeologiesPolítiques . |
| hasLlocs | TipusEscenaris | Llocs | hasTipusEscenaris | :hasLlocs a owl:ObjectProperty ; rdfs:domain :TipusEscenaris ; rdfs:range :Llocs . |
| hasFontsDocumentals | TipusDocumental | FontsDocumentals | hasTipusDocumental | :hasFontsDocumentals a owl:ObjectProperty ; rdfs:domain :TipusDocumental ; rdfs:range :FontsDocumentals . |
| hasIdiomes | FontsDocumentals | Idiomes | hasFontsDocumentals | :hasIdiomes a owl:ObjectProperty ; rdfs:domain :FontsDocumentals ; rdfs:range :Idiomes . |
| hasEnfocaments | FontsDocumentals | Enfocaments | hasFontsDocumentals | :hasEnfocaments a owl:ObjectProperty ; rdfs:domain :FontsDocumentals ; rdfs:range :Enfocaments . |
| hasLiteraturaMitjansComunicacio | FontsDocumentals | LiteraturaMitjansComunicacio | hasFontsDocumentals | :hasLiteraturaMitjansComunicacio a owl:ObjectProperty ; rdfs:domain :FontsDocumentals ; rdfs:range :LiteraturaMitjansComunicacio . |
| hasCultura | FontsDocumentals | Cultura | hasFontsDocumentals | :hasCultura a owl:ObjectProperty ; rdfs:domain :FontsDocumentals ; rdfs:range :Cultura . |
| hasTipusDocumental | FontsDocumentals | TipusDocumental | hasFontsDocumentals | :hasTipusDocumental a owl:ObjectProperty ; rdfs:domain :FontsDocumentals ; rdfs:range :TipusDocumental . |
| hasMoviments | Brigadistes | Moviments | hasBrigadistes | :hasMoviments a owl:ObjectProperty ; rdfs:domain :Brigadistes ; rdfs:range :Moviments . |
| hasPresonsCamps | BrigadistesPresonsCamps | PresonsCamps | isPresonsCampsOf | :hasPresonsCamps a owl:ObjectProperty ; rdfs:domain :BrigadistesPresonsCamps ; rdfs:range :PresonsCamps . |
| isPresonsCampsOf | PresonsCamps | BrigadistesPresonsCamps | hasPresonsCamps | :isPresonsCampsOf a owl:ObjectProperty ; rdfs:domain :PresonsCamps ; rdfs:range :BrigadistesPresonsCamps . |
| hasBrigadistesPresonsCamps | Brigadistes | BrigadistesPresonsCamps | isBrigadistesPresonsCampsOf | :hasBrigadistesPresonsCamps a owl:ObjectProperty ; rdfs:domain :Brigadistes ; rdfs:range :BrigadistesPresonsCamps . |
| isBrigadistesPresonsCampsOf | BrigadistesPresonsCamps | Brigadistes | hasBrigadistesPresonsCamps | :isBrigadistesPresonsCampsOf a owl:ObjectProperty ; rdfs:domain :BrigadistesPresonsCamps ; rdfs:range :Brigadistes . |
| hasTipusEscenarisPresonsCamps | PresonsCamps | TipusEscenaris | isTipusEscenarisPresonsCampsOf | :hasTipusEscenarisPresonsCamps a owl:ObjectProperty ; rdfs:domain :PresonsCamps ; rdfs:range :TipusEscenaris . |
| isTipusEscenarisPresonsCampsOf | TipusEscenaris | PresonsCamps | hasTipusEscenarisPresonsCamps | :isTipusEscenarisPresonsCampsOf a owl:ObjectProperty ; rdfs:domain :TipusEscenaris ; rdfs:range :PresonsCamps . |
| hasEspaisSanitaris | BrigadistesEspaisSanitaris | EspaisSanitaris | isEspaisSanitarisOf | :hasEspaisSanitaris a owl:ObjectProperty ; rdfs:domain :BrigadistesEspaisSanitaris ; rdfs:range :EspaisSanitaris . |
| isEspaisSanitarisOf | EspaisSanitaris | BrigadistesEspaisSanitaris | hasEspaisSanitaris | :isEspaisSanitarisOf a owl:ObjectProperty ; rdfs:domain :EspaisSanitaris ; rdfs:range :BrigadistesEspaisSanitaris . |
| hasBrigadistesEspaisSanitaris | Brigadistes | BrigadistesEspaisSanitaris | isBrigadistesEspaisSanitarisOf | :hasBrigadistesEspaisSanitaris a owl:ObjectProperty ; rdfs:domain :Brigadistes ; rdfs:range :BrigadistesEspaisSanitaris . |
| isBrigadistesEspaisSanitarisOf | BrigadistesEspaisSanitaris | Brigadistes | hasBrigadistesEspaisSanitaris | :isBrigadistesEspaisSanitarisOf a owl:ObjectProperty ; rdfs:domain :BrigadistesEspaisSanitaris ; rdfs:range :Brigadistes . |
| hasTipusEscenarisEspaisSanitaris | EspaisSanitaris | TipusEscenaris | isTipusEscenarisEspaisSanitarisOf | :hasTipusEscenarisEspaisSanitaris a owl:ObjectProperty ; rdfs:domain :EspaisSanitaris ; rdfs:range :TipusEscenaris . |
| isTipusEscenarisEspaisSanitarisOf | TipusEscenaris | EspaisSanitaris | hasTipusEscenarisEspaisSanitaris | :isTipusEscenarisEspaisSanitarisOf a owl:ObjectProperty ; rdfs:domain :TipusEscenaris ; rdfs:range :EspaisSanitaris . |

## Tabla de Inferencias

| Inferencia | Tipo | Explicación | Expresión Turtle (TTL) |
| - | - | - | - |
| Si un Brigadistes hasPaïsosProcedencia un Països, entonces ese Països isPaïsosProcedenciaOf ese Brigadistes | Implícita | Por las propiedades inversas owl:inverseOf entre hasPaïsosProcedencia y isPaïsosProcedenciaOf | :hasPaïsosProcedencia owl:inverseOf :isPaïsosProcedenciaOf . |
| Si un Països isPaïsosProcedenciaOf un Brigadistes, entonces ese Brigadistes hasPaïsosProcedencia ese Països | Implícita | Por las propiedades inversas owl:inverseOf entre isPaïsosProcedenciaOf y hasPaïsosProcedencia | :isPaïsosProcedenciaOf owl:inverseOf :hasPaïsosProcedencia . |
| Si un ProcedènciaReligióÈtnia hasTipuscaracteristica un Tipuscaracteristica, entonces ese Tipuscaracteristica isTipuscaracteristicaOf ese ProcedènciaReligióÈtnia | Implícita | Por las propiedades inversas owl:inverseOf entre hasTipuscaracteristica y isTipuscaracteristicaOf | :hasTipuscaracteristica owl:inverseOf :isTipuscaracteristicaOf . |
| Si un Tipuscaracteristica isTipuscaracteristicaOf un ProcedènciaReligióÈtnia, entonces ese ProcedènciaReligióÈtnia hasTipuscaracteristica ese Tipuscaracteristica | Implícita | Por las propiedades inversas owl:inverseOf entre isTipuscaracteristicaOf y hasTipuscaracteristica | :isTipuscaracteristicaOf owl:inverseOf :hasTipuscaracteristica . |
| Si un Llocs hasTipusEscenaris un TipusEscenaris, entonces ese TipusEscenaris hasLlocs ese Llocs | Implícita | Por las propiedades inversas owl:inverseOf entre hasTipusEscenaris y hasLlocs | :hasTipusEscenaris owl:inverseOf :hasLlocs . |
| Si un BatallesFrontsRelacionats hasBatallesFronts un BatallesFronts, entonces ese BatallesFronts isBatallesFrontsOf ese BatallesFrontsRelacionats | Implícita | Por las propiedades inversas owl:inverseOf entre hasBatallesFronts y isBatallesFrontsOf | :hasBatallesFronts owl:inverseOf :isBatallesFrontsOf . |
| Si un BatallesFronts isBatallesFrontsOf un BatallesFrontsRelacionats, entonces ese BatallesFrontsRelacionats hasBatallesFronts ese BatallesFronts | Implícita | Por las propiedades inversas owl:inverseOf entre isBatallesFrontsOf y hasBatallesFronts | :isBatallesFrontsOf owl:inverseOf :hasBatallesFronts . |
| Si un Moviments hasBrigadistes un Brigadistes, entonces ese Brigadistes hasMoviments ese Moviments | Implícita | Por las propiedades inversas owl:inverseOf entre hasBrigadistes y hasMoviments | :hasBrigadistes owl:inverseOf :hasMoviments . |
| Si un Brigadistes isBrigadistesOf un BrigadistesEstructures, entonces ese BrigadistesEstructures hasBrigadistes ese Brigadistes | Implícita | Por las propiedades inversas owl:inverseOf entre isBrigadistesOf y hasBrigadistes | :isBrigadistesOf owl:inverseOf :hasBrigadistes . |
| Si un Esdeveniments hasEsdeveniments un Esdeveniments, entonces ese Esdeveniments isEsdevenimentsOf ese Esdeveniments | Implícita | Por las propiedades inversas owl:inverseOf entre hasEsdeveniments y isEsdevenimentsOf | :hasEsdeveniments owl:inverseOf :isEsdevenimentsOf . |
| Si un Esdeveniments isEsdevenimentsOf un Esdeveniments, entonces ese Esdeveniments hasEsdeveniments ese Esdeveniments | Implícita | Por las propiedades inversas owl:inverseOf entre isEsdevenimentsOf y hasEsdeveniments | :isEsdevenimentsOf owl:inverseOf :hasEsdeveniments . |
| Si un BrigadistesEsdeveniments hasTipusEsdeveniments un TipusEsdeveniments, entonces ese TipusEsdeveniments isTipusEsdevenimentsOf ese BrigadistesEsdeveniments | Implícita | Por las propiedades inversas owl:inverseOf entre hasTipusEsdeveniments y isTipusEsdevenimentsOf | :hasTipusEsdeveniments owl:inverseOf :isTipusEsdevenimentsOf . |
| Si un TipusEsdeveniments isTipusEsdevenimentsOf un BrigadistesEsdeveniments, entonces ese BrigadistesEsdeveniments hasTipusEsdeveniments ese TipusEsdeveniments | Implícita | Por las propiedades inversas owl:inverseOf entre isTipusEsdevenimentsOf y hasTipusEsdeveniments | :isTipusEsdevenimentsOf owl:inverseOf :hasTipusEsdeveniments . |
| Si un EstructuresMilitars hasTipusEstructures un TipusEstructures, entonces ese TipusEstructures isTipusEstructuresOf ese EstructuresMilitars | Implícita | Por las propiedades inversas owl:inverseOf entre hasTipusEstructures y isTipusEstructuresOf | :hasTipusEstructures owl:inverseOf :isTipusEstructuresOf . |
| Si un TipusEstructures isTipusEstructuresOf un EstructuresMilitars, entonces ese EstructuresMilitars hasTipusEstructures ese TipusEstructures | Implícita | Por las propiedades inversas owl:inverseOf entre isTipusEstructuresOf y hasTipusEstructures | :isTipusEstructuresOf owl:inverseOf :hasTipusEstructures . |
| Si un BrigadistesEstructures hasEstructuresMilitars un EstructuresMilitars, entonces ese EstructuresMilitars isEstructuresMilitarsOf ese BrigadistesEstructures | Implícita | Por las propiedades inversas owl:inverseOf entre hasEstructuresMilitars y isEstructuresMilitarsOf | :hasEstructuresMilitars owl:inverseOf :isEstructuresMilitarsOf . |
| Si un EstructuresMilitars isEstructuresMilitarsOf un BrigadistesEstructures, entonces ese BrigadistesEstructures hasEstructuresMilitars ese EstructuresMilitars | Implícita | Por las propiedades inversas owl:inverseOf entre isEstructuresMilitarsOf y hasEstructuresMilitars | :isEstructuresMilitarsOf owl:inverseOf :hasEstructuresMilitars . |
| Si un Brigadistes hasIdeologiesPolítiques un IdeologiesPolítiques, entonces ese IdeologiesPolítiques hasBrigadistes ese Brigadistes | Implícita | Por las propiedades inversas owl:inverseOf entre hasIdeologiesPolítiques y hasBrigadistes | :hasIdeologiesPolítiques owl:inverseOf :hasBrigadistes . |
| Si un TipusEscenaris hasLlocs un Llocs, entonces ese Llocs hasTipusEscenaris ese TipusEscenaris | Implícita | Por las propiedades inversas owl:inverseOf entre hasLlocs y hasTipusEscenaris | :hasLlocs owl:inverseOf :hasTipusEscenaris . |
| Si un TipusDocumental hasFontsDocumentals un FontsDocumentals, entonces ese FontsDocumentals hasTipusDocumental ese TipusDocumental | Implícita | Por las propiedades inversas owl:inverseOf entre hasFontsDocumentals y hasTipusDocumental | :hasFontsDocumentals owl:inverseOf :hasTipusDocumental . |
| Si un FontsDocumentals hasIdiomes un Idiomes, entonces ese Idiomes hasFontsDocumentals ese FontsDocumentals | Implícita | Por las propiedades inversas owl:inverseOf entre hasIdiomes y hasFontsDocumentals | :hasIdiomes owl:inverseOf :hasFontsDocumentals . |
| Si un FontsDocumentals hasEnfocaments un Enfocaments, entonces ese Enfocaments hasFontsDocumentals ese FontsDocumentals | Implícita | Por las propiedades inversas owl:inverseOf entre hasEnfocaments y hasFontsDocumentals | :hasEnfocaments owl:inverseOf :hasFontsDocumentals . |
| Si un FontsDocumentals hasLiteraturaMitjansComunicacio un LiteraturaMitjansComunicacio, entonces ese LiteraturaMitjansComunicacio hasFontsDocumentals ese FontsDocumentals | Implícita | Por las propiedades inversas owl:inverseOf entre hasLiteraturaMitjansComunicacio y hasFontsDocumentals | :hasLiteraturaMitjansComunicacio owl:inverseOf :hasFontsDocumentals . |
| Si un FontsDocumentals hasCultura un Cultura, entonces ese Cultura hasFontsDocumentals ese FontsDocumentals | Implícita | Por las propiedades inversas owl:inverseOf entre hasCultura y hasFontsDocumentals | :hasCultura owl:inverseOf :hasFontsDocumentals . |
| Si un FontsDocumentals hasTipusDocumental un TipusDocumental, entonces ese TipusDocumental hasFontsDocumentals ese FontsDocumentals | Implícita | Por las propiedades inversas owl:inverseOf entre hasTipusDocumental y hasFontsDocumentals | :hasTipusDocumental owl:inverseOf :hasFontsDocumentals . |
| Si un Brigadistes hasMoviments un Moviments, entonces ese Moviments hasBrigadistes ese Brigadistes | Implícita | Por las propiedades inversas owl:inverseOf entre hasMoviments y hasBrigadistes | :hasMoviments owl:inverseOf :hasBrigadistes . |
| Si un BrigadistesPresonsCamps hasPresonsCamps un PresonsCamps, entonces ese PresonsCamps isPresonsCampsOf ese BrigadistesPresonsCamps | Implícita | Por las propiedades inversas owl:inverseOf entre hasPresonsCamps y isPresonsCampsOf | :hasPresonsCamps owl:inverseOf :isPresonsCampsOf . |
| Si un PresonsCamps isPresonsCampsOf un BrigadistesPresonsCamps, entonces ese BrigadistesPresonsCamps hasPresonsCamps ese PresonsCamps | Implícita | Por las propiedades inversas owl:inverseOf entre isPresonsCampsOf y hasPresonsCamps | :isPresonsCampsOf owl:inverseOf :hasPresonsCamps . |
| Si un Brigadistes hasBrigadistesPresonsCamps un BrigadistesPresonsCamps, entonces ese BrigadistesPresonsCamps isBrigadistesPresonsCampsOf ese Brigadistes | Implícita | Por las propiedades inversas owl:inverseOf entre hasBrigadistesPresonsCamps y isBrigadistesPresonsCampsOf | :hasBrigadistesPresonsCamps owl:inverseOf :isBrigadistesPresonsCampsOf . |
| Si un BrigadistesPresonsCamps isBrigadistesPresonsCampsOf un Brigadistes, entonces ese Brigadistes hasBrigadistesPresonsCamps ese BrigadistesPresonsCamps | Implícita | Por las propiedades inversas owl:inverseOf entre isBrigadistesPresonsCampsOf y hasBrigadistesPresonsCamps | :isBrigadistesPresonsCampsOf owl:inverseOf :hasBrigadistesPresonsCamps . |
| Si un PresonsCamps hasTipusEscenarisPresonsCamps un TipusEscenaris, entonces ese TipusEscenaris isTipusEscenarisPresonsCampsOf ese PresonsCamps | Implícita | Por las propiedades inversas owl:inverseOf entre hasTipusEscenarisPresonsCamps y isTipusEscenarisPresonsCampsOf | :hasTipusEscenarisPresonsCamps owl:inverseOf :isTipusEscenarisPresonsCampsOf . |
| Si un TipusEscenaris isTipusEscenarisPresonsCampsOf un PresonsCamps, entonces ese PresonsCamps hasTipusEscenarisPresonsCamps ese TipusEscenaris | Implícita | Por las propiedades inversas owl:inverseOf entre isTipusEscenarisPresonsCampsOf y hasTipusEscenarisPresonsCamps | :isTipusEscenarisPresonsCampsOf owl:inverseOf :hasTipusEscenarisPresonsCamps . |
| Si un BrigadistesEspaisSanitaris hasEspaisSanitaris un EspaisSanitaris, entonces ese EspaisSanitaris isEspaisSanitarisOf ese BrigadistesEspaisSanitaris | Implícita | Por las propiedades inversas owl:inverseOf entre hasEspaisSanitaris y isEspaisSanitarisOf | :hasEspaisSanitaris owl:inverseOf :isEspaisSanitarisOf . |
| Si un EspaisSanitaris isEspaisSanitarisOf un BrigadistesEspaisSanitaris, entonces ese BrigadistesEspaisSanitaris hasEspaisSanitaris ese EspaisSanitaris | Implícita | Por las propiedades inversas owl:inverseOf entre isEspaisSanitarisOf y hasEspaisSanitaris | :isEspaisSanitarisOf owl:inverseOf :hasEspaisSanitaris . |
| Si un Brigadistes hasBrigadistesEspaisSanitaris un BrigadistesEspaisSanitaris, entonces ese BrigadistesEspaisSanitaris isBrigadistesEspaisSanitarisOf ese Brigadistes | Implícita | Por las propiedades inversas owl:inverseOf entre hasBrigadistesEspaisSanitaris y isBrigadistesEspaisSanitarisOf | :hasBrigadistesEspaisSanitaris owl:inverseOf :isBrigadistesEspaisSanitarisOf . |
| Si un BrigadistesEspaisSanitaris isBrigadistesEspaisSanitarisOf un Brigadistes, entonces ese Brigadistes hasBrigadistesEspaisSanitaris ese BrigadistesEspaisSanitaris | Implícita | Por las propiedades inversas owl:inverseOf entre isBrigadistesEspaisSanitarisOf y hasBrigadistesEspaisSanitaris | :isBrigadistesEspaisSanitarisOf owl:inverseOf :hasBrigadistesEspaisSanitaris . |
| Si un EspaisSanitaris hasTipusEscenarisEspaisSanitaris un TipusEscenaris, entonces ese TipusEscenaris isTipusEscenarisEspaisSanitarisOf ese EspaisSanitaris | Implícita | Por las propiedades inversas owl:inverseOf entre hasTipusEscenarisEspaisSanitaris y isTipusEscenarisEspaisSanitarisOf | :hasTipusEscenarisEspaisSanitaris owl:inverseOf :isTipusEscenarisEspaisSanitarisOf . |
| Si un TipusEscenaris isTipusEscenarisEspaisSanitarisOf un EspaisSanitaris, entonces ese EspaisSanitaris hasTipusEscenarisEspaisSanitaris ese TipusEscenaris | Implícita | Por las propiedades inversas owl:inverseOf entre isTipusEscenarisEspaisSanitarisOf y hasTipusEscenarisEspaisSanitaris | :isTipusEscenarisEspaisSanitarisOf owl:inverseOf :hasTipusEscenarisEspaisSanitaris . |

