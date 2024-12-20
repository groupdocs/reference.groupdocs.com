---
title: ReadOnlyListT
second_title: GroupDocs.Metadata for .NET API Reference
description: Provides an abstract base class for a strongly typed readonly list.
type: docs
weight: 200
url: /net/groupdocs.metadata.common/readonlylist-1/
---
## ReadOnlyList&lt;T&gt; class

Provides an abstract base class for a strongly typed read-only list.

```csharp
public class ReadOnlyList<T> : IList, IList<T>, IReadOnlyList<T>
```

| Parameter | Description |
| --- | --- |
| T | The type of the element. |

## Properties

| Name | Description |
| --- | --- |
| [Count](../../groupdocs.metadata.common/readonlylist-1/count) { get; } | Gets the number of elements contained in the collection. |
| [IsReadOnly](../../groupdocs.metadata.common/readonlylist-1/isreadonly) { get; } | Gets a value indicating whether the collection is read-only. |
| [Item](../../groupdocs.metadata.common/readonlylist-1/item) { get; } | Gets the element at the specified index in the collection. |

## Methods

| Name | Description |
| --- | --- |
| [Contains](../../groupdocs.metadata.common/readonlylist-1/contains#contains_1)(T) | Determines whether the collection contains a specific item. |
| [Contains](../../groupdocs.metadata.common/readonlylist-1/contains#contains)(TagCategory) | Determines whether the collection contains a TagCategory item. |
| [GetEnumerator](../../groupdocs.metadata.common/readonlylist-1/getenumerator)() | Returns an enumerator that iterates through a collection. |
| [IndexOf](../../groupdocs.metadata.common/readonlylist-1/indexof)(T) | Determines the index of a specific item in the collection. |

### See Also

* interface [IReadOnlyList&lt;T&gt;](../ireadonlylist-1)
* namespace [GroupDocs.Metadata.Common](../../groupdocs.metadata.common)
* assembly [GroupDocs.Metadata](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.metadata.dll -->
