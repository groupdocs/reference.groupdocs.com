---
title: RemoveApeV2
second_title: GroupDocs.Metadata for .NET API 参考
description: 删除 APEv2 音频标签
type: docs
weight: 70
url: /zh/net/groupdocs.metadata.formats.audio/mp3rootpackage/removeapev2/
---
## MP3RootPackage.RemoveApeV2 method

删除 APEv2 音频标签。

```csharp
public void RemoveApeV2()
```

### 评论

此功能在试用模式下不可用。

### 例子

此示例说明如何从 MP3 文件中删除 APEv2 标签。

```csharp
using (Metadata metadata = new Metadata(Constants.MP3WithApe))
{
    var root = metadata.GetRootPackage<MP3RootPackage>();

    root.RemoveApeV2();

    metadata.Save(Constants.OutputMp3);
}
```

### 也可以看看

* class [MP3RootPackage](../../mp3rootpackage)
* 命名空间 [GroupDocs.Metadata.Formats.Audio](../../mp3rootpackage)
* 部件 [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->