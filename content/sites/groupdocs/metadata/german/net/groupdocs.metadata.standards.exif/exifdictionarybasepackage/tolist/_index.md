---
title: ToList
second_title: GroupDocs.Metadata für .NET-API-Referenz
description: Erstellt eine Liste aus dem Paket.
type: docs
weight: 50
url: /de/net/groupdocs.metadata.standards.exif/exifdictionarybasepackage/tolist/
---
## ExifDictionaryBasePackage.ToList method

Erstellt eine Liste aus dem Paket.

```csharp
public IReadOnlyList<TiffTag> ToList()
```

### Rückgabewert

Eine Liste, die alle TIFF-Tags aus dem Paket enthält.

### Beispiele

Dieses Beispiel zeigt, wie alle aus einer Datei extrahierten EXIF-Tags gelesen werden.

```csharp
using (Metadata metadata = new Metadata(Constants.JpegWithExif))
{
    IExif root = metadata.GetRootPackage() as IExif;
    if (root != null && root.ExifPackage != null)
    {
        const string pattern = "{0} = {1}";

        foreach (TiffTag tag in root.ExifPackage.ToList())
        {
            Console.WriteLine(pattern, tag.TagID, tag.Value);
        }

        foreach (TiffTag tag in root.ExifPackage.ExifIfdPackage.ToList())
        {
            Console.WriteLine(pattern, tag.TagID, tag.Value);
        }

        foreach (TiffTag tag in root.ExifPackage.GpsPackage.ToList())
        {
            Console.WriteLine(pattern, tag.TagID, tag.Value);
        }
    }
}
```

### Siehe auch

* interface [IReadOnlyList&lt;T&gt;](../../../groupdocs.metadata.common/ireadonlylist-1)
* class [TiffTag](../../../groupdocs.metadata.formats.image/tifftag)
* class [ExifDictionaryBasePackage](../../exifdictionarybasepackage)
* namensraum [GroupDocs.Metadata.Standards.Exif](../../exifdictionarybasepackage)
* Montage [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
