---
title: FileCache
second_title: GroupDocs.Viewer voor .NET API-referentie
description: Vertegenwoordigt een lokale cache op schijf.
type: docs
weight: 20
url: /nl/net/groupdocs.viewer.caching/filecache/
---
## FileCache class

Vertegenwoordigt een lokale cache op schijf.

```csharp
public class FileCache : ICache
```

## Constructeurs

| Naam | Beschrijving |
| --- | --- |
| [FileCache](filecache#constructor)(string) | Maakt een nieuw exemplaar van[`FileCache`](../filecache) klasse. |
| [FileCache](filecache#constructor_1)(string, string) | Maakt een nieuw exemplaar van[`FileCache`](../filecache) klasse. |

## Eigenschappen

| Naam | Beschrijving |
| --- | --- |
| [CachePath](../../groupdocs.viewer.caching/filecache/cachepath) { get; } | Het relatieve of absolute pad naar de cachemap. |
| [CacheSubFolder](../../groupdocs.viewer.caching/filecache/cachesubfolder) { get; } | De submap die moet worden toegevoegd aan het[`CachePath`](./cachepath) . |

## methoden

| Naam | Beschrijving |
| --- | --- |
| [GetKeys](../../groupdocs.viewer.caching/filecache/getkeys)(string) | Retourneert alle bestandsnamen die een filter bevatten in bestandsnaam. |
| [Set](../../groupdocs.viewer.caching/filecache/set)(string, object) | Serialiseert gegevens naar de lokale schijf. |
| [TryGetValue&lt;T&gt;](../../groupdocs.viewer.caching/filecache/trygetvalue)(string, out T) | Deserialiseert gegevens die aan deze sleutel zijn gekoppeld, indien aanwezig. |

### Zie ook

* interface [ICache](../icache)
* naamruimte [GroupDocs.Viewer.Caching](../../groupdocs.viewer.caching)
* montage [GroupDocs.Viewer](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->
