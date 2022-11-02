---
title: KnownTypeSet
second_title: GroupDocs.Assembly für .NET-API-Referenz
description: Repräsentiert einen ungeordneten Satz d. h. eine Sammlung einzigartiger Elemente der Folgendes enthältType Objekte  deren vollständig oder teilweise qualifizierte Namen in Dokumentvorlagen verwendet werden können um die statischen Member der entsprechenden Typen aufzurufen Typumwandlungen durchzuführen usw.
type: docs
weight: 230
url: /de/net/groupdocs.assembly/knowntypeset/
---
## KnownTypeSet class

Repräsentiert einen ungeordneten Satz (d. h. eine Sammlung einzigartiger Elemente), der Folgendes enthältType Objekte , deren vollständig oder teilweise qualifizierte Namen in Dokumentvorlagen verwendet werden können, um die statischen Member der entsprechenden -Typen aufzurufen, Typumwandlungen durchzuführen usw.

```csharp
public class KnownTypeSet : IEnumerable
```

## Eigenschaften

| Name | Beschreibung |
| --- | --- |
| [Count](../../groupdocs.assembly/knowntypeset/count) { get; } | Ruft die Anzahl der Elemente im Satz ab. |

## Methoden

| Name | Beschreibung |
| --- | --- |
| [Add](../../groupdocs.assembly/knowntypeset/add)(Type) | Fügt die angegebene hinzuType Einspruch gegen den Satz. WirftArgumentException in die folgenden Fälle: |
| [Clear](../../groupdocs.assembly/knowntypeset/clear)() | Entfernt alle Elemente aus dem Set. |
| [GetEnumerator](../../groupdocs.assembly/knowntypeset/getenumerator)() | Gibt ein zurückIEnumerator Objekt, um Elemente des Satzes zu durchlaufen. |
| [Remove](../../groupdocs.assembly/knowntypeset/remove)(Type) | Entfernt die angegebeneType Objekt aus dem Set. WirftArgumentException if *type* ist null. |

### Siehe auch

* namensraum [GroupDocs.Assembly](../../groupdocs.assembly)
* Montage [GroupDocs.Assembly](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Assembly.dll -->