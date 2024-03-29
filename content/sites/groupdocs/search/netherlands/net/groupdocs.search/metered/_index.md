---
title: Metered
second_title: GroupDocs. Zoek naar .NET API-referentie
description: Biedt methoden die het mogelijk maken om het product te activeren met Gemeten licentie en het aantal verwerkte MBs op te halen. Meer informatie over Gemeten licentieshierhttps//purchase.groupdocs.com/faqs/licensing/metered .
type: docs
weight: 730
url: /nl/net/groupdocs.search/metered/
---
## Metered class

Biedt methoden die het mogelijk maken om het product te activeren met Gemeten licentie en het aantal verwerkte MB's op te halen. Meer informatie over Gemeten licenties[hier](https://purchase.groupdocs.com/faqs/licensing/metered) .

```csharp
public class Metered
```

## Constructeurs

| Naam | Beschrijving |
| --- | --- |
| [Metered](metered)() | Initialiseert een nieuw exemplaar van[`Metered`](../metered) klasse. |

## methoden

| Naam | Beschrijving |
| --- | --- |
| [SetMeteredKey](../../groupdocs.search/metered/setmeteredkey)(string, string) | Stelt gemeten publieke en private sleutel in. |
| static [GetConsumptionCredit](../../groupdocs.search/metered/getconsumptioncredit)() | Krijgt het verbruikstegoed. |
| static [GetConsumptionQuantity](../../groupdocs.search/metered/getconsumptionquantity)() | Krijgt de verbruikshoeveelheid. |

### Opmerkingen

**Kom meer te weten**

* [Evaluatiebeperkingen en licenties](https://docs.groupdocs.com/display/searchnet/Evaluation+Limitations+and+Licensing)

### Voorbeelden

Het voorbeeld laat zien hoe gedoseerde openbare en privésleutels worden ingesteld.

```csharp
Metered metered = new Metered();
metered.SetMeteredKey("PublicKey", "PrivateKey");
```

### Zie ook

* naamruimte [GroupDocs.Search](../../groupdocs.search)
* montage [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
