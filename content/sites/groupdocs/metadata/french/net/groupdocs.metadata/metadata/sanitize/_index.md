---
title: Sanitize
second_title: Référence de l'API GroupDocs.Metadata pour .NET
description: Supprime les propriétés de métadonnées inscriptibles de tous les packages détectés ou de packages entiers si possible. Lopération est récursive elle affecte donc également tous les packages imbriqués.
type: docs
weight: 100
url: /fr/net/groupdocs.metadata/metadata/sanitize/
---
## Metadata.Sanitize method

Supprime les propriétés de métadonnées inscriptibles de tous les packages détectés ou de packages entiers si possible. L'opération est récursive, elle affecte donc également tous les packages imbriqués.

```csharp
public int Sanitize()
```

### Return_Value

Le nombre de propriétés concernées.

### Remarques

**Apprendre encore plus**

* [Nettoyer les métadonnées](https://docs.groupdocs.com/display/metadatanet/Clean+metadata)

### Exemples

Cet exemple montre comment supprimer tous les packages/propriétés de métadonnées détectés d'un fichier.

```csharp
using (Metadata metadata = new Metadata(Constants.InputPdf))
{
    // Supprimer les packages de métadonnées détectés
    var affected = metadata.Sanitize();
    Console.WriteLine("Properties removed: {0}", affected);

    metadata.Save(Constants.OutputPdf);
}
```

### Voir également

* class [Metadata](../../metadata)
* espace de noms [GroupDocs.Metadata](../../metadata)
* Assemblée [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
