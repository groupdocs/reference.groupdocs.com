---
title: SavePageStreamForFileType
second_title: GroupDocs.Conversion für .NET-API-Referenz
description: Beschreibt den Delegaten zum Speichern der konvertierten Dokumentseite im Stream.
type: docs
weight: 460
url: /de/net/groupdocs.conversion.contracts/savepagestreamforfiletype/
---
## SavePageStreamForFileType delegate

Beschreibt den Delegaten zum Speichern der konvertierten Dokumentseite im Stream.

```csharp
public delegate Stream SavePageStreamForFileType(int pageNumber, FileType fileType);
```

| Parameter | Typ | Beschreibung |
| --- | --- | --- |
| pageNumber | Int32 | Seitenzahl umgewandelt |
| fileType | FileType | Konvertierter Dokumenttyp |

### Rückgabewert

Muss einen Stream zurückgeben, in dem die konvertierte Dokumentseite gespeichert wird

### Siehe auch

* class [FileType](../../groupdocs.conversion.filetypes/filetype)
* namensraum [GroupDocs.Conversion.Contracts](../../groupdocs.conversion.contracts)
* Montage [GroupDocs.Conversion](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Conversion.dll -->