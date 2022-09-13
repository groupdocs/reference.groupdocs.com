---
title: GetRootPackage
second_title: GroupDocs.Metadata for .NET API Reference
description: Gets the root package providing access to all metadata properties extracted from the file.
type: docs
weight: 80
url: /net/groupdocs.metadata/metadata/getrootpackage/
---
## GetRootPackage() {#getrootpackage}

Gets the root package providing access to all metadata properties extracted from the file.

```csharp
public RootMetadataPackage GetRootPackage()
```

### Return Value

The root package providing access to all metadata properties extracted from the file.

### Remarks

**Learn more**

* [Traverse a whole metadata tree](https://docs.groupdocs.com/display/metadatanet/Traverse+a+whole+metadata+tree)

### Examples

This example demonstrates how to traverse the whole metadata tree for a specific file regardless of the format.

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

### See Also

* class [RootMetadataPackage](../../../groupdocs.metadata.common/rootmetadatapackage)
* class [Metadata](../../metadata)
* namespace [GroupDocs.Metadata](../../metadata)
* assembly [GroupDocs.Metadata](../../../)

---

## GetRootPackage&lt;TRoot&gt;() {#getrootpackage_1}

Gets the root package providing access to all metadata properties extracted from the file.

```csharp
public TRoot GetRootPackage<TRoot>()
    where TRoot : RootMetadataPackage
```

| Parameter | Description |
| --- | --- |
| TRoot | The exact type of the root package. |

### Return Value

The root package providing access to all metadata properties extracted from the file.

### Remarks

**Learn more**

* [Traverse a whole metadata tree](https://docs.groupdocs.com/display/metadatanet/Traverse+a+whole+metadata+tree)

### See Also

* class [RootMetadataPackage](../../../groupdocs.metadata.common/rootmetadatapackage)
* class [Metadata](../../metadata)
* namespace [GroupDocs.Metadata](../../metadata)
* assembly [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.metadata.dll -->