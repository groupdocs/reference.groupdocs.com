---
title: GetConsumptionCredit
second_title: GroupDocs.Conversion for .NET API Referens
description: Hämtar antalet förbrukade krediter.
type: docs
weight: 30
url: /sv/net/groupdocs.conversion/metered/getconsumptioncredit/
---
## Metered.GetConsumptionCredit method

Hämtar antalet förbrukade krediter.

```csharp
public static decimal GetConsumptionCredit()
```

### Exempel

Följande exempel visar hur man hämtar antalet förbrukade krediter.

```csharp
string publicKey = "Public Key";
string privateKey = "Private Key";

Metered metered = new Metered();
metered.SetMeteredKey(publicKey, privateKey);

decimal creditsConsumed = Metered.GetConsumptionCredit();
```

### Se även

* class [Metered](../../metered)
* namnutrymme [GroupDocs.Conversion](../../metered)
* hopsättning [GroupDocs.Conversion](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Conversion.dll -->
