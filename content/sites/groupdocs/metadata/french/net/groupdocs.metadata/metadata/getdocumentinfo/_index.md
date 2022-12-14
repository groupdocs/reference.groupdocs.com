---
title: GetDocumentInfo
second_title: Référence de l'API GroupDocs.Metadata pour .NET
description: Obtient des informations communes sur le document chargé.
type: docs
weight: 70
url: /fr/net/groupdocs.metadata/metadata/getdocumentinfo/
---
## Metadata.GetDocumentInfo method

Obtient des informations communes sur le document chargé.

```csharp
public IDocumentInfo GetDocumentInfo()
```

### Return_Value

Un objet représentant des informations de document communes.

### Remarques

**Apprendre encore plus**

* [Obtenir des informations sur les documents](https://docs.groupdocs.com/display/metadatanet/Get+document+info)

### Exemples

Cet exemple montre comment extraire les informations de format de base d'un fichier.

```csharp
using (Metadata metadata = new Metadata(Constants.InputXlsx))
{
    if (metadata.FileFormat != FileFormat.Unknown)
    {
        IDocumentInfo info = metadata.GetDocumentInfo();
        Console.WriteLine("File format: {0}", info.FileType.FileFormat);
        Console.WriteLine("File extension: {0}", info.FileType.Extension);
        Console.WriteLine("MIME Type: {0}", info.FileType.MimeType);
        Console.WriteLine("Number of pages: {0}", info.PageCount);
        Console.WriteLine("Document size: {0} bytes", info.Size);
        Console.WriteLine("Is document encrypted: {0}", info.IsEncrypted);
    }
}
```

### Voir également

* interface [IDocumentInfo](../../../groupdocs.metadata.common/idocumentinfo)
* class [Metadata](../../metadata)
* espace de noms [GroupDocs.Metadata](../../metadata)
* Assemblée [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
