---
title: TextSearchOptions
second_title: GroupDocs.Signature für .NET-API-Referenz
description: Repräsentiert Suchoptionen für Textsignaturen.
type: docs
weight: 1720
url: /de/net/groupdocs.signature.options/textsearchoptions/
---
## TextSearchOptions class

Repräsentiert Suchoptionen für Textsignaturen.

```csharp
public class TextSearchOptions : SearchOptions
```

## Konstrukteure

| Name | Beschreibung |
| --- | --- |
| [TextSearchOptions](textsearchoptions#constructor)() | Initialisiert eine neue Instanz der TextSearchOptions-Klasse mit Standardwerten. |
| [TextSearchOptions](textsearchoptions#constructor_1)(string) | Initialisiert eine neue Instanz der TextSearchOptions-Klasse mit Textwert. |

## Eigenschaften

| Name | Beschreibung |
| --- | --- |
| [AllPages](../../groupdocs.signature.options/searchoptions/allpages) { get; set; } | Markierung für die Suche auf jeder Dokumentseite. Standardmäßig ist dieser Wert auf true gesetzt. |
| [MatchType](../../groupdocs.signature.options/textsearchoptions/matchtype) { get; set; } | Ruft Text-Match-Typ-Suche ab oder legt sie fest. |
| [PageNumber](../../groupdocs.signature.options/searchoptions/pagenumber) { get; set; } | Ruft die Seitennummer des Dokuments für die Suche ab oder legt sie fest. Der Wert ist optional. |
| [PagesSetup](../../groupdocs.signature.options/searchoptions/pagessetup) { get; set; } | Optionen zum Angeben von Seiten für die Signatursuche. |
| [SignatureImplementation](../../groupdocs.signature.options/textsearchoptions/signatureimplementation) { get; set; } | Gibt die zu durchsuchende Implementierung der Textsignatur an. |
| [SkipExternal](../../groupdocs.signature.options/searchoptions/skipexternal) { get; set; } | Flag, um nur Signaturen zurückzugeben, die als IsSignature gekennzeichnet sind. Standardmäßig ist der Wert „false“, was bedeutet, dass alle Signaturen zurückgegeben werden, die den angegebenen Kriterien entsprechen. |
| [Text](../../groupdocs.signature.options/textsearchoptions/text) { get; set; } | Gibt den Signaturtext an, der beim Suchen abgeglichen werden soll. |

### Bemerkungen

**Erfahren Sie mehr**

* Grundlegende Verwendung der Suche nach elektronischer Textunterschrift von GroupDocs.Signatur: [ So suchen Sie nach Textsignaturen in einem Dokument](https://docs.groupdocs.com/display/signaturenet/Search+for+Text+e-signatures)
* Erweiterte Verwendung der Sucheinstellungen für Text elektronische Signatur mit GroupDocs.Signature: [Erweiterte Verwendung von eSearch-Textsignaturen in einem Dokument und zusätzliche Einstellungen](https://docs.groupdocs.com/display/signaturenet/Advanced+search+for+Text+signatures)

### Siehe auch

* class [SearchOptions](../searchoptions)
* namensraum [GroupDocs.Signature.Options](../../groupdocs.signature.options)
* Montage [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
