---
title: MetadataIndexingOptions
second_title: GroupDocs.Search for .NET API Reference
description: Provides options for indexing metadata fields.
type: docs
weight: 840
url: /net/groupdocs.search.options/metadataindexingoptions/
---
## MetadataIndexingOptions class

Provides options for indexing metadata fields.

```csharp
public class MetadataIndexingOptions
```

## Properties

| Name | Description |
| --- | --- |
| [DefaultFieldName](../../groupdocs.search.options/metadataindexingoptions/defaultfieldname) { get; set; } | Gets or sets the default field name used to index empty field names. The default value is `"unknown"`. |
| [IndexingEmptyNames](../../groupdocs.search.options/metadataindexingoptions/indexingemptynames) { get; set; } | Gets or sets a value indicating whether to index empty field names ​​or not. The default value is `true`. |
| [IndexingEmptyValues](../../groupdocs.search.options/metadataindexingoptions/indexingemptyvalues) { get; set; } | Gets or sets a value indicating whether to index empty field values ​​or not. The default value is `true`. |
| [MaxBytesToIndexField](../../groupdocs.search.options/metadataindexingoptions/maxbytestoindexfield) { get; set; } | Gets or sets the maximum number of values in an array of type byte to index the field. The default value is `int.MaxValue`. |
| [MaxDoublesToIndexField](../../groupdocs.search.options/metadataindexingoptions/maxdoublestoindexfield) { get; set; } | Gets or sets the maximum number of values in an array of type double to index the field. The default value is `int.MaxValue`. |
| [MaxIntsToIndexField](../../groupdocs.search.options/metadataindexingoptions/maxintstoindexfield) { get; set; } | Gets or sets the maximum number of values in an array of type int to index the field. The default value is `int.MaxValue`. |
| [MaxLongsToIndexField](../../groupdocs.search.options/metadataindexingoptions/maxlongstoindexfield) { get; set; } | Gets or sets the maximum number of values in an array of type long to index the field. The default value is `int.MaxValue`. |
| [SeparatorBetweenValues](../../groupdocs.search.options/metadataindexingoptions/separatorbetweenvalues) { get; set; } | Gets or sets the separator between values ​​in a field of type array. The default value is the space sign. |
| [SeparatorInCompoundName](../../groupdocs.search.options/metadataindexingoptions/separatorincompoundname) { get; set; } | Gets or sets the separator in the compound name of a field. The default value is `"."`. |

### Remarks

**Learn more**

* [Indexing options](https://docs.groupdocs.com/display/searchnet/Indexing+options)
* MetadataIndexingOptions are used when retrieving document text from an index: [Getting indexed documents](https://docs.groupdocs.com/display/searchnet/Getting+indexed+documents)
* MetadataIndexingOptions are used when highlighting search results: [Highlighting search results](https://docs.groupdocs.com/display/searchnet/Highlighting+search+results)

### See Also

* namespace [GroupDocs.Search.Options](../../groupdocs.search.options)
* assembly [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.search.dll -->