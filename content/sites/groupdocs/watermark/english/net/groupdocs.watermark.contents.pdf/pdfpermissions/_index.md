---
title: PdfPermissions
second_title: GroupDocs.Watermark for .NET API Reference
description: Represents users permissions for a pdf document.
type: docs
weight: 710
url: /net/groupdocs.watermark.contents.pdf/pdfpermissions/
---
## PdfPermissions enumeration

Represents user's permissions for a pdf document.

```csharp
[Flags]
public enum PdfPermissions
```

### Values

| Name | Value | Description |
| --- | --- | --- |
| PrintDocument | `4` | Print the content. |
| ModifyContent | `8` | Modify the content. |
| ExtractContent | `10` | Copy or otherwise extract text and graphics from the document. |
| ModifyTextAnnotations | `20` | Add or modify text annotations. |
| FillForm | `100` | Fill in existing interactive form fields. |
| ExtractContentWithDisabilities | `200` | Extract text and graphics. |
| AssembleDocument | `400` | Assemble the content. |
| PrintingQuality | `800` | Print the content to a representation from which a faithful digital copy of the PDF document could be generated. |

### See Also

* namespace [GroupDocs.Watermark.Contents.Pdf](../../groupdocs.watermark.contents.pdf)
* assembly [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.watermark.dll -->
