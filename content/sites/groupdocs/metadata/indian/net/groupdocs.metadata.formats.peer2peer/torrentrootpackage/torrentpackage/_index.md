---
title: TorrentPackage
second_title: .NET API संदर्भ के लिए GroupDocs.Metadata
description: टरेंट फ़इल मेटडेट पैकेज प्रप्त करत है
type: docs
weight: 10
url: /hi/net/groupdocs.metadata.formats.peer2peer/torrentrootpackage/torrentpackage/
---
## TorrentRootPackage.TorrentPackage property

टोरेंट फ़ाइल मेटाडेटा पैकेज प्राप्त करता है।

```csharp
public TorrentPackage TorrentPackage { get; }
```

### संपत्ति मूल्य

टोरेंट फ़ाइल मेटाडेटा पैकेज।

### टिप्पणियों

**और अधिक जानें**

* [टोरेंट फाइलों के साथ काम करना](https://docs.groupdocs.com/display/metadatanet/Working+with+TORRENT+files)

### उदाहरण

यह कोड नमूना दिखाता है कि टोरेंट फ़ाइल में मेटाडेटा को कैसे अपडेट किया जाए।

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

### यह सभी देखें

* class [TorrentPackage](../../torrentpackage)
* class [TorrentRootPackage](../../torrentrootpackage)
* नाम स्थान [GroupDocs.Metadata.Formats.Peer2Peer](../../torrentrootpackage)
* सभा [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
