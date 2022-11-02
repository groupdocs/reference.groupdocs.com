---
title: PdfEditOptions
second_title: GroupDocs.Editor für .NET-API-Referenz
description: Ermöglicht das Festlegen benutzerdefinierter Optionen zum Bearbeiten von PDFDokumenten
type: docs
weight: 830
url: /de/net/groupdocs.editor.options/pdfeditoptions/
---
## PdfEditOptions class

Ermöglicht das Festlegen benutzerdefinierter Optionen zum Bearbeiten von PDF-Dokumenten

```csharp
public sealed class PdfEditOptions : FixedLayoutEditOptionsBase
```

## Konstrukteure

| Name | Beschreibung |
| --- | --- |
| [PdfEditOptions](pdfeditoptions#constructor)() | Erstellt eine neue Instanz der PdfEditOptions-Klasse und gibt sie zurück, wobei alle Optionen auf ihre Standardwerte gesetzt werden |
| [PdfEditOptions](pdfeditoptions#constructor_1)(bool) | Erstellt und gibt eine neue Instanz der PdfEditOptions-Klasse mit angegebener Paginierung und Standardeinstellung für alle anderen Optionen zurück |

## Eigenschaften

| Name | Beschreibung |
| --- | --- |
| [EnablePagination](../../groupdocs.editor.options/fixedlayouteditoptionsbase/enablepagination) { get; set; } | Ermöglicht das Aktivieren (true) oder Deaktivieren (false) der Paginierung im resultierenden HTML-Dokument. Standardmäßig ist deaktiviert (false). |
| [Pages](../../groupdocs.editor.options/fixedlayouteditoptionsbase/pages) { get; set; } | Ermöglicht das Festlegen eines zu verarbeitenden Seitenbereichs. Standardmäßig werden alle Seiten eines Dokuments mit festem Layout verarbeitet. |
| [SkipImages](../../groupdocs.editor.options/fixedlayouteditoptionsbase/skipimages) { get; set; } | Ruft das Flag ab oder setzt es, das angibt, ob Bilder übersprungen werden müssen, während das eingegebene Dokument mit festem Layout in das resultierende HTML konvertiert wird. Standard ist „false“ – Bilder bleiben erhalten. |

### Siehe auch

* class [FixedLayoutEditOptionsBase](../fixedlayouteditoptionsbase)
* namensraum [GroupDocs.Editor.Options](../../groupdocs.editor.options)
* Montage [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->