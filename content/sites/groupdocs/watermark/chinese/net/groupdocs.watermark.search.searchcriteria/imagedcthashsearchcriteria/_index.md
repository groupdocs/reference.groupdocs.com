---
title: ImageDctHashSearchCriteria
second_title: .NET API 参考的 GroupDocs.Watermark
description: 表示在文档中查找图像的搜索条件
type: docs
weight: 2590
url: /zh/net/groupdocs.watermark.search.searchcriteria/imagedcthashsearchcriteria/
---
## ImageDctHashSearchCriteria class

表示在文档中查找图像的搜索条件。

```csharp
public class ImageDctHashSearchCriteria : ImageSearchCriteria
```

## 构造函数

| 姓名 | 描述 |
| --- | --- |
| [ImageDctHashSearchCriteria](imagedcthashsearchcriteria#constructor)(Stream) | 初始化一个新的实例[`ImageDctHashSearchCriteria`](../imagedcthashsearchcriteria)具有指定流的类. |
| [ImageDctHashSearchCriteria](imagedcthashsearchcriteria#constructor_1)(string) | 初始化一个新的实例[`ImageDctHashSearchCriteria`](../imagedcthashsearchcriteria)具有指定文件路径的类. |

## 特性

| 姓名 | 描述 |
| --- | --- |
| [MaxDifference](../../groupdocs.watermark.search.searchcriteria/imagesearchcriteria/maxdifference) { get; set; } | 获取或设置图像之间的最大允许差异。 |

## 方法

| 姓名 | 描述 |
| --- | --- |
| [And](../../groupdocs.watermark.search.searchcriteria/searchcriteria/and)(SearchCriteria) | 结合这个[`SearchCriteria`](../searchcriteria)与其他标准使用逻辑 AND 运算符. |
| [Not](../../groupdocs.watermark.search.searchcriteria/searchcriteria/not)() | 否定这个[`SearchCriteria`](../searchcriteria). |
| [Or](../../groupdocs.watermark.search.searchcriteria/searchcriteria/or)(SearchCriteria) | 结合这个[`SearchCriteria`](../searchcriteria)与其他标准使用逻辑或运算符. |

### 评论

此搜索条件使用基于 DCT 的感知图像哈希来计算图像相似度。 **了解更多：**

* [搜索水印](https://docs.groupdocs.com/display/watermarknet/Searching+watermarks)

### 例子

在附件 (pdf) 中搜索图像。

```csharp
WatermarkerSettings settings = new WatermarkerSettings();
settings.SearchableObjects = new SearchableObjects
{
    PdfSearchableObjects = PdfSearchableObjects.All
};
PdfLoadOptions loadOptions = new PdfLoadOptions();
using (Watermarker watermarker = new Watermarker(@"D:\test.pdf", loadOptions, settings))
{
    // 指定样本图像与文档图像进行比较
    ImageSearchCriteria criteria = new ImageDctHashSearchCriteria(@"D:\sample.png");
    // 搜索相似图片
    PossibleWatermarkCollection possibleWatermarks = watermarker.Search(criteria);
    // 删除或修改找到的图像水印
    // ...
}
```

### 也可以看看

* class [ImageSearchCriteria](../imagesearchcriteria)
* 命名空间 [GroupDocs.Watermark.Search.SearchCriteria](../../groupdocs.watermark.search.searchcriteria)
* 部件 [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
