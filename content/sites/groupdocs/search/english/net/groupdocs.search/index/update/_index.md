---
title: Update
second_title: GroupDocs.Search for .NET API Reference
description: Reindexes documents that have been changed or deleted since last update. Adds new files that have been added to the indexed folders.
type: docs
weight: 280
url: /net/groupdocs.search/index/update/
---
## Update() {#update}

Re-indexes documents that have been changed or deleted since last update. Adds new files that have been added to the indexed folders.

```csharp
public void Update()
```

### Examples

The example demonstrates how to update an index.

```csharp
string indexFolder = @"c:\MyIndex\";
string documentsFolder = @"c:\MyDocuments\";

Index index = new Index(indexFolder); // Creating index in the specified folder
index.Add(documentsFolder); // Indexing documents from the specified folder

// Delete documents from the documents folder or modify them or add new documents to the folder

index.Update(); // Updating the index
```

### See Also

* class [Index](../../index)
* namespace [GroupDocs.Search](../../../groupdocs.search)
* assembly [GroupDocs.Search](../../../)

---

## Update(UpdateOptions) {#update_1}

Re-indexes documents that have been changed or deleted since last update. Adds new files that have been added to the indexed folders.

```csharp
public void Update(UpdateOptions options)
```

| Parameter | Type | Description |
| --- | --- | --- |
| options | UpdateOptions | The update options. |

### Examples

The example demonstrates how to update an index with particular update options.

```csharp
string indexFolder = @"c:\MyIndex\";
string documentsFolder = @"c:\MyDocuments\";

Index index = new Index(indexFolder); // Creating index in the specified folder
index.Add(documentsFolder); // Indexing documents from the specified folder

// Delete documents from the documents folder or modify them or add new documents to the folder

UpdateOptions options = new UpdateOptions();
options.Threads = 2; // Setting the number of indexing threads
index.Update(options); // Updating the index
```

### See Also

* class [UpdateOptions](../../../groupdocs.search.options/updateoptions)
* class [Index](../../index)
* namespace [GroupDocs.Search](../../../groupdocs.search)
* assembly [GroupDocs.Search](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.search.dll -->
