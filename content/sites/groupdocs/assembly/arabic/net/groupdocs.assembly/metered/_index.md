---
title: Metered
second_title: GroupDocs.Assembly للحصول على مرجع .NET API
description: يوفر طرقًا للعمل مع الترخيص المحدود .
type: docs
weight: 260
url: /ar/net/groupdocs.assembly/metered/
---
## Metered class

يوفر طرقًا للعمل مع الترخيص المحدود .

```csharp
public class Metered
```

## المنشئون

| اسم | وصف |
| --- | --- |
| [Metered](metered)() | إنشاء مثيل جديد لهذه الفئة . |

## طُرق

| اسم | وصف |
| --- | --- |
| [SetMeteredKey](../../groupdocs.assembly/metered/setmeteredkey)(string, string) | تمكين الترخيص المقنن للمكون عن طريق تحديد المفاتيح ذات المقاييس العامة والخاصة المناسبة. |
| static [GetConsumptionCredit](../../groupdocs.assembly/metered/getconsumptioncredit)() | إرجاع عدد الائتمانات المستهلك حاليًا. |
| static [GetConsumptionQuantity](../../groupdocs.assembly/metered/getconsumptionquantity)() | إرجاع العدد المستهلك حاليًا بالميجابايت. |

### أمثلة

في هذا المثال ، تم إجراء محاولة لتعيين المفاتيح العامة والخاصة التي تم قياسها:

```csharp
[C#]

Metered metered = new Metered();
metered.SetMeteredKey("PublicKey", "PrivateKey");

[Visual Basic]

Dim metered As Metered = New Metered
metered.SetMeteredKey("PublicKey", "PrivateKey")
```

### أنظر أيضا

* مساحة الاسم [GroupDocs.Assembly](../../groupdocs.assembly)
* المجسم [GroupDocs.Assembly](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Assembly.dll -->
