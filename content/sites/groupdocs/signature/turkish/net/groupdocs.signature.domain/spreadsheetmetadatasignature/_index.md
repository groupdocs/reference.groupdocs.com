---
title: SpreadsheetMetadataSignature
second_title: .NET API Başvurusu için GroupDocs.Signature
description: Elektronik Tablo Meta Veri İmzası özelliklerini içerir.
type: docs
weight: 870
url: /tr/net/groupdocs.signature.domain/spreadsheetmetadatasignature/
---
## SpreadsheetMetadataSignature class

Elektronik Tablo Meta Veri İmzası özelliklerini içerir.

```csharp
public sealed class SpreadsheetMetadataSignature : MetadataSignature
```

## yapıcılar

| İsim | Tanım |
| --- | --- |
| [SpreadsheetMetadataSignature](spreadsheetmetadatasignature#constructor)(string) | Önceden tanımlanmış ad ve boş değerle Elektronik Tablo Meta Veri İmzası oluşturur. |
| [SpreadsheetMetadataSignature](spreadsheetmetadatasignature#constructor_1)(string, object) | Önceden tanımlanmış değerlerle Elektronik Tablo Meta Veri İmzası oluşturur. |

## Özellikleri

| İsim | Tanım |
| --- | --- |
| [CreatedOn](../../groupdocs.signature.domain/basesignature/createdon) { get; set; } | İmza oluşturma tarihini alın veya ayarlayın. |
| [DataEncryption](../../groupdocs.signature.domain/metadatasignature/dataencryption) { get; set; } | Şunun uygulanmasını alır veya ayarlar:[`IDataEncryption`](../../groupdocs.signature.domain.extensions/idataencryption) imza Değeri özelliklerini kodlamak ve kodunu çözmek için arayüz. |
| [Deleted](../../groupdocs.signature.domain/basesignature/deleted) { get; } | Bu imzanın belgeden silinip silinmediğini gösteren bayrağı alın. Bu özellik, silinen imzaların listesini tutmak için yalnızca belge geçmişi günlük kayıtları için kullanılır. |
| [Height](../../groupdocs.signature.domain/basesignature/height) { get; set; } | İmzanın yüksekliğini belirtir. |
| [IsSignature](../../groupdocs.signature.domain/basesignature/issignature) { get; set; } | Bu bileşenin İmza mı yoksa belge içeriği mi olduğunu belirtmek için işaret alın veya ayarlayın. Bu özellik, öğeyi imza (doğru) veya belge öğesi (yanlış) olarak ayarlamak için Update yöntemiyle birlikte kullanılıyor. |
| [Left](../../groupdocs.signature.domain/basesignature/left) { get; set; } | İmzanın sol konumunu belirtir. |
| [ModifiedOn](../../groupdocs.signature.domain/basesignature/modifiedon) { get; set; } | İmza değiştirme tarihini alın veya ayarlayın. |
| [Name](../../groupdocs.signature.domain/metadatasignature/name) { get; set; } | Benzersiz meta veri adını belirtir. |
| [PageNumber](../../groupdocs.signature.domain/basesignature/pagenumber) { get; } | . üzerinde bulunan sayfa imzasını belirtir |
| [SignatureId](../../groupdocs.signature.domain/basesignature/signatureid) { get; } | Belgedeki imzayı Güncelleme veya Silme yöntemleri üzerinden değiştirmek için benzersiz imza tanımlayıcı. Bu özellik, İmzalama veya Arama yöntemi çağrıldıktan sonra otomatik olarak ayarlanacaktır. Bu özellik, imzayı değiştirmek için manuel olarak ayarlanmadan önce kaydedilmişse. |
| [SignatureType](../../groupdocs.signature.domain/basesignature/signaturetype) { get; } | İmza türünü belirtir. |
| [Top](../../groupdocs.signature.domain/basesignature/top) { get; set; } | İmzanın en üst konumunu belirtir. |
| [Type](../../groupdocs.signature.domain/metadatasignature/type) { get; } | Meta veri değeri türünü belirtir. |
| [Value](../../groupdocs.signature.domain/metadatasignature/value) { get; set; } | Meta veri nesnesini belirtir. |
| [Width](../../groupdocs.signature.domain/basesignature/width) { get; set; } | İmza genişliğini belirtir. |

## yöntemler

| İsim | Tanım |
| --- | --- |
| override [Clone](../../groupdocs.signature.domain/spreadsheetmetadatasignature/clone#clone_1)() | Klon Meta Veri İmza örneği. |
| override [Clone](../../groupdocs.signature.domain/spreadsheetmetadatasignature/clone#clone)(object) | Elektronik Tablo Meta Veri İmza örneğini verilen değerle Klonla. |
| override [Equals](../../groupdocs.signature.domain/metadatasignature/equals)(object) | İmza özelliklerini karşılaştırmak için Equals yönteminin üzerine yazar |
| [GetData&lt;T&gt;](../../groupdocs.signature.domain/metadatasignature/getdata)() | Seri kaldırma üzerinden Meta Veri İmza Değerinden nesne elde edin. |
| [GetData&lt;T&gt;](../../groupdocs.signature.domain/metadatasignature/getdata)(IDataEncryption) | Seri kaldırma üzerinden Meta Veri İmza Metninden nesne elde edin. |
| override [GetHashCode](../../groupdocs.signature.domain/metadatasignature/gethashcode)() | GetHashCode yöntemini geçersiz kılar |
| virtual [ToBoolean](../../groupdocs.signature.domain/metadatasignature/toboolean)() | Boole değerine dönüştürür. |
| virtual [ToDateTime](../../groupdocs.signature.domain/metadatasignature/todatetime)() | DateTime. biçimine dönüştürür |
| virtual [ToDateTime](../../groupdocs.signature.domain/metadatasignature/todatetime)(IFormatProvider) | DateTime. biçimine dönüştürür |
| virtual [ToDecimal](../../groupdocs.signature.domain/metadatasignature/todecimal)() | Ondalık Sayıya Dönüştürür. |
| virtual [ToDecimal](../../groupdocs.signature.domain/metadatasignature/todecimal)(IFormatProvider) | Ondalık Sayıya Dönüştürür. |
| virtual [ToDouble](../../groupdocs.signature.domain/metadatasignature/todouble)() | Çifte Dönüştürür. |
| virtual [ToDouble](../../groupdocs.signature.domain/metadatasignature/todouble)(IFormatProvider) | Çifte Dönüştürür. |
| virtual [ToInteger](../../groupdocs.signature.domain/metadatasignature/tointeger)() | Tamsayıya dönüştürür. |
| virtual [ToSingle](../../groupdocs.signature.domain/metadatasignature/tosingle)() | Float'a dönüştürür. |
| virtual [ToSingle](../../groupdocs.signature.domain/metadatasignature/tosingle)(IFormatProvider) | Float'a dönüştürür. |
| override [ToString](../../groupdocs.signature.domain/spreadsheetmetadatasignature/tostring#tostring)() | ToString() yöntemini geçersiz kılarak Dizeye dönüştürür |
| virtual [ToString](../../groupdocs.signature.domain/metadatasignature/tostring)(string) | Belirtilen format ile Dizeye dönüştürür |
| override [ToString](../../groupdocs.signature.domain/spreadsheetmetadatasignature/tostring#tostring_2)(string, IFormatProvider) | Belirtilen format ile Dizeye dönüştürür |

### Ayrıca bakınız

* class [MetadataSignature](../metadatasignature)
* ad alanı [GroupDocs.Signature.Domain](../../groupdocs.signature.domain)
* toplantı [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
