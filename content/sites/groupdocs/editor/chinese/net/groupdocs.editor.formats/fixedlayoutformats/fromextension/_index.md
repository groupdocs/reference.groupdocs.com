---
title: FromExtension
second_title: GroupDocs.Editor for .NET API 参考
description: 返回实例FixedLayoutFormatsgroupdocs.editor.formats/fixedlayoutformats结构关联到指定的文件扩展名或者如果扩展名无法正确解析则抛出异常
type: docs
weight: 30
url: /zh/net/groupdocs.editor.formats/fixedlayoutformats/fromextension/
---
## FixedLayoutFormats.FromExtension method

返回实例[`FixedLayoutFormats`](../../fixedlayoutformats)结构，关联到指定的文件扩展名，或者如果扩展名无法正确解析，则抛出异常

```csharp
public static FixedLayoutFormats FromExtension(string extension)
```

| 范围 | 类型 | 描述 |
| --- | --- | --- |
| extension | String | 任何可支持的 FixedLayoutFormats 格式的文件扩展名，带或不带前导点字符，与大小写无关。 不能为 NULL 或为空，应该是有效的。 |

### 返回值

实例[`FixedLayoutFormats`](../../fixedlayoutformats)成功时的结构或失败时抛出的异常

### 也可以看看

* struct [FixedLayoutFormats](../../fixedlayoutformats)
* 命名空间 [GroupDocs.Editor.Formats](../../fixedlayoutformats)
* 部件 [GroupDocs.Editor](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->