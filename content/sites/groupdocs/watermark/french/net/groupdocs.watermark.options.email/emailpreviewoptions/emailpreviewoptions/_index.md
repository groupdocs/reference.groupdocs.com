---
title: EmailPreviewOptions
second_title: Référence de l'API GroupDocs.Watermark pour .NET
description: Initialise une nouvelle instance duEmailPreviewOptionsgroupdocs.watermark.options.email/emailpreviewoptions classe provoquant la fermeture du flux de sortie.
type: docs
weight: 10
url: /fr/net/groupdocs.watermark.options.email/emailpreviewoptions/emailpreviewoptions/
---
## EmailPreviewOptions(CreatePageStream) {#constructor}

Initialise une nouvelle instance du[`EmailPreviewOptions`](../../emailpreviewoptions) classe provoquant la fermeture du flux de sortie.

```csharp
public EmailPreviewOptions(CreatePageStream createPageStream)
```

| Paramètre | Taper | La description |
| --- | --- | --- |
| createPageStream | CreatePageStream | Crée un flux pour un aperçu de page spécifique. |

### Voir également

* delegate [CreatePageStream](../../../groupdocs.watermark.options/createpagestream)
* class [EmailPreviewOptions](../../emailpreviewoptions)
* espace de noms [GroupDocs.Watermark.Options.Email](../../emailpreviewoptions)
* Assemblée [GroupDocs.Watermark](../../../)

---

## EmailPreviewOptions(CreatePageStream, ReleasePageStream) {#constructor_1}

Initialise une nouvelle instance de[`EmailPreviewOptions`](../../emailpreviewoptions) classe provoquant le retour du flux de sortie au client pour une utilisation ultérieure.

```csharp
public EmailPreviewOptions(CreatePageStream createPageStream, ReleasePageStream releasePageStream)
```

| Paramètre | Taper | La description |
| --- | --- | --- |
| createPageStream | CreatePageStream | Crée un flux pour un aperçu de page spécifique. |
| releasePageStream | ReleasePageStream | Notifie que la génération de l'aperçu de la page est terminée et obtient le flux de sortie. |

### Voir également

* delegate [CreatePageStream](../../../groupdocs.watermark.options/createpagestream)
* delegate [ReleasePageStream](../../../groupdocs.watermark.options/releasepagestream)
* class [EmailPreviewOptions](../../emailpreviewoptions)
* espace de noms [GroupDocs.Watermark.Options.Email](../../emailpreviewoptions)
* Assemblée [GroupDocs.Watermark](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
