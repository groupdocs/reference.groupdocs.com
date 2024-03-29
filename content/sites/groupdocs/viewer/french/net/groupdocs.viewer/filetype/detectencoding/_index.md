---
title: DetectEncoding
second_title: Référence de l'API GroupDocs.Viewer pour .NET
description: Tente de détecter du texteTXTgroupdocs.viewer/filetype/txt TSVgroupdocs.viewer/filetype/tsv  etCSVgroupdocs.viewer/filetype/csvfichiers encodés par chemin.
type: docs
weight: 2010
url: /fr/net/groupdocs.viewer/filetype/detectencoding/
---
## DetectEncoding(string) {#detectencoding_1}

Tente de détecter du texte[`TXT`](../txt) ,[`TSV`](../tsv) , et[`CSV`](../csv)fichiers encodés par chemin.

```csharp
public static Encoding DetectEncoding(string filePath)
```

| Paramètre | Taper | La description |
| --- | --- | --- |
| filePath | String | Le nom de fichier ou le chemin d'accès au fichier. |

### Return_Value

Encoding ou null en cas d'échec de la détection d'un encodage de fichier.

### Exemples

L'exemple montre comment détecter l'encodage d'un fichier texte.

```csharp
Encoding encoding = FileType.DetectEncoding("message.txt");
```

### Voir également

* class [FileType](../../filetype)
* espace de noms [GroupDocs.Viewer](../../filetype)
* Assemblée [GroupDocs.Viewer](../../../)

---

## DetectEncoding(Stream) {#detectencoding}

Tente de détecter du texte[`TXT`](../txt) ,[`TSV`](../tsv) , et[`CSV`](../csv) encodage de fichier par stream.

```csharp
public static Encoding DetectEncoding(Stream stream)
```

| Paramètre | Taper | La description |
| --- | --- | --- |
| stream | Stream | Le flux de fichiers. |

### Return_Value

Encoding ou null en cas d'échec de la détection d'un encodage de fichier.

### Exemples

L'exemple montre comment détecter l'encodage d'un fichier texte.

```csharp
Stream stream = File.OpenRead("message.txt");
Encoding encoding = FileType.DetectEncoding(stream);
```

### Voir également

* class [FileType](../../filetype)
* espace de noms [GroupDocs.Viewer](../../filetype)
* Assemblée [GroupDocs.Viewer](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->
