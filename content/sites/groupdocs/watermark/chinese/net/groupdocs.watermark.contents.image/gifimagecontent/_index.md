---
title: GifImageContent
second_title: .NET API 参考的 GroupDocs.Watermark
description: 表示可以放水印的gif图片
type: docs
weight: 360
url: /zh/net/groupdocs.watermark.contents.image/gifimagecontent/
---
## GifImageContent class

表示可以放水印的gif图片。

```csharp
public sealed class GifImageContent : MultiframeImageContent
```

## 特性

| 姓名 | 描述 |
| --- | --- |
| [Frames](../../groupdocs.watermark.contents.image/multiframeimagecontent/frames) { get; } | 获取图像所有帧的集合。 |
| [Height](../../groupdocs.watermark.contents.image/imagecontent/height) { get; } | 获取这个的高度[`ImageContent`](../imagecontent)以像素为单位。 |
| [Width](../../groupdocs.watermark.contents.image/imagecontent/width) { get; } | 获取这个的宽度[`ImageContent`](../imagecontent)以像素为单位。 |

## 方法

| 姓名 | 描述 |
| --- | --- |
| [Dispose](../../groupdocs.watermark.contents/content/dispose)() | 处理当前实例。 |
| [FindImages](../../groupdocs.watermark.contents/contentpart/findimages)() | 查找内容中的所有图像。 在指定的对象中进行搜索[`SearchableObjects`](../../groupdocs.watermark/watermarker/searchableobjects). |
| [FindImages](../../groupdocs.watermark.contents/contentpart/findimages)(ImageSearchCriteria) | 根据指定的搜索条件查找图像。 在指定的对象中进行搜索[`SearchableObjects`](../../groupdocs.watermark/watermarker/searchableobjects). |
| [Search](../../groupdocs.watermark.contents/contentpart/search)() | 查找内容中所有可能的水印。 在指定的对象中进行搜索[`SearchableObjects`](../../groupdocs.watermark/watermarker/searchableobjects). |
| [Search](../../groupdocs.watermark.contents/contentpart/search)(SearchCriteria) | 根据指定的搜索条件查找可能的水印。 在指定的对象中进行搜索[`SearchableObjects`](../../groupdocs.watermark/watermarker/searchableobjects). |

### 也可以看看

* class [MultiframeImageContent](../multiframeimagecontent)
* 命名空间 [GroupDocs.Watermark.Contents.Image](../../groupdocs.watermark.contents.image)
* 部件 [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->