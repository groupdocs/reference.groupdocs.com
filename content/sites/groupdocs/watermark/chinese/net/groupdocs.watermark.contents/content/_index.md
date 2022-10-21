---
title: Content
second_title: .NET API 参考的 GroupDocs.Watermark
description: 表示可以放置水印的内容
type: docs
weight: 120
url: /zh/net/groupdocs.watermark.contents/content/
---
## Content class

表示可以放置水印的内容。

```csharp
public abstract class Content : ContentPart, IDisposable
```

## 方法

| 姓名 | 描述 |
| --- | --- |
| [Dispose](../../groupdocs.watermark.contents/content/dispose)() | 处理当前实例。 |
| [FindImages](../../groupdocs.watermark.contents/contentpart/findimages)() | 查找内容中的所有图像。 在指定的对象中进行搜索[`SearchableObjects`](../../groupdocs.watermark/watermarker/searchableobjects). |
| [FindImages](../../groupdocs.watermark.contents/contentpart/findimages)(ImageSearchCriteria) | 根据指定的搜索条件查找图像。 在指定的对象中进行搜索[`SearchableObjects`](../../groupdocs.watermark/watermarker/searchableobjects). |
| [Search](../../groupdocs.watermark.contents/contentpart/search)() | 查找内容中所有可能的水印。 在指定的对象中进行搜索[`SearchableObjects`](../../groupdocs.watermark/watermarker/searchableobjects). |
| [Search](../../groupdocs.watermark.contents/contentpart/search)(SearchCriteria) | 根据指定的搜索条件查找可能的水印。 在指定的对象中进行搜索[`SearchableObjects`](../../groupdocs.watermark/watermarker/searchableobjects). |

### 也可以看看

* class [ContentPart](../contentpart)
* 命名空间 [GroupDocs.Watermark.Contents](../../groupdocs.watermark.contents)
* 部件 [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->