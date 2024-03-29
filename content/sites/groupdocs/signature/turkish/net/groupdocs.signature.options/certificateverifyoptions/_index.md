---
title: CertificateVerifyOptions
second_title: .NET API Başvurusu için GroupDocs.Signature
description: Sertifika belgelerini doğrulama seçeneklerini korur.
type: docs
weight: 1300
url: /tr/net/groupdocs.signature.options/certificateverifyoptions/
---
## CertificateVerifyOptions class

Sertifika belgelerini doğrulama seçeneklerini korur.

```csharp
public class CertificateVerifyOptions : VerifyOptions
```

## yapıcılar

| İsim | Tanım |
| --- | --- |
| [CertificateVerifyOptions](certificateverifyoptions#constructor)() | Varsayılan değerlerle TextVerifyOptions'ın yeni bir örneğini başlatır. |
| [CertificateVerifyOptions](certificateverifyoptions#constructor_1)(string) | Verify. 'ye tabi olarak CertificateVerifyOptions'ın yeni bir örneğini başlatır. |

## Özellikleri

| İsim | Tanım |
| --- | --- |
| [AllPages](../../groupdocs.signature.options/verifyoptions/allpages) { get; set; } | Her belge sayfasını doğrulamak için işaretleyin. Varsayılan değer olarak true. |
| [Expired](../../groupdocs.signature.options/certificateverifyoptions/expired) { get; } | Sertifika geçerlilik sonucu nedeniyle geçerlilik süresinin dolduğunu gösterir. Özellik salt okunurdur. |
| [Extensions](../../groupdocs.signature.options/verifyoptions/extensions) { get; set; } | Alternatif imza seçenekleri doğrulaması için ek uzantılar. |
| [Issuer](../../groupdocs.signature.options/certificateverifyoptions/issuer) { get; set; } | Doğrulanması gerekiyorsa Sertifika Veren'i belirtin. |
| [IsValid](../../groupdocs.signature.options/verifyoptions/isvalid) { get; } | Geçerli özellik bayrağı. |
| [MatchType](../../groupdocs.signature.options/certificateverifyoptions/matchtype) { get; set; } | Metin Eşleme Türü doğrulamasını alır veya ayarlar. |
| virtual [PageNumber](../../groupdocs.signature.options/verifyoptions/pagenumber) { get; set; } | Doğrulanacak Belge Sayfa Numarası. Özellik ayarlanmazsa - Belgesinin tüm Sayfaları ilk geçtiği için doğrulanacaktır. Minimum değer: 1. |
| virtual [PagesSetup](../../groupdocs.signature.options/verifyoptions/pagessetup) { get; set; } | Doğrulanacak sayfaları belirtmek için Sayfa Seçenekleri. |
| [PerformChainValidation](../../groupdocs.signature.options/certificateverifyoptions/performchainvalidation) { get; set; } | Doğrulama işleminin temel doğrulama ilkesini kullanarak X.509 zincir doğrulaması sağlaması gerekiyorsa alın veya ayarlayın. Varsayılan olarak bu değer doğrudur. |
| [SerialNumber](../../groupdocs.signature.options/certificateverifyoptions/serialnumber) { get; set; } | Doğrulanması gerekiyorsa Sertifika Seri Numarasını belirtin. |
| [Subject](../../groupdocs.signature.options/certificateverifyoptions/subject) { get; set; } | Doğrulanması gerekiyorsa Sertifika konusunu belirtin. |
| [Thumbprint](../../groupdocs.signature.options/certificateverifyoptions/thumbprint) { get; set; } | Doğrulanması gerekiyorsa Sertifika Parmak İzi'ni belirtin. |

### Notlar

**Daha fazla bilgi edin**

* GroupDocs.Signature tarafından sertifika belgelerinin temel kullanımı: [Dijital Sertifika özelliklerini önizleyin](https://docs.groupdocs.com/signature/net/preview-certificate-properties/)

### Ayrıca bakınız

* class [VerifyOptions](../verifyoptions)
* ad alanı [GroupDocs.Signature.Options](../../groupdocs.signature.options)
* toplantı [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
