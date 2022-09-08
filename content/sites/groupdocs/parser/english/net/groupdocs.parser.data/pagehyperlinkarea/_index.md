---
title: PageHyperlinkArea
second_title: GroupDocs.Parser for .NET API Reference
description: Represents a page area which is used to represent a hyperlink on the page.
type: docs
weight: 100
url: /net/groupdocs.parser.data/pagehyperlinkarea/
---
## PageHyperlinkArea class

Represents a page area which is used to represent a hyperlink on the page.

```csharp
public sealed class PageHyperlinkArea : PageArea
```

## Constructors

| Name | Description |
| --- | --- |
| [PageHyperlinkArea](pagehyperlinkarea)(string, string, Page, Rectangle) | Initializes a new instance of the [`PageHyperlinkArea`](../pagehyperlinkarea) class. |

## Properties

| Name | Description |
| --- | --- |
| [Page](../../groupdocs.parser.data/pagearea/page) { get; } | Gets the document page information such as page index and page size. |
| [Rectangle](../../groupdocs.parser.data/pagearea/rectangle) { get; } | Gets the rectangular area. |
| [Text](../../groupdocs.parser.data/pagehyperlinkarea/text) { get; } | Gets the hyperlink text. |
| [Url](../../groupdocs.parser.data/pagehyperlinkarea/url) { get; } | Gets the hyperlink URL. |

### Remarks

An instance of [`PageHyperlinkArea`](../pagehyperlinkarea) class is used as return value of the following methods:

* [`GetHyperlinks`](../../groupdocs.parser/parser/gethyperlinks)
* [`GetHyperlinks`](../../groupdocs.parser/parser/gethyperlinks)
* [`GetHyperlinks`](../../groupdocs.parser/parser/gethyperlinks)
* [`GetHyperlinks`](../../groupdocs.parser/parser/gethyperlinks)

See the usage examples there.

### See Also

* class [PageArea](../pagearea)
* namespace [GroupDocs.Parser.Data](../../groupdocs.parser.data)
* assembly [GroupDocs.Parser](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.parser.dll -->