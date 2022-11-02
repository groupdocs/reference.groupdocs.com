---
title: TorrentPackage
second_title: GroupDocs.Metadata für .NET-API-Referenz
description: Ruft das Metadatenpaket der TORRENTDatei ab.
type: docs
weight: 10
url: /de/net/groupdocs.metadata.formats.peer2peer/torrentrootpackage/torrentpackage/
---
## TorrentRootPackage.TorrentPackage property

Ruft das Metadatenpaket der TORRENT-Datei ab.

```csharp
public TorrentPackage TorrentPackage { get; }
```

### Eigentumswert

Das Metadatenpaket der TORRENT-Datei.

### Bemerkungen

**Mehr erfahren**

* [Arbeiten mit TORRENT-Dateien](https://docs.groupdocs.com/display/metadatanet/Working+with+TORRENT+files)

### Beispiele

Dieses Codebeispiel zeigt, wie Metadaten in einer TORRENT-Datei aktualisiert werden.

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

### Siehe auch

* class [TorrentPackage](../../torrentpackage)
* class [TorrentRootPackage](../../torrentrootpackage)
* namensraum [GroupDocs.Metadata.Formats.Peer2Peer](../../torrentrootpackage)
* Montage [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->