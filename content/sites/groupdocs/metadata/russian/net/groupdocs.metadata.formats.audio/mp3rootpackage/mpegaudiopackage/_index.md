---
title: MpegAudioPackage
second_title: Справочник по API GroupDocs.Metadata для .NET
description: Получает пакет аудио метаданных MPEG.
type: docs
weight: 50
url: /ru/net/groupdocs.metadata.formats.audio/mp3rootpackage/mpegaudiopackage/
---
## MP3RootPackage.MpegAudioPackage property

Получает пакет аудио метаданных MPEG.

```csharp
public MpegAudioPackage MpegAudioPackage { get; }
```

### Стоимость имущества

Пакет аудио метаданных MPEG.

### Примеры

В этом примере показано, как читать аудио метаданные MPEG из файла MP3.

```csharp
using (Metadata metadata = new Metadata(Constants.MP3WithID3V2))
{
    var root = metadata.GetRootPackage<MP3RootPackage>();

    Console.WriteLine(root.MpegAudioPackage.Bitrate);
    Console.WriteLine(root.MpegAudioPackage.ChannelMode);
    Console.WriteLine(root.MpegAudioPackage.Emphasis);
    Console.WriteLine(root.MpegAudioPackage.Frequency);
    Console.WriteLine(root.MpegAudioPackage.HeaderPosition);
    Console.WriteLine(root.MpegAudioPackage.Layer);

    // ...
}
```

### Смотрите также

* class [MpegAudioPackage](../../../groupdocs.metadata.formats.mpeg/mpegaudiopackage)
* class [MP3RootPackage](../../mp3rootpackage)
* пространство имен [GroupDocs.Metadata.Formats.Audio](../../mp3rootpackage)
* сборка [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
