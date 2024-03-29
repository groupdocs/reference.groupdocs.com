---
title: FromExtension
second_title: GroupDocs.Signature für .NET-API-Referenz
description: Ordnet die Dateierweiterung dem Dateityp zu.
type: docs
weight: 580
url: /de/net/groupdocs.signature.domain/filetype/fromextension/
---
## FileType.FromExtension method

Ordnet die Dateierweiterung dem Dateityp zu.

```csharp
public static FileType FromExtension(string extension)
```

| Parameter | Typ | Beschreibung |
| --- | --- | --- |
| extension | String | Dateiendung (einschließlich Punkt „.“). |

### Rückgabewert

Wenn der Dateityp unterstützt wird, wird er zurückgegeben, andernfalls wird der Standardwert zurückgegeben[`Unknown`](../unknown) Dateityp.

### Ausnahmen

| Ausnahme | Bedingung |
| --- | --- |
| ArgumentException | Wann geworfen*extension* ist null oder eine leere Zeichenfolge. |

### Siehe auch

* class [FileType](../../filetype)
* namensraum [GroupDocs.Signature.Domain](../../filetype)
* Montage [GroupDocs.Signature](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
