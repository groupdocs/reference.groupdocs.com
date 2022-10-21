---
title: MarkdownDocumentInfo
second_title: GroupDocs.Editor for .NET API 参考
description: 表示一个 Markdown 文档的元数据
type: docs
weight: 600
url: /zh/net/groupdocs.editor.metadata/markdowndocumentinfo/
---
## MarkdownDocumentInfo structure

表示一个 Markdown 文档的元数据

```csharp
public struct MarkdownDocumentInfo : IDocumentInfo, IEquatable<MarkdownDocumentInfo>
```

## 特性

| 姓名 | 描述 |
| --- | --- |
| [Format](../../groupdocs.editor.metadata/markdowndocumentinfo/format) { get; } | 返回此 Markdown 文档的格式 - 始终为[`Md`](../../groupdocs.editor.formats/textualformats/md) |
| [IsEncrypted](../../groupdocs.editor.metadata/markdowndocumentinfo/isencrypted) { get; } | 因为 Markdown 文档不能用密码加密，所以这个属性总是返回 'false' |
| [PageCount](../../groupdocs.editor.metadata/markdowndocumentinfo/pagecount) { get; } | 返回页数。 Markdown 文档通常没有固定的页面，因此页数，所以这个数字是根据纵向设置为 A4 的标准页面大小计算的。 |
| [Size](../../groupdocs.editor.metadata/markdowndocumentinfo/size) { get; } | 返回此 Markdown 文档的大小（以字节为单位） |

## 方法

| 姓名 | 描述 |
| --- | --- |
| [Equals](../../groupdocs.editor.metadata/markdowndocumentinfo/equals#equals)(MarkdownDocumentInfo) | 判断这个实例是否等于另一个指定的实例[`MarkdownDocumentInfo`](../markdowndocumentinfo)实例. |

### 也可以看看

* interface [IDocumentInfo](../idocumentinfo)
* 命名空间 [GroupDocs.Editor.Metadata](../../groupdocs.editor.metadata)
* 部件 [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->