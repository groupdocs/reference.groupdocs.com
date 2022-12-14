---
title: ID3V2
second_title: GroupDocs.Metadata for .NET API 参考
description: 获取或设置 ID3v2 元数据标记
type: docs
weight: 30
url: /zh/net/groupdocs.metadata.formats.audio/mp3rootpackage/id3v2/
---
## MP3RootPackage.ID3V2 property

获取或设置 ID3v2 元数据标记。

```csharp
public ID3V2Tag ID3V2 { get; set; }
```

### 适当的价值

附加到音频文件的 ID3v2 元数据标签。

### 例子

代码示例展示了如何更新 MP3 文件中的 ID3v2 标签。

```csharp
using (Metadata metadata = new Metadata(Constants.MP3WithID3V2))
{
    var root = metadata.GetRootPackage<MP3RootPackage>();

    if (root.ID3V2 == null)
    {
        root.ID3V2 = new ID3V2Tag();
    }

    root.ID3V2.Album = "test album";
    root.ID3V2.Artist = "test artist";
    root.ID3V2.Band = "test band";
    root.ID3V2.TrackNumber = "1";
    root.ID3V2.MusicalKey = "C#";
    root.ID3V2.Title = "code sample";
    root.ID3V2.Date = "2019";

    // ...

    metadata.Save(Constants.OutputMp3);
}
```

### 也可以看看

* class [ID3V2Tag](../../id3v2tag)
* class [MP3RootPackage](../../mp3rootpackage)
* 命名空间 [GroupDocs.Metadata.Formats.Audio](../../mp3rootpackage)
* 部件 [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
