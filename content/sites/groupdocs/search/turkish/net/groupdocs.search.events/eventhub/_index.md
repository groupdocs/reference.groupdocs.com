---
title: EventHub
second_title: .NET API Başvurusu için GroupDocs.Search
description: Abone olmak için indeks olayları sağlar.
type: docs
weight: 510
url: /tr/net/groupdocs.search.events/eventhub/
---
## EventHub class

Abone olmak için indeks olayları sağlar.

```csharp
public class EventHub
```

## Olaylar

| İsim | Tanım |
| --- | --- |
| event [ErrorOccurred](../../groupdocs.search.events/eventhub/erroroccurred) | Dizin işlemi sırasında bir hata oluştuğunda oluşur. |
| event [FileIndexing](../../groupdocs.search.events/eventhub/fileindexing) | Bir belge dizine ekleneceği zaman oluşur. |
| event [ImagePreparing](../../groupdocs.search.events/eventhub/imagepreparing) | Bir resim indekslemeye hazırlanırken oluşur. |
| event [OperationFinished](../../groupdocs.search.events/eventhub/operationfinished) | Bir dizin işlemi bittiğinde gerçekleşir. |
| event [OperationProgressChanged](../../groupdocs.search.events/eventhub/operationprogresschanged) | İndeksleme veya güncelleme işleminin ilerlemesi değiştiğinde gerçekleşir. |
| event [PasswordRequired](../../groupdocs.search.events/eventhub/passwordrequired) | Bir belge açmak için parola gerektirdiğinde oluşur. |
| event [SearchPhaseCompleted](../../groupdocs.search.events/eventhub/searchphasecompleted) | Arama aşaması tamamlandığında gerçekleşir. |
| event [StatusChanged](../../groupdocs.search.events/eventhub/statuschanged) | Dizin durumu değiştiğinde gerçekleşir. |

### Notlar

**Daha fazla bilgi edin**

* [Dizin etkinliklerini ara](https://docs.groupdocs.com/display/searchnet/Search+index+events)

### Örnekler

Örnek, arabirimin tipik bir kullanımını gösterir.

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

* ad alanı [GroupDocs.Search.Events](../../groupdocs.search.events)
* toplantı [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
