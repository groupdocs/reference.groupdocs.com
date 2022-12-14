---
title: SetProperties
second_title: Référence de l'API GroupDocs.Metadata pour .NET
description: Définit les propriétés de métadonnées connues satisfaisant le prédicat spécifié. Lopération est récursive et affecte donc également tous les packages imbriqués. Cette méthode est une combinaison deAddPropertiesgroupdocs.metadata/metadata/addproperties etUpdatePropertiesgroupdocs.metadata/metadata/updateproperties . Si une propriété existante satisfait le prédicat sa valeur est mise à jour. Sil manque une propriété connue dans un package qui satisfait le prédicat elle est ajoutée au package.
type: docs
weight: 120
url: /fr/net/groupdocs.metadata/metadata/setproperties/
---
## Metadata.SetProperties method

Définit les propriétés de métadonnées connues satisfaisant le prédicat spécifié. L'opération est récursive et affecte donc également tous les packages imbriqués. Cette méthode est une combinaison de[`AddProperties`](../addproperties) et[`UpdateProperties`](../updateproperties) . Si une propriété existante satisfait le prédicat, sa valeur est mise à jour. S'il manque une propriété connue dans un package qui satisfait le prédicat, elle est ajoutée au package.

```csharp
public int SetProperties(Func<MetadataProperty, bool> predicate, PropertyValue value)
```

| Paramètre | Taper | La description |
| --- | --- | --- |
| predicate | Func`2 | Une fonction pour tester chaque propriété de métadonnées pour une condition. |
| value | PropertyValue | Une nouvelle valeur pour les propriétés filtrées. |

### Return_Value

Le nombre de propriétés concernées.

### Remarques

Veuillez noter que GroupDocs.Metadata vérifie implicitement le type de chaque propriété filtrée. Il est impossible de définir une propriété avec une valeur ayant un type inapproprié.

**Apprendre encore plus**

* [Définir les propriétés des métadonnées](https://docs.groupdocs.com/display/metadatanet/Set+metadata+properties)

### Exemples

Cet exemple montre comment définir des propriétés de métadonnées spécifiques à l'aide de différents critères.

```csharp
using (Metadata metadata = new Metadata(Constants.InputVsdx))
{
    // Définissez la valeur de chaque propriété qui satisfait le prédicat :
    // la propriété contient la date/heure à laquelle le document a été créé OU modifié
    var affected = metadata.SetProperties(
    p => p.Tags.Contains(Tags.Time.Created) || p.Tags.Contains(Tags.Time.Modified),
    new PropertyValue(DateTime.Now));

    Console.WriteLine("Properties set: {0}", affected);

    metadata.Save(Constants.OutputVsdx);
}
```

### Voir également

* delegate [Func&lt;T,TResult&gt;](../../../groupdocs.metadata.common/func-2)
* class [MetadataProperty](../../../groupdocs.metadata.common/metadataproperty)
* class [PropertyValue](../../../groupdocs.metadata.common/propertyvalue)
* class [Metadata](../../metadata)
* espace de noms [GroupDocs.Metadata](../../metadata)
* Assemblée [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
