---
title: ApeV2
second_title: GroupDocs.Metadata für .NET-API-Referenz
description: Ruft die Metadaten von APE v2 ab.
type: docs
weight: 10
url: /de/net/groupdocs.metadata.formats.audio/mp3rootpackage/apev2/
---
## MP3RootPackage.ApeV2 property

Ruft die Metadaten von APE v2 ab.

```csharp
public ApePackage ApeV2 { get; }
```

### Eigentumswert

Die Metadaten von APE v2.

### Beispiele

Dieses Beispiel zeigt, wie das APEv2-Tag in einer MP3-Datei gelesen wird.

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

### Siehe auch

* class [ApePackage](../../apepackage)
* class [MP3RootPackage](../../mp3rootpackage)
* namensraum [GroupDocs.Metadata.Formats.Audio](../../mp3rootpackage)
* Montage [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
