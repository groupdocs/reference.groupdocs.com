---
title: ReleasePageStream
second_title: Référence de l'API GroupDocs.Watermark pour .NET
description: Représente une méthode qui libère le flux créé par leCreatePageStream./createpagestream délégué.
type: docs
weight: 2090
url: /fr/net/groupdocs.watermark.options/releasepagestream/
---
## ReleasePageStream delegate

Représente une méthode qui libère le flux créé par le[`CreatePageStream`](../createpagestream) délégué.

```csharp
public delegate void ReleasePageStream(int pageNumber, Stream pageStream);
```

| Paramètre | Taper | La description |
| --- | --- | --- |
| pageNumber | Int32 | Le numéro de page d'un aperçu de page généré. |
| pageStream | Stream | Le flux contenant l'aperçu de page généré. |

### Voir également

* espace de noms [GroupDocs.Watermark.Options](../../groupdocs.watermark.options)
* Assemblée [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
