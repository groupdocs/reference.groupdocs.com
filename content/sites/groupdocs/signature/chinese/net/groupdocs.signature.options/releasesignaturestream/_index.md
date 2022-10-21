---
title: ReleaseSignatureStream
second_title: GroupDocs.Signature for .NET API 参考
description: 定义释放输出签名预览流的方法的委托
type: docs
weight: 1580
url: /zh/net/groupdocs.signature.options/releasesignaturestream/
---
## ReleaseSignatureStream delegate

定义释放输出签名预览流的方法的委托。

```csharp
public delegate void ReleaseSignatureStream(PreviewSignatureOptions previewOptions, 
    Stream signatureStream);
```

| 范围 | 类型 | 描述 |
| --- | --- | --- |
| previewOptions | PreviewSignatureOptions | 预览签名的选项。 |
| signatureStream | Stream | 要发布的签名图像流。 |

### 也可以看看

* class [PreviewSignatureOptions](../previewsignatureoptions)
* 命名空间 [GroupDocs.Signature.Options](../../groupdocs.signature.options)
* 部件 [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->