---
title: ZipFile
second_title: .NET API Başvurusu için GroupDocs.Metadata
description: Arşivlenmiş bir dosya veya dizinle ilişkili meta verileri temsil eder.
type: docs
weight: 350
url: /tr/net/groupdocs.metadata.formats.archive/zipfile/
---
## ZipFile class

Arşivlenmiş bir dosya veya dizinle ilişkili meta verileri temsil eder.

```csharp
public sealed class ZipFile : CustomPackage
```

## Özellikleri

| İsim | Tanım |
| --- | --- |
| [CompressedSize](../../groupdocs.metadata.formats.archive/zipfile/compressedsize) { get; } | Bayt cinsinden sıkıştırılmış boyutu alır. |
| [CompressionMethod](../../groupdocs.metadata.formats.archive/zipfile/compressionmethod) { get; } | Sıkıştırma yöntemini alır. |
| [Count](../../groupdocs.metadata.common/metadatapackage/count) { get; } | Meta veri özelliklerinin sayısını alır. |
| [Flags](../../groupdocs.metadata.formats.archive/zipfile/flags) { get; } | ZIP giriş işaretlerini alır. |
| [Item](../../groupdocs.metadata.common/metadatapackage/item) { get; } | Şunu alır:[`MetadataProperty`](../../groupdocs.metadata.common/metadataproperty) belirtilen ada sahip. |
| [Keys](../../groupdocs.metadata.common/metadatapackage/keys) { get; } | Meta veri özellik adlarının bir koleksiyonunu alır. |
| [MetadataType](../../groupdocs.metadata.common/metadatapackage/metadatatype) { get; } | Meta veri türünü alır. |
| [ModificationDateTime](../../groupdocs.metadata.formats.archive/zipfile/modificationdatetime) { get; } | Son değişiklik tarihini ve saatini alır. |
| [Name](../../groupdocs.metadata.formats.archive/zipfile/name) { get; } | Giriş adını alır. |
| [PropertyDescriptors](../../groupdocs.metadata.common/metadatapackage/propertydescriptors) { get; } | GroupDocs.Metadata arama motoru aracılığıyla erişilebilen özellikler hakkında bilgi içeren tanımlayıcılardan oluşan bir koleksiyon alır. |
| [RawName](../../groupdocs.metadata.formats.archive/zipfile/rawname) { get; } | Girişin adını temsil eden bir bayt dizisi alır. |
| [UncompressedSize](../../groupdocs.metadata.formats.archive/zipfile/uncompressedsize) { get; } | Bayt cinsinden sıkıştırılmamış boyutu alır. |

## yöntemler

| İsim | Tanım |
| --- | --- |
| [AddProperties](../../groupdocs.metadata.common/metadatapackage/addproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | Belirtilen yüklemi karşılayan bilinen meta veri özelliklerini ekler. İşlem özyinelemeli olduğundan tüm iç içe geçmiş paketleri de etkiler. |
| [Contains](../../groupdocs.metadata.common/metadatapackage/contains)(string) | Paketin belirtilen ada sahip bir meta veri özelliği içerip içermediğini belirler. |
| virtual [FindProperties](../../groupdocs.metadata.common/metadatapackage/findproperties)(Func&lt;MetadataProperty, bool&gt;) | Belirtilen yüklemi karşılayan meta veri özelliklerini bulur. Arama özyinelemeli olduğu için iç içe geçmiş tüm paketleri de etkiler. |
| [GetEnumerator](../../groupdocs.metadata.common/metadatapackage/getenumerator)() | Koleksiyon boyunca yinelenen bir numaralandırıcı döndürür. |
| virtual [RemoveProperties](../../groupdocs.metadata.common/metadatapackage/removeproperties)(Func&lt;MetadataProperty, bool&gt;) | Belirtilen yüklemi karşılayan meta veri özelliklerini kaldırır. |
| virtual [Sanitize](../../groupdocs.metadata.common/metadatapackage/sanitize)() | Paketten yazılabilir meta veri özelliklerini kaldırır. İşlem özyinelemeli olduğundan iç içe geçmiş tüm paketleri de etkiler. |
| [SetProperties](../../groupdocs.metadata.common/metadatapackage/setproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | Belirtilen yüklemi karşılayan bilinen meta veri özelliklerini ayarlar. İşlem özyinelemeli olduğundan tüm iç içe geçmiş paketleri de etkiler. Bu yöntem,[`AddProperties`](../../groupdocs.metadata.common/metadatapackage/addproperties) Ve[`UpdateProperties`](../../groupdocs.metadata.common/metadatapackage/updateproperties) Mevcut bir özellik yüklemi karşılıyorsa, değeri güncellenir. Yüklemi karşılayan pakette eksik bilinen bir özellik varsa, pakete eklenir. |
| [UpdateProperties](../../groupdocs.metadata.common/metadatapackage/updateproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | Belirtilen yüklemi karşılayan bilinen meta veri özelliklerini günceller. İşlem yinelemeli olduğundan tüm iç içe geçmiş paketleri de etkiler. |

### Notlar

**Daha fazla bilgi edin**

* [ZIP arşivleriyle çalışma](https://docs.groupdocs.com/display/metadatanet/Working+with+ZIP+archives)

### Ayrıca bakınız

* class [CustomPackage](../../groupdocs.metadata.common/custompackage)
* ad alanı [GroupDocs.Metadata.Formats.Archive](../../groupdocs.metadata.formats.archive)
* toplantı [GroupDocs.Metadata](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
