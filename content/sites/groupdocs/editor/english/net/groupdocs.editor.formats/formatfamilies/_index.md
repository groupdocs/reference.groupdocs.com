---
title: FormatFamilies
second_title: GroupDocs.Editor for .NET API Reference
description: Represents the different format families available in the system.
type: docs
weight: 110
url: /net/groupdocs.editor.formats/formatfamilies/
---
## FormatFamilies class

Represents the different format families available in the system.

```csharp
public class FormatFamilies : FormatFamilyBase
```

## Properties

| Name | Description |
| --- | --- |
| [Id](../../groupdocs.editor.formats.abstraction/formatfamilybase/id) { get; } | Gets the unique identifier for the format family. |
| [Name](../../groupdocs.editor.formats.abstraction/formatfamilybase/name) { get; } | Gets the name of the format family. |

## Methods

| Name | Description |
| --- | --- |
| [Equals](../../groupdocs.editor.formats.abstraction/formatfamilybase/equals)(FormatFamilyBase) | Determines whether this instance is equal to the specified [`FormatFamilyBase`](../../groupdocs.editor.formats.abstraction/formatfamilybase) instance. |
| override [Equals](../../groupdocs.editor.formats.abstraction/formatfamilybase/equals)(object) | Determines whether this instance is equal to the specified [`FormatFamilyBase`](../../groupdocs.editor.formats.abstraction/formatfamilybase) instance. |
| override [GetHashCode](../../groupdocs.editor.formats.abstraction/formatfamilybase/gethashcode)() | Returns a hash code for the current object. |
| override [ToString](../../groupdocs.editor.formats.abstraction/formatfamilybase/tostring)() | Returns a string that represents the current object. |

## Fields

| Name | Description |
| --- | --- |
| static readonly [EBook](../../groupdocs.editor.formats/formatfamilies/ebook) | Represents the eBook format family. Learn more about Mobi format [here](https://docs.fileformat.com/ebook/mobi/), about AZW3 format [here](https://docs.fileformat.com/ebook/azw3/), and about ePub format [here](https://docs.fileformat.com/ebook/epub/). |
| static readonly [Email](../../groupdocs.editor.formats/formatfamilies/email) | Represents the Email format family. Learn more about emails format [here](https://docs.fileformat.com/email/). |
| static readonly [FixedLayout](../../groupdocs.editor.formats/formatfamilies/fixedlayout) | Represents the Fixed Layout format family. Various document viewing or publishing applications allow users to open (Adobe Acrobat, XPS Viewer), and sometimes edit (Adobe InDesign) documents of specific formats. These applications typically produce so-called “fixed-page” format documents. Such a document format describes precisely where a document’s content is placed on every page. Internally, the PDF or XPS format contains a description of every page, as well as drawing instructions, specifying the layout of the content on the page. This is similar to image formats, describing where the content is shown either in raster or vector form. |
| static readonly [Presentation](../../groupdocs.editor.formats/formatfamilies/presentation) | Represents the Presentation format family. Learn more about Presentation formats [here](https://wiki.fileformat.com/presentation). |
| static readonly [Spreadsheet](../../groupdocs.editor.formats/formatfamilies/spreadsheet) | Represents the Spreadsheet format family. All binary, XML and textual Spreadsheet formats (excluding all textual delimiter-based formats with separator like CSV, TSV, semicolon-delimited etc.), in which the workbook can be saved. |
| static readonly [Textual](../../groupdocs.editor.formats/formatfamilies/textual) | Represents the Textual format family. Encapsulates all textual (text-based) formats, including markup (XML, HTML) and others. |
| static readonly [WordProcessing](../../groupdocs.editor.formats/formatfamilies/wordprocessing) | Represents the Word Processing format family. Learn more about Word Processing formats [here](https://wiki.fileformat.com/word-processing). |

### See Also

* class [FormatFamilyBase](../../groupdocs.editor.formats.abstraction/formatfamilybase)
* namespace [GroupDocs.Editor.Formats](../../groupdocs.editor.formats)
* assembly [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.editor.dll -->
