---
title: ConvertedPageStream
second_title: GroupDocs.Conversion für .NET-API-Referenz
description: Beschreibt den Delegaten zum Empfangen des konvertierten Dokumentseitenstreams.
type: docs
weight: 120
url: /de/net/groupdocs.conversion.contracts/convertedpagestream/
---
## ConvertedPageStream delegate

Beschreibt den Delegaten zum Empfangen des konvertierten Dokumentseitenstreams.

```csharp
public delegate void ConvertedPageStream(int pageNumber, Stream stream, string sourceFileName);
```

| Parameter | Typ | Beschreibung |
| --- | --- | --- |
| pageNumber | Int32 | Seitenzahl umgewandelt |
| stream | Stream | Konvertierter Seitenstrom |
| sourceFileName | String | Der Name des konvertierten Dokuments |

### Siehe auch

* namensraum [GroupDocs.Conversion.Contracts](../../groupdocs.conversion.contracts)
* Montage [GroupDocs.Conversion](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Conversion.dll -->
