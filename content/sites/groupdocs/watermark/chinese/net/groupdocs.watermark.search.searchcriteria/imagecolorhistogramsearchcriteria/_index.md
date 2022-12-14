---
title: ImageColorHistogramSearchCriteria
second_title: .NET API 参考的 GroupDocs.Watermark
description: 表示在内容中查找图像的搜索条件
type: docs
weight: 2580
url: /zh/net/groupdocs.watermark.search.searchcriteria/imagecolorhistogramsearchcriteria/
---
## ImageColorHistogramSearchCriteria class

表示在内容中查找图像的搜索条件。

```csharp
public class ImageColorHistogramSearchCriteria : ImageSearchCriteria
```

## 构造函数

| 姓名 | 描述 |
| --- | --- |
| [ImageColorHistogramSearchCriteria](imagecolorhistogramsearchcriteria#constructor)(Stream) | 初始化[`ImageColorHistogramSearchCriteria`](../imagecolorhistogramsearchcriteria)具有指定流的类。 |
| [ImageColorHistogramSearchCriteria](imagecolorhistogramsearchcriteria#constructor_1)(string) | 初始化[`ImageColorHistogramSearchCriteria`](../imagecolorhistogramsearchcriteria)具有指定文件路径的类。 |

## 特性

| 姓名 | 描述 |
| --- | --- |
| [BinsCount](../../groupdocs.watermark.search.searchcriteria/imagecolorhistogramsearchcriteria/binscount) { get; set; } | 获取或设置将用于构建颜色直方图的 bin 计数。 |
| [MaxDifference](../../groupdocs.watermark.search.searchcriteria/imagesearchcriteria/maxdifference) { get; set; } | 获取或设置图像之间允许的最大差异。 |

## 方法

| 姓名 | 描述 |
| --- | --- |
| [And](../../groupdocs.watermark.search.searchcriteria/searchcriteria/and)(SearchCriteria) | 结合这个[`SearchCriteria`](../searchcriteria)使用逻辑 AND 运算符的其他条件。 |
| [Not](../../groupdocs.watermark.search.searchcriteria/searchcriteria/not)() | 否定这个[`SearchCriteria`](../searchcriteria). |
| [Or](../../groupdocs.watermark.search.searchcriteria/searchcriteria/or)(SearchCriteria) | 结合这个[`SearchCriteria`](../searchcriteria)与使用逻辑 OR 运算符的其他条件。 |

### 评论

此搜索条件使用图像颜色直方图来计算图像相似度。

### 也可以看看

* class [ImageSearchCriteria](../imagesearchcriteria)
* 命名空间 [GroupDocs.Watermark.Search.SearchCriteria](../../groupdocs.watermark.search.searchcriteria)
* 部件 [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
