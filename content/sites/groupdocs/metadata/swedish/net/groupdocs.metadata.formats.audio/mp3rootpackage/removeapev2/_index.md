---
title: RemoveApeV2
second_title: GroupDocs.Metadata for .NET API-referens
description: Tar bort APEv2ljudtaggen.
type: docs
weight: 70
url: /sv/net/groupdocs.metadata.formats.audio/mp3rootpackage/removeapev2/
---
## MP3RootPackage.RemoveApeV2 method

Tar bort APEv2-ljudtaggen.

```csharp
public void RemoveApeV2()
```

### Anmärkningar

Den här funktionen är inte tillgänglig i testläge.

### Exempel

Det här exemplet visar hur man tar bort APEv2-taggen från en MP3-fil.

```csharp
using (Metadata metadata = new Metadata(Constants.MP3WithApe))
{
    var root = metadata.GetRootPackage<MP3RootPackage>();

    root.RemoveApeV2();

    metadata.Save(Constants.OutputMp3);
}
```

### Se även

* class [MP3RootPackage](../../mp3rootpackage)
* namnutrymme [GroupDocs.Metadata.Formats.Audio](../../mp3rootpackage)
* hopsättning [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
