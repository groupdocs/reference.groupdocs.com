---
title: ImageSaveOptions
second_title: .NET API Başvurusu için GroupDocs.Signature
description: Görüntü belgeleri için seçenekleri kaydedin.
type: docs
weight: 1320
url: /tr/net/groupdocs.signature.options/imagesaveoptions/
---
## ImageSaveOptions class

Görüntü belgeleri için seçenekleri kaydedin.

```csharp
public class ImageSaveOptions : SaveOptions
```

## yapıcılar

| İsim | Tanım |
| --- | --- |
| [ImageSaveOptions](imagesaveoptions#constructor)() | Varsayılan değerlerle ImagesSaveOptions sınıfının yeni bir örneğini başlatır. |
| [ImageSaveOptions](imagesaveoptions#constructor_1)(bool) | Üzerine yazma bayrağıyla ImagesSaveOptions sınıfının yeni bir örneğini başlatır. |
| [ImageSaveOptions](imagesaveoptions#constructor_2)(ImageSaveFileFormat, bool) | Belirtilen çıktı türü ve üzerine yazma bayrağıyla ImagesSaveOptions sınıfının yeni bir örneğini başlatır. |

## Özellikleri

| İsim | Tanım |
| --- | --- |
| [AddMissingExtenstion](../../groupdocs.signature.options/saveoptions/addmissingextenstion) { get; set; } | Çıktı dosyası path 'de eksik olduğunda uzantıyı otomatik olarak eklemek için bayrağı alır veya ayarlar. Varsayılan değer false. |
| [FileFormat](../../groupdocs.signature.options/imagesaveoptions/fileformat) { get; set; } | İmzalı belgenin dosya biçimini alır veya ayarlar. |
| [OverwriteExistingFiles](../../groupdocs.signature.options/saveoptions/overwriteexistingfiles) { get; set; } | Mevcut dosyanın üzerine yeni çıktı dosyası yazılıp yazılmayacağını ayarlar veya alır. Aksi takdirde, sonek olarak sayı ile yeni dosya oluşturulur. Varsayılan olarak bu değer, dosyanın üzerine yazılacağı anlamına gelen true olarak ayarlanır. |
| [Password](../../groupdocs.signature.options/saveoptions/password) { get; set; } | İmzalı belgeyi parola korumalı olarak kaydetmek için parolayı alır veya ayarlar. Bu özellik Görüntü belgeleri için desteklenmez. |
| [UseOriginalPassword](../../groupdocs.signature.options/saveoptions/useoriginalpassword) { get; set; } | İmzalı belgeyi korumalı olarak kaydetmek için LoadOptions'tan parola kullanılıp kullanılmayacağını ayarlar. Varsayılan değer true'dur. Bu özellik Görüntü belgeleri için desteklenmez. |

### Ayrıca bakınız

* class [SaveOptions](../saveoptions)
* ad alanı [GroupDocs.Signature.Options](../../groupdocs.signature.options)
* toplantı [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
