---
title: License
second_title: GroupDocs.Watermark für .NET-API-Referenz
description: Stellt Methoden zur Lizenzierung der Komponente bereit.
type: docs
weight: 1610
url: /de/net/groupdocs.watermark/license/
---
## License class

Stellt Methoden zur Lizenzierung der Komponente bereit.

```csharp
public sealed class License
```

## Konstrukteure

| Name | Beschreibung |
| --- | --- |
| [License](license)() | Initialisiert eine neue Instanz von[`License`](../license) Klasse. |

## Methoden

| Name | Beschreibung |
| --- | --- |
| [SetLicense](../../groupdocs.watermark/license/setlicense#setlicense)(Stream) | Lizenziert die Komponente. |
| [SetLicense](../../groupdocs.watermark/license/setlicense#setlicense_1)(string) | Lizenziert die Komponente. |

### Bemerkungen

* Mehr zur Lizenzierung: [Häufig gestellte Fragen zur GroupDocs-Lizenzierung](https://purchase.groupdocs.com/faqs/licensing)
* Mehr über**GroupDocs.Watermark** Lizenzierung: [Bewertungsbeschränkungen und Lizenzierung](https://docs.groupdocs.com/display/watermarknet/Evaluation+Limitations+and+Licensing)

### Beispiele

Dieses Beispiel zeigt, wie die Lizenz aus der lokalen Datei eingerichtet wird.

```csharp
// Lizenzklasse initialisieren.
License license = new License();

// Pfad zur .lic-Datei setzen.
license.SetLicense("C:\\GroupDocs.Watermark.lic");
```

### Siehe auch

* namensraum [GroupDocs.Watermark](../../groupdocs.watermark)
* Montage [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
