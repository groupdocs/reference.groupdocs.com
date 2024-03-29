---
title: DocumentAssemblyOptions
second_title: .NET API Başvurusu için GroupDocs.Assembly
description: Davranışını kontrol eden seçenekleri belirtir.DocumentAssembler./documentassembler bir belgeyi bir araya getirirken.
type: docs
weight: 210
url: /tr/net/groupdocs.assembly/documentassemblyoptions/
---
## DocumentAssemblyOptions enumeration

Davranışını kontrol eden seçenekleri belirtir.[`DocumentAssembler`](../documentassembler) bir belgeyi bir araya getirirken.

```csharp
[Flags]
public enum DocumentAssemblyOptions
```

### değerler

| İsim | Değer | Tanım |
| --- | --- | --- |
| None | `0` | Varsayılan seçenekleri belirtir. |
| AllowMissingMembers | `1` | Eksik nesne üyelerine derleyici tarafından boş hazır değerler olarak davranılması gerektiğini belirtir. Bu seçenek yalnızca örnek (yani statik olmayan) nesne üyelerine ve uzantı yöntemlerine erişimi etkiler. Bu seçeneği ayarlanmamışsa, derleyici eksik bir nesne üyesiyle karşılaştığında bir istisna atar. |
| UpdateFieldsAndFormulas | `2` | Sözcük İşleme sonuç belgelerinin alanlarının ve Elektronik Tablo belgelerinin formüllerinin birleştirici tarafından güncellenmesi gerektiğini belirtir. |
| RemoveEmptyParagraphs | `4` | Şablon sözdizimi etiketleri kaldırıldıktan veya boş değerlerle değiştirildikten sonra birleştiricinin boş kalan paragrafları kaldırması gerektiğini belirtir. |
| InlineErrorMessages | `8` | Çeviricinin şablon sözdizimi hata iletilerini çıktı belgelerine satır içi olarak eklemesi gerektiğini belirtir. Bu seçenek ayarlanmazsa, derleyici bir sözdizimi hatasıyla karşılaştığında bir istisna atar. |
| UseSpreadsheetDataTypes | `10` | Yalnızca Elektronik Tablo belgeleriyle ilgilidir. Değerlendirilen ifade sonuçlarının, hücreler içindeki varsayılan biçimlendirmesini de etkileyen karşılık gelen Elektronik Tablo veri türleriyle eşlenmesi gerektiğini belirtir. Bu seçeneği ayarlanmamışsa, ifade sonuçları her zaman çevirici tarafından dizeler olarak yazılır. İfade sonuçları şablon sözdizimi kullanılarak biçimlendirildiğinde bu seçeneğin hiçbir etkisi yoktur - ifade sonuçları her zaman dizeler olarak yazılır. |

### Ayrıca bakınız

* ad alanı [GroupDocs.Assembly](../../groupdocs.assembly)
* toplantı [GroupDocs.Assembly](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Assembly.dll -->
