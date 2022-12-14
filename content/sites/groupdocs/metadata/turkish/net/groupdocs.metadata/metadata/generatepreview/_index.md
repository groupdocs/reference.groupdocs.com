---
title: GeneratePreview
second_title: .NET API Başvurusu için GroupDocs.Metadata
description: Belirtilen sayfalar için önizleme görüntüleri oluşturur.
type: docs
weight: 60
url: /tr/net/groupdocs.metadata/metadata/generatepreview/
---
## Metadata.GeneratePreview method

Belirtilen sayfalar için önizleme görüntüleri oluşturur.

```csharp
public void GeneratePreview(PreviewOptions previewOptions)
```

| Parametre | Tip | Tanım |
| --- | --- | --- |
| previewOptions | PreviewOptions | Önizleme oluşturma için bir dizi seçenek. |

### Notlar

**Daha fazla bilgi edin**

* [Belge önizlemesi oluştur](https://docs.groupdocs.com/display/metadatanet/Generate+document+preview)

### Örnekler

Bu kod parçacığı, belge sayfaları için resim önizlemelerinin nasıl oluşturulacağını gösterir.

```csharp
using (Metadata metadata = new Metadata(Constants.InputDocx))
{
    PreviewOptions previewOptions = new PreviewOptions(pageNumber => File.Create($"{Constants.OutputPath}\\result_{pageNumber}.png"));
    previewOptions.PreviewFormat = PreviewOptions.PreviewFormats.PNG;
    previewOptions.PageNumbers = new int[] { 1 };

    metadata.GeneratePreview(previewOptions);
}
```

### Ayrıca bakınız

* class [PreviewOptions](../../../groupdocs.metadata.options/previewoptions)
* class [Metadata](../../metadata)
* ad alanı [GroupDocs.Metadata](../../metadata)
* toplantı [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
