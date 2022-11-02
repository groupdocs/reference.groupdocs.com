---
title: FontExtractionOptions
second_title: Referencia de API de GroupDocs.Editor para .NET
description: Las opciones de extracción de fuentes controlan qué fuentes deben extraerse y de dónde
type: docs
weight: 750
url: /es/net/groupdocs.editor.options/fontextractionoptions/
---
## FontExtractionOptions enumeration

Las opciones de extracción de fuentes controlan qué fuentes deben extraerse y de dónde

```csharp
public enum FontExtractionOptions : byte
```

### Valores

| Nombre | Valor | Descripción |
| --- | --- | --- |
| NotExtract | `0` | No extrae ningún recurso tipográfico ni del documento ni del sistema. Valor predeterminado. |
| ExtractAllEmbedded | `1` | Extrae todos los recursos de fuentes, que están incrustados en el documento de entrada de Word, independientemente de cuáles sean: personalizados o del sistema. |
| ExtractEmbeddedWithoutSystem | `2` | Extrae solo los recursos de fuente incrustados, que son personalizados (no del sistema) |
| ExtractAll | `3` | Intenta extraer todas las fuentes que se utilizan en el documento de procesamiento de texto de entrada, incluidas las fuentes del sistema. |

### Ver también

* espacio de nombres [GroupDocs.Editor.Options](../../groupdocs.editor.options)
* asamblea [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->