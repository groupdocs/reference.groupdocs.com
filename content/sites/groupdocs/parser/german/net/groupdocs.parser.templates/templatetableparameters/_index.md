---
title: TemplateTableParameters
second_title: GroupDocs.Parser für .NET-API-Referenz
description: Stellt Parameter für die Tabellenerkennungsalgorithmen bereit.
type: docs
weight: 760
url: /de/net/groupdocs.parser.templates/templatetableparameters/
---
## TemplateTableParameters class

Stellt Parameter für die Tabellenerkennungsalgorithmen bereit.

```csharp
public sealed class TemplateTableParameters
```

## Konstrukteure

| Name | Beschreibung |
| --- | --- |
| [TemplateTableParameters](templatetableparameters#constructor)(Rectangle, IEnumerable&lt;double&gt;) | Initialisiert eine neue Instanz von[`TemplateTableParameters`](../templatetableparameters) Klasse. |
| [TemplateTableParameters](templatetableparameters#constructor_1)(Rectangle, IEnumerable&lt;double&gt;, bool?, int?, int?, int?) | Initialisiert eine neue Instanz von[`TemplateTableParameters`](../templatetableparameters) Klasse. |

## Eigenschaften

| Name | Beschreibung |
| --- | --- |
| [HasMergedCells](../../groupdocs.parser.templates/templatetableparameters/hasmergedcells) { get; } | Ruft den Wert ab, der angibt, ob die Tabelle verbundene Zellen hat. |
| [MinColumnCount](../../groupdocs.parser.templates/templatetableparameters/mincolumncount) { get; } | Ruft die minimale Anzahl der Tabellenspalten ab. |
| [MinRowCount](../../groupdocs.parser.templates/templatetableparameters/minrowcount) { get; } | Ruft die minimale Anzahl der Tabellenzeilen ab. |
| [MinVerticalSpace](../../groupdocs.parser.templates/templatetableparameters/minverticalspace) { get; } | Ruft den Mindestabstand zwischen den Tabellenspalten ab. |
| [Rectangle](../../groupdocs.parser.templates/templatetableparameters/rectangle) { get; } | Ruft den rechteckigen Bereich ab, der die Tabelle enthält. |
| [VerticalSeparators](../../groupdocs.parser.templates/templatetableparameters/verticalseparators) { get; } | Ruft die Trennzeichen der Tabellenspalten ab. |

### Bemerkungen

Es gibt zwei Algorithmen, um eine Tabelle zu erkennen:

* Ermöglicht die Erkennung einer Tabelle im rechteckigen Bereich mit festgelegten Spalten. Dieser Algorithmus ist nützlich für einfache Tabellen (ohne zusammengeführte Spalten) und bietet eine genauere Erkennung.
* Ermöglicht das Erkennen einer Tabelle an jeder Stelle auf der Seite. Dies ist ein komplexerer Algorithmus. Es kann Tabellen an jeder Stelle auf der Seite erkennen. Zusätzliche Parameter helfen, eine Tabelle korrekter zu erkennen.

In einigen Fällen, wenn Algorithmen eine Tabelle nicht erkennen können oder dies auf ungenaue Weise geschieht [`TemplateTableLayout`](../templatetablelayout) Klasse wird verwendet.

### Siehe auch

* namensraum [GroupDocs.Parser.Templates](../../groupdocs.parser.templates)
* Montage [GroupDocs.Parser](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->
