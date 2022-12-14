---
title: SpreadsheetContent
second_title: .NET API Başvurusu için GroupDocs.Watermark
description: Filigranın yerleştirilebileceği bir Excel belgesini temsil eder.
type: docs
weight: 1100
url: /tr/net/groupdocs.watermark.contents.spreadsheet/spreadsheetcontent/
---
## SpreadsheetContent class

Filigranın yerleştirilebileceği bir Excel belgesini temsil eder.

```csharp
public class SpreadsheetContent : Content
```

## Özellikleri

| İsim | Tanım |
| --- | --- |
| [Worksheets](../../groupdocs.watermark.contents.spreadsheet/spreadsheetcontent/worksheets) { get; } | Bunun tüm çalışma sayfalarının koleksiyonunu alır[`SpreadsheetContent`](../spreadsheetcontent) . |

## yöntemler

| İsim | Tanım |
| --- | --- |
| [Decrypt](../../groupdocs.watermark.contents.spreadsheet/spreadsheetcontent/decrypt)() | Belgenin şifresini çözer. |
| [Dispose](../../groupdocs.watermark.contents/content/dispose)() | Geçerli örneği ortadan kaldırır. |
| [Encrypt](../../groupdocs.watermark.contents.spreadsheet/spreadsheetcontent/encrypt)(string) | İçeriği şifreler. |
| [FindImages](../../groupdocs.watermark.contents/contentpart/findimages)() | İçerikteki tüm resimleri bulur. Arama, belirtilen nesnelerde gerçekleştirilir.[`SearchableObjects`](../../groupdocs.watermark/watermarker/searchableobjects) . |
| [FindImages](../../groupdocs.watermark.contents/contentpart/findimages)(ImageSearchCriteria) | Belirtilen arama kriterlerine göre görüntüleri bulur. Arama, belirtilen nesnelerde gerçekleştirilir.[`SearchableObjects`](../../groupdocs.watermark/watermarker/searchableobjects) . |
| [Search](../../groupdocs.watermark.contents/contentpart/search)() | İçerikteki tüm olası filigranları bulur. Arama, belirtilen nesnelerde gerçekleştirilir.[`SearchableObjects`](../../groupdocs.watermark/watermarker/searchableobjects) . |
| [Search](../../groupdocs.watermark.contents/contentpart/search)(SearchCriteria) | Belirtilen arama kriterlerine göre olası filigranları bulur. Arama, belirtilen nesnelerde gerçekleştirilir.[`SearchableObjects`](../../groupdocs.watermark/watermarker/searchableobjects) . |

### Notlar

**Daha fazla bilgi edin:**

* [Elektronik tablo belgelerine filigran ekleme](https://docs.groupdocs.com/display/watermarknet/Add+watermarks+to+spreadsheet+documents)
* [Elektronik tablo belgesindeki şekiller](https://docs.groupdocs.com/display/watermarknet/Shapes+in+spreadsheet+document)
* [Elektronik tablo belgesi ekleriyle çalışma](https://docs.groupdocs.com/display/watermarknet/Working+with+spreadsheet+document+attachments)
* [Çalışma sayfası arka planlarıyla çalışma](https://docs.groupdocs.com/display/watermarknet/Working+with+worksheet+backgrounds)
* [Çalışma sayfası üstbilgileri ve altbilgileriyle çalışma](https://docs.groupdocs.com/display/watermarknet/Working+with+worksheet+headers+and+footers)

### Örnekler

Desteklenen herhangi bir türden Excel belgesini yükleyin ve kaydedin.

```csharp
SpreadsheetLoadOptions loadOptions = new SpreadsheetLoadOptions();
using (Watermarker watermarker = new Watermarker(@"D:\input.xls", loadOptions))
{
    // Belirli bir çalışma sayfasına veya tüm çalışma sayfalarına filigran eklemek için Ekle yöntemini kullanın.

    // Değişiklikleri Kaydet.
    watermarker.Save(@"D:\output.xls");
}
```

### Ayrıca bakınız

* class [Content](../../groupdocs.watermark.contents/content)
* ad alanı [GroupDocs.Watermark.Contents.Spreadsheet](../../groupdocs.watermark.contents.spreadsheet)
* toplantı [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
