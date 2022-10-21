---
title: TiffSaveOptions
second_title: GroupDocs.Signature for .NET API 参考
description: Tiff 图像文档的保存选项
type: docs
weight: 1680
url: /zh/net/groupdocs.signature.options/tiffsaveoptions/
---
## TiffSaveOptions class

Tiff 图像文档的保存选项。

```csharp
public sealed class TiffSaveOptions : ImageSaveOptions
```

## 构造函数

| 姓名 | 描述 |
| --- | --- |
| [TiffSaveOptions](tiffsaveoptions)() | 使用默认值创建 TiffSaveOptions。 |

## 特性

| 姓名 | 描述 |
| --- | --- |
| [AddMissingExtenstion](../../groupdocs.signature.options/saveoptions/addmissingextenstion) { get; set; } | 获取或设置标志以在输出文件路径中缺少扩展名时自动添加扩展名 默认值为 false。 |
| [ExpectedTiffFormat](../../groupdocs.signature.options/tiffsaveoptions/expectedtiffformat) { get; set; } | 获取或设置签名文档的 TIFF 格式。 |
| [FileFormat](../../groupdocs.signature.options/imagesaveoptions/fileformat) { get; set; } | 获取或设置签名文档的文件格式。 |
| [OverwriteExistingFiles](../../groupdocs.signature.options/saveoptions/overwriteexistingfiles) { get; set; } | 获取或设置是否用新的输出文件覆盖现有文件。 否则将创建以数字为后缀的新文件。 默认情况下，此值设置为 true，表示文件将被覆盖。 |
| [Password](../../groupdocs.signature.options/saveoptions/password) { get; set; } | 获取或设置密码以保存带有密码保护的签名文档。 Image 文档不支持此属性。 |
| [UseOriginalPassword](../../groupdocs.signature.options/saveoptions/useoriginalpassword) { get; set; } | 获取或设置是否使用 LoadOptions 中的密码将签名文档保存为受保护。 默认值为 true。 图片文档不支持此属性。 |

### 也可以看看

* class [ImageSaveOptions](../imagesaveoptions)
* 命名空间 [GroupDocs.Signature.Options](../../groupdocs.signature.options)
* 部件 [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->