---
title: RedactorConfiguration
second_title: GroupDocs.Redaction für .NET-API-Referenz
description: Bietet Zugriff auf eine Liste unterstützter Formate integrierter und benutzerdefinierter Benutzerformate.
type: docs
weight: 20
url: /de/net/groupdocs.redaction.configuration/redactorconfiguration/
---
## RedactorConfiguration class

Bietet Zugriff auf eine Liste unterstützter Formate, integrierter und benutzerdefinierter Benutzerformate.

```csharp
public class RedactorConfiguration
```

## Eigenschaften

| Name | Beschreibung |
| --- | --- |
| [AvailableFormats](../../groupdocs.redaction.configuration/redactorconfiguration/availableformats) { get; } | Ruft eine Liste der erkannten Formate ab, siehe[`DocumentFormatConfiguration`](../documentformatconfiguration) . |

## Methoden

| Name | Beschreibung |
| --- | --- |
| static [GetInstance](../../groupdocs.redaction.configuration/redactorconfiguration/getinstance)() | Stellt eine Singleton-Instanz mit Standardkonfiguration integrierter Formate bereit. |
| [FindFormat](../../groupdocs.redaction.configuration/redactorconfiguration/findformat)(string) | Findet Formatkonfigurationen für eine bestimmte Dateierweiterung. |

### Bemerkungen

**Mehr erfahren**

* Mehr Details über**GroupDocs.Redaktion** Konfiguration: [Erweitern Sie die Liste der unterstützten Erweiterungen](https://docs.groupdocs.com/redaction/net/extend-supported-extensions-list/)
* Weitere Details zur Implementierung benutzerdefinierter Formate: [Erstellen Sie einen benutzerdefinierten Formathandler](https://docs.groupdocs.com/redaction/net/create-custom-format-handler/)

### Beispiele

Das folgende Beispiel zeigt, wie Sie einen benutzerdefinierten Benutzerformat-Handler hinzufügen.

```csharp
var adobePhotoshopSettings = new DocumentFormatConfiguration();
adobePhotoshopSettings.ExtensionFilter = ".psd";
adobePhotoshopSettings.DocumentType = typeof(MyAdobePhotoshopFormatInstance);
var configuration = RedactorConfiguration.GetInstance();
configuration.AvailableFormats.Add(adobePhotoshopSettings);
```

Das folgende Beispiel zeigt, wie Sie integrierte oder benutzerdefinierte Benutzerformat-Handler erhalten.

```csharp
var configuration = RedactorConfiguration.GetInstance();
var formatSettings = configuration.FindFormat(".psd");
```

### Siehe auch

* namensraum [GroupDocs.Redaction.Configuration](../../groupdocs.redaction.configuration)
* Montage [GroupDocs.Redaction](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Redaction.dll -->