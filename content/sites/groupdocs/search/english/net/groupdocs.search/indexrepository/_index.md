---
title: IndexRepository
second_title: GroupDocs.Search for .NET API Reference
description: Represents a container for combining multiple indexes and performing common operations on them.
type: docs
weight: 590
url: /net/groupdocs.search/indexrepository/
---
## IndexRepository class

Represents a container for combining multiple indexes and performing common operations on them.

```csharp
public class IndexRepository : IDisposable
```

## Constructors

| Name | Description |
| --- | --- |
| [IndexRepository](indexrepository)() | Initializes a new instance of the [`IndexRepository`](../indexrepository) class. |

## Properties

| Name | Description |
| --- | --- |
| [Events](../../groupdocs.search/indexrepository/events) { get; } | Gets the event hub for subscribing to events. |
| [Indexes](../../groupdocs.search/indexrepository/indexes) { get; } | Gets the indexes contained in this [`IndexRepository`](../indexrepository). |

## Methods

| Name | Description |
| --- | --- |
| [AddToRepository](../../groupdocs.search/indexrepository/addtorepository#addtorepository)(Index) | Adds an index to the index repository. |
| [AddToRepository](../../groupdocs.search/indexrepository/addtorepository#addtorepository_1)(string) | Opens and adds an index to the index repository. |
| [Create](../../groupdocs.search/indexrepository/create#create)() | Creates a new index in memory. |
| [Create](../../groupdocs.search/indexrepository/create#create_1)(IndexSettings) | Creates a new index in memory. |
| [Create](../../groupdocs.search/indexrepository/create#create_2)(string) | Creates a new index on disk. The index folder will be cleaned before the index creation. |
| [Create](../../groupdocs.search/indexrepository/create#create_3)(string, IndexSettings) | Creates a new index on disk. The index folder will be cleaned before the index creation. |
| [Dispose](../../groupdocs.search/indexrepository/dispose)() | Releases all resources used by the [`IndexRepository`](../indexrepository). |
| [Search](../../groupdocs.search/indexrepository/search#search)(SearchQuery) | Searches in all indexes of the repository. |
| [Search](../../groupdocs.search/indexrepository/search#search_2)(string) | Searches in all indexes of the repository. |
| [Search](../../groupdocs.search/indexrepository/search#search_1)(SearchQuery, SearchOptions) | Searches in all indexes of the repository. |
| [Search](../../groupdocs.search/indexrepository/search#search_3)(string, SearchOptions) | Searches in all indexes of the repository. |
| [Update](../../groupdocs.search/indexrepository/update#update)() | Updates all indexes in the repository. |
| [Update](../../groupdocs.search/indexrepository/update#update_1)(UpdateOptions) | Updates all indexes in the repository. |

### Remarks

**Learn more**

* [Search index repository](https://docs.groupdocs.com/display/searchnet/Search+index+repository)

### Examples

The example demonstrates a typical usage of the class.

```csharp
string indexFolder1 = @"c:\MyIndex\";
string indexFolder2 = @"c:\MyIndex\";
string query = "Einstein";

IndexRepository repository = new IndexRepository();
repository.AddToRepository(indexFolder1); // Loading an existing index
repository.AddToRepository(indexFolder2); // Loading another existing index

SearchResult result = repository.Search(query); // Searching in indexes of the repository
```

### See Also

* namespace [GroupDocs.Search](../../groupdocs.search)
* assembly [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.search.dll -->