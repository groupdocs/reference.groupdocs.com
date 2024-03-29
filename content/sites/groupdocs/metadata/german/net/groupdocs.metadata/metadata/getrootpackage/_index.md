---
title: GetRootPackage
second_title: GroupDocs.Metadata für .NET-API-Referenz
description: Ruft das Stammpaket ab das Zugriff auf alle Metadateneigenschaften bietet die aus der Datei extrahiert wurden.
type: docs
weight: 80
url: /de/net/groupdocs.metadata/metadata/getrootpackage/
---
## GetRootPackage() {#getrootpackage}

Ruft das Stammpaket ab, das Zugriff auf alle Metadateneigenschaften bietet, die aus der Datei extrahiert wurden.

```csharp
public RootMetadataPackage GetRootPackage()
```

### Rückgabewert

Das Stammpaket, das Zugriff auf alle Metadateneigenschaften bietet, die aus der Datei extrahiert wurden.

### Bemerkungen

**Erfahren Sie mehr**

* [Durchlaufen Sie einen ganzen Metadatenbaum](https://docs.groupdocs.com/display/metadatanet/Traverse+a+whole+metadata+tree)

### Beispiele

Dieses Beispiel zeigt, wie der gesamte Metadatenbaum für eine bestimmte Datei unabhängig vom Format durchlaufen wird.

```csharp
public static void Run()
{
    using (Metadata metadata = new Metadata(Constants.JpegWithXmp))
    {
        DisplayMetadataTree(metadata.GetRootPackage(), 0);
    }
}

private static void DisplayMetadataTree(MetadataPackage package, int indent)
{
    if (package != null)
    {
        var stringMetadataType = package.MetadataType.ToString();
        Console.WriteLine(stringMetadataType.PadLeft(stringMetadataType.Length + indent));
        foreach (MetadataProperty property in package)
        {
            string stringPropertyRepresentation = string.Format("Name: {0}, Value: {1}", property.Name, property.Value);
            Console.WriteLine(stringPropertyRepresentation.PadLeft(stringPropertyRepresentation.Length + indent + 1));
            if (property.Value != null)
            {
                switch (property.Value.Type)
                {
                    case MetadataPropertyType.Metadata:
                        DisplayMetadataTree(property.Value.ToClass<MetadataPackage>(), indent + 2);
                    break;
                    case MetadataPropertyType.MetadataArray:
                        DisplayMetadataTree(property.Value.ToArray<MetadataPackage>(), indent + 2);
                    break;
                }
            }
        }
    }
}

private static void DisplayMetadataTree(MetadataPackage[] packages, int indent)
{
    if (packages != null)
    {
        foreach (var package in packages)
        {
            DisplayMetadataTree(package, indent);
        }
    }
}
```

### Siehe auch

* class [RootMetadataPackage](../../../groupdocs.metadata.common/rootmetadatapackage)
* class [Metadata](../../metadata)
* namensraum [GroupDocs.Metadata](../../metadata)
* Montage [GroupDocs.Metadata](../../../)

---

## GetRootPackage&lt;TRoot&gt;() {#getrootpackage_1}

Ruft das Stammpaket ab, das Zugriff auf alle Metadateneigenschaften bietet, die aus der Datei extrahiert wurden.

```csharp
public TRoot GetRootPackage<TRoot>()
    where TRoot : RootMetadataPackage
```

| Parameter | Beschreibung |
| --- | --- |
| TRoot | Der genaue Typ des Root-Pakets. |

### Rückgabewert

Das Stammpaket, das Zugriff auf alle Metadateneigenschaften bietet, die aus der Datei extrahiert wurden.

### Bemerkungen

**Erfahren Sie mehr**

* [Durchlaufen Sie einen ganzen Metadatenbaum](https://docs.groupdocs.com/display/metadatanet/Traverse+a+whole+metadata+tree)

### Siehe auch

* class [RootMetadataPackage](../../../groupdocs.metadata.common/rootmetadatapackage)
* class [Metadata](../../metadata)
* namensraum [GroupDocs.Metadata](../../metadata)
* Montage [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
