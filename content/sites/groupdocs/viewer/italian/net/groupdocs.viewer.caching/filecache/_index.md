---
title: FileCache
second_title: Riferimento API GroupDocs.Viewer per .NET
description: Rappresenta una cache su disco locale.
type: docs
weight: 20
url: /it/net/groupdocs.viewer.caching/filecache/
---
## FileCache class

Rappresenta una cache su disco locale.

```csharp
public class FileCache : ICache
```

## Costruttori

| Nome | Descrizione |
| --- | --- |
| [FileCache](filecache#constructor)(string) | Crea una nuova istanza di[`FileCache`](../filecache) classe. |
| [FileCache](filecache#constructor_1)(string, string) | Crea una nuova istanza di[`FileCache`](../filecache) classe. |

## Proprietà

| Nome | Descrizione |
| --- | --- |
| [CachePath](../../groupdocs.viewer.caching/filecache/cachepath) { get; } | Il percorso relativo o assoluto della cartella della cache. |
| [CacheSubFolder](../../groupdocs.viewer.caching/filecache/cachesubfolder) { get; } | La sottocartella da aggiungere al file[`CachePath`](./cachepath) . |

## Metodi

| Nome | Descrizione |
| --- | --- |
| [GetKeys](../../groupdocs.viewer.caching/filecache/getkeys)(string) | Restituisce tutti i nomi di file che contengono il filtro nel nome file. |
| [Set](../../groupdocs.viewer.caching/filecache/set)(string, object) | Serializza i dati sul disco locale. |
| [TryGetValue&lt;T&gt;](../../groupdocs.viewer.caching/filecache/trygetvalue)(string, out T) | Deserializza i dati associati a questa chiave se presente. |

### Guarda anche

* interface [ICache](../icache)
* spazio dei nomi [GroupDocs.Viewer.Caching](../../groupdocs.viewer.caching)
* assemblea [GroupDocs.Viewer](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->
