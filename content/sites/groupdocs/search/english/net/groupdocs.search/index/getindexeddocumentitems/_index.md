---
title: GetIndexedDocumentItems
second_title: GroupDocs.Search for .NET API Reference
description: Gets an array of nested items of the specified document for container documents such as ZIP OST PST.
type: docs
weight: 160
url: /net/groupdocs.search/index/getindexeddocumentitems/
---
## Index.GetIndexedDocumentItems method

Gets an array of nested items of the specified document (for container documents such as ZIP, OST, PST).

```csharp
public DocumentInfo[] GetIndexedDocumentItems(DocumentInfo documentInfo)
```

| Parameter | Type | Description |
| --- | --- | --- |
| documentInfo | DocumentInfo | The document info. |

### Return Value

An array of a document items.

### Examples

The example demonstrates how to get a list of items of an indexed document from an index.

```csharp
string indexFolder = @"c:\MyIndex\";
string documentsFolder = @"c:\MyDocuments\";
 
// Creating an index in the specified folder
Index index = new Index(indexFolder);
 
// Indexing documents from the specified folder
index.Add(documentsFolder);
 
// Getting list of indexed documents
DocumentInfo[] documents = index.GetIndexedDocuments();
for (int i = 0; i < documents.Length; i++)
{
    DocumentInfo document = documents[i];
    Console.WriteLine(document.FilePath);
    DocumentInfo[] items = index.GetIndexedDocumentItems(document); // Getting list of document items
    for (int j = 0; j < items.Length; j++)
    {
        DocumentInfo item = items[j];
        Console.WriteLine("\t" + item.InnerPath);
    }
}
```

### See Also

* class [DocumentInfo](../../../groupdocs.search.results/documentinfo)
* class [Index](../../index)
* namespace [GroupDocs.Search](../../../groupdocs.search)
* assembly [GroupDocs.Search](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.search.dll -->
