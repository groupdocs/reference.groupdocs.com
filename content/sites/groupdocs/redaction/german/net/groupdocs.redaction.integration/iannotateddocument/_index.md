---
title: IAnnotatedDocument
second_title: GroupDocs.Redaction für .NET-API-Referenz
description: Definiert Methoden die für den Zugriff auf Anmerkungen wie Kommentare erforderlich sind. Muss implementiert werden vonDocumentFormatInstance./documentformatinstance abgeleitete Klasse zum Durchführen von Anmerkungsschwärzungen.
type: docs
weight: 120
url: /de/net/groupdocs.redaction.integration/iannotateddocument/
---
## IAnnotatedDocument interface

Definiert Methoden, die für den Zugriff auf Anmerkungen wie Kommentare erforderlich sind. Muss implementiert werden von[`DocumentFormatInstance`](../documentformatinstance) -abgeleitete Klasse zum Durchführen von Anmerkungsschwärzungen.

```csharp
public interface IAnnotatedDocument
```

## Methoden

| Name | Beschreibung |
| --- | --- |
| [DeleteAnnotations](../../groupdocs.redaction.integration/iannotateddocument/deleteannotations)(Regex) | Löscht alle Anmerkungen, die mit regulären Ausdrücken innerhalb des Dokuments übereinstimmen. |
| [RedactAnnotation](../../groupdocs.redaction.integration/iannotateddocument/redactannotation)(Regex, string) | Ersetzt den übereinstimmenden Text in allen Anmerkungen innerhalb des Dokuments. |

### Bemerkungen

**Mehr erfahren**

* Weitere Details zum Anwenden von Schwärzungen: [Grundlagen der Redaktion](https://docs.groupdocs.com/redaction/net/redaction-basics/)
* Weitere Details zum Schwärzen von Dokumentanmerkungen: [Anmerkungsredaktionen](https://docs.groupdocs.com/redaction/net/annotation-redactions/)
* Weitere Details zur Implementierung benutzerdefinierter Formate: [Erstellen Sie einen benutzerdefinierten Formathandler](https://docs.groupdocs.com/redaction/net/create-custom-format-handler/)

### Siehe auch

* namensraum [GroupDocs.Redaction.Integration](../../groupdocs.redaction.integration)
* Montage [GroupDocs.Redaction](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Redaction.dll -->