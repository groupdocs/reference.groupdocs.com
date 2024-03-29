---
title: PreviewOptions
second_title: .NET API 参考的 GroupDocs.Annotation
description: 表示文档预览选项
type: docs
weight: 1000
url: /zh/net/groupdocs.annotation.options/previewoptions/
---
## PreviewOptions class

表示文档预览选项。

```csharp
public class PreviewOptions
```

## 构造函数

| 姓名 | 描述 |
| --- | --- |
| [PreviewOptions](previewoptions#constructor)(CreatePageStream) | 初始化一个新实例[`PreviewOptions`](../previewoptions)类. |
| [PreviewOptions](previewoptions#constructor_1)(CreatePageStream, ReleasePageStream) | 初始化一个新实例[`PreviewOptions`](../previewoptions)类. |

## 特性

| 姓名 | 描述 |
| --- | --- |
| [CreatePageStream](../../groupdocs.annotation.options/previewoptions/createpagestream) { get; set; } | 委托定义了创建输出页面预览流的方法。 |
| [Height](../../groupdocs.annotation.options/previewoptions/height) { get; set; } | 页面预览高度. |
| [PageNumbers](../../groupdocs.annotation.options/previewoptions/pagenumbers) { get; set; } | 将被预览的页码。 |
| [PreviewFormat](../../groupdocs.annotation.options/previewoptions/previewformat) { get; set; } | 预览图片格式. |
| [ReleasePageStream](../../groupdocs.annotation.options/previewoptions/releasepagestream) { get; set; } | Delegate 定义了删除输出页面预览 stream 的方法 |
| [RenderAnnotations](../../groupdocs.annotation.options/previewoptions/renderannotations) { get; set; } | 控制是否在预览中生成注释的属性。默认状态 - true. |
| [RenderComments](../../groupdocs.annotation.options/previewoptions/rendercomments) { get; set; } | 控制是否在预览中生成注释的属性。默认状态 - 真。现在仅在 MS Word 文档中受支持 |
| [Resolution](../../groupdocs.annotation.options/previewoptions/resolution) { get; set; } | 获取或设置生成图像的分辨率，以每英寸点数为单位。 |
| [Width](../../groupdocs.annotation.options/previewoptions/width) { get; set; } | 页面预览宽度。 |
| [WorksheetColumns](../../groupdocs.annotation.options/previewoptions/worksheetcolumns) { get; set; } | 要生成的工作表列。生成按指定顺序进行。 |

### 也可以看看

* 命名空间 [GroupDocs.Annotation.Options](../../groupdocs.annotation.options)
* 部件 [GroupDocs.Annotation](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Annotation.dll -->
