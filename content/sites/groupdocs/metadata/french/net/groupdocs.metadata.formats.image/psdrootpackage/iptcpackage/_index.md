---
title: IptcPackage
second_title: Référence de l'API GroupDocs.Metadata pour .NET
description: Obtient ou définit le package de métadonnées IPTC.
type: docs
weight: 30
url: /fr/net/groupdocs.metadata.formats.image/psdrootpackage/iptcpackage/
---
## PsdRootPackage.IptcPackage property

Obtient ou définit le package de métadonnées IPTC.

```csharp
public IptcRecordSet IptcPackage { get; set; }
```

### Valeur de la propriété

Le package de métadonnées IPTC.

### Remarques

**Apprendre encore plus**

* [Utilisation des métadonnées IPTC IIM](https://docs.groupdocs.com/display/metadatanet/Working+with+IPTC+IIM+metadata)

### Exemples

Cet exemple montre comment lire les propriétés de base des métadonnées IPTC.

```csharp
using (Metadata metadata = new Metadata(Constants.PsdWithIptc))
{
    var root = metadata.GetRootPackage<PsdRootPackage>();
    if (root.IptcPackage != null)
    {
        if (root.IptcPackage.EnvelopeRecord != null)
        {
            Console.WriteLine(root.IptcPackage.EnvelopeRecord.DateSent);
            Console.WriteLine(root.IptcPackage.EnvelopeRecord.Destination);
            Console.WriteLine(root.IptcPackage.EnvelopeRecord.FileFormat);
            Console.WriteLine(root.IptcPackage.EnvelopeRecord.FileFormatVersion);

            // ...
        }

        if (root.IptcPackage.ApplicationRecord != null)
        {
            Console.WriteLine(root.IptcPackage.ApplicationRecord.Headline);
            Console.WriteLine(root.IptcPackage.ApplicationRecord.ByLine);
            Console.WriteLine(root.IptcPackage.ApplicationRecord.ByLineTitle);
            Console.WriteLine(root.IptcPackage.ApplicationRecord.CaptionAbstract);
            Console.WriteLine(root.IptcPackage.ApplicationRecord.City);
            Console.WriteLine(root.IptcPackage.ApplicationRecord.DateCreated);
            Console.WriteLine(root.IptcPackage.ApplicationRecord.ReleaseDate);

            // ...
        }
    }
}
```

### Voir également

* class [IptcRecordSet](../../../groupdocs.metadata.standards.iptc/iptcrecordset)
* class [PsdRootPackage](../../psdrootpackage)
* espace de noms [GroupDocs.Metadata.Formats.Image](../../psdrootpackage)
* Assemblée [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
