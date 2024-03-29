---
title: TorrentPackage
second_title: Справочник по API GroupDocs.Metadata для .NET
description: Получает пакет метаданных файла TORRENT.
type: docs
weight: 10
url: /ru/net/groupdocs.metadata.formats.peer2peer/torrentrootpackage/torrentpackage/
---
## TorrentRootPackage.TorrentPackage property

Получает пакет метаданных файла TORRENT.

```csharp
public TorrentPackage TorrentPackage { get; }
```

### Стоимость имущества

Пакет метаданных файла TORRENT.

### Примечания

**Узнать больше**

* [Работа с TORRENT-файлами](https://docs.groupdocs.com/display/metadatanet/Working+with+TORRENT+files)

### Примеры

В этом примере кода показано, как обновить метаданные в файле TORRENT.

```csharp
using (Metadata metadata = new Metadata(Constants.InputTorrent))
{
    var root = metadata.GetRootPackage<TorrentRootPackage>();

    root.TorrentPackage.Comment = "test comment";
    root.TorrentPackage.CreatedBy = "GroupDocs.Metadata";
    root.TorrentPackage.CreationDate = DateTime.Today;

    metadata.Save(Constants.OutputTorrent);
}
```

### Смотрите также

* class [TorrentPackage](../../torrentpackage)
* class [TorrentRootPackage](../../torrentrootpackage)
* пространство имен [GroupDocs.Metadata.Formats.Peer2Peer](../../torrentrootpackage)
* сборка [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
