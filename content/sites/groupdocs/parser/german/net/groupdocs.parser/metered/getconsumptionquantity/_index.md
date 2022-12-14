---
title: GetConsumptionQuantity
second_title: GroupDocs.Parser für .NET-API-Referenz
description: Ruft die Menge der verarbeiteten MB ab.
type: docs
weight: 40
url: /de/net/groupdocs.parser/metered/getconsumptionquantity/
---
## Metered.GetConsumptionQuantity method

Ruft die Menge der verarbeiteten MB ab.

```csharp
public static decimal GetConsumptionQuantity()
```

### Rückgabewert

Ein Dezimalwert, der die Verbrauchsmenge darstellt.

### Beispiele

Das folgende Beispiel zeigt, wie die Menge der verarbeiteten MB abgerufen wird.

```csharp
string publicKey = "Public Key";
string privateKey = "Private Key";

Metered metered = new Metered();
metered.SetMeteredKey(publicKey, privateKey);

decimal mbProcessed = Metered.GetConsumptionQuantity();
```

### Siehe auch

* class [Metered](../../metered)
* namensraum [GroupDocs.Parser](../../metered)
* Montage [GroupDocs.Parser](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->
