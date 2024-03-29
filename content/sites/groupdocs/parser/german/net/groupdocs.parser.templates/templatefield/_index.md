---
title: TemplateField
second_title: GroupDocs.Parser für .NET-API-Referenz
description: Stellt das Vorlagentextfeld bereit.
type: docs
weight: 670
url: /de/net/groupdocs.parser.templates/templatefield/
---
## TemplateField class

Stellt das Vorlagentextfeld bereit.

```csharp
public sealed class TemplateField : TemplateItem
```

## Konstrukteure

| Name | Beschreibung |
| --- | --- |
| [TemplateField](templatefield#constructor)(TemplatePosition, string) | Initialisiert eine neue Instanz von[`TemplateField`](../templatefield) Klasse. |
| [TemplateField](templatefield#constructor_1)(TemplatePosition, string, int?) | Initialisiert eine neue Instanz von[`TemplateField`](../templatefield) Klasse. |

## Eigenschaften

| Name | Beschreibung |
| --- | --- |
| [Name](../../groupdocs.parser.templates/templateitem/name) { get; } | Ruft den Namen des Vorlagenelements ab. |
| [PageIndex](../../groupdocs.parser.templates/templateitem/pageindex) { get; } | Ruft den Seitenindex des Vorlagenelements ab. |
| [Position](../../groupdocs.parser.templates/templatefield/position) { get; } | Ruft den Wert ab, der beschreibt, wie das Vorlagenfeld auf der Dokumentseite zu finden ist. |

### Bemerkungen

Textfelder werden durch ihre Position auf der Seite definiert. Es gibt drei Möglichkeiten, ein Textfeld zu definieren:

* [`Verwendung des rechteckigen Bereichs`](../templatefixedposition)
* [`Verwenden des regulären Ausdrucks`](../templateregexposition)
* [`Verwenden Sie das verknüpfte Feld`](../templatelinkedposition)

### Siehe auch

* class [TemplateItem](../templateitem)
* namensraum [GroupDocs.Parser.Templates](../../groupdocs.parser.templates)
* Montage [GroupDocs.Parser](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->
