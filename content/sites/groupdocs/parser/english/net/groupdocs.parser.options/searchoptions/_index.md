---
title: SearchOptions
second_title: GroupDocs.Parser for .NET API Reference
description: Provides the options which are used for text search.
type: docs
weight: 740
url: /net/groupdocs.parser.options/searchoptions/
---
## SearchOptions class

Provides the options which are used for text search.

```csharp
public sealed class SearchOptions
```

## Constructors

| Name | Description |
| --- | --- |
| [SearchOptions](searchoptions#constructor)() | Initializes a new instance of the [`SearchOptions`](../searchoptions) class with default values. See remarks for details. |
| [SearchOptions](searchoptions#constructor_1)(bool, bool, bool) | Initializes a new instance of the [`SearchOptions`](../searchoptions) class which is used to search without highlight extraction. |
| [SearchOptions](searchoptions#constructor_2)(bool, bool, bool, bool) | Initializes a new instance of the [`SearchOptions`](../searchoptions) class which is used to search by pages and without highlight extraction. |
| [SearchOptions](searchoptions#constructor_4)(bool, bool, bool, HighlightOptions) | Initializes a new instance of the [`SearchOptions`](../searchoptions) class which is used to search with the same highlight options for the left and the right highlight extraction. |
| [SearchOptions](searchoptions#constructor_5)(bool, bool, bool, HighlightOptions, HighlightOptions) | Initializes a new instance of the [`SearchOptions`](../searchoptions) class which is used to search with the highlight options for the left and the right highlight extraction. |
| [SearchOptions](searchoptions#constructor_3)(bool, bool, bool, bool, HighlightOptions, HighlightOptions) | Initializes a new instance of the [`SearchOptions`](../searchoptions) class. |
| [SearchOptions](searchoptions#constructor_6)(bool, bool, bool, int, HighlightOptions, HighlightOptions) | Initializes a new instance of the [`SearchOptions`](../searchoptions) class with the page limit. |

## Properties

| Name | Description |
| --- | --- |
| [LeftHighlightOptions](../../groupdocs.parser.options/searchoptions/lefthighlightoptions) { get; } | Gets the options for the left highlight. |
| [MatchCase](../../groupdocs.parser.options/searchoptions/matchcase) { get; } | Gets the value that indicates whether a text case isn't ignored. |
| [MatchWholeWord](../../groupdocs.parser.options/searchoptions/matchwholeword) { get; } | Gets the value that indicates whether text search is limited by a whole word. |
| [MaxPageIndex](../../groupdocs.parser.options/searchoptions/maxpageindex) { get; } | Gets the value that represents the max index of the page to search. |
| [RightHighlightOptions](../../groupdocs.parser.options/searchoptions/righthighlightoptions) { get; } | Gets the options for the right highlight. |
| [SearchByPages](../../groupdocs.parser.options/searchoptions/searchbypages) { get; } | Gets the value that indicates whether the search is performed by pages. |
| [UseRegularExpression](../../groupdocs.parser.options/searchoptions/useregularexpression) { get; } | Gets the value that indicates whether a regular expression is used. |

### Remarks

An instance of [`SearchOptions`](../searchoptions) class is used as parameter in [`Search`](../../groupdocs.parser/parser/search) method. See the usage examples there.

**Learn more:**

* [Search text](https://docs.groupdocs.com/display/parsernet/Search+text)
* [Search text in Microsoft Office Word documents](https://docs.groupdocs.com/display/parsernet/Search+text+in+Microsoft+Office+Word+documents)
* [Search text in Microsoft Office Excel spreadsheets](https://docs.groupdocs.com/display/parsernet/Search+text+in+Microsoft+Office+Excel+spreadsheets)
* [Search text in Microsoft Office PowerPoint presentations](https://docs.groupdocs.com/display/parsernet/Search+text+in+Microsoft+Office+PowerPoint+presentations)
* [Search text in PDF documents](https://docs.groupdocs.com/display/parsernet/Search+text+in+PDF+documents)
* [Search text in Emails](https://docs.groupdocs.com/display/parsernet/Search+text+in+Emails)
* [Search text in EPUB eBooks](https://docs.groupdocs.com/display/parsernet/Search+text+in+EPUB+eBooks)
* [Search text in HTML documents](https://docs.groupdocs.com/display/parsernet/Search+text+in+HTML+documents)
* [Search text in Microsoft OneNote sections](https://docs.groupdocs.com/display/parsernet/Search+text+in+Microsoft+OneNote+sections)

### See Also

* namespace [GroupDocs.Parser.Options](../../groupdocs.parser.options)
* assembly [GroupDocs.Parser](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.parser.dll -->
