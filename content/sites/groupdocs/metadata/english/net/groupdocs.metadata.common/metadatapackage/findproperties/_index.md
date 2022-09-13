---
title: FindProperties
second_title: GroupDocs.Metadata for .NET API Reference
description: Finds the metadata properties satisfying the specified predicate. The search is recursive so it affects all nested packages as well.
type: docs
weight: 80
url: /net/groupdocs.metadata.common/metadatapackage/findproperties/
---
## MetadataPackage.FindProperties method

Finds the metadata properties satisfying the specified predicate. The search is recursive so it affects all nested packages as well.

```csharp
public virtual IEnumerable<MetadataProperty> FindProperties(Func<MetadataProperty, bool> predicate)
```

| Parameter | Type | Description |
| --- | --- | --- |
| predicate | Func`2 | A function to test each metadata property for a condition. |

### Return Value

An IEnumerable that contains properties from the package that satisfy the condition.

### Remarks

**Learn more**

* More examples demonstrating usages of this method: [Extracting metadata](https://docs.groupdocs.com/display/metadatanet/Extracting+metadata)

### See Also

* class [MetadataProperty](../../metadataproperty)
* delegate [Func&lt;T,TResult&gt;](../../func-2)
* class [MetadataPackage](../../metadatapackage)
* namespace [GroupDocs.Metadata.Common](../../metadatapackage)
* assembly [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.metadata.dll -->