---
title: GetConsumptionCredit
second_title: GroupDocs.Viewer voor .NET API-referentie
description: Haalt het aantal verbruikte credits op.
type: docs
weight: 30
url: /nl/net/groupdocs.viewer/metered/getconsumptioncredit/
---
## Metered.GetConsumptionCredit method

Haalt het aantal verbruikte credits op.

```csharp
public static decimal GetConsumptionCredit()
```

### Voorbeelden

Het volgende voorbeeld laat zien hoe u het aantal verbruikte credits kunt ophalen.

```csharp
string publicKey = "Public Key";
string privateKey = "Private Key";

Metered metered = new Metered();
metered.SetMeteredKey(publicKey, privateKey);

decimal creditsConsumed = Metered.GetConsumptionCredit();
```

### Zie ook

* class [Metered](../../metered)
* naamruimte [GroupDocs.Viewer](../../metered)
* montage [GroupDocs.Viewer](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->
