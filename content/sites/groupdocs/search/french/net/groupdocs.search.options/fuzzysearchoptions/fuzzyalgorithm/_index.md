---
title: FuzzyAlgorithm
second_title: Référence de l'API GroupDocs.Search pour .NET
description: Obtient ou définit lalgorithme de recherche floue. Les algorithmes de recherche floue actuellement disponibles sontSimilarityLevelgroupdocs.search.options/similaritylevel etTableDiscreteFunctiongroupdocs.search.options/tablediscretefunction. La valeur par défaut est une instance deSimilarityLevelgroupdocs.search.options/similaritylevel avec une valeur de niveau de similarité de05 .
type: docs
weight: 30
url: /fr/net/groupdocs.search.options/fuzzysearchoptions/fuzzyalgorithm/
---
## FuzzySearchOptions.FuzzyAlgorithm property

Obtient ou définit l'algorithme de recherche floue. Les algorithmes de recherche floue actuellement disponibles sont[`SimilarityLevel`](../../similaritylevel) et[`TableDiscreteFunction`](../../tablediscretefunction). La valeur par défaut est une instance de[`SimilarityLevel`](../../similaritylevel) avec une valeur de niveau de similarité de`0,5` .

```csharp
public FuzzyAlgorithm FuzzyAlgorithm { get; set; }
```

### Valeur de la propriété

L'algorithme de recherche floue.

### Exceptions

| exception | condition |
| --- | --- |
| ArgumentNullException | Jeté quand*value* est`nul`. |

### Exemples

L'exemple montre comment définir l'algorithme de recherche floue.

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

* class [FuzzyAlgorithm](../../fuzzyalgorithm)
* class [FuzzySearchOptions](../../fuzzysearchoptions)
* espace de noms [GroupDocs.Search.Options](../../fuzzysearchoptions)
* Assemblée [GroupDocs.Search](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
