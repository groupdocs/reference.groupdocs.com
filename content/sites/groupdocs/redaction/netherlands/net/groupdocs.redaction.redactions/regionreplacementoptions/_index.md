---
title: RegionReplacementOptions
second_title: GroupDocs.Redaction voor .NET API-referentie
description: Vertegenwoordigt kleur en gebiedsparameters voor vervanging van afbeeldingsregios. ZienImageAreaRedaction./imagearearedaction .
type: docs
weight: 600
url: /nl/net/groupdocs.redaction.redactions/regionreplacementoptions/
---
## RegionReplacementOptions class

Vertegenwoordigt kleur- en gebiedsparameters voor vervanging van afbeeldingsregio's. Zien[`ImageAreaRedaction`](../imagearearedaction) .

```csharp
public class RegionReplacementOptions
```

## Constructeurs

| Naam | Beschrijving |
| --- | --- |
| [RegionReplacementOptions](regionreplacementoptions#constructor_1)(Color, Size) | Initialiseert een nieuw exemplaar van de klasse RegionReplacementOptions. |
| [RegionReplacementOptions](regionreplacementoptions#constructor)(Color, Font, string) | Initialiseert een nieuwe instantie van de klasse RegionReplacementOptions waarvan de grootte overeenkomt met de gegeven tekst. |

## Eigenschappen

| Naam | Beschrijving |
| --- | --- |
| [FillColor](../../groupdocs.redaction.redactions/regionreplacementoptions/fillcolor) { get; set; } | Krijgt of stelt de kleur in om het geredigeerde gebied te vullen. |
| [Size](../../groupdocs.redaction.redactions/regionreplacementoptions/size) { get; set; } | Haalt of stelt de rechthoek in met en hoogte. |

### Opmerkingen

**Kom meer te weten**

* Meer details over beeldredactie: [Beeldredacties](https://docs.groupdocs.com/redaction/net/image-redactions/)

### Voorbeelden

In het volgende voorbeeld wordt getoond hoe u een gebied in de afbeelding vervangt door een rechthoek met een effen kleur.

```csharp
    using (Redactor redactor = new Redactor("D:\\test.jpg"))
    {
       System.Drawing.Point samplePoint = new System.Drawing.Point(516, 311);
       System.Drawing.Size sampleSize = new System.Drawing.Size(170, 35);
       RedactorChangeLog result = redactor.Apply(new ImageAreaRedaction(samplePoint,
                     new RegionReplacementOptions(System.Drawing.Color.Blue, sampleSize)));
       if (result.Status != RedactionStatus.Failed)
       {
          redactor.Save();
       };
    } 
```

### Zie ook

* naamruimte [GroupDocs.Redaction.Redactions](../../groupdocs.redaction.redactions)
* montage [GroupDocs.Redaction](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Redaction.dll -->
