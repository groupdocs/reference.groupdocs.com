---
title: Set
second_title: GroupDocs.Metadata für .NET-API-Referenz
description: Fügt das angegebene Tag hinzu oder ersetzt es.
type: docs
weight: 40
url: /de/net/groupdocs.metadata.standards.exif/exifdictionarybasepackage/set/
---
## ExifDictionaryBasePackage.Set method

Fügt das angegebene Tag hinzu oder ersetzt es.

```csharp
public void Set(TiffTag tag)
```

| Parameter | Typ | Beschreibung |
| --- | --- | --- |
| tag | TiffTag | Das festzulegende Tag. |

### Beispiele

Dieses Codebeispiel zeigt, wie Sie einem EXIF-Paket ein benutzerdefiniertes Tag hinzufügen.

```csharp
using (Metadata metadata = new Metadata(Constants.TiffWithExif))
{
    IExif root = metadata.GetRootPackage() as IExif;
    if (root != null)
    {
        // Setzen Sie das EXIF-Paket, falls es fehlt
        if (root.ExifPackage == null)
        {
            root.ExifPackage = new ExifPackage();
        }

        // Eine bekannte Eigenschaft hinzufügen
        root.ExifPackage.Set(new TiffAsciiTag(TiffTagID.Artist, "test artist"));

        // Fügen Sie eine vollständig benutzerdefinierte Eigenschaft hinzu (die nicht in der EXIF-Spezifikation beschrieben ist).
        // Bitte beachten Sie, dass sich die gewählte ID mit den IDs überschneiden kann, die von einigen Tools von Drittanbietern verwendet werden.
        root.ExifPackage.Set(new TiffAsciiTag((TiffTagID)65523, "custom"));

        metadata.Save(Constants.OutputTiff);
    }
}
```

### Siehe auch

* class [TiffTag](../../../groupdocs.metadata.formats.image/tifftag)
* class [ExifDictionaryBasePackage](../../exifdictionarybasepackage)
* namensraum [GroupDocs.Metadata.Standards.Exif](../../exifdictionarybasepackage)
* Montage [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->