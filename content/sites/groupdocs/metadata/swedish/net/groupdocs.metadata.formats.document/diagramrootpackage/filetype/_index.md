---
title: FileType
second_title: GroupDocs.Metadata for .NET API-referens
description: Hämtar filtypens metadatapaket.
type: docs
weight: 20
url: /sv/net/groupdocs.metadata.formats.document/diagramrootpackage/filetype/
---
## DiagramRootPackage.FileType property

Hämtar filtypens metadatapaket.

```csharp
public DiagramTypePackage FileType { get; }
```

### Fastighetsvärde

Filtypens metadatapaket.

### Exempel

Detta kodexempel visar hur man upptäcker den exakta typen av ett laddat diagram och extraherar ytterligare information om filformat.

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

### Se även

* class [DiagramTypePackage](../../diagramtypepackage)
* class [DiagramRootPackage](../../diagramrootpackage)
* namnutrymme [GroupDocs.Metadata.Formats.Document](../../diagramrootpackage)
* hopsättning [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
