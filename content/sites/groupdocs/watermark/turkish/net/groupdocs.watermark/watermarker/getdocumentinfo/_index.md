---
title: GetDocumentInfo
second_title: .NET API Başvurusu için GroupDocs.Watermark
description: Yüklenen belgenin formatı hakkında bilgi alır.
type: docs
weight: 70
url: /tr/net/groupdocs.watermark/watermarker/getdocumentinfo/
---
## Watermarker.GetDocumentInfo method

Yüklenen belgenin formatı hakkında bilgi alır.

```csharp
public IDocumentInfo GetDocumentInfo()
```

### Geri dönüş değeri

bu[`IDocumentInfo`](../../../groupdocs.watermark.common/idocumentinfo) algılanan bilgileri içeren örnek.

### Notlar

Belge bilgilerini alma hakkında daha fazla bilgi edinin [Belge bilgilerini al](https://docs.groupdocs.com/display/watermarknet/Get+document+info) .

### Örnekler

Desteklenen herhangi bir belge türü hakkında bilgi alın.

```csharp
using (Watermarker watermarker = new Watermarker(@"D:\test.ppt"))
{
    IDocumentInfo docInfo = watermarker.GetDocumentInfo();
    Console.WriteLine("Document size: {0}", docInfo.Size);
    Console.WriteLine("Document format: {0}", docInfo.FileType.FileFormat);
    Console.WriteLine("Document contains {0} pages", docInfo.PageCount);
}
```

### Ayrıca bakınız

* interface [IDocumentInfo](../../../groupdocs.watermark.common/idocumentinfo)
* class [Watermarker](../../watermarker)
* ad alanı [GroupDocs.Watermark](../../watermarker)
* toplantı [GroupDocs.Watermark](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
