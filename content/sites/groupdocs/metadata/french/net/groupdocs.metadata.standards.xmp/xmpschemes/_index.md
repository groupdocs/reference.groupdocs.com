---
title: XmpSchemes
second_title: Référence de l'API GroupDocs.Metadata pour .NET
description: Fournit un accès aux schémas XMP connus.
type: docs
weight: 3560
url: /fr/net/groupdocs.metadata.standards.xmp/xmpschemes/
---
## XmpSchemes class

Fournit un accès aux schémas XMP connus.

```csharp
public sealed class XmpSchemes
```

## Propriétés

| Nom | La description |
| --- | --- |
| [BasicJobTicket](../../groupdocs.metadata.standards.xmp/xmpschemes/basicjobticket) { get; set; } | Obtient ou définit le schéma BasicJobTicket. |
| [CameraRaw](../../groupdocs.metadata.standards.xmp/xmpschemes/cameraraw) { get; set; } | Obtient ou définit le schéma Camera Raw. |
| [DublinCore](../../groupdocs.metadata.standards.xmp/xmpschemes/dublincore) { get; set; } | Obtient ou définit le schéma Dublin Core. |
| [PagedText](../../groupdocs.metadata.standards.xmp/xmpschemes/pagedtext) { get; set; } | Obtient ou définit le schéma PagedText. |
| [Pdf](../../groupdocs.metadata.standards.xmp/xmpschemes/pdf) { get; set; } | Obtient ou définit le schéma PDF. |
| [Photoshop](../../groupdocs.metadata.standards.xmp/xmpschemes/photoshop) { get; set; } | Obtient ou définit le schéma Photoshop. |
| [XmpBasic](../../groupdocs.metadata.standards.xmp/xmpschemes/xmpbasic) { get; set; } | Obtient ou définit le schéma XmpBasic. |
| [XmpDynamicMedia](../../groupdocs.metadata.standards.xmp/xmpschemes/xmpdynamicmedia) { get; set; } | Obtient ou définit le schéma XmpDynamicMedia. |
| [XmpMediaManagement](../../groupdocs.metadata.standards.xmp/xmpschemes/xmpmediamanagement) { get; set; } | Obtient ou définit le schéma XmpMediaManagement. |
| [XmpRightsManagement](../../groupdocs.metadata.standards.xmp/xmpschemes/xmprightsmanagement) { get; set; } | Obtient ou définit le schéma XmpRightsManagement. |

### Exemples

Cet exemple montre comment extraire les métadonnées XMP d'un fichier.

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

            // ...
        }

        if (root.XmpPackage.Schemes.DublinCore != null)
        {
            Console.WriteLine(root.XmpPackage.Schemes.DublinCore.Format);
            Console.WriteLine(root.XmpPackage.Schemes.DublinCore.Coverage);
            Console.WriteLine(root.XmpPackage.Schemes.DublinCore.Identifier);
            Console.WriteLine(root.XmpPackage.Schemes.DublinCore.Source);

            // ...
        }

        if (root.XmpPackage.Schemes.Photoshop != null)
        {
            Console.WriteLine(root.XmpPackage.Schemes.Photoshop.ColorMode);
            Console.WriteLine(root.XmpPackage.Schemes.Photoshop.IccProfile);
            Console.WriteLine(root.XmpPackage.Schemes.Photoshop.Country);
            Console.WriteLine(root.XmpPackage.Schemes.Photoshop.City);
            Console.WriteLine(root.XmpPackage.Schemes.Photoshop.DateCreated);

            // ... 
        }

        // ...
    }
}
```

### Voir également

* espace de noms [GroupDocs.Metadata.Standards.Xmp](../../groupdocs.metadata.standards.xmp)
* Assemblée [GroupDocs.Metadata](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
