---
title: GetHighlight
second_title: GroupDocs.Parser für .NET-API-Referenz
description: Extrahiert eine Markierung aus dem Dokument.
type: docs
weight: 90
url: /de/net/groupdocs.parser/parser/gethighlight/
---
## Parser.GetHighlight method

Extrahiert eine Markierung aus dem Dokument.

```csharp
public HighlightItem GetHighlight(int position, bool isDirect, HighlightOptions options)
```

| Parameter | Typ | Beschreibung |
| --- | --- | --- |
| position | Int32 | Die Startposition der Markierung. |
| isDirect | Boolean | Der Wert, der angibt, ob die Highlight-Extraktion direkt ist. `WAHR` wenn das Highlight von rechts extrahiert wird*position* ; ansonsten,`FALSCH` . |
| options | HighlightOptions | Die Highlight-Extraktionsoptionen. |

### Rückgabewert

Eine Instanz von[`HighlightItem`](../../../groupdocs.parser.data/highlightitem) Klasse, die das extrahierte Highlight darstellt; `Null` wenn die Highlight-Extraktion nicht unterstützt wird.

### Bemerkungen

**Erfahren Sie mehr:**

* [Highlights extrahieren](https://docs.groupdocs.com/display/parsernet/Extract+highlights)

### Beispiele

Das folgende Beispiel zeigt, wie Sie eine Markierung extrahieren, die 3 Wörter enthält:

```csharp
// Erstellen Sie eine Instanz der Parser-Klasse
using (Parser parser = new Parser(filePath))
{
    // Highlight extrahieren:
    HighlightItem hl = parser.GetHighlight(2, true, new HighlightOptions(3));
    
    // Prüfen, ob Highlight-Extraktion unterstützt wird
    if (hl == null)
    {
        Console.WriteLine("Highlight extraction isn't supported");
        return;
    }
    
    // Eine extrahierte Markierung drucken
    Console.WriteLine(string.Format("At {0}: {1}", hl.Position, hl.Text));
}
```

### Siehe auch

* class [HighlightItem](../../../groupdocs.parser.data/highlightitem)
* class [HighlightOptions](../../../groupdocs.parser.options/highlightoptions)
* class [Parser](../../parser)
* namensraum [GroupDocs.Parser](../../parser)
* Montage [GroupDocs.Parser](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->
