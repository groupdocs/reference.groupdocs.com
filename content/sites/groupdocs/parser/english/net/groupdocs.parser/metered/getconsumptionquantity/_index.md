---
title: GetConsumptionQuantity
second_title: GroupDocs.Parser for .NET API Reference
description: Retrieves amount of MBs processed.
type: docs
weight: 40
url: /net/groupdocs.parser/metered/getconsumptionquantity/
---
## Metered.GetConsumptionQuantity method

Retrieves amount of MBs processed.

```csharp
public static decimal GetConsumptionQuantity()
```

### Return Value

A decimal value that represents the consumption quantity.

### Examples

Following example demonstrates how to retrieve amount of MBs processed.

```csharp
string publicKey = "Public Key";
string privateKey = "Private Key";

Metered metered = new Metered();
metered.SetMeteredKey(publicKey, privateKey);

decimal mbProcessed = Metered.GetConsumptionQuantity();
```

### See Also

* class [Metered](../../metered)
* namespace [GroupDocs.Parser](../../../groupdocs.parser)
* assembly [GroupDocs.Parser](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.parser.dll -->
