---
title: Item
second_title: GroupDocs.Parser for .NET API Reference
description: Gets the field data by an index.
type: docs
weight: 30
url: /net/groupdocs.parser.data/documentdata/item/
---
## DocumentData indexer

Gets the field data by an index.

```csharp
public FieldData this[int index] { get; }
```

| Parameter | Description |
| --- | --- |
| index | The zero-based index of the field. |

### Return Value

An instance of [`FieldData`](../../fielddata) class.

### Examples

Iteration via all the fields:

```csharp
for (int i = 0; i < data.Count; i++)
{
    Console.Write(data[i].Name + ": ");
    PageTextArea area = data[i].PageArea as PageTextArea;
    Console.WriteLine(area == null ? "Not a template field" : area.Text);
}
```

[`FieldData`](../../fielddata) class represents field data. Depending on the field [`PageArea`](../../fielddata/pagearea) property can contain any of the inheritors of [`PageArea`](../../pagearea) class. For example, [`ParseForm`](../../../groupdocs.parser/parser/parseform) method extracts only text fields:

```csharp
// Create the parser
using (Parser parser = new Parser(filePath))
{
    // Extract data from PDF Form
    DocumentData data = parser.ParseForm();
    // Iterate over extracted fields
    for (int i = 0; i < data.Count; i++)
    {
        // Get the extracted field
        FieldData field = data[i];
        // Print the field name
        Console.Write(field.Name + ": ");
        // Check if the field value is a text and print it
        PageTextArea area = field.PageArea as PageTextArea;
        Console.WriteLine(area == null ? "Not a template field" : area.Text);
    }
}
```

### See Also

* class [FieldData](../../fielddata)
* class [DocumentData](../../documentdata)
* namespace [GroupDocs.Parser.Data](../../documentdata)
* assembly [GroupDocs.Parser](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.parser.dll -->