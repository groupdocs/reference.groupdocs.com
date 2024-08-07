---
title: EbookEditOptions
second_title: GroupDocs.Editor for .NET API Reference
description: Allows to specify and adjust custom options for editing Ebook documents in all supported formats ePub MOBI and AZW3.
type: docs
weight: 820
url: /net/groupdocs.editor.options/ebookeditoptions/
---
## EbookEditOptions class

Allows to specify and adjust custom options for editing E-book documents in all supported formats: ePub, MOBI, and AZW3.

```csharp
public sealed class EbookEditOptions : IEditOptions
```

## Constructors

| Name | Description |
| --- | --- |
| [EbookEditOptions](ebookeditoptions#constructor)() | Initializes a new instance of the [`EbookEditOptions`](../ebookeditoptions) class, where all options are set to their default values |
| [EbookEditOptions](ebookeditoptions#constructor_1)(bool) | Initializes a new instance of the [`EbookEditOptions`](../ebookeditoptions) class with specified pagination mode |

## Properties

| Name | Description |
| --- | --- |
| [EnableLanguageInformation](../../groupdocs.editor.options/ebookeditoptions/enablelanguageinformation) { get; set; } | Specifies whether language information is exported to the HTML markup in a form of 'lang' HTML attributes. This option may be useful for roundtrip conversion of the multi-language documents. By default it is disabled (`false`). |
| [EnablePagination](../../groupdocs.editor.options/ebookeditoptions/enablepagination) { get; set; } | Allows to enable or disable pagination in the resultant HTML document. By default is disabled (`false`). |

### Remarks

Supported E-book formats:

1. [ePub](https://docs.fileformat.com/ebook/epub/) (Electronic Publication)
2. [MOBI](https://docs.fileformat.com/ebook/mobi/) (MobiPocket)
3. [AZW3](https://docs.fileformat.com/ebook/azw3/) (Kindle Format 8t)

### See Also

* interface [IEditOptions](../ieditoptions)
* namespace [GroupDocs.Editor.Options](../../groupdocs.editor.options)
* assembly [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.editor.dll -->
