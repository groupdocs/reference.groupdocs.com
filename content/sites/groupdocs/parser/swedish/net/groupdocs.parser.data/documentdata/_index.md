---
title: DocumentData
second_title: GroupDocs.Parser för .NET API-referens
description: Representerar data i dokumentet. Den består avFieldData./fielddataobjects som innehåller fältdata från document.
type: docs
weight: 20
url: /sv/net/groupdocs.parser.data/documentdata/
---
## DocumentData class

Representerar data i dokumentet. Den består av[`FieldData`](../fielddata)objects som innehåller fältdata från document.

```csharp
public class DocumentData : IEnumerable<FieldData>
```

## Konstruktörer

| namn | Beskrivning |
| --- | --- |
| [DocumentData](documentdata)(IEnumerable&lt;FieldData&gt;) | Initierar en ny instans av[`FieldData`](../fielddata) class. |

## Egenskaper

| namn | Beskrivning |
| --- | --- |
| [Count](../../groupdocs.parser.data/documentdata/count) { get; } | Hämtar det totala antalet fältdata. |
| [Item](../../groupdocs.parser.data/documentdata/item) { get; } | Hämtar fältdata med ett index. |

## Metoder

| namn | Beskrivning |
| --- | --- |
| [GetEnumerator](../../groupdocs.parser.data/documentdata/getenumerator)() | Returnerar en uppräkning för fältdata. |
| [GetFieldsByName](../../groupdocs.parser.data/documentdata/getfieldsbyname)(string) | Returnerar samlingen av fältdata där namnet är lika med*fieldName* . |

### Anmärkningar

En instans av[`DocumentData`](../documentdata) klass används som returvärde av[`ParseByTemplate`](../../groupdocs.parser/parser/parsebytemplate) och[`ParseForm`](../../groupdocs.parser/parser/parseform) metoder. Se användningsexemplen där.

### Se även

* class [FieldData](../fielddata)
* namnutrymme [GroupDocs.Parser.Data](../../groupdocs.parser.data)
* hopsättning [GroupDocs.Parser](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->
