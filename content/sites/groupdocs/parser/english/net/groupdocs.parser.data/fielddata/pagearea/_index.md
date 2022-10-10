---
title: PageArea
second_title: GroupDocs.Parser for .NET API Reference
description: Gets the value of the field.
type: docs
weight: 40
url: /net/groupdocs.parser.data/fielddata/pagearea/
---
## FieldData.PageArea property

Gets the value of the field.

```csharp
public PageArea PageArea { get; }
```

### Property Value

An instance of [`PageArea`](../../pagearea) class that represents the value of the field.

### Examples

Depending on field `PageArea` property can contain any of the inheritors of [`PageArea`](../../pagearea) class. For example, [`ParseForm`](../../../groupdocs.parser/parser/parseform) method extracts only text fields.

```csharp
// Get the field data
FieldData field = data[i];
// Check if the field data contains a text
if(field.PageArea is PageTextArea)
{
    // Print the field text value
    Console.WriteLine(field.Text);
}
```

### See Also

* class [PageArea](../../pagearea)
* class [FieldData](../../fielddata)
* namespace [GroupDocs.Parser.Data](../../fielddata)
* assembly [GroupDocs.Parser](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.parser.dll -->