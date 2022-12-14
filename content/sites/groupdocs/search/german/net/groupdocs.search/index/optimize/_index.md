---
title: Optimize
second_title: GroupDocs.Suche nach .NET-API-Referenz
description: Minimiert die Anzahl der Indexsegmente indem sie miteinander verbunden werden. Dieser Vorgang verbessert die Suchleistung.
type: docs
weight: 210
url: /de/net/groupdocs.search/index/optimize/
---
## Optimize() {#optimize}

Minimiert die Anzahl der Indexsegmente, indem sie miteinander verbunden werden. Dieser Vorgang verbessert die Suchleistung.

```csharp
public void Optimize()
```

### Beispiele

Das Beispiel zeigt, wie Segmente eines Index zusammengeführt werden.

```csharp
string indexFolder = @"c:\MyIndex\";
string documentsFolder1 = @"c:\MyDocuments1\";
string documentsFolder2 = @"c:\MyDocuments2\";
string documentsFolder3 = @"c:\MyDocuments3\";

Index index = new Index(indexFolder); // Index im angegebenen Ordner erstellen

index.Add(documentsFolder1); // Indizierung von Dokumenten aus dem angegebenen Ordner
index.Add(documentsFolder2); // Jeder Aufruf von Add erstellt mindestens ein neues Segment im Index
index.Add(documentsFolder3);

// Segmente des Index zusammenführen
index.Optimize();
```

### Siehe auch

* class [Index](../../index)
* namensraum [GroupDocs.Search](../../index)
* Montage [GroupDocs.Search](../../../)

---

## Optimize(MergeOptions) {#optimize_1}

Minimiert die Anzahl der Indexsegmente, indem sie miteinander verbunden werden. Dieser Vorgang verbessert die Suchleistung.

```csharp
public void Optimize(MergeOptions options)
```

| Parameter | Typ | Beschreibung |
| --- | --- | --- |
| options | MergeOptions | Die Zusammenführungsoptionen. |

### Beispiele

Das Beispiel zeigt, wie Segmente eines Index mit bestimmten Zusammenführungsoptionen zusammengeführt werden.

```csharp
string indexFolder = @"c:\MyIndex\";
string documentsFolder1 = @"c:\MyDocuments1\";
string documentsFolder2 = @"c:\MyDocuments2\";
string documentsFolder3 = @"c:\MyDocuments3\";

Index index = new Index(indexFolder); // Index im angegebenen Ordner erstellen

index.Add(documentsFolder1); // Indizierung von Dokumenten aus dem angegebenen Ordner
index.Add(documentsFolder2); // Jeder Aufruf von Add erstellt mindestens ein neues Segment im Index
index.Add(documentsFolder3);

MergeOptions options = new MergeOptions();
options.IsAsync = true; // Asynchroner Betrieb
options.Cancellation = new Cancellation(); // Stornoobjekt erstellen

// Segmente des Index zusammenführen
index.Optimize(options); // Diese Methode wird zurückgegeben, bevor die Operation abgeschlossen ist

options.Cancellation.CancelAfter(10000); // Festlegen der maximalen Dauer des Vorgangs auf 10 Sekunden
```

### Siehe auch

* class [MergeOptions](../../../groupdocs.search.options/mergeoptions)
* class [Index](../../index)
* namensraum [GroupDocs.Search](../../index)
* Montage [GroupDocs.Search](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
