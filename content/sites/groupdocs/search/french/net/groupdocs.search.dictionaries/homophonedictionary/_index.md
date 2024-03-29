---
title: HomophoneDictionary
second_title: Référence de l'API GroupDocs.Search pour .NET
description: Représente un dictionnaire dhomophones hétérographiques.
type: docs
weight: 440
url: /fr/net/groupdocs.search.dictionaries/homophonedictionary/
---
## HomophoneDictionary class

Représente un dictionnaire d'homophones hétérographiques.

```csharp
public class HomophoneDictionary : DictionaryBase, IEnumerable<string>
```

## Propriétés

| Nom | La description |
| --- | --- |
| [Count](../../groupdocs.search.dictionaries/homophonedictionary/count) { get; } | Obtient le nombre de mots contenus dans ce[`HomophoneDictionary`](../homophonedictionary) . |

## Méthodes

| Nom | La description |
| --- | --- |
| [AddRange](../../groupdocs.search.dictionaries/homophonedictionary/addrange#addrange)(IEnumerable&lt;string[]&gt;) | Ajoute la collection spécifiée de groupes d'homophones à cette instance du[`HomophoneDictionary`](../homophonedictionary) . |
| [AddRange](../../groupdocs.search.dictionaries/homophonedictionary/addrange#addrange_1)(string[][]) | Ajoute la collection spécifiée de groupes d'homophones à cette instance du[`HomophoneDictionary`](../homophonedictionary) . |
| [Clear](../../groupdocs.search.dictionaries/homophonedictionary/clear)() | Supprime tous les mots d'un[`HomophoneDictionary`](../homophonedictionary) objet. |
| [ExportDictionary](../../groupdocs.search.dictionaries/dictionarybase/exportdictionary)(string) | Exporte le dictionnaire vers un fichier avec le nom spécifié. |
| [GetAllHomophoneGroups](../../groupdocs.search.dictionaries/homophonedictionary/getallhomophonegroups)() | Obtient tous les groupes d'homophones contenus dans ce dictionnaire. |
| [GetEnumerator](../../groupdocs.search.dictionaries/homophonedictionary/getenumerator)() | Renvoie un énumérateur qui parcourt la collection. |
| [GetHomophoneGroups](../../groupdocs.search.dictionaries/homophonedictionary/gethomophonegroups)(string) | Obtient tous les groupes d'homophones auxquels appartient le mot spécifié. |
| [GetHomophones](../../groupdocs.search.dictionaries/homophonedictionary/gethomophones)(string) | Obtient les homophones pour le mot spécifié. Le tableau résultant ne contient pas le mot d'origine. |
| [ImportDictionary](../../groupdocs.search.dictionaries/dictionarybase/importdictionary)(string) | Importe un dictionnaire à partir du fichier spécifié. |

### Remarques

**Apprendre encore plus**

* [Recherche d'homophones](https://docs.groupdocs.com/display/searchnet/Homophone+search)
* [Gestion du dictionnaire d'homophones](https://docs.groupdocs.com/display/searchnet/Homophone+dictionary)

### Voir également

* class [DictionaryBase](../dictionarybase)
* espace de noms [GroupDocs.Search.Dictionaries](../../groupdocs.search.dictionaries)
* Assemblée [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
