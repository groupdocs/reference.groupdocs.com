---
title: FileType
second_title: GroupDocs.Metadata for .NET API Reference
description: Gets the file type metadata package.
type: docs
weight: 20
url: /net/groupdocs.metadata.formats.document/diagramrootpackage/filetype/
---
## DiagramRootPackage.FileType property

Gets the file type metadata package.

```csharp
public DiagramTypePackage FileType { get; }
```

### Property Value

The file type metadata package.

### Examples

This code sample shows how to detect the exact type of a loaded diagram and extract some additional file format information.

```csharp
using (Metadata metadata = new Metadata(Constants.InputVdx))
{
    var root = metadata.GetRootPackage<DiagramRootPackage>();

    Console.WriteLine(root.FileType.FileFormat);
    Console.WriteLine(root.FileType.DiagramFormat);
    Console.WriteLine(root.FileType.MimeType);
    Console.WriteLine(root.FileType.Extension);
}
```

### See Also

* class [DiagramTypePackage](../../diagramtypepackage)
* class [DiagramRootPackage](../../diagramrootpackage)
* namespace [GroupDocs.Metadata.Formats.Document](../../diagramrootpackage)
* assembly [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.metadata.dll -->