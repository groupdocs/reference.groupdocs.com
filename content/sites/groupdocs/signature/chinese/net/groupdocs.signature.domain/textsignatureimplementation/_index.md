---
title: TextSignatureImplementation
second_title: GroupDocs.Signature for .NET API 参考
description: 指定 PDF 文本签名的实现类型
type: docs
weight: 1010
url: /zh/net/groupdocs.signature.domain/textsignatureimplementation/
---
## TextSignatureImplementation enumeration

指定 PDF 文本签名的实现类型。

```csharp
public enum TextSignatureImplementation
```

### 价值观

| 姓名 | 价值 | 描述 |
| --- | --- | --- |
| Native | `1` | 文本签名作为文档页面上的本机文本对象。 |
| Image | `2` | 文本签名作为文档页面上的图像对象。 |
| Annotation | `3` | 文本签名作为 PDF 页面上的文本注释对象。 注释仅对许可版本可见。 |
| Sticker | `4` | 文本签名作为 PDF 页面上的贴纸对象。 |
| FormField | `5` | Text Signature as text in specified form field. 这种类型的实现只能使用 TextSignOptions.Text、 TextSignOptions.FormTextFieldType 和 TextSignOptions.FormTextFieldTitle 选项。 |
| Watermark | `6` | 文本签名作为文档页面上的水印。 |

### 也可以看看

* 命名空间 [GroupDocs.Signature.Domain](../../groupdocs.signature.domain)
* 部件 [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
