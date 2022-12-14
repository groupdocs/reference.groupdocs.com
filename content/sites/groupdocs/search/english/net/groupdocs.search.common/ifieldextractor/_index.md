---
title: IFieldExtractor
second_title: GroupDocs.Search for .NET API Reference
description: Provides methods for extracting fields from a document.
type: docs
weight: 190
url: /net/groupdocs.search.common/ifieldextractor/
---
## IFieldExtractor interface

Provides methods for extracting fields from a document.

```csharp
public interface IFieldExtractor
```

## Properties

| Name | Description |
| --- | --- |
| [Extensions](../../groupdocs.search.common/ifieldextractor/extensions) { get; } | Gets the supported extensions. |

## Methods

| Name | Description |
| --- | --- |
| [GetFields](../../groupdocs.search.common/ifieldextractor/getfields#getfields)(Stream) | Extracts all fields from the specified document. |
| [GetFields](../../groupdocs.search.common/ifieldextractor/getfields#getfields_1)(string) | Extracts all fields from the specified document. |

### Remarks

**Learn more**

* [Custom text extractors](https://docs.groupdocs.com/display/searchnet/Custom+text+extractors)

### Examples

The example demonstrates how to implement the interface [`IFieldExtractor`](../ifieldextractor).

```csharp
public class LogExtractor : IFieldExtractor
{
    private readonly string[] extensions = new string[] { ".log" };

    public string[] Extensions
    {
        get { return extensions; }
    }

    public DocumentField[] GetFields(string filePath)
    {
        FileInfo fileInfo = new FileInfo(filePath);
        DocumentField[] fields = new DocumentField[]
        {
            new DocumentField("FileName", fileInfo.FullName),
            new DocumentField("CreationDate", fileInfo.CreationTime.ToString(CultureInfo.InvariantCulture)),
            new DocumentField("Content", ExtractContent(filePath)),
        };
        return fields;
    }

    private string ExtractContent(string filePath)
    {
        StringBuilder result = new StringBuilder();
        using (StreamReader streamReader = File.OpenText(filePath))
        {
            string line = streamReader.ReadLine();
            string processedLine = line.Remove(0, 12);
            result.AppendLine(processedLine);
        }
        return result.ToString();
    }
}
```

The example demonstrates how to use the custorm extractor for indexing.

```csharp
string indexFolder = @"c:\MyIndex\"; // Specify path to the index folder
string documentsFolder = @"c:\MyDocuments\"; // Specify path to a folder containing documents to search

Index index = new Index(indexFolder); // Creating or loading an index

index.IndexSettings.CustomExtractors.Add(new LogExtractor()); // Adding custom text extractor to index settings

index.Add(documentsFolder); // Indexing documents from the specified folder
```

### See Also

* namespace [GroupDocs.Search.Common](../../groupdocs.search.common)
* assembly [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.search.dll -->
