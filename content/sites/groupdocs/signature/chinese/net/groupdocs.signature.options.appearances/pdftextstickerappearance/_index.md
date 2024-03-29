---
title: PdfTextStickerAppearance
second_title: GroupDocs.Signature for .NET API 参考
description: 描述了PDF文本注释贴纸对象的外观和贴纸的弹出窗口
type: docs
weight: 1230
url: /zh/net/groupdocs.signature.options.appearances/pdftextstickerappearance/
---
## PdfTextStickerAppearance class

描述了PDF文本注释贴纸对象的外观和贴纸的弹出窗口。

```csharp
public sealed class PdfTextStickerAppearance : SignatureAppearance
```

## 构造函数

| 姓名 | 描述 |
| --- | --- |
| [PdfTextStickerAppearance](pdftextstickerappearance)() | 创建 PDF 签名文本注释外观对象。 |

## 特性

| 姓名 | 描述 |
| --- | --- |
| static [DefaultAppearance](../../groupdocs.signature.options.appearances/pdftextstickerappearance/defaultappearance) { get; } | 获取贴纸的默认外观。如果未指定 Options.SignatureAppearance 属性，则默认应用这些属性。 用户可以随时更改这些属性。 |
| [Contents](../../groupdocs.signature.options.appearances/pdftextstickerappearance/contents) { get; set; } | 获取或设置弹出窗口的内容。 |
| [Icon](../../groupdocs.signature.options.appearances/pdftextstickerappearance/icon) { get; set; } | 获取或设置贴纸图标。 |
| [Opened](../../groupdocs.signature.options.appearances/pdftextstickerappearance/opened) { get; set; } | 设置是否默认打开贴纸弹出窗口. |
| [Subject](../../groupdocs.signature.options.appearances/pdftextstickerappearance/subject) { get; set; } | 获取或设置主题。 |
| [Title](../../groupdocs.signature.options.appearances/pdftextstickerappearance/title) { get; set; } | 获取或设置弹出窗口的标题。 |

## 方法

| 姓名 | 描述 |
| --- | --- |
| static [ResetDefaultAppearance](../../groupdocs.signature.options.appearances/pdftextstickerappearance/resetdefaultappearance)() | 清除贴纸的默认外观值。 |

### 也可以看看

* class [SignatureAppearance](../signatureappearance)
* 命名空间 [GroupDocs.Signature.Options.Appearances](../../groupdocs.signature.options.appearances)
* 部件 [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
