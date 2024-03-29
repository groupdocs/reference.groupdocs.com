---
title: SearchOptions
second_title: Référence de l'API GroupDocs.Search pour .NET
description: Fournit des options pour lopération de recherche.
type: docs
weight: 1040
url: /fr/net/groupdocs.search.options/searchoptions/
---
## SearchOptions class

Fournit des options pour l'opération de recherche.

```csharp
public class SearchOptions
```

## Constructeurs

| Nom | La description |
| --- | --- |
| [SearchOptions](searchoptions)() | Initialise une nouvelle instance du[`SearchOptions`](../searchoptions) classe. |

## Propriétés

| Nom | La description |
| --- | --- |
| [Cancellation](../../groupdocs.search.options/searchoptions/cancellation) { get; set; } | Obtient ou définit l'objet d'annulation d'opération. La valeur par défaut est`nul` . |
| [DateFormats](../../groupdocs.search.options/searchoptions/dateformats) { get; } | Obtient la collection de formats de date pour la recherche de plage de dates. Les formats de date par défaut sont 'dd.MM.yyyy', 'MM/dd/yyyy' et 'yyyy-MM-dd'. |
| [FuzzySearch](../../groupdocs.search.options/searchoptions/fuzzysearch) { get; } | Obtient les options de recherche floue. |
| [IsChunkSearch](../../groupdocs.search.options/searchoptions/ischunksearch) { get; set; } | Obtient ou définit l'indicateur de recherche par morceaux. La valeur par défaut est`FAUX` . |
| [KeyboardLayoutCorrector](../../groupdocs.search.options/searchoptions/keyboardlayoutcorrector) { get; } | Obtient les options du correcteur de disposition du clavier. |
| [MaxOccurrenceCountPerTerm](../../groupdocs.search.options/searchoptions/maxoccurrencecountperterm) { get; set; } | Obtient ou définit le nombre maximal d'occurrences de chaque terme dans une requête de recherche. La valeur par défaut est`100000` . |
| [MaxTotalOccurrenceCount](../../groupdocs.search.options/searchoptions/maxtotaloccurrencecount) { get; set; } | Obtient ou définit le nombre total maximal d'occurrences de tous les termes dans une requête de recherche. La valeur par défaut est`500000` . |
| [SearchDocumentFilter](../../groupdocs.search.options/searchoptions/searchdocumentfilter) { get; set; } | Obtient ou définit le filtre de document de recherche. [`SearchDocumentFilter`](./searchdocumentfilter) fonctionne sur la logique d'inclusion. Utilisation[`SearchDocumentFilter`](../searchdocumentfilter) classe pour la création d'instances de filtre de document de recherche. La valeur par défaut est`nul` , ce qui signifie que tous les documents trouvés seront renvoyés. |
| [SpellingCorrector](../../groupdocs.search.options/searchoptions/spellingcorrector) { get; } | Obtient les options du correcteur orthographique. |
| [UseCaseSensitiveSearch](../../groupdocs.search.options/searchoptions/usecasesensitivesearch) { get; set; } | Obtient ou définit l'indicateur de recherche sensible à la casse. La valeur par défaut est`FAUX` . |
| [UseHomophoneSearch](../../groupdocs.search.options/searchoptions/usehomophonesearch) { get; set; } | Obtient ou définit l'indicateur d'utilisation des homophones dans la recherche. La valeur par défaut est`FAUX` . |
| [UseSynonymSearch](../../groupdocs.search.options/searchoptions/usesynonymsearch) { get; set; } | Obtient ou définit l'indicateur d'utilisation des synonymes dans la recherche. La valeur par défaut est`FAUX` . |
| [UseWordFormsSearch](../../groupdocs.search.options/searchoptions/usewordformssearch) { get; set; } | Obtient ou définit l'indicateur d'utilisation de différentes formes de mots dans la recherche. La valeur par défaut est`FAUX` . |

### Remarques

**Apprendre encore plus**

* [Options de recherche](https://docs.groupdocs.com/display/searchnet/Search+options)

### Voir également

* espace de noms [GroupDocs.Search.Options](../../groupdocs.search.options)
* Assemblée [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
