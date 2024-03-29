---
title: Word
second_title: Référence de l'API GroupDocs.Viewer pour .NET
description: Initialise la nouvelle instance deWordgroupdocs.viewer.results/word classe.
type: docs
weight: 10
url: /fr/net/groupdocs.viewer.results/word/word/
---
## Word() {#constructor}

Initialise la nouvelle instance de[`Word`](../../word) classe.

```csharp
public Word()
```

### Voir également

* class [Word](../../word)
* espace de noms [GroupDocs.Viewer.Results](../../word)
* Assemblée [GroupDocs.Viewer](../../../)

---

## Word(string, double, double, double, double, List&lt;Character&gt;) {#constructor_1}

Initialise la nouvelle instance de[`Word`](../../word) classe.

```csharp
public Word(string word, double x, double y, double width, double height, 
    List<Character> characters)
```

| Paramètre | Taper | La description |
| --- | --- | --- |
| word | String | Le mot. |
| x | Double | Coordonnée X du point supérieur gauche de la mise en page où commence le rectangle contenant le mot. |
| y | Double | Coordonnée Y du point le plus haut à gauche de la mise en page où commence le rectangle contenant le mot. |
| width | Double | La largeur du rectangle qui contient le mot. |
| height | Double | La hauteur du rectangle qui contient le mot. |
| characters | List`1 | Les caractères contenus par le mot. |

### Exceptions

| exception | condition |
| --- | --- |
| ArgumentException | Jeté quand*word* est nul ou vide. |
| ArgumentNullException | Jeté quand*characters* est nul. |

### Voir également

* class [Character](../../character)
* class [Word](../../word)
* espace de noms [GroupDocs.Viewer.Results](../../word)
* Assemblée [GroupDocs.Viewer](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->
