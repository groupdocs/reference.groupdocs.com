---
title: GetConsumptionQuantity
second_title: GroupDocs.Editor لمرجع .NET API
description: استرداد كمية الميغابايت التي تمت معالجتها .
type: docs
weight: 40
url: /ar/net/groupdocs.editor/metered/getconsumptionquantity/
---
## Metered.GetConsumptionQuantity method

استرداد كمية الميغابايت التي تمت معالجتها .

```csharp
public static decimal GetConsumptionQuantity()
```

### أمثلة

المثال التالي يوضح كيفية استرداد كمية الميغابايت التي تمت معالجتها.

```csharp
string publicKey = "Public Key";
string privateKey = "Private Key";

Metered metered = new Metered();
metered.SetMeteredKey(publicKey, privateKey);

decimal mbProcessed = Metered.GetConsumptionQuantity();
```

### أنظر أيضا

* class [Metered](../../metered)
* مساحة الاسم [GroupDocs.Editor](../../metered)
* المجسم [GroupDocs.Editor](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
