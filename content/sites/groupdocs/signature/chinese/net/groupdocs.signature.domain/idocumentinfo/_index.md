---
title: IDocumentInfo
second_title: GroupDocs.Signature for .NET API 参考
description: 定义文档描述属性
type: docs
weight: 510
url: /zh/net/groupdocs.signature.domain/idocumentinfo/
---
## IDocumentInfo interface

定义文档描述属性。

```csharp
public interface IDocumentInfo
```

## 特性

| 姓名 | 描述 |
| --- | --- |
| [BarcodeSignatures](../../groupdocs.signature.domain/idocumentinfo/barcodesignatures) { get; } | 添加或更新的文档条码签名集合[`Signature`](../../groupdocs.signature/signature)方法. |
| [DigitalSignatures](../../groupdocs.signature.domain/idocumentinfo/digitalsignatures) { get; } | 添加或更新的文档数字签名集合[`Signature`](../../groupdocs.signature/signature)方法. |
| [FileType](../../groupdocs.signature.domain/idocumentinfo/filetype) { get; set; } | 文件格式类型 |
| [FormFields](../../groupdocs.signature.domain/idocumentinfo/formfields) { get; } | 文档中所有现有支持的表单字段的集合。只有 Pdf 和文字处理文档类型支持此属性。 |
| [FormFieldSignatures](../../groupdocs.signature.domain/idocumentinfo/formfieldsignatures) { get; } | 添加或更新的文档表单字段签名集合[`Signature`](../../groupdocs.signature/signature)方法. |
| [ImageSignatures](../../groupdocs.signature.domain/idocumentinfo/imagesignatures) { get; } | 添加或更新的文档图像签名集合[`Signature`](../../groupdocs.signature/signature)方法. |
| [MaxPageHeight](../../groupdocs.signature.domain/idocumentinfo/maxpageheight) { get; set; } | 指定最大页面高度。 |
| [MetadataSignatures](../../groupdocs.signature.domain/idocumentinfo/metadatasignatures) { get; } | 文档元数据签名集合。 |
| [PageCount](../../groupdocs.signature.domain/idocumentinfo/pagecount) { get; set; } | 文档页数。 |
| [Pages](../../groupdocs.signature.domain/idocumentinfo/pages) { get; set; } | 文档页面描述集合。 |
| [ProcessLogs](../../groupdocs.signature.domain/idocumentinfo/processlogs) { get; } | 文档历史进程日志集合。 |
| [QrCodeSignatures](../../groupdocs.signature.domain/idocumentinfo/qrcodesignatures) { get; } | 添加或更新的文档二维码签名集合[`Signature`](../../groupdocs.signature/signature)方法. |
| [Signatures](../../groupdocs.signature.domain/idocumentinfo/signatures) { get; } | 文档所有类型签名的集合[`BaseSignature`](../basesignature). |
| [Size](../../groupdocs.signature.domain/idocumentinfo/size) { get; set; } | 文档大小（以字节为单位）。 |
| [TextSignatures](../../groupdocs.signature.domain/idocumentinfo/textsignatures) { get; } | 添加或更新的文档文本签名集合[`Signature`](../../groupdocs.signature/signature)方法. |
| [WidthForMaxHeight](../../groupdocs.signature.domain/idocumentinfo/widthformaxheight) { get; set; } | 指定最大页面高度的宽度。 |

### 也可以看看

* 命名空间 [GroupDocs.Signature.Domain](../../groupdocs.signature.domain)
* 部件 [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
