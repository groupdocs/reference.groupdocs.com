---
title: PdfCompliance
second_title: Referencia de API de GroupDocs.Editor para .NET
description: Especifica el nivel de cumplimiento de estándares de PDF
type: docs
weight: 820
url: /es/net/groupdocs.editor.options/pdfcompliance/
---
## PdfCompliance enumeration

Especifica el nivel de cumplimiento de estándares de PDF

```csharp
public enum PdfCompliance : byte
```

### Valores

| Nombre | Valor | Descripción |
| --- | --- | --- |
| Pdf17 | `0` | PDF 1.7 (ISO 32000-1) estándar |
| Pdf20 | `1` | PDF 2.0 (ISO 32000-2) estándar |
| PdfA1a | `2` | PDF/A-1a estándar. Este nivel incluye todos los requisitos de PDF/A-1b y, además, requiere que se incluya la estructura del documento (también conocido como "etiquetado"), con el objetivo de garantizar que el contenido del documento se pueda buscar y reutilizar. |
| PdfA1b | `3` | PDF/A-1b (ISO 19005-1). PDF/A-1b tiene como objetivo garantizar una reproducción fiable del aspecto visual del documento. |
| PdfA2a | `4` | Estándar PDF/A-2a (ISO 19005-2). Este nivel incluye todos los requisitos de PDF/A-2u y, además, requiere que se incluya la estructura del documento (también conocido como "etiquetado"), con el objetivo de garantizar que el contenido del documento se pueda buscar y reutilizar. |
| PdfA2u | `5` | PDF/A-2u (ISO 19005-2) estándar. PDF/A-2u tiene el objetivo de preservar la apariencia visual estática del documento a lo largo del tiempo, independientemente de las herramientas y sistemas utilizados para crear, almacenar o renderizar los archivos. Además, cualquier texto contenido en el documento se puede extraer de forma fiable como una serie de puntos de código Unicode. |
| PdfUa1 | `6` | Estándar PDF/UA-1 (ISO 14289-1). El propósito principal de PDF/UA es definir cómo representar documentos electrónicos en formato PDF de una manera que permita el acceso al archivo. |

### Ver también

* espacio de nombres [GroupDocs.Editor.Options](../../groupdocs.editor.options)
* asamblea [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->