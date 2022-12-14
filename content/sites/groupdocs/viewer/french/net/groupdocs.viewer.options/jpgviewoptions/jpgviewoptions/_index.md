---
title: JpgViewOptions
second_title: Référence de l'API GroupDocs.Viewer pour .NET
description: Initialise la nouvelle instance deJpgViewOptionsgroupdocs.viewer.options/jpgviewoptions classe.
type: docs
weight: 10
url: /fr/net/groupdocs.viewer.options/jpgviewoptions/jpgviewoptions/
---
## JpgViewOptions(CreatePageStream) {#constructor_1}

Initialise la nouvelle instance de[`JpgViewOptions`](../../jpgviewoptions) classe.

```csharp
public JpgViewOptions(CreatePageStream createPageStream)
```

| Paramètre | Taper | La description |
| --- | --- | --- |
| createPageStream | CreatePageStream | La méthode qui instancie le flux utilisé pour écrire les données de la page de sortie. |

### Exceptions

| exception | condition |
| --- | --- |
| ArgumentNullException | Jeté quand*createPageStream* est nul. |

### Voir également

* delegate [CreatePageStream](../../../groupdocs.viewer.interfaces/createpagestream)
* class [JpgViewOptions](../../jpgviewoptions)
* espace de noms [GroupDocs.Viewer.Options](../../jpgviewoptions)
* Assemblée [GroupDocs.Viewer](../../../)

---

## JpgViewOptions(CreatePageStream, ReleasePageStream) {#constructor_2}

Initialise la nouvelle instance de[`JpgViewOptions`](../../jpgviewoptions) classe.

```csharp
public JpgViewOptions(CreatePageStream createPageStream, ReleasePageStream releasePageStream)
```

| Paramètre | Taper | La description |
| --- | --- | --- |
| createPageStream | CreatePageStream | La méthode qui instancie le flux utilisé pour écrire les données de la page de sortie. |
| releasePageStream | ReleasePageStream | La méthode qui libère le flux créé par la méthode affectée au délégué qui est passé à*createPageStream* paramètre. |

### Exceptions

| exception | condition |
| --- | --- |
| ArgumentNullException | Jeté quand*createPageStream* est nul. |
| ArgumentNullException | Jeté quand*releasePageStream* est nul. |

### Voir également

* delegate [CreatePageStream](../../../groupdocs.viewer.interfaces/createpagestream)
* delegate [ReleasePageStream](../../../groupdocs.viewer.interfaces/releasepagestream)
* class [JpgViewOptions](../../jpgviewoptions)
* espace de noms [GroupDocs.Viewer.Options](../../jpgviewoptions)
* Assemblée [GroupDocs.Viewer](../../../)

---

## JpgViewOptions(IPageStreamFactory) {#constructor_3}

Initialise la nouvelle instance de[`JpgViewOptions`](../../jpgviewoptions) classe.

```csharp
public JpgViewOptions(IPageStreamFactory pageStreamFactory)
```

| Paramètre | Taper | La description |
| --- | --- | --- |
| pageStreamFactory | IPageStreamFactory | La fabrique qui implémente les méthodes de création et de publication du flux de page de sortie. |

### Exceptions

| exception | condition |
| --- | --- |
| ArgumentNullException | Jeté quand*pageStreamFactory* est nul. |

### Voir également

* interface [IPageStreamFactory](../../../groupdocs.viewer.interfaces/ipagestreamfactory)
* class [JpgViewOptions](../../jpgviewoptions)
* espace de noms [GroupDocs.Viewer.Options](../../jpgviewoptions)
* Assemblée [GroupDocs.Viewer](../../../)

---

## JpgViewOptions() {#constructor}

Initialise la nouvelle instance de[`JpgViewOptions`](../../jpgviewoptions) classe.

```csharp
public JpgViewOptions()
```

### Remarques

Ce constructeur initialise une nouvelle instance de[`JpgViewOptions`](../../jpgviewoptions) avec "p_{0}.jpg" comme format de chemin de fichier pour les fichiers de sortie. Les fichiers de sortie seront placés dans le répertoire de travail actuel de l'application.

### Voir également

* class [JpgViewOptions](../../jpgviewoptions)
* espace de noms [GroupDocs.Viewer.Options](../../jpgviewoptions)
* Assemblée [GroupDocs.Viewer](../../../)

---

## JpgViewOptions(string) {#constructor_4}

Initialise la nouvelle instance de[`JpgViewOptions`](../../jpgviewoptions) classe.

```csharp
public JpgViewOptions(string filePathFormat)
```

| Paramètre | Taper | La description |
| --- | --- | --- |
| filePathFormat | String | Le format du chemin du fichier, par exemple 'page_{0}.jpg'. |

### Exceptions

| exception | condition |
| --- | --- |
| ArgumentException | Jeté quand*filePathFormat* est nul ou vide. |

### Voir également

* class [JpgViewOptions](../../jpgviewoptions)
* espace de noms [GroupDocs.Viewer.Options](../../jpgviewoptions)
* Assemblée [GroupDocs.Viewer](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->
