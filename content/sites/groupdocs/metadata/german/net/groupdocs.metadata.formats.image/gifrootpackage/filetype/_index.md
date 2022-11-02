---
title: FileType
second_title: GroupDocs.Metadata für .NET-API-Referenz
description: Ruft das DateitypMetadatenpaket ab.
type: docs
weight: 10
url: /de/net/groupdocs.metadata.formats.image/gifrootpackage/filetype/
---
## GifRootPackage.FileType property

Ruft das Dateityp-Metadatenpaket ab.

```csharp
public GifImageTypePackage FileType { get; }
```

### Eigentumswert

Das Dateityp-Metadatenpaket.

### Beispiele

Dieses Code-Snippet zeigt, wie die Version eines geladenen GIF-Bildes erkannt und einige zusätzliche Dateiformatinformationen extrahiert werden.

```csharp
using (Metadata metadata = new Metadata(Constants.InputGif))
{
    var root = metadata.GetRootPackage<GifRootPackage>();

    Console.WriteLine(root.FileType.FileFormat);
    Console.WriteLine(root.FileType.Version);
    Console.WriteLine(root.FileType.ByteOrder);
    Console.WriteLine(root.FileType.MimeType);
    Console.WriteLine(root.FileType.Extension);
    Console.WriteLine(root.FileType.Width);
    Console.WriteLine(root.FileType.Height);
}
```

### Siehe auch

* class [GifImageTypePackage](../../gifimagetypepackage)
* class [GifRootPackage](../../gifrootpackage)
* namensraum [GroupDocs.Metadata.Formats.Image](../../gifrootpackage)
* Montage [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->