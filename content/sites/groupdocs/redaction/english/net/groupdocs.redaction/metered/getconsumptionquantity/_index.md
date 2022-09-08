---
title: GetConsumptionQuantity
second_title: GroupDocs.Redaction for .NET API Reference
description: Retrieves the amount of MBs processed.
type: docs
weight: 40
url: /net/groupdocs.redaction/metered/getconsumptionquantity/
---
## Metered.GetConsumptionQuantity method

Retrieves the amount of MBs processed.

```csharp
public static decimal GetConsumptionQuantity()
```

### Return Value

consumption quantity

### Examples

The following example demonstrates how to retrieve the amount of MBs processed.

```csharp
string publicKey = "Public Key";
string privateKey = "Private Key";

Metered metered = new Metered();
metered.SetMeteredKey(publicKey, privateKey);

decimal mbProcessed = Metered.GetConsumptionQuantity();
```

### See Also

* class [Metered](../../metered)
* namespace [GroupDocs.Redaction](../../metered)
* assembly [GroupDocs.Redaction](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.redaction.dll -->