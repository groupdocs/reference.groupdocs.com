---
title: HtmlHighlighter
second_title: GroupDocs.Search efter .NET API Reference
description: Representerar en överstrykning av sökresultat som markerar sökresultat i en hel dokumenttext formaterad i HTML.
type: docs
weight: 640
url: /sv/net/groupdocs.search.highlighters/htmlhighlighter/
---
## HtmlHighlighter class

Representerar en överstrykning av sökresultat som markerar sökresultat i en hel dokumenttext formaterad i HTML.

```csharp
public class HtmlHighlighter : Highlighter
```

## Konstruktörer

| namn | Beskrivning |
| --- | --- |
| [HtmlHighlighter](htmlhighlighter)(OutputAdapter) | Initierar en ny instans av[`HtmlHighlighter`](../htmlhighlighter) class. |

## Egenskaper

| namn | Beskrivning |
| --- | --- |
| [OutputAdapter](../../groupdocs.search.highlighters/htmlhighlighter/outputadapter) { get; } | Får utgångsadaptern skickad i konstruktorn. |

### Anmärkningar

**Läs mer**

* [Markera sökresultat](https://docs.groupdocs.com/display/searchnet/Highlighting+search+results)

### Exempel

Exemplet visar en typisk användning av klassen.

```csharp
string indexFolder = @"c:\MyIndex\";
string documentsFolder = @"c:\MyDocuments\";

// Skapa ett index
Index index = new Index(indexFolder);

// Indexering av dokument från den angivna mappen
index.Add(documentsFolder);

// Sök efter fasen 'relativitetsteori'
SearchResult result = index.Search("\"Theory of Relativity\"");

// Markera hittade ord i texten i ett dokument
FoundDocument document = result.GetFoundDocument(0);
OutputAdapter outputAdapter = new FileOutputAdapter("Highlighted.html");
Highlighter highlighter = new HtmlHighlighter(outputAdapter);
index.Highlight(document, highlighter);
```

### Se även

* class [Highlighter](../highlighter)
* namnutrymme [GroupDocs.Search.Highlighters](../../groupdocs.search.highlighters)
* hopsättning [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
