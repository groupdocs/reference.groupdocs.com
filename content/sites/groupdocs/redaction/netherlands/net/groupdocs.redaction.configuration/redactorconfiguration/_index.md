---
title: RedactorConfiguration
second_title: GroupDocs.Redaction voor .NET API-referentie
description: Biedt toegang tot een lijst met ondersteunde indelingen ingebouwde en aangepaste gebruikersindelingen.
type: docs
weight: 20
url: /nl/net/groupdocs.redaction.configuration/redactorconfiguration/
---
## RedactorConfiguration class

Biedt toegang tot een lijst met ondersteunde indelingen, ingebouwde en aangepaste gebruikersindelingen.

```csharp
public class RedactorConfiguration
```

## Eigenschappen

| Naam | Beschrijving |
| --- | --- |
| [AvailableFormats](../../groupdocs.redaction.configuration/redactorconfiguration/availableformats) { get; } | Krijgt een lijst met herkende formaten, zie[`DocumentFormatConfiguration`](../documentformatconfiguration) . |

## methoden

| Naam | Beschrijving |
| --- | --- |
| static [GetInstance](../../groupdocs.redaction.configuration/redactorconfiguration/getinstance)() | Biedt een singleton-instantie met standaardconfiguratie van ingebouwde indelingen. |
| [FindFormat](../../groupdocs.redaction.configuration/redactorconfiguration/findformat)(string) | Zoekt formaatconfiguraties voor een bepaalde bestandsextensie. |

### Opmerkingen

**Kom meer te weten**

* Meer details over**GroupDocs. Redactie** configuratie: [Breid de lijst met ondersteunde extensies uit](https://docs.groupdocs.com/redaction/net/extend-supported-extensions-list/)
* Meer details over het implementeren van aangepaste formaten: [Maak een aangepaste formaathandler](https://docs.groupdocs.com/redaction/net/create-custom-format-handler/)

### Voorbeelden

Het volgende voorbeeld laat zien hoe u een aangepaste handler voor gebruikersindelingen kunt toevoegen.

```csharp
var adobePhotoshopSettings = new DocumentFormatConfiguration();
adobePhotoshopSettings.ExtensionFilter = ".psd";
adobePhotoshopSettings.DocumentType = typeof(MyAdobePhotoshopFormatInstance);
var configuration = RedactorConfiguration.GetInstance();
configuration.AvailableFormats.Add(adobePhotoshopSettings);
```

Het volgende voorbeeld laat zien hoe u ingebouwde of aangepaste handlers voor gebruikersindelingen kunt krijgen.

```csharp
var configuration = RedactorConfiguration.GetInstance();
var formatSettings = configuration.FindFormat(".psd");
```

### Zie ook

* naamruimte [GroupDocs.Redaction.Configuration](../../groupdocs.redaction.configuration)
* montage [GroupDocs.Redaction](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Redaction.dll -->
