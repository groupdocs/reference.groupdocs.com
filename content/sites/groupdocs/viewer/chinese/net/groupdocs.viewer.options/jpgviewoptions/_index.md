---
title: JpgViewOptions
second_title: GroupDocs.Viewer for .NET API 参考
description: 提供将文档呈现为 JPG 格式的选项
type: docs
weight: 360
url: /zh/net/groupdocs.viewer.options/jpgviewoptions/
---
## JpgViewOptions class

提供将文档呈现为 JPG 格式的选项。

```csharp
public class JpgViewOptions : ViewOptions, IMaxSizeOptions
```

## 构造函数

| 姓名 | 描述 |
| --- | --- |
| [JpgViewOptions](jpgviewoptions#constructor)() | 初始化的新实例[`JpgViewOptions`](../jpgviewoptions)类. |
| [JpgViewOptions](jpgviewoptions#constructor_1)(CreatePageStream) | 初始化的新实例[`JpgViewOptions`](../jpgviewoptions)类. |
| [JpgViewOptions](jpgviewoptions#constructor_3)(IPageStreamFactory) | 初始化的新实例[`JpgViewOptions`](../jpgviewoptions)类. |
| [JpgViewOptions](jpgviewoptions#constructor_4)(string) | 初始化的新实例[`JpgViewOptions`](../jpgviewoptions)类. |
| [JpgViewOptions](jpgviewoptions#constructor_2)(CreatePageStream, ReleasePageStream) | 初始化的新实例[`JpgViewOptions`](../jpgviewoptions)类. |

## 特性

| 姓名 | 描述 |
| --- | --- |
| [ArchiveOptions](../../groupdocs.viewer.options/baseviewoptions/archiveoptions) { get; set; } | 存档文件查看选项。 |
| [CadOptions](../../groupdocs.viewer.options/baseviewoptions/cadoptions) { get; set; } | CAD 工程图视图选项。 |
| [DefaultFontName](../../groupdocs.viewer.options/baseviewoptions/defaultfontname) { get; set; } | 找不到文档中使用的特定字体时使用的默认字体。 |
| [EmailOptions](../../groupdocs.viewer.options/baseviewoptions/emailoptions) { get; set; } | 电子邮件消息视图选项。 |
| [ExtractText](../../groupdocs.viewer.options/jpgviewoptions/extracttext) { get; set; } | 启用文本提取。 |
| [Height](../../groupdocs.viewer.options/jpgviewoptions/height) { get; set; } | 输出图像的高度（以像素为单位）。 |
| [MailStorageOptions](../../groupdocs.viewer.options/baseviewoptions/mailstorageoptions) { get; set; } | 邮件存储数据文件查看选项。 |
| [MaxHeight](../../groupdocs.viewer.options/jpgviewoptions/maxheight) { get; set; } | 输出图像的最大高度（以像素为单位）。 |
| [MaxWidth](../../groupdocs.viewer.options/jpgviewoptions/maxwidth) { get; set; } | 输出图像的最大宽度（以像素为单位）。 |
| [OutlookOptions](../../groupdocs.viewer.options/baseviewoptions/outlookoptions) { get; set; } | MS Outlook 数据文件查看选项。 |
| [PdfOptions](../../groupdocs.viewer.options/baseviewoptions/pdfoptions) { get; set; } | PDF 文档查看选项。 |
| [PresentationOptions](../../groupdocs.viewer.options/baseviewoptions/presentationoptions) { get; set; } | 演示文稿处理文档视图选项。 |
| [ProjectManagementOptions](../../groupdocs.viewer.options/baseviewoptions/projectmanagementoptions) { get; set; } | 项目管理文件查看选项。 |
| [Quality](../../groupdocs.viewer.options/jpgviewoptions/quality) { get; set; } | 输出图像的质量； 有效值在1到100之间； 默认值为90。 |
| [RenderComments](../../groupdocs.viewer.options/baseviewoptions/rendercomments) { get; set; } | 启用呈现评论。 |
| [RenderHiddenPages](../../groupdocs.viewer.options/baseviewoptions/renderhiddenpages) { get; set; } | 启用隐藏页面的呈现。 |
| [RenderNotes](../../groupdocs.viewer.options/baseviewoptions/rendernotes) { get; set; } | 启用渲染注释。 |
| [SpreadsheetOptions](../../groupdocs.viewer.options/baseviewoptions/spreadsheetoptions) { get; set; } | 电子表格文件查看选项。 |
| [TextOptions](../../groupdocs.viewer.options/baseviewoptions/textoptions) { get; set; } | 文本文件拆分到页面选项。 |
| [VisioRenderingOptions](../../groupdocs.viewer.options/baseviewoptions/visiorenderingoptions) { get; set; } | Visio 文件处理文档视图选项。 |
| [Watermark](../../groupdocs.viewer.options/viewoptions/watermark) { get; set; } | 应用于每个页面的文本水印。 |
| [WebDocumentOptions](../../groupdocs.viewer.options/baseviewoptions/webdocumentoptions) { get; set; } | 此呈现选项使您能够在呈现 Web 文档时自定义 输出 HTML/PDF/PNG/JPEG 的外观。 |
| [Width](../../groupdocs.viewer.options/jpgviewoptions/width) { get; set; } | 输出图像的宽度，以像素为单位。 |
| [WordProcessingOptions](../../groupdocs.viewer.options/baseviewoptions/wordprocessingoptions) { get; set; } | 此渲染选项使您能够在渲染 Word 文档时自定义 输出 HTML/PDF/PNG/JPEG 的外观。 |

## 方法

| 姓名 | 描述 |
| --- | --- |
| [RotatePage](../../groupdocs.viewer.options/viewoptions/rotatepage)(int, Rotation) | 对页面应用顺时针旋转。 |

## 字段

| 姓名 | 描述 |
| --- | --- |
| readonly [PageRotations](../../groupdocs.viewer.options/viewoptions/pagerotations) | 页面旋转。 |

### 也可以看看

* class [ViewOptions](../viewoptions)
* interface [IMaxSizeOptions](../imaxsizeoptions)
* 命名空间 [GroupDocs.Viewer.Options](../../groupdocs.viewer.options)
* 部件 [GroupDocs.Viewer](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->