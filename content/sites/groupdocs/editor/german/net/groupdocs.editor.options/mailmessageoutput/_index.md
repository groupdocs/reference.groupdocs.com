---
title: MailMessageOutput
second_title: GroupDocs.Editor für .NET-API-Referenz
description: Steuert welche Teile der EMailNachricht an die Ausgabeverarbeitung geliefert werden sollen
type: docs
weight: 950
url: /de/net/groupdocs.editor.options/mailmessageoutput/
---
## MailMessageOutput enumeration

Steuert, welche Teile der E-Mail-Nachricht an die Ausgabeverarbeitung geliefert werden sollen

```csharp
[Flags]
public enum MailMessageOutput : ushort
```

### Werte

| Name | Wert | Beschreibung |
| --- | --- | --- |
| None | `0` | Keiner der Teile der E-Mail-Nachricht wird verarbeitet |
| Body | `1` | Prozesstext der E-Mail-Nachricht |
| Subject | `2` | Betreff der E-Mail-Nachricht bearbeiten |
| Date | `4` | Prozessdatum und -uhrzeit, als die Nachricht zugestellt wurde |
| To | `8` | Alle Empfänger der E-Mail-Nachricht verarbeiten |
| Cc | `10` | Alle CC-Empfänger der E-Mail-Nachricht verarbeiten |
| Bcc | `20` | Alle BCC-Empfänger der E-Mail-Nachricht verarbeiten |
| From | `40` | Absender der E-Mail-Nachricht bearbeiten |
| Attachments | `80` | Alle Anhänge der E-Mail-Nachricht verarbeiten |
| Metadata | `100` | Alle anderen technischen Metadaten verarbeiten (Sensitivität, Priorität, Kodierung, MIME, X-Mailer usw.) |
| Common | `7B` | Gemeinsame Ausgabe – Hauptteil mit allen Hauptmetadaten |
| All | `1FF` | Vollständige Ausgabe - Hauptteil mit allen Metadaten |

### Siehe auch

* namensraum [GroupDocs.Editor.Options](../../groupdocs.editor.options)
* Montage [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
