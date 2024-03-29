---
title: IXmp
second_title: Riferimento API GroupDocs.Metadata per .NET
description: Definisce le operazioni di base destinate a funzionare con i metadati XMP.
type: docs
weight: 3040
url: /it/net/groupdocs.metadata.standards.xmp/ixmp/
---
## IXmp interface

Definisce le operazioni di base destinate a funzionare con i metadati XMP.

```csharp
public interface IXmp
```

## Proprietà

| Nome | Descrizione |
| --- | --- |
| [XmpPackage](../../groupdocs.metadata.standards.xmp/ixmp/xmppackage) { get; set; } | Ottiene o imposta il pacchetto di metadati XMP. |

### Osservazioni

**Saperne di più**

* [Lavorare con i metadati XMP](https://docs.groupdocs.com/display/metadatanet/Working+with+XMP+metadata)

### Esempi

Questo esempio mostra come estrarre i metadati XMP da un file.

```csharp
using (Metadata metadata = new Metadata(Constants.PngWithXmp))
{
    IXmp root = metadata.GetRootPackage() as IXmp;
    if (root != null && root.XmpPackage != null)
    {
        if (root.XmpPackage.Schemes.XmpBasic != null)
        {
            Console.WriteLine(root.XmpPackage.Schemes.XmpBasic.CreatorTool);
            Console.WriteLine(root.XmpPackage.Schemes.XmpBasic.CreateDate);
            Console.WriteLine(root.XmpPackage.Schemes.XmpBasic.ModifyDate);
            Console.WriteLine(root.XmpPackage.Schemes.XmpBasic.Label);
            Console.WriteLine(root.XmpPackage.Schemes.XmpBasic.Nickname);

            //...
        }

        if (root.XmpPackage.Schemes.DublinCore != null)
        {
            Console.WriteLine(root.XmpPackage.Schemes.DublinCore.Format);
            Console.WriteLine(root.XmpPackage.Schemes.DublinCore.Coverage);
            Console.WriteLine(root.XmpPackage.Schemes.DublinCore.Identifier);
            Console.WriteLine(root.XmpPackage.Schemes.DublinCore.Source);

            //...
        }

        if (root.XmpPackage.Schemes.Photoshop != null)
        {
            Console.WriteLine(root.XmpPackage.Schemes.Photoshop.ColorMode);
            Console.WriteLine(root.XmpPackage.Schemes.Photoshop.IccProfile);
            Console.WriteLine(root.XmpPackage.Schemes.Photoshop.Country);
            Console.WriteLine(root.XmpPackage.Schemes.Photoshop.City);
            Console.WriteLine(root.XmpPackage.Schemes.Photoshop.DateCreated);

            //... 
        }

        //...
    }
}
```

### Guarda anche

* spazio dei nomi [GroupDocs.Metadata.Standards.Xmp](../../groupdocs.metadata.standards.xmp)
* assemblea [GroupDocs.Metadata](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
