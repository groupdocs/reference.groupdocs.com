---
title: JsonDataLoadOptions
second_title: Referencia de API de GroupDocs.Assembly para .NET
description: Representa opciones para analizar datos JSON.
type: docs
weight: 140
url: /es/net/groupdocs.assembly.data/jsondataloadoptions/
---
## JsonDataLoadOptions class

Representa opciones para analizar datos JSON.

```csharp
public class JsonDataLoadOptions
```

## Constructores

| Nombre | Descripción |
| --- | --- |
| [JsonDataLoadOptions](jsondataloadoptions)() | Inicializa una nueva instancia de esta clase con opciones predeterminadas. |

## Propiedades

| Nombre | Descripción |
| --- | --- |
| [AlwaysGenerateRootObject](../../groupdocs.assembly.data/jsondataloadoptions/alwaysgeneraterootobject) { get; set; } | Obtiene o establece una marca que indica si una fuente de datos generada siempre contendrá un objeto para un elemento JSON root . Si un elemento raíz JSON contiene una única propiedad compleja, dicho objeto no se crea de forma predeterminada. |
| [ExactDateTimeParseFormats](../../groupdocs.assembly.data/jsondataloadoptions/exactdatetimeparseformats) { get; set; } | Obtiene o establece formatos exactos para analizar los valores de fecha y hora de JSON al cargar JSON. El valor predeterminado es**nulo** . |
| [SimpleValueParseMode](../../groupdocs.assembly.data/jsondataloadoptions/simplevalueparsemode) { get; set; } | Obtiene o establece un modo para analizar valores simples de JSON (null, boolean, number, integer y string) al cargar JSON. Este modo no afecta el análisis de los valores de fecha y hora. El valor predeterminado es Loose . |

### Observaciones

Una instancia de esta clase se puede pasar a los constructores de[`JsonDataSource`](../jsondatasource) .

### Ver también

* espacio de nombres [GroupDocs.Assembly.Data](../../groupdocs.assembly.data)
* asamblea [GroupDocs.Assembly](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Assembly.dll -->
