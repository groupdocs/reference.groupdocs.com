---
title: PdfRecognitionMode
second_title: GroupDocs.Conversion for .NET API Reference
description: Allows to control how a PDF document is converted into a word processing document.
type: docs
weight: 2100
url: /net/groupdocs.conversion.options.convert/pdfrecognitionmode/
---
## PdfRecognitionMode class

Allows to control how a PDF document is converted into a word processing document.

```csharp
public sealed class PdfRecognitionMode : Enumeration
```

## Constructors

| Name | Description |
| --- | --- |
| [PdfRecognitionMode](pdfrecognitionmode)() | Serialization constructor |

## Methods

| Name | Description |
| --- | --- |
| [CompareTo](../../groupdocs.conversion.contracts/enumeration/compareto)(object) | Compares current object to other. |
| virtual [Equals](../../groupdocs.conversion.contracts/enumeration/equals)(Enumeration) | Determines whether two object instances are equal. |
| override [Equals](../../groupdocs.conversion.contracts/enumeration/equals)(object) | Determines whether two object instances are equal. |
| override [GetHashCode](../../groupdocs.conversion.contracts/enumeration/gethashcode)() | Serves as the default hash function. |
| override [ToString](../../groupdocs.conversion.contracts/enumeration/tostring)() | Returns a string that represents the current object. |

## Fields

| Name | Description |
| --- | --- |
| static readonly [Flow](../../groupdocs.conversion.options.convert/pdfrecognitionmode/flow) | Full recognition mode, the engine performs grouping and multi-level analysis to restore the original document author's intent and produce a maximally editable document. The downside is that the output document might look different from the original PDF file. |
| static readonly [Textbox](../../groupdocs.conversion.options.convert/pdfrecognitionmode/textbox) | This mode is fast and good for maximally preserving original look of the PDF file, but editability of the resulting document could be limited. Every visually grouped block of text int the original PDF file is converted into a textbox in the resulting document. This achieves maximal resemblance of the output document to the original PDF file. The output document will look good, but it will consist entirely of textboxes and it could makes further editing of the document in Microsoft Word quite hard. This is the default mode. |

### See Also

* class [Enumeration](../../groupdocs.conversion.contracts/enumeration)
* namespace [GroupDocs.Conversion.Options.Convert](../../groupdocs.conversion.options.convert)
* assembly [GroupDocs.Conversion](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.conversion.dll -->
