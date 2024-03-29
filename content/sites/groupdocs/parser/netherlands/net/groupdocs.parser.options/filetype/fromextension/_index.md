---
title: FromExtension
second_title: GroupDocs.Parser voor .NET API-referentie
description: Wijst bestandsextensie toe aan bestandstype.
type: docs
weight: 900
url: /nl/net/groupdocs.parser.options/filetype/fromextension/
---
## FileType.FromExtension method

Wijst bestandsextensie toe aan bestandstype.

```csharp
public static FileType FromExtension(string extension)
```

| Parameter | Type | Beschrijving |
| --- | --- | --- |
| extension | String | Bestandsextensie (inclusief de punt "."). |

### Winstwaarde

Wanneer het bestandstype wordt ondersteund, wordt het geretourneerd, anders wordt standaard geretourneerd[`Unknown`](../unknown) bestandstype.

### Uitzonderingen

| uitzondering | voorwaarde |
| --- | --- |
| ArgumentException | Wanneer gegooid*extension* is null of een lege tekenreeks. |

### Zie ook

* class [FileType](../../filetype)
* naamruimte [GroupDocs.Parser.Options](../../filetype)
* montage [GroupDocs.Parser](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->
