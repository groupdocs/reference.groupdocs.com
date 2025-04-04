---
title: NetworkSearchResult
second_title: GroupDocs.Search for .NET API Reference
description: Represents a search result matching a search query.
type: docs
weight: 1520
url: /net/groupdocs.search.scaling.results/networksearchresult/
---
## NetworkSearchResult class

Represents a search result matching a search query.

```csharp
public class NetworkSearchResult : IEnumerable<NetworkFoundDocument>
```

## Properties

| Name | Description |
| --- | --- |
| [DocumentCount](../../groupdocs.search.scaling.results/networksearchresult/documentcount) { get; } | Gets the number of documents found. |
| [EndTime](../../groupdocs.search.scaling.results/networksearchresult/endtime) { get; } | Gets the end time of the search. |
| [NextChunkSearchToken](../../groupdocs.search.scaling.results/networksearchresult/nextchunksearchtoken) { get; } | Gets a chunk search token for searching the next chunk. |
| [NodeIndex](../../groupdocs.search.scaling.results/networksearchresult/nodeindex) { get; } | Gets the index of the node from which the result was received. |
| [OccurrenceCount](../../groupdocs.search.scaling.results/networksearchresult/occurrencecount) { get; } | Gets the total number of occurrences found. |
| [SearchDuration](../../groupdocs.search.scaling.results/networksearchresult/searchduration) { get; } | Gets the search duration. |
| [StartTime](../../groupdocs.search.scaling.results/networksearchresult/starttime) { get; } | Gets the start time of the search. |
| [Truncated](../../groupdocs.search.scaling.results/networksearchresult/truncated) { get; } | Gets a value indicating that the result is truncated. |
| [Warnings](../../groupdocs.search.scaling.results/networksearchresult/warnings) { get; } | Gets a warnings describing the result. |

## Methods

| Name | Description |
| --- | --- |
| [GetEnumerator](../../groupdocs.search.scaling.results/networksearchresult/getenumerator)() | Returns an enumerator that iterates through the collection of the documents found. |
| [GetFoundDocument](../../groupdocs.search.scaling.results/networksearchresult/getfounddocument)(int) | Gets the found document by index. |

### See Also

* class [NetworkFoundDocument](../networkfounddocument)
* namespace [GroupDocs.Search.Scaling.Results](../../groupdocs.search.scaling.results)
* assembly [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.search.dll -->
