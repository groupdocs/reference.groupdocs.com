---
title: Remove
second_title: .NET API 参考的 GroupDocs.Watermark
description: 从文档中删除水印
type: docs
weight: 90
url: /zh/net/groupdocs.watermark/watermarker/remove/
---
## Remove(PossibleWatermark) {#remove}

从文档中删除水印。

```csharp
public void Remove(PossibleWatermark possibleWatermark)
```

| 范围 | 类型 | 描述 |
| --- | --- | --- |
| possibleWatermark | PossibleWatermark | 要删除的水印。 |

### 评论

了解有关去除水印的更多信息： [删除找到的水印](https://docs.groupdocs.com/display/watermarknet/Removing+found+watermarks) .

### 例子

从任何受支持类型的文档 中查找并删除包含特定文本或图像的第一个可能的水印。

```csharp
using (Watermarker watermarker = new Watermarker(@"D:\input.doc"))
{
    ImageSearchCriteria imageSearchCriteria = new ImageDctHashSearchCriteria(@"D:\logo.png");
    Regex regex = new Regex(@"^Company\sName$", RegexOptions.IgnoreCase);
    TextSearchCriteria textSearchCriteria = new TextSearchCriteria(regex);
    PossibleWatermarkCollection watermarks = watermarker.Search(textSearchCriteria.Or(imageSearchCriteria));
    if (watermarks.Count > 0)
    {
        watermarker.Remove(watermarks[0]);
    }

    watermarker.Save(@"D:\output.doc");
}
```

### 也可以看看

* class [PossibleWatermark](../../../groupdocs.watermark.search/possiblewatermark)
* class [Watermarker](../../watermarker)
* 命名空间 [GroupDocs.Watermark](../../watermarker)
* 部件 [GroupDocs.Watermark](../../../)

---

## Remove(PossibleWatermarkCollection) {#remove_1}

从文档中删除集合中的所有水印。

```csharp
public void Remove(PossibleWatermarkCollection possibleWatermarks)
```

| 范围 | 类型 | 描述 |
| --- | --- | --- |
| possibleWatermarks | PossibleWatermarkCollection | 要删除的水印集合。 |

### 评论

了解有关去除水印的更多信息 [删除找到的水印](https://docs.groupdocs.com/display/watermarknet/Removing+found+watermarks).

### 例子

从任何受支持类型的文档 中查找并删除所有可能包含特定文本或图像的水印。

```csharp
using (Watermarker watermarker = new Watermarker(@"D:\input.doc"))
{
    ImageSearchCriteria imageSearchCriteria = new ImageDctHashSearchCriteria(@"D:\logo.png");
    Regex regex = new Regex(@"^Company\sName$", RegexOptions.IgnoreCase);
    TextSearchCriteria textSearchCriteria = new TextSearchCriteria(regex);
    PossibleWatermarkCollection watermarks = watermarker.Search(textSearchCriteria.Or(imageSearchCriteria));
    watermarker.Remove(watermarks);
    watermarker.Save(@"D:\output.doc");
}
```

### 也可以看看

* class [PossibleWatermarkCollection](../../../groupdocs.watermark.search/possiblewatermarkcollection)
* class [Watermarker](../../watermarker)
* 命名空间 [GroupDocs.Watermark](../../watermarker)
* 部件 [GroupDocs.Watermark](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->