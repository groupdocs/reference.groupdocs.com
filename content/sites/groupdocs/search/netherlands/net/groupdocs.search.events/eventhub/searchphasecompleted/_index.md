---
title: SearchPhaseCompleted
second_title: GroupDocs. Zoek naar .NET API-referentie
description: Treedt op wanneer de zoekfase is voltooid.
type: docs
weight: 70
url: /nl/net/groupdocs.search.events/eventhub/searchphasecompleted/
---
## EventHub.SearchPhaseCompleted event

Treedt op wanneer de zoekfase is voltooid.

```csharp
public event EventHandler<SearchPhaseEventArgs> SearchPhaseCompleted;
```

### Voorbeelden

Het voorbeeld laat zien hoe u de gebeurtenis gebruikt.

```csharp
string indexFolder = @"c:\MyIndex\";
string documentsFolder = @"c:\MyDocuments\";

// Een index maken
Index index = new Index(indexFolder);

// Documenten uit de opgegeven map indexeren
index.Add(documentsFolder);

// Aanmelden voor het evenement
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

### Zie ook

* class [SearchPhaseEventArgs](../../searchphaseeventargs)
* class [EventHub](../../eventhub)
* naamruimte [GroupDocs.Search.Events](../../eventhub)
* montage [GroupDocs.Search](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
