---
title: TableDiscreteFunction
second_title: Référence de l'API GroupDocs.Search pour .NET
description: Représente lalgorithme de recherche floue qui contient les correspondances entre les longueurs de mot et le nombre derreurs autorisées. Cet algorithme peut être spécifié par un tableau de valeurs de sortie ou par une fonction détape.
type: docs
weight: 1090
url: /fr/net/groupdocs.search.options/tablediscretefunction/
---
## TableDiscreteFunction class

Représente l'algorithme de recherche floue qui contient les correspondances entre les longueurs de mot et le nombre d'erreurs autorisées. Cet algorithme peut être spécifié par un tableau de valeurs de sortie ou par une fonction d'étape.

```csharp
public class TableDiscreteFunction : FuzzyAlgorithm
```

## Constructeurs

| Nom | La description |
| --- | --- |
| [TableDiscreteFunction](tablediscretefunction#constructor_1)(int, int[]) | Initialise une nouvelle instance du[`TableDiscreteFunction`](../tablediscretefunction) classe. |
| [TableDiscreteFunction](tablediscretefunction#constructor)(int, params Step[]) | Initialise une nouvelle instance du[`TableDiscreteFunction`](../tablediscretefunction) classe. |

## Méthodes

| Nom | La description |
| --- | --- |
| override [GetMaxMistakeCount](../../groupdocs.search.options/tablediscretefunction/getmaxmistakecount)(int) | Obtient un nombre maximal autorisé d'erreurs pour la longueur de terme spécifiée. |
| override [GetSimilarityLevel](../../groupdocs.search.options/tablediscretefunction/getsimilaritylevel)(int) | Obtient un niveau de similarité pour la longueur de terme spécifiée. |

### Remarques

**Apprendre encore plus**

* [Recherche floue](https://docs.groupdocs.com/display/searchnet/Fuzzy+search)

### Exemples

L'exemple montre une utilisation typique de la classe.

```csharp
string indexFolder = @"c:\MyIndex\";
string documentsFolder = @"c:\MyDocuments\";
string query = "Einstein";

Index index = new Index(indexFolder); // Création d'un index dans le dossier spécifié
index.Add(documentsFolder); // Indexation des documents du dossier spécifié

SearchOptions options = new SearchOptions();
options.FuzzySearch.Enabled = true; // Activation de la recherche floue
options.FuzzySearch.FuzzyAlgorithm = new TableDiscreteFunction(1, new Step(5, 2), new Step(8, 3)); // Création de l'algorithme de recherche floue
// Cette fonction spécifie 1 comme nombre maximum d'erreurs pour les mots de 1 à 4 caractères.
// Il spécifie 2 comme nombre maximum d'erreurs pour les mots de 5 à 7 caractères.
// Il spécifie 3 comme nombre maximum d'erreurs pour les mots de 8 caractères et plus.

SearchResult result = index.Search(query, options); // Recherche dans l'index
```

### Voir également

* class [FuzzyAlgorithm](../fuzzyalgorithm)
* espace de noms [GroupDocs.Search.Options](../../groupdocs.search.options)
* Assemblée [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
