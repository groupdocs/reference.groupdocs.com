---
title: ExportImagesAsBase64
second_title: Référence de l'API GroupDocs.Editor pour .NET
description: Spécifie si les images sont enregistrées au format Base64 dans le fichier de sortie. La valeur par défaut estFAUX .
type: docs
weight: 20
url: /fr/net/groupdocs.editor.options/markdownsaveoptions/exportimagesasbase64/
---
## MarkdownSaveOptions.ExportImagesAsBase64 property

Spécifie si les images sont enregistrées au format Base64 dans le fichier de sortie. La valeur par défaut est`FAUX` .

```csharp
public bool ExportImagesAsBase64 { get; set; }
```

### Remarques

Lorsque cette propriété est définie sur`vrai` les données d'images sont exportées directement dans les éléments d'image the ![]() et des fichiers séparés ne sont pas créés. Cette propriété, si elle est définie sur`vrai` , a la priorité la plus élevée que[`ImagesFolder`](../imagesfolder) propriété.

### Voir également

* class [MarkdownSaveOptions](../../markdownsaveoptions)
* espace de noms [GroupDocs.Editor.Options](../../markdownsaveoptions)
* Assemblée [GroupDocs.Editor](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
