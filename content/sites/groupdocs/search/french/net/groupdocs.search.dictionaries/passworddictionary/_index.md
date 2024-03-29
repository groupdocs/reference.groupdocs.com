---
title: PasswordDictionary
second_title: Référence de l'API GroupDocs.Search pour .NET
description: Représente un dictionnaire de mots de passe de document.
type: docs
weight: 460
url: /fr/net/groupdocs.search.dictionaries/passworddictionary/
---
## PasswordDictionary class

Représente un dictionnaire de mots de passe de document.

```csharp
public class PasswordDictionary : DictionaryBase, IEnumerable<string>
```

## Propriétés

| Nom | La description |
| --- | --- |
| [Count](../../groupdocs.search.dictionaries/passworddictionary/count) { get; } | Obtient le nombre d'éléments contenus dans le dictionnaire. |

## Méthodes

| Nom | La description |
| --- | --- |
| [Add](../../groupdocs.search.dictionaries/passworddictionary/add)(string, string) | Ajoute un mot de passe pour un document au dictionnaire. |
| [Clear](../../groupdocs.search.dictionaries/passworddictionary/clear)() | Supprime tous les mots de passe de ce[`PasswordDictionary`](../passworddictionary) objet. |
| [Contains](../../groupdocs.search.dictionaries/passworddictionary/contains)(string) | Détermine si le dictionnaire contient un mot de passe pour le document spécifié. |
| [ExportDictionary](../../groupdocs.search.dictionaries/dictionarybase/exportdictionary)(string) | Exporte le dictionnaire vers un fichier avec le nom spécifié. |
| [GetEnumerator](../../groupdocs.search.dictionaries/passworddictionary/getenumerator)() | Renvoie un énumérateur qui parcourt la collection. |
| [GetPassword](../../groupdocs.search.dictionaries/passworddictionary/getpassword)(string) | Obtient le mot de passe du fichier. |
| [ImportDictionary](../../groupdocs.search.dictionaries/dictionarybase/importdictionary)(string) | Importe un dictionnaire à partir du fichier spécifié. |
| [Remove](../../groupdocs.search.dictionaries/passworddictionary/remove)(string) | Supprime un mot de passe du document spécifié du dictionnaire. |

### Remarques

**Apprendre encore plus**

* [Indexation de documents protégés par mot de passe](https://docs.groupdocs.com/display/searchnet/Indexing+password+protected+documents)
* [Gestion des mots de passe des documents](https://docs.groupdocs.com/display/searchnet/Document+passwords)

### Voir également

* class [DictionaryBase](../dictionarybase)
* espace de noms [GroupDocs.Search.Dictionaries](../../groupdocs.search.dictionaries)
* Assemblée [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
