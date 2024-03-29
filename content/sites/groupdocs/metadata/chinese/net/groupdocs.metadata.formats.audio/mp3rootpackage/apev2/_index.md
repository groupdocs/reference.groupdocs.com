---
title: ApeV2
second_title: GroupDocs.Metadata for .NET API 参考
description: 获取 APE v2 元数据
type: docs
weight: 10
url: /zh/net/groupdocs.metadata.formats.audio/mp3rootpackage/apev2/
---
## MP3RootPackage.ApeV2 property

获取 APE v2 元数据。

```csharp
public ApePackage ApeV2 { get; }
```

### 适当的价值

APE v2 元数据。

### 例子

此示例演示如何读取 MP3 文件中的 APEv2 标签。

```csharp
using (Metadata metadata = new Metadata(Constants.MP3WithApe))
{
    var root = metadata.GetRootPackage<MP3RootPackage>();

    if (root.ApeV2 != null)
    {
        Console.WriteLine(root.ApeV2.Album);
        Console.WriteLine(root.ApeV2.Title);
        Console.WriteLine(root.ApeV2.Artist);
        Console.WriteLine(root.ApeV2.Composer);
        Console.WriteLine(root.ApeV2.Copyright);
        Console.WriteLine(root.ApeV2.Genre);
        Console.WriteLine(root.ApeV2.Language);

        // ...
    }
}
```

### 也可以看看

* class [ApePackage](../../apepackage)
* class [MP3RootPackage](../../mp3rootpackage)
* 命名空间 [GroupDocs.Metadata.Formats.Audio](../../mp3rootpackage)
* 部件 [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
