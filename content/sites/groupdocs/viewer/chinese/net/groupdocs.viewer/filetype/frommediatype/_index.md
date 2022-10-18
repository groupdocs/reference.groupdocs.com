---
title: FromMediaType
second_title: GroupDocs.Viewer for .NET API 参考
description: 将文件媒体类型映射到文件类型例如应用程序/pdf将被映射到PDFgroupdocs.viewer/filetype/pdf.
type: docs
weight: 1890
url: /zh/net/groupdocs.viewer/filetype/frommediatype/
---
## FileType.FromMediaType method

将文件媒体类型映射到文件类型，例如“应用程序/pdf”将被映射到[`PDF`](../pdf).

```csharp
public static FileType FromMediaType(string mediaType)
```

| 范围 | 类型 | 描述 |
| --- | --- | --- |
| mediaType | String | 文件媒体类型，例如应用程序/pdf。 |

### 返回值

找到时返回对应的媒体类型，否则返回默认值[`Unknown`](../unknown)文件类型。

### 也可以看看

* class [FileType](../../filetype)
* 命名空间 [GroupDocs.Viewer](../../filetype)
* 部件 [GroupDocs.Viewer](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->