---
title: AsfExtendedStreamPropertyFlags
second_title: Référence de l'API GroupDocs.Metadata pour .NET
description: Définit les indicateurs de propriété de flux étendu ASF.
type: docs
weight: 2300
url: /fr/net/groupdocs.metadata.formats.video/asfextendedstreampropertyflags/
---
## AsfExtendedStreamPropertyFlags enumeration

Définit les indicateurs de propriété de flux étendu ASF.

```csharp
[Flags]
public enum AsfExtendedStreamPropertyFlags : uint
```

### Valeurs

| Nom | Évaluer | La description |
| --- | --- | --- |
| Reliable | `1` | Ce flux multimédia numérique, s'il est envoyé sur un réseau, doit être acheminé via un mécanisme de transport de communication de données fiable. |
| Seekable | `2` | Cet indicateur doit être défini uniquement si le flux est recherchable. |
| NoCleanpoints | `2` | Le flux ne contient aucun point de nettoyage. |
| ResendLiveCleanpoints | `2` | Un flux est joint au milieu de la transmission, toutes les informations depuis le point de nettoyage le plus récent jusqu'à l'heure actuelle doivent être envoyées avant que le flux normal ne commence à l'heure actuelle. |

### Voir également

* espace de noms [GroupDocs.Metadata.Formats.Video](../../groupdocs.metadata.formats.video)
* Assemblée [GroupDocs.Metadata](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
