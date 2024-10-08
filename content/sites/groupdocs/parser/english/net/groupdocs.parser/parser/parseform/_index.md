---
title: ParseForm
second_title: GroupDocs.Parser for .NET API Reference
description: Parses the document form.
type: docs
weight: 220
url: /net/groupdocs.parser/parser/parseform/
---
## Parser.ParseForm method

Parses the document form.

```csharp
public DocumentData ParseForm()
```

### Return Value

An instance of [`DocumentData`](../../../groupdocs.parser.data/documentdata) class that contains the extracted data; `null` if parsing by template isn't supported.

### Remarks

**Learn more:**

* [Extract data from PDF forms](https://docs.groupdocs.com/display/parsernet/Extract+data+from+PDF+forms)
* [Working with extracted data](https://docs.groupdocs.com/display/parsernet/Working+with+data+extracted+by+template)
* [Parse data from PDF documents](https://docs.groupdocs.com/display/parsernet/Parse+data+from+PDF+documents)

### Examples

The following example shows how to parse a form of the document:

```csharp
// Create an instance of Parser class
using (Parser parser = new Parser(filePath))
{
    // Extract data from PDF document
    DocumentData data = parser.ParseForm();
    // Iterate over extracted data
    for (int i = 0; i<data.Count; i++)
    {
        Console.Write(data[i].Name + ": ");
        PageTextArea area = data[i].PageArea as PageTextArea;
        Console.WriteLine(area == null ? "Not a template field" : area.Text);
    }
}
```

### See Also

* class [DocumentData](../../../groupdocs.parser.data/documentdata)
* class [Parser](../../parser)
* namespace [GroupDocs.Parser](../../../groupdocs.parser)
* assembly [GroupDocs.Parser](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.parser.dll -->
