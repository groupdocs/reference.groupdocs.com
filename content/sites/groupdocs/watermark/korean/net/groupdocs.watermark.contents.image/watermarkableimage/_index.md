---
title: WatermarkableImage
second_title: .NET API 참조용 GroupDocs.Watermark
description: 문서 내부의 이미지를 나타냅니다.
type: docs
weight: 420
url: /ko/net/groupdocs.watermark.contents.image/watermarkableimage/
---
## WatermarkableImage class

문서 내부의 이미지를 나타냅니다.

```csharp
public abstract class WatermarkableImage : ContentPart
```

## 속성

| 이름 | 설명 |
| --- | --- |
| [Height](../../groupdocs.watermark.contents.image/watermarkableimage/height) { get; } | 이것의 높이를 얻습니다.[`WatermarkableImage`](../watermarkableimage) 픽셀 단위. |
| [Width](../../groupdocs.watermark.contents.image/watermarkableimage/width) { get; } | 이것의 너비를 얻습니다.[`WatermarkableImage`](../watermarkableimage) 픽셀 단위. |

## 행동 양식

| 이름 | 설명 |
| --- | --- |
| [Add](../../groupdocs.watermark.contents.image/watermarkableimage/add)(Watermark) | 여기에 워터마크를 추가합니다.[`WatermarkableImage`](../watermarkableimage) . 이 방법은 워터마크 오프셋 및 크기가 픽셀 단위로 측정된다고 가정합니다(할당된 경우). |
| [FindImages](../../groupdocs.watermark.contents/contentpart/findimages)() | 콘텐츠의 모든 이미지를 찾습니다. 에 지정된 개체에서 검색이 수행됩니다.[`SearchableObjects`](../../groupdocs.watermark/watermarker/searchableobjects) . |
| [FindImages](../../groupdocs.watermark.contents/contentpart/findimages)(ImageSearchCriteria) | 지정된 검색 기준에 따라 이미지를 찾습니다. 지정된 개체에서 검색이 수행됩니다.[`SearchableObjects`](../../groupdocs.watermark/watermarker/searchableobjects) . |
| [GetBytes](../../groupdocs.watermark.contents.image/watermarkableimage/getbytes)() | 이미지를 바이트 배열로 가져옵니다. |
| [Search](../../groupdocs.watermark.contents/contentpart/search)() | 콘텐츠에서 가능한 모든 워터마크를 찾습니다. 검색은 다음에 지정된 개체에서 수행됩니다.[`SearchableObjects`](../../groupdocs.watermark/watermarker/searchableobjects) . |
| [Search](../../groupdocs.watermark.contents/contentpart/search)(SearchCriteria) | 지정된 검색 기준에 따라 가능한 워터마크를 찾습니다. 지정된 개체에서 검색이 수행됩니다.[`SearchableObjects`](../../groupdocs.watermark/watermarker/searchableobjects) . |

### 비고

**더 알아보기:**

* [문서 내 이미지에 워터마크 추가](https://docs.groupdocs.com/display/watermarknet/Adding+watermark+to+images+inside+a+document)

### 예

지원되는 모든 유형의 문서 내의 모든 이미지에 워터마크를 추가합니다.

```csharp
using (Watermarker watermarker = new Watermarker(@"D:\input.doc"))
{
    // 텍스트 또는 이미지 워터마크를 초기화합니다.
    TextWatermark watermark = new TextWatermark("DRAFT", new Font("Arial", 19));

    // 콘텐츠의 모든 이미지를 찾습니다.
    WatermarkableImageCollection images = watermarker.GetImages();

    // 워터 마크를 추가.
    foreach (WatermarkableImage watermarkableImage in images)
    {
        watermarkableImage.Add(watermark);
    }

    // 변경 사항을 저장하다.
    watermarker.Save(@"D:\output.doc");
}
```

### 또한보십시오

* class [ContentPart](../../groupdocs.watermark.contents/contentpart)
* 네임스페이스 [GroupDocs.Watermark.Contents.Image](../../groupdocs.watermark.contents.image)
* 집회 [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
