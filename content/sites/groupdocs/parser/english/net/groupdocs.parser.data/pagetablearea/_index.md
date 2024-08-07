---
title: PageTableArea
second_title: GroupDocs.Parser for .NET API Reference
description: Represents a table page area which is used to represent a table in the parsing by template functionality.
type: docs
weight: 130
url: /net/groupdocs.parser.data/pagetablearea/
---
## PageTableArea class

Represents a table page area which is used to represent a table in the parsing by template functionality.

```csharp
public sealed class PageTableArea : PageArea
```

## Constructors

| Name | Description |
| --- | --- |
| [PageTableArea](pagetablearea)(IEnumerable&lt;double&gt;, IEnumerable&lt;double&gt;, IEnumerable&lt;PageTableAreaCell&gt;, Page, Rectangle) | Initializes a new instance of the [`PageTableArea`](../pagetablearea) class. |

## Properties

| Name | Description |
| --- | --- |
| [Cells](../../groupdocs.parser.data/pagetablearea/cells) { get; } | Gets the collection of cells. |
| [ColumnCount](../../groupdocs.parser.data/pagetablearea/columncount) { get; } | Gets the total number of the table colums. |
| [Item](../../groupdocs.parser.data/pagetablearea/item) { get; } | Gets the table cell by row and column indexes. |
| [Page](../../groupdocs.parser.data/pagearea/page) { get; } | Gets the document page information such as page index and page size. |
| [Rectangle](../../groupdocs.parser.data/pagearea/rectangle) { get; } | Gets the rectangular area. |
| [RowCount](../../groupdocs.parser.data/pagetablearea/rowcount) { get; } | Gets the total number of the table rows. |

## Methods

| Name | Description |
| --- | --- |
| [GetColumnWidth](../../groupdocs.parser.data/pagetablearea/getcolumnwidth)(int) | Returns the column width. |
| [GetRowHeight](../../groupdocs.parser.data/pagetablearea/getrowheight)(int) | Returns the row height. |

### Remarks

[`PageTableArea`](../pagetablearea) class is used to organize inheritors of [`PageArea`](../pagearea) class in table structure.

### See Also

* class [PageArea](../pagearea)
* namespace [GroupDocs.Parser.Data](../../groupdocs.parser.data)
* assembly [GroupDocs.Parser](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.parser.dll -->
