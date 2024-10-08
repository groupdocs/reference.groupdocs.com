---
title: CreateFromStream
second_title: GroupDocs.Search for .NET API Reference
description: Creates a document from a stream.
type: docs
weight: 20
url: /net/groupdocs.search.common/document/createfromstream/
---
## Document.CreateFromStream method

Creates a document from a stream.

```csharp
public static Document CreateFromStream(string documentKey, DateTime modificationDate, 
    string extension, Stream stream)
```

| Parameter | Type | Description |
| --- | --- | --- |
| documentKey | String | The document key. |
| modificationDate | DateTime | The document modification date. |
| extension | String | The document extension. The extension must start with the period character '.'. |
| stream | Stream | The document stream. |

### Return Value

The created document.

### See Also

* class [Document](../../document)
* namespace [GroupDocs.Search.Common](../../../groupdocs.search.common)
* assembly [GroupDocs.Search](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.search.dll -->
