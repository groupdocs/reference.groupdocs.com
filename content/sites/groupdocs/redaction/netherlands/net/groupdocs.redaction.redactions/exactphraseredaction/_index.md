---
title: ExactPhraseRedaction
second_title: GroupDocs.Redaction voor .NET API-referentie
description: Vertegenwoordigt een tekstredactie die de exacte woordgroep in de documenttekst vervangt standaard niet hoofdlettergevoelig.
type: docs
weight: 490
url: /nl/net/groupdocs.redaction.redactions/exactphraseredaction/
---
## ExactPhraseRedaction class

Vertegenwoordigt een tekstredactie die de exacte woordgroep in de documenttekst vervangt, standaard niet hoofdlettergevoelig.

```csharp
public class ExactPhraseRedaction : TextRedaction
```

## Constructeurs

| Naam | Beschrijving |
| --- | --- |
| [ExactPhraseRedaction](exactphraseredaction#constructor_1)(string, ReplacementOptions) | Initialiseert een nieuwe instantie van de klasse ExactPhraseRedaction in hoofdlettergevoelige modus. |
| [ExactPhraseRedaction](exactphraseredaction#constructor)(string, bool, ReplacementOptions) | Initialiseert een nieuwe instantie van ExactPhraseRedaction class. |

## Eigenschappen

| Naam | Beschrijving |
| --- | --- |
| [ActionOptions](../../groupdocs.redaction.redactions/textredaction/actionoptions) { get; } | Krijgt de[`ReplacementOptions`](../replacementoptions) instantie, specificeert het type tekstvervanging. |
| override [Description](../../groupdocs.redaction.redactions/exactphraseredaction/description) { get; } | Retourneert een tekenreeks die de redactie en de bijbehorende parameters beschrijft. |
| [IsCaseSensitive](../../groupdocs.redaction.redactions/exactphraseredaction/iscasesensitive) { get; } | Krijgt een waarde die aangeeft of de zoekopdracht hoofdlettergevoelig is of niet. |
| [OcrConnector](../../groupdocs.redaction.redactions/textredaction/ocrconnector) { get; set; } | Haalt of stelt de[`IOcrConnector`](../../groupdocs.redaction.integration.ocr/iocrconnector) implementatie, vereist om tekst uit grafische inhoud te extraheren. |
| [SearchPhrase](../../groupdocs.redaction.redactions/exactphraseredaction/searchphrase) { get; } | Haalt de tekenreeks op om te zoeken en te vervangen. |

## methoden

| Naam | Beschrijving |
| --- | --- |
| override [ApplyTo](../../groupdocs.redaction.redactions/exactphraseredaction/applyto)(DocumentFormatInstance) | Past de redactie toe op een bepaalde indelingsinstantie. |

### Opmerkingen

**Kom meer te weten**

* Meer informatie over het toepassen van redacties: [Basisprincipes van redactie](https://docs.groupdocs.com/redaction/net/redaction-basics/)
* Meer details over redactie van documenttekst: [Tekstredacties](https://docs.groupdocs.com/redaction/net/text-redactions/)

### Voorbeelden

Het volgende voorbeeld demonstreert het zoeken en vervangen van hoofdlettergevoelige woordgroepen. Het volgende voorbeeld demonstreert het vervangen van zin (niet hoofdlettergevoelig) door een effen rode rechthoek.

```csharp
using (Redactor redactor = new Redactor(@"C:\sample.pdf"))
{
  // Standaard is isCaseSensitive = false;
  doc.Apply(new ExactPhraseRedaction("John Doe", true /*isCaseSensitive*/, new ReplacementOptions("[personal]")));
  doc.Save();
}
```

```csharp
using (Redactor redactor = new Redactor(@"C:\sample.pdf"))
{
  // Standaard is isCaseSensitive = false;
  doc.Apply(new ExactPhraseRedaction("John Doe", new ReplacementOptions(System.Drawing.Color.Red)));
  doc.Save();
}
```

### Zie ook

* class [TextRedaction](../textredaction)
* naamruimte [GroupDocs.Redaction.Redactions](../../groupdocs.redaction.redactions)
* montage [GroupDocs.Redaction](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Redaction.dll -->
