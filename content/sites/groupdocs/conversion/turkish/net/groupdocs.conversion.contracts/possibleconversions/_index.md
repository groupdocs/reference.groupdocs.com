---
title: PossibleConversions
second_title: .NET API Başvurusu için GroupDocs.Conversion
description: Belirli kaynak dosya formatı için hangi dönüşüm çiftlerinin desteklendiğini gösteren bir eşlemeyi temsil eder.
type: docs
weight: 370
url: /tr/net/groupdocs.conversion.contracts/possibleconversions/
---
## PossibleConversions class

Belirli kaynak dosya formatı için hangi dönüşüm çiftlerinin desteklendiğini gösteren bir eşlemeyi temsil eder.

```csharp
public sealed class PossibleConversions : ValueObject
```

## Özellikleri

| İsim | Tanım |
| --- | --- |
| [All](../../groupdocs.conversion.contracts/possibleconversions/all) { get; } | Tüm hedef dosya türleri ve birincil/ikincil bayrak  IEnumerable of[`TargetConversion`](../targetconversion) |
| [Item](../../groupdocs.conversion.contracts/possibleconversions/item) { get; } | Belirtilen hedef dosya türü için hedef dönüştürmeyi döndürür (2 indexers) |
| [LoadOptions](../../groupdocs.conversion.contracts/possibleconversions/loadoptions) { get; } | Geçerli türden dönüştürmek için kullanılabilecek önceden tanımlanmış yükleme seçenekleri |
| [Primary](../../groupdocs.conversion.contracts/possibleconversions/primary) { get; } | Birincil hedef dosya türleri |
| [Secondary](../../groupdocs.conversion.contracts/possibleconversions/secondary) { get; } | İkincil hedef dosya türleri |
| [Source](../../groupdocs.conversion.contracts/possibleconversions/source) { get; } | Kaynak dosya biçimleri |

## yöntemler

| İsim | Tanım |
| --- | --- |
| override [Equals](../../groupdocs.conversion.contracts/valueobject/equals)(object) | İki nesne örneğinin eşit olup olmadığını belirler. |
| virtual [Equals](../../groupdocs.conversion.contracts/valueobject/equals)(ValueObject) | İki nesne örneğinin eşit olup olmadığını belirler. |
| override [GetHashCode](../../groupdocs.conversion.contracts/valueobject/gethashcode)() | Varsayılan hash işlevi olarak işlev görür. |

### Ayrıca bakınız

* class [ValueObject](../valueobject)
* ad alanı [GroupDocs.Conversion.Contracts](../../groupdocs.conversion.contracts)
* toplantı [GroupDocs.Conversion](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Conversion.dll -->
