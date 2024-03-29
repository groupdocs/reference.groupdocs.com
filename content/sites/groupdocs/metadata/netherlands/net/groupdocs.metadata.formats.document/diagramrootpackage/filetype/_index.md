---
title: FileType
second_title: GroupDocs.Metadata voor .NET API-referentie
description: Haalt het metadatapakket van het bestandstype op.
type: docs
weight: 20
url: /nl/net/groupdocs.metadata.formats.document/diagramrootpackage/filetype/
---
## DiagramRootPackage.FileType property

Haalt het metadatapakket van het bestandstype op.

```csharp
public DiagramTypePackage FileType { get; }
```

### Eigendoms-waarde

Het metadatapakket van het bestandstype.

### Voorbeelden

Dit codevoorbeeld laat zien hoe u het exacte type van een geladen diagram kunt detecteren en aanvullende informatie over de bestandsindeling kunt extraheren.

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

### Zie ook

* class [DiagramTypePackage](../../diagramtypepackage)
* class [DiagramRootPackage](../../diagramrootpackage)
* naamruimte [GroupDocs.Metadata.Formats.Document](../../diagramrootpackage)
* montage [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
