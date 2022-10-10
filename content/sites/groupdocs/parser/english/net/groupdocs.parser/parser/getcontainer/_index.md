---
title: GetContainer
second_title: GroupDocs.Parser for .NET API Reference
description: Extracts a container object from the document to work with formats that contain attachments ZIP archives etc.
type: docs
weight: 60
url: /net/groupdocs.parser/parser/getcontainer/
---
## Parser.GetContainer method

Extracts a container object from the document to work with formats that contain attachments, ZIP archives etc.

```csharp
public IEnumerable<ContainerItem> GetContainer()
```

### Return Value

A collection of container items; `null` if container extraction isn't supported.

### Remarks

To check if the format supports extracting attachments see [Supported Document Formats](https://docs.groupdocs.com/parser/net/supported-document-formats/) (**Extract Containers and Attachments** column).

**Learn more:**

* [Extract data from attachments and ZIP archives](https://docs.groupdocs.com/display/parsernet/Extract+data+from+attachments+and+ZIP+archives)
* [Iterate through container items](https://docs.groupdocs.com/display/parsernet/Iterate+through+container+items)
* [Extract attachments from PDF portfolios](https://docs.groupdocs.com/display/parsernet/Extract+attachments+from+PDF+portfolios)
* [Extract attachments from Emails](https://docs.groupdocs.com/display/parsernet/Extract+attachments+from+Emails)
* [Extract emails from Outlook Storage](https://docs.groupdocs.com/display/parsernet/Extract+emails+from+Outlook+Storage)
* [Extract text from ZIP archive files](https://docs.groupdocs.com/display/parsernet/Extract+text+from+ZIP+archive+files)

### Examples

The following example shows how to extract attachments from a container:

```csharp
// Create an instance of Parser class
using(Parser parser = new Parser(filePath))
{
    // Extract attachments from the container
    IEnumerable<ContainerItem> attachments = parser.GetContainer();
    // Check if container extraction is supported
    if(attachments == null)
    {
        Console.WriteLine("Container extraction isn't supported");
    }
 
    // Iterate over attachments
    foreach(ContainerItem item in attachments)
    {
        // Print an item name and size
        Console.WriteLine(string.Format("{0}: {1}", item.Name, item.Size));
    }
}
```

### See Also

* class [ContainerItem](../../../groupdocs.parser.data/containeritem)
* class [Parser](../../parser)
* namespace [GroupDocs.Parser](../../parser)
* assembly [GroupDocs.Parser](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.parser.dll -->