---
title: Metered
second_title: GroupDocs.Redaction for .NET API Reference
description: Provides methods which allow to activate product with Metered license and retrieve amount of MBs processed. Learn more about Metered licenses herehttps//purchase.groupdocs.com/faqs/licensing/metered.
type: docs
weight: 280
url: /net/groupdocs.redaction/metered/
---
## Metered class

Provides methods which allow to activate product with Metered license and retrieve amount of MBs processed. Learn more about Metered licenses [here](https://purchase.groupdocs.com/faqs/licensing/metered).

```csharp
public class Metered
```

## Constructors

| Name | Description |
| --- | --- |
| [Metered](metered)() | Initializes a new instance of Metered class. |

## Methods

| Name | Description |
| --- | --- |
| [SetMeteredKey](../../groupdocs.redaction/metered/setmeteredkey)(string, string) | Activates the product with Metered keys. |
| static [GetConsumptionCredit](../../groupdocs.redaction/metered/getconsumptioncredit)() | Gets the consumption credit. |
| static [GetConsumptionQuantity](../../groupdocs.redaction/metered/getconsumptionquantity)() | Retrieves the amount of MBs processed. |

### Remarks

**Learn more**

* More about licensing: [GroupDocs Licensing FAQ](https://purchase.groupdocs.com/faqs/licensing)
* More about **GroupDocs.Redaction** licensing: [Evaluation Limitations and Licensing](https://docs.groupdocs.com/redaction/net/evaluation-limitations-and-licensing/)

### Examples

The following example demonstrates how to activate the product with Metered keys.

```csharp
[C#]

Metered matered = new Metered();
matered.SetMeteredKey("PublicKey", "PrivateKey");


[Visual Basic]

Dim matered As Metered = New Metered
matered.SetMeteredKey("PublicKey", "PrivateKey")
```

the component jar file:

```csharp
Metered matered = new Metered();
matered.setMeteredKey("PublicKey", "PrivateKey");
```

### See Also

* namespace [GroupDocs.Redaction](../../groupdocs.redaction)
* assembly [GroupDocs.Redaction](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.redaction.dll -->
