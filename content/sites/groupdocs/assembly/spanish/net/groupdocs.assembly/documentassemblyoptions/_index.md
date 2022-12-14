---
title: DocumentAssemblyOptions
second_title: Referencia de API de GroupDocs.Assembly para .NET
description: Especifica opciones que controlan el comportamiento deDocumentAssembler./documentassembler mientras ensambla un documento.
type: docs
weight: 210
url: /es/net/groupdocs.assembly/documentassemblyoptions/
---
## DocumentAssemblyOptions enumeration

Especifica opciones que controlan el comportamiento de[`DocumentAssembler`](../documentassembler) mientras ensambla un documento.

```csharp
[Flags]
public enum DocumentAssemblyOptions
```

### Valores

| Nombre | Valor | Descripción |
| --- | --- | --- |
| None | `0` | Especifica las opciones predeterminadas. |
| AllowMissingMembers | `1` | Especifica que el ensamblador debe tratar los miembros de objetos faltantes como literales nulos. Esta opción solo afecta el acceso a miembros de objetos de instancia (es decir, no estáticos) y métodos de extensión. Si esta opción no está configurada, el ensamblador lanza una excepción cuando encuentra un objeto miembro faltante. |
| UpdateFieldsAndFormulas | `2` | Especifica que los campos de los documentos de procesamiento de texto de resultado y las fórmulas de los documentos de hoja de cálculo de resultado deben ser actualizados por el ensamblador. |
| RemoveEmptyParagraphs | `4` | Especifica que el ensamblador debe eliminar los párrafos que quedan vacíos después de que las etiquetas de sintaxis de plantilla se eliminen o reemplacen con valores vacíos. |
| InlineErrorMessages | `8` | Especifica que el ensamblador debe incluir mensajes de error de sintaxis de plantilla en línea en los documentos de salida. Si esta opción no está configurada, el ensamblador lanza una excepción cuando encuentra un error de sintaxis. |

### Ver también

* espacio de nombres [GroupDocs.Assembly](../../groupdocs.assembly)
* asamblea [GroupDocs.Assembly](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Assembly.dll -->
