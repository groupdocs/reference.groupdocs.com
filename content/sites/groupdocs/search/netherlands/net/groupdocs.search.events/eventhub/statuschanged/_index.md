---
title: StatusChanged
second_title: GroupDocs. Zoek naar .NET API-referentie
description: Treedt op wanneer de indexstatus verandert.
type: docs
weight: 80
url: /nl/net/groupdocs.search.events/eventhub/statuschanged/
---
## EventHub.StatusChanged event

Treedt op wanneer de indexstatus verandert.

```csharp
public event EventHandler<BaseIndexEventArgs> StatusChanged;
```

### Voorbeelden

Het voorbeeld laat zien hoe u de gebeurtenis gebruikt.

```csharp
string indexFolder = @"c:\MyIndex\";
string documentsFolder = @"c:\MyDocuments\";

// Een index maken
Index index = new Index(indexFolder);

// Aanmelden voor het evenement
index.Events.StatusChanged += (sender, args) =>
{
    if (args.Status != IndexStatus.InProgress)
    {
        // Een melding van de voltooiing van de bewerking zou hier moeten zijn
    }
};

// De vlag instellen voor asynchrone indexering
IndexingOptions options = new IndexingOptions();
options.IsAsync = true;

// Asynchrone indexering van documenten uit de opgegeven map
// De methode wordt beëindigd voordat de bewerking is voltooid
index.Add(documentsFolder, options);
```

### Zie ook

* class [BaseIndexEventArgs](../../baseindexeventargs)
* class [EventHub](../../eventhub)
* naamruimte [GroupDocs.Search.Events](../../eventhub)
* montage [GroupDocs.Search](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
