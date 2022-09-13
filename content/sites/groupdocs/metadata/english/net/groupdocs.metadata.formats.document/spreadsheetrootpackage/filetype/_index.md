---
title: FileType
second_title: GroupDocs.Metadata for .NET API Reference
description: Gets the file type metadata package.
type: docs
weight: 20
url: /net/groupdocs.metadata.formats.document/spreadsheetrootpackage/filetype/
---
## SpreadsheetRootPackage.FileType property

Gets the file type metadata package.

```csharp
public SpreadsheetTypePackage FileType { get; }
```

### Property Value

The file type metadata package.

### Examples

This example shows how to detect the exact type of a loaded spreadsheet and extract some additional file format information.

```csharp
using (Metadata metadata = new Metadata(Constants.InputXlsx))
{
    var root = metadata.GetRootPackage<SpreadsheetRootPackage>();

    Console.WriteLine(root.FileType.FileFormat);
    Console.WriteLine(root.FileType.SpreadsheetFormat);
    Console.WriteLine(root.FileType.MimeType);
    Console.WriteLine(root.FileType.Extension);
}
```

### See Also

* class [SpreadsheetTypePackage](../../spreadsheettypepackage)
* class [SpreadsheetRootPackage](../../spreadsheetrootpackage)
* namespace [GroupDocs.Metadata.Formats.Document](../../spreadsheetrootpackage)
* assembly [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.metadata.dll -->