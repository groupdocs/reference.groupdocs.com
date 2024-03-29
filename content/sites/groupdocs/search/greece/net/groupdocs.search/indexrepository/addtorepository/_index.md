---
title: AddToRepository
second_title: GroupDocs.Αναζήτηση για αναφορά API .NET
description: Προσθέτει ένα ευρετήριο στο αποθετήριο ευρετηρίου.
type: docs
weight: 40
url: /el/net/groupdocs.search/indexrepository/addtorepository/
---
## AddToRepository(Index) {#addtorepository}

Προσθέτει ένα ευρετήριο στο αποθετήριο ευρετηρίου.

```csharp
public void AddToRepository(Index index)
```

| Παράμετρος | Τύπος | Περιγραφή |
| --- | --- | --- |
| index | Index | Το ευρετήριο για προσθήκη. |

### Παραδείγματα

Το παράδειγμα δείχνει πώς να προσθέσετε ένα ευρετήριο στο αποθετήριο ευρετηρίου.

```csharp
Index index = new Index();

IndexRepository indexRepository = new IndexRepository();

indexRepository.AddToRepository(index);
```

### Δείτε επίσης

* class [Index](../../index)
* class [IndexRepository](../../indexrepository)
* χώρος ονομάτων [GroupDocs.Search](../../indexrepository)
* συνέλευση [GroupDocs.Search](../../../)

---

## AddToRepository(string) {#addtorepository_1}

Ανοίγει και προσθέτει ένα ευρετήριο στο αποθετήριο ευρετηρίου.

```csharp
public void AddToRepository(string indexFolder)
```

| Παράμετρος | Τύπος | Περιγραφή |
| --- | --- | --- |
| indexFolder | String | Ο φάκελος ευρετηρίου. |

### Παραδείγματα

Το παράδειγμα δείχνει πώς να προσθέσετε ένα ευρετήριο στο αποθετήριο ευρετηρίου.

```csharp
string indexFolder = @"c:\MyIndex\";

IndexRepository indexRepository = new IndexRepository();

indexRepository.AddToRepository(indexFolder);
```

### Δείτε επίσης

* class [IndexRepository](../../indexrepository)
* χώρος ονομάτων [GroupDocs.Search](../../indexrepository)
* συνέλευση [GroupDocs.Search](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
