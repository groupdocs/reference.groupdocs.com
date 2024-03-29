---
title: FormFieldSignature
second_title: .NET API Başvurusu için GroupDocs.Signature
description: Form alanı imza özelliklerini içerir.
type: docs
weight: 460
url: /tr/net/groupdocs.signature.domain/formfieldsignature/
---
## FormFieldSignature class

Form alanı imza özelliklerini içerir.

```csharp
public abstract class FormFieldSignature : BaseSignature
```

## Özellikleri

| İsim | Tanım |
| --- | --- |
| [CreatedOn](../../groupdocs.signature.domain/basesignature/createdon) { get; set; } | İmza oluşturma tarihini alın veya ayarlayın. |
| [Deleted](../../groupdocs.signature.domain/basesignature/deleted) { get; } | Bu imzanın belgeden silinip silinmediğini gösteren bayrağı alın. Bu özellik, silinen imzaların listesini tutmak için yalnızca belge geçmişi günlük kayıtları için kullanılır. |
| [Height](../../groupdocs.signature.domain/basesignature/height) { get; set; } | İmzanın yüksekliğini belirtir. |
| [IsSignature](../../groupdocs.signature.domain/basesignature/issignature) { get; set; } | Bu bileşenin İmza mı yoksa belge içeriği mi olduğunu belirtmek için işaret alın veya ayarlayın. Bu özellik, öğeyi imza (doğru) veya belge öğesi (yanlış) olarak ayarlamak için Update yöntemiyle birlikte kullanılıyor. |
| [Left](../../groupdocs.signature.domain/basesignature/left) { get; set; } | İmzanın sol konumunu belirtir. |
| [ModifiedOn](../../groupdocs.signature.domain/basesignature/modifiedon) { get; set; } | İmza değiştirme tarihini alın veya ayarlayın. |
| [Name](../../groupdocs.signature.domain/formfieldsignature/name) { get; set; } | Benzersiz form alanı adını belirtir. |
| [PageNumber](../../groupdocs.signature.domain/basesignature/pagenumber) { get; } | . üzerinde bulunan sayfa imzasını belirtir |
| [SignatureId](../../groupdocs.signature.domain/basesignature/signatureid) { get; } | Belgedeki imzayı Güncelleme veya Silme yöntemleri üzerinden değiştirmek için benzersiz imza tanımlayıcı. Bu özellik, İmzalama veya Arama yöntemi çağrıldıktan sonra otomatik olarak ayarlanacaktır. Bu özellik, imzayı değiştirmek için manuel olarak ayarlanmadan önce kaydedilmişse. |
| [SignatureType](../../groupdocs.signature.domain/basesignature/signaturetype) { get; } | İmza türünü belirtir. |
| [Top](../../groupdocs.signature.domain/basesignature/top) { get; set; } | İmzanın en üst konumunu belirtir. |
| [Type](../../groupdocs.signature.domain/formfieldsignature/type) { get; } | Form alanı türünü belirtir. |
| [Value](../../groupdocs.signature.domain/formfieldsignature/value) { get; set; } | Form alanı veri nesnesini belirtir. |
| [Width](../../groupdocs.signature.domain/basesignature/width) { get; set; } | İmza genişliğini belirtir. |

## yöntemler

| İsim | Tanım |
| --- | --- |
| override [Clone](../../groupdocs.signature.domain/formfieldsignature/clone)() | FormField Signature örneğini Klonla. |
| override [Equals](../../groupdocs.signature.domain/formfieldsignature/equals)(object) | İmza özelliklerini karşılaştırmak için Equals yönteminin üzerine yazar |
| override [GetHashCode](../../groupdocs.signature.domain/formfieldsignature/gethashcode)() | GetHashCode yöntemini geçersiz kılar |

### Ayrıca bakınız

* class [BaseSignature](../basesignature)
* ad alanı [GroupDocs.Signature.Domain](../../groupdocs.signature.domain)
* toplantı [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
