---
title: RemoveProperties
second_title: GroupDocs.Metadata für .NET-API-Referenz
description: Entfernt Metadateneigenschaften die das angegebene Prädikat erfüllen.
type: docs
weight: 110
url: /de/net/groupdocs.metadata.formats.document/wordprocessinginspectionpackage/removeproperties/
---
## WordProcessingInspectionPackage.RemoveProperties method

Entfernt Metadateneigenschaften, die das angegebene Prädikat erfüllen.

```csharp
public override int RemoveProperties(Func<MetadataProperty, bool> predicate)
```

| Parameter | Typ | Beschreibung |
| --- | --- | --- |
| predicate | Func`2 | Eine Funktion zum Testen jeder Metadateneigenschaft auf eine Bedingung. |

### Rückgabewert

Die Anzahl der betroffenen Eigenschaften.

### Siehe auch

* delegate [Func&lt;T,TResult&gt;](../../../groupdocs.metadata.common/func-2)
* class [MetadataProperty](../../../groupdocs.metadata.common/metadataproperty)
* class [WordProcessingInspectionPackage](../../wordprocessinginspectionpackage)
* namensraum [GroupDocs.Metadata.Formats.Document](../../wordprocessinginspectionpackage)
* Montage [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
