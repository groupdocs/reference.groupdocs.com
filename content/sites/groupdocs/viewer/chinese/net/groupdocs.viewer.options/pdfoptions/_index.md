---
title: PdfOptions
second_title: GroupDocs.Viewer for .NET API 参考
description: 提供用于呈现 PDF 文档的选项
type: docs
weight: 410
url: /zh/net/groupdocs.viewer.options/pdfoptions/
---
## PdfOptions class

提供用于呈现 PDF 文档的选项。

```csharp
public class PdfOptions
```

## 构造函数

| 姓名 | 描述 |
| --- | --- |
| [PdfOptions](pdfoptions)() | 初始化的新实例[`PdfOptions`](../pdfoptions)类. |

## 特性

| 姓名 | 描述 |
| --- | --- |
| [DisableCharsGrouping](../../groupdocs.viewer.options/pdfoptions/disablecharsgrouping) { get; set; } | 在渲染页面时禁用字符分组以在字符定位期间保持最大精度。 |
| [EnableFontHinting](../../groupdocs.viewer.options/pdfoptions/enablefonthinting) { get; set; } | 启用字体提示。字体提示调整轮廓字体的显示。 仅在源文档中使用 TTF 字体时支持这些字体。 |
| [EnableLayeredRendering](../../groupdocs.viewer.options/pdfoptions/enablelayeredrendering) { get; set; } | 在呈现为 HTML 时，根据原始 PDF 文档中的 z 顺序启用文本和图形的呈现。 |
| [ImageQuality](../../groupdocs.viewer.options/pdfoptions/imagequality) { get; set; } | 指定渲染成 HTML 时图像资源的输出图像质量。 默认值为低。 |
| [RenderOriginalPageSize](../../groupdocs.viewer.options/pdfoptions/renderoriginalpagesize) { get; set; } | 启用此选项后，输出页面将具有与源 PDF 文档中页面大小相同的 size （以像素为单位）。 默认情况下，GroupDocs.Viewer 计算输出图像页面大小以获得更好的渲染质量。 |
| [RenderTextAsImage](../../groupdocs.viewer.options/pdfoptions/rendertextasimage) { get; set; } | 当此选项设置为真的，文本在输出 HTML 中呈现为图像。 启用此选项以使文本无法选择或修复字符呈现并使 HTML 看起来像 PDF。 默认值为错误的. |

### 也可以看看

* 命名空间 [GroupDocs.Viewer.Options](../../groupdocs.viewer.options)
* 部件 [GroupDocs.Viewer](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->