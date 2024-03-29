---
title: Metered
second_title: .NET API Başvurusu için GroupDocs.Search
description: Ürünün Metered lisansıyla etkinleştirilmesine ve işlenen MB miktarının alınmasına izin veren yöntemler sağlar. Metered lisansları hakkında daha fazla bilgi edininBuradahttps//purchase.groupdocs.com/faqs/licensing/metered .
type: docs
weight: 730
url: /tr/net/groupdocs.search/metered/
---
## Metered class

Ürünün Metered lisansıyla etkinleştirilmesine ve işlenen MB miktarının alınmasına izin veren yöntemler sağlar. Metered lisansları hakkında daha fazla bilgi edinin[Burada](https://purchase.groupdocs.com/faqs/licensing/metered) .

```csharp
public class Metered
```

## yapıcılar

| İsim | Tanım |
| --- | --- |
| [Metered](metered)() | Yeni bir örneğini başlatır[`Metered`](../metered) sınıf. |

## yöntemler

| İsim | Tanım |
| --- | --- |
| [SetMeteredKey](../../groupdocs.search/metered/setmeteredkey)(string, string) | Tarifeli genel ve özel anahtarı ayarlar. |
| static [GetConsumptionCredit](../../groupdocs.search/metered/getconsumptioncredit)() | Tüketim kredisini alır. |
| static [GetConsumptionQuantity](../../groupdocs.search/metered/getconsumptionquantity)() | Tüketim miktarını alır. |

### Notlar

**Daha fazla bilgi edin**

* [Değerlendirme Sınırlamaları ve Lisanslama](https://docs.groupdocs.com/display/searchnet/Evaluation+Limitations+and+Licensing)

### Örnekler

Örnek, ölçülü genel ve özel anahtarların nasıl ayarlanacağını gösterir.

```csharp
Metered metered = new Metered();
metered.SetMeteredKey("PublicKey", "PrivateKey");
```

### Ayrıca bakınız

* ad alanı [GroupDocs.Search](../../groupdocs.search)
* toplantı [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
