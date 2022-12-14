---
title: ErrorOccurred
second_title: .NET API Başvurusu için GroupDocs.Search
description: Dizin işlemi sırasında bir hata oluştuğunda oluşur.
type: docs
weight: 10
url: /tr/net/groupdocs.search.events/eventhub/erroroccurred/
---
## EventHub.ErrorOccurred event

Dizin işlemi sırasında bir hata oluştuğunda oluşur.

```csharp
public event EventHandler<IndexErrorEventArgs> ErrorOccurred;
```

### Örnekler

Örnek, olayın nasıl kullanılacağını gösterir.

```csharp
string indexFolder = @"c:\MyIndex\";
string documentsFolder = @"c:\MyDocuments\";
string query = "Einstein";

// Bir dizin oluşturma
Index index = new Index(indexFolder);

// Etkinliğe abone oluyoruz
index.Events.ErrorOccurred += (sender, args) =>
{
    Console.WriteLine(args.Message);
};

// Belgeleri belirtilen klasörden indeksleme
index.Add(documentsFolder);

// dizinde arama
SearchResult result = index.Search(query);
```

### Ayrıca bakınız

* class [IndexErrorEventArgs](../../indexerroreventargs)
* class [EventHub](../../eventhub)
* ad alanı [GroupDocs.Search.Events](../../eventhub)
* toplantı [GroupDocs.Search](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
