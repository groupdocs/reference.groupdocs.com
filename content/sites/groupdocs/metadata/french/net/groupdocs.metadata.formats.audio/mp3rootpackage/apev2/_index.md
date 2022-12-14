---
title: ApeV2
second_title: Référence de l'API GroupDocs.Metadata pour .NET
description: Obtient les métadonnées APE v2.
type: docs
weight: 10
url: /fr/net/groupdocs.metadata.formats.audio/mp3rootpackage/apev2/
---
## MP3RootPackage.ApeV2 property

Obtient les métadonnées APE v2.

```csharp
public ApePackage ApeV2 { get; }
```

### Valeur de la propriété

Les métadonnées APE v2.

### Exemples

Cet exemple montre comment lire la balise APEv2 dans un fichier MP3.

```csharp
using (Metadata metadata = new Metadata(Constants.MP3WithApe))
{
    var root = metadata.GetRootPackage<MP3RootPackage>();

    if (root.ApeV2 != null)
    {
        Console.WriteLine(root.ApeV2.Album);
        Console.WriteLine(root.ApeV2.Title);
        Console.WriteLine(root.ApeV2.Artist);
        Console.WriteLine(root.ApeV2.Composer);
        Console.WriteLine(root.ApeV2.Copyright);
        Console.WriteLine(root.ApeV2.Genre);
        Console.WriteLine(root.ApeV2.Language);

        // ...
    }
}
```

### Voir également

* class [ApePackage](../../apepackage)
* class [MP3RootPackage](../../mp3rootpackage)
* espace de noms [GroupDocs.Metadata.Formats.Audio](../../mp3rootpackage)
* Assemblée [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
