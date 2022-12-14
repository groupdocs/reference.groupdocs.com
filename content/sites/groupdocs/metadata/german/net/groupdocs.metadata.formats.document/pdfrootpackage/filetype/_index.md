---
title: FileType
second_title: GroupDocs.Metadata für .NET-API-Referenz
description: Ruft das DateitypMetadatenpaket ab.
type: docs
weight: 20
url: /de/net/groupdocs.metadata.formats.document/pdfrootpackage/filetype/
---
## PdfRootPackage.FileType property

Ruft das Dateityp-Metadatenpaket ab.

```csharp
public PdfTypePackage FileType { get; }
```

### Eigentumswert

Das Dateityp-Metadatenpaket.

### Beispiele

Dieses Code-Snippet zeigt, wie die PDF-Version eines geladenen Dokuments erkannt und einige zusätzliche Dateiformatinformationen extrahiert werden.

```csharp
using (Metadata metadata = new Metadata(Constants.InputPdf))
{
    var root = metadata.GetRootPackage<PdfRootPackage>();

    Console.WriteLine(root.FileType.FileFormat);
    Console.WriteLine(root.FileType.Version);
    Console.WriteLine(root.FileType.MimeType);
    Console.WriteLine(root.FileType.Extension);
}
```

### Siehe auch

* class [PdfTypePackage](../../pdftypepackage)
* class [PdfRootPackage](../../pdfrootpackage)
* namensraum [GroupDocs.Metadata.Formats.Document](../../pdfrootpackage)
* Montage [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
