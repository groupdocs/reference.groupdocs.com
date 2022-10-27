---
title: SaveFormat
second_title: Referencia de API de GroupDocs.Assembly para .NET
description: Obtiene o establece un formato de archivo para guardar un documento ensamblado.Unspecified es el predeterminado.
type: docs
weight: 40
url: /es/net/groupdocs.assembly/loadsaveoptions/saveformat/
---
## LoadSaveOptions.SaveFormat property

Obtiene o establece un formato de archivo para guardar un documento ensamblado.Unspecified es el predeterminado.

```csharp
public FileFormat SaveFormat { get; set; }
```

### Observaciones

Cuando no se especifica el valor de esta propiedad,[`DocumentAssembler`](../../documentassembler) se comporta de la siguiente manera:

: cuando especifica una ruta de archivo para guardar un documento ensamblado, el formato de archivo guardado se determina según la extensión del archivo de la ruta.

: cuando especifica una secuencia para guardar un documento ensamblado, el formato de archivo guardado sigue siendo el mismo que el formato de archivo de un documento de plantilla cargado.

Tenga en cuenta que no siempre es posible guardar un documento ensamblado en cualquier formato de archivo usando GroupDocs.Assembly. Por ejemplo, es imposible guardar un documento cargado desde un formato de archivo de procesamiento de textos (como DOCX) a un formato de archivo de hoja de cálculo (como XLSX). Para obtener más información sobre las posibles combinaciones de formatos de archivo de carga y guardado admitidos por GroupDocs.Assembly, consulte la documentación en línea de GroupDocs.Assembly.

### Ver también

* enum [FileFormat](../../fileformat)
* class [LoadSaveOptions](../../loadsaveoptions)
* espacio de nombres [GroupDocs.Assembly](../../loadsaveoptions)
* asamblea [GroupDocs.Assembly](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Assembly.dll -->