---
title: PdfSaveOptions
second_title: .NET API Başvurusu için GroupDocs.Editor
description: PDF Taşınabilir Belge Biçimi belgelerini oluşturmak ve kaydetmek için özel seçenekleri belirlemeye izin verir
type: docs
weight: 1060
url: /tr/net/groupdocs.editor.options/pdfsaveoptions/
---
## PdfSaveOptions class

PDF (Taşınabilir Belge Biçimi) belgelerini oluşturmak ve kaydetmek için özel seçenekleri belirlemeye izin verir

```csharp
public sealed class PdfSaveOptions : ISaveOptions
```

## yapıcılar

| İsim | Tanım |
| --- | --- |
| [PdfSaveOptions](pdfsaveoptions)() | Default_Constructor |

## Özellikleri

| İsim | Tanım |
| --- | --- |
| [Compliance](../../groupdocs.editor.options/pdfsaveoptions/compliance) { get; set; } | Çıktı belgeleri için PDF standartlarına uygunluk düzeyini belirtir. Varsayılan: PdfCompliance.Pdf17. |
| [FontEmbedding](../../groupdocs.editor.options/pdfsaveoptions/fontembedding) { get; set; } | Orijinal belgede kullanılan yazı tipi kaynaklarının ortaya çıkan PDF belgesine gömülmesinden sorumludur. Varsayılan olarak herhangi bir yazı tipi gömmez (NotEmbed). |
| [OptimizeMemoryUsage](../../groupdocs.editor.options/pdfsaveoptions/optimizememoryusage) { get; set; } | HTML'den belge oluşturma sırasında, bellek kullanımını azaltma maliyeti olarak performansı düşüren bellek optimizasyon mekanizmalarını etkinleştirir. Bu seçeneğin doğru olarak ayarlanması, daha yavaş kaydetme süresi pahasına büyük belgeler oluştururken bellek tüketimini önemli ölçüde azaltabilir. Varsayılan değer yanlış (daha iyi performans için bellek optimizasyonu devre dışı bırakıldı). |
| [Password](../../groupdocs.editor.options/pdfsaveoptions/password) { get; set; } | Parola, oluşturulan PDF belgesine kullanıcı parolası olarak uygulanacak, açılış için gereklidir. NULL veya boşsa, belgeye parola uygulanmaz. Aksi takdirde, belge RC4 (anahtar uzunluğu 128 bit) ile şifrelenecektir. Varsayılan olarak NULL'dur — parola uygulanmaz. |

### Ayrıca bakınız

* interface [ISaveOptions](../isaveoptions)
* ad alanı [GroupDocs.Editor.Options](../../groupdocs.editor.options)
* toplantı [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
