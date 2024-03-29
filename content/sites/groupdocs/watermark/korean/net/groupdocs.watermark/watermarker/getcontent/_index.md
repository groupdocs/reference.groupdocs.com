---
title: GetContent
second_title: .NET API 참조용 GroupDocs.Watermark
description: 반환Contentgroupdocs.watermark.contents/content 로드된 문서의 개체.
type: docs
weight: 60
url: /ko/net/groupdocs.watermark/watermarker/getcontent/
---
## Watermarker.GetContent&lt;T&gt; method

반환[`Content`](../../../groupdocs.watermark.contents/content) 로드된 문서의 개체.

```csharp
public T GetContent<T>()
    where T : Content
```

| 모수 | 설명 |
| --- | --- |
| T | 요청된 유형의[`Content`](../../../groupdocs.watermark.contents/content) 물체. |

### 반환 값

그만큼[`Content`](../../../groupdocs.watermark.contents/content) 로드된 문서의 개체입니다.

### 예

워터마크가 추가된 PDF 문서 페이지 래스터화.

```csharp
PdfLoadOptions loadOptions = new PdfLoadOptions();
using (Watermarker watermarker = new Watermarker(@"C:\doc.pdf", loadOptions))
{ 
    using (ImageWatermark watermark = new ImageWatermark(@"C:\watermark.png"))
    {
        watermarker.Add(watermark);
    }

    PdfContent content = watermarker.GetContent<PdfContent>();
    content.Rasterize(300, 300, PdfImageConversionFormat.Png);

    watermarker.Save();
}
```

### 또한보십시오

* class [Content](../../../groupdocs.watermark.contents/content)
* class [Watermarker](../../watermarker)
* 네임스페이스 [GroupDocs.Watermark](../../watermarker)
* 집회 [GroupDocs.Watermark](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
