---
title: SearchPhaseCompleted
second_title: Référence de l'API GroupDocs.Search pour .NET
description: Se produit lorsque la phase de recherche est terminée.
type: docs
weight: 70
url: /fr/net/groupdocs.search.events/eventhub/searchphasecompleted/
---
## EventHub.SearchPhaseCompleted event

Se produit lorsque la phase de recherche est terminée.

```csharp
public event EventHandler<SearchPhaseEventArgs> SearchPhaseCompleted;
```

### Exemples

L'exemple montre comment utiliser l'événement.

```csharp
string indexFolder = @"c:\MyIndex\";
string documentsFolder = @"c:\MyDocuments\";

// Création d'un index
Index index = new Index(indexFolder);

// Indexation des documents du dossier spécifié
index.Add(documentsFolder);

// S'inscrire à l'événement
index.Events.SearchPhaseCompleted += (sender, args) =>
{
    Console.WriteLine("Search phase: " + args.SearchPhase);
    Console.WriteLine("Words: " + args.Words.Length);
};

SearchOptions options = new SearchOptions();
options.UseSynonymSearch = true;
options.UseWordFormsSearch = true;
options.FuzzySearch.Enabled = true;
options.UseHomophoneSearch = true;
SearchResult result = index.Search("Einstein", options);
```

### Voir également

* class [SearchPhaseEventArgs](../../searchphaseeventargs)
* class [EventHub](../../eventhub)
* espace de noms [GroupDocs.Search.Events](../../eventhub)
* Assemblée [GroupDocs.Search](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
