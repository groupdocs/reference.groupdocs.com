---
title: GroupDocs.Assembly.Data
second_title: Referencia de API de GroupDocs.Assembly para .NET
description: Proporciona clases para acceder a datos de documentos externos que se utilizarán al ensamblar un documento.
type: docs
weight: 20
url: /es/net/groupdocs.assembly.data/
---
Proporciona clases para acceder a datos de documentos externos que se utilizarán al ensamblar un documento.

## Clases

| Clase | Descripción |
| --- | --- |
| [CsvDataLoadOptions](./csvdataloadoptions) | Representa opciones para analizar datos CSV. |
| [CsvDataSource](./csvdatasource) | Proporciona acceso a los datos de un archivo CSV o flujo que se usará al ensamblar un documento. |
| [DocumentTable](./documenttable) | Proporciona acceso a los datos de una sola tabla (u hoja de cálculo) ubicada en un documento externo que se utilizará mientras ensambla un documento. |
| [DocumentTableCollection](./documenttablecollection) | Representa una colección de solo lectura de[`DocumentTable`](../groupdocs.assembly.data/documenttable) objetos de un particular[`DocumentTableSet`](../groupdocs.assembly.data/documenttableset) instancia. |
| [DocumentTableColumn](./documenttablecolumn) | Representa una sola columna de un determinado[`DocumentTable`](../groupdocs.assembly.data/documenttable) objeto. |
| [DocumentTableColumnCollection](./documenttablecolumncollection) | Representa una colección de solo lectura de[`DocumentTableColumn`](../groupdocs.assembly.data/documenttablecolumn) objetos de un particular[`DocumentTable`](../groupdocs.assembly.data/documenttable) instancia. |
| [DocumentTableLoadArgs](./documenttableloadargs) | Proporciona datos para el[`Handle`](../groupdocs.assembly.data/idocumenttableloadhandler/handle) método. |
| [DocumentTableOptions](./documenttableoptions) | Proporciona un conjunto de opciones para controlar la extracción de datos de una tabla de documentos. |
| [DocumentTableRelation](./documenttablerelation) | Representa una relación padre-hijo entre dos[`DocumentTable`](../groupdocs.assembly.data/documenttable) objetos. |
| [DocumentTableRelationCollection](./documenttablerelationcollection) | Representa la colección de[`DocumentTableRelation`](../groupdocs.assembly.data/documenttablerelation) objetos de un solo[`DocumentTableSet`](../groupdocs.assembly.data/documenttableset) instancia. |
| [DocumentTableSet](./documenttableset) | Proporciona acceso a datos de varias tablas (u hojas de cálculo) ubicadas en un documento externo para usar mientras ensambla un documento. Además, permite definir relaciones padre-hijo para las tablas de documentos, lo que simplifica el acceso a los datos relacionados dentro de los documentos de plantilla. |
| [JsonDataLoadOptions](./jsondataloadoptions) | Representa opciones para analizar datos JSON. |
| [JsonDataSource](./jsondatasource) | Proporciona acceso a los datos de un archivo JSON o flujo que se usará al ensamblar un documento. |
| [XmlDataLoadOptions](./xmldataloadoptions) | Representa opciones para la carga de datos XML. |
| [XmlDataSource](./xmldatasource) | Proporciona acceso a los datos de un archivo o flujo XML que se usará al ensamblar un documento. |
## Interfaces

| Interfaz | Descripción |
| --- | --- |
| [IDocumentTableLoadHandler](./idocumenttableloadhandler) | Anula la carga predeterminada de[`DocumentTable`](../groupdocs.assembly.data/documenttable) objetos al crear un[`DocumentTableSet`](../groupdocs.assembly.data/documenttableset) instancia. |
## Enumeración

| Enumeración | Descripción |
| --- | --- |
| [JsonSimpleValueParseMode](./jsonsimplevalueparsemode) | Especifica un modo para analizar valores simples de JSON (null, boolean, number, integer y string) mientras se carga JSON. Este modo no afecta el análisis de los valores de fecha y hora. |

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Assembly.dll -->