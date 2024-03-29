---
title: IHtmlResource
second_title: GroupDocs.Editor för .NET API-referens
description: Representerar en instans av den okända HTMLresursen raster eller vektorbild stilmall typsnitt textresurs CSS XML ljud etc.
type: docs
weight: 440
url: /sv/net/groupdocs.editor.htmlcss.resources/ihtmlresource/
---
## IHtmlResource interface

Representerar en instans av den okända HTML-resursen (raster- eller vektorbild, stilmall, typsnitt, textresurs (CSS, XML), ljud etc.)

```csharp
public interface IHtmlResource : IAuxDisposable, IEquatable<IHtmlResource>
```

## Egenskaper

| namn | Beskrivning |
| --- | --- |
| [ByteContent](../../groupdocs.editor.htmlcss.resources/ihtmlresource/bytecontent) { get; } | Innehållet i HTML-resursen i form av en byte stream |
| [FilenameWithExtension](../../groupdocs.editor.htmlcss.resources/ihtmlresource/filenamewithextension) { get; } | Korrekt filnamn för den angivna resursen med lämplig filtillägg |
| [Name](../../groupdocs.editor.htmlcss.resources/ihtmlresource/name) { get; } | Namnet på HTML-resursen |
| [TextContent](../../groupdocs.editor.htmlcss.resources/ihtmlresource/textcontent) { get; } | HTML-resursens innehåll i form av en base64-kodad textsträng för binära resurser eller en enkel text för textresurser |
| [Type](../../groupdocs.editor.htmlcss.resources/ihtmlresource/type) { get; } | Typ av HTML-resurs |

## Metoder

| namn | Beskrivning |
| --- | --- |
| [Save](../../groupdocs.editor.htmlcss.resources/ihtmlresource/save)(string) | Sparar en aktuell resurs till den angivna filen |

### Se även

* interface [IAuxDisposable](../iauxdisposable)
* namnutrymme [GroupDocs.Editor.HtmlCss.Resources](../../groupdocs.editor.htmlcss.resources)
* hopsättning [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
