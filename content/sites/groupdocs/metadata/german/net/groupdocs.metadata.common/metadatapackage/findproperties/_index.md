---
title: FindProperties
second_title: GroupDocs.Metadata für .NET-API-Referenz
description: Findet die Metadateneigenschaften die das angegebene Prädikat erfüllen. Die Suche ist rekursiv sodass sie auch alle verschachtelten Pakete betrifft.
type: docs
weight: 80
url: /de/net/groupdocs.metadata.common/metadatapackage/findproperties/
---
## MetadataPackage.FindProperties method

Findet die Metadateneigenschaften, die das angegebene Prädikat erfüllen. Die Suche ist rekursiv, sodass sie auch alle verschachtelten Pakete betrifft.

```csharp
public virtual IEnumerable<MetadataProperty> FindProperties(Func<MetadataProperty, bool> predicate)
```

| Parameter | Typ | Beschreibung |
| --- | --- | --- |
| predicate | Func`2 | Eine Funktion zum Testen jeder Metadateneigenschaft auf eine Bedingung. |

### Rückgabewert

EinIEnumerable das Eigenschaften aus dem Paket enthält, die die Bedingung erfüllen.

### Bemerkungen

**Mehr erfahren**

* Weitere Beispiele, die die Verwendung dieser Methode demonstrieren: [Extrahieren von Metadaten](https://docs.groupdocs.com/display/metadatanet/Extracting+metadata)

### Siehe auch

* class [MetadataProperty](../../metadataproperty)
* delegate [Func&lt;T,TResult&gt;](../../func-2)
* class [MetadataPackage](../../metadatapackage)
* namensraum [GroupDocs.Metadata.Common](../../metadatapackage)
* Montage [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->