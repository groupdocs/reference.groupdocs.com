---
title: Lyrics3V2
second_title: GroupDocs.Metadata for .NET API 参考
description: 获取或设置 Lyrics3v2 元数据标签
type: docs
weight: 40
url: /zh/net/groupdocs.metadata.formats.audio/mp3rootpackage/lyrics3v2/
---
## MP3RootPackage.Lyrics3V2 property

获取或设置 Lyrics3v2 元数据标签。

```csharp
public LyricsTag Lyrics3V2 { get; set; }
```

### 适当的价值

Lyrics3v2 元数据标签。

### 例子

此示例显示如何更新 MP3 文件中的歌词标签

```csharp
using (Metadata metadata = new Metadata(Constants.MP3WithLyrics))
{
    var root = metadata.GetRootPackage<MP3RootPackage>();

    if (root.Lyrics3V2 == null)
    {
        root.Lyrics3V2 = new LyricsTag();
    }

    root.Lyrics3V2.Lyrics = "[00:01]Test lyrics";
    root.Lyrics3V2.Artist = "test artist";
    root.Lyrics3V2.Album = "test album";
    root.Lyrics3V2.Track = "test track";

    // 您可以在标签中添加一个完全自定义的字段
    root.Lyrics3V2.Set(new LyricsField("ABC", "custom value"));

    // ...

    metadata.Save(Constants.OutputMp3);
}
```

### 也可以看看

* class [LyricsTag](../../lyricstag)
* class [MP3RootPackage](../../mp3rootpackage)
* 命名空间 [GroupDocs.Metadata.Formats.Audio](../../mp3rootpackage)
* 部件 [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->