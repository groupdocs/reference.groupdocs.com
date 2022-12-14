---
title: GetFormattedText
second_title: GroupDocs.Parser för .NET API-referens
description: Extraherar en formaterad text från dokumentet.
type: docs
weight: 80
url: /sv/net/groupdocs.parser/parser/getformattedtext/
---
## GetFormattedText(FormattedTextOptions) {#getformattedtext}

Extraherar en formaterad text från dokumentet.

```csharp
public TextReader GetFormattedText(FormattedTextOptions options)
```

| Parameter | Typ | Beskrivning |
| --- | --- | --- |
| options | FormattedTextOptions | Alternativen för formaterad textextraktion. |

### Returvärde

En instans avTextReader klass med den extraherade texten; `null` om formaterad textextraktion inte stöds.

### Anmärkningar

**Läs mer:**

* [Extrahera formaterad text från dokument](https://docs.groupdocs.com/display/parsernet/Extract+formatted+text+from+document)
* Extrahera en dokumenttext som[HTML](https://docs.groupdocs.com/display/parsernet/HTML)
* Extrahera en dokumenttext som[Prissänkning](https://docs.groupdocs.com/display/parsernet/Markdown)
* Extrahera en dokumenttext som[Oformatterad text](https://docs.groupdocs.com/display/parsernet/Plain+text)

### Exempel

Följande exempel visar hur man extraherar en dokumenttext som HTML-text:

```csharp
// Skapa en instans av Parser-klassen
using (Parser parser = new Parser(filePath))
{
    // Extrahera en formaterad text i läsaren
    using (TextReader reader = parser.GetFormattedText(new FormattedTextOptions(FormattedTextMode.Html)))
    {
        // Skriv ut en formaterad text från dokumentet
        // Om formaterad textextraktion inte stöds är en läsare null
        Console.WriteLine(reader == null ? "Formatted text extraction isn't suppported" : reader.ReadToEnd());
    }
}
```

### Se även

* class [FormattedTextOptions](../../../groupdocs.parser.options/formattedtextoptions)
* class [Parser](../../parser)
* namnutrymme [GroupDocs.Parser](../../parser)
* hopsättning [GroupDocs.Parser](../../../)

---

## GetFormattedText(int, FormattedTextOptions) {#getformattedtext_1}

Extraherar en formaterad text från dokumentsidan.

```csharp
public TextReader GetFormattedText(int pageIndex, FormattedTextOptions options)
```

| Parameter | Typ | Beskrivning |
| --- | --- | --- |
| pageIndex | Int32 | Det nollbaserade sidindexet. |
| options | FormattedTextOptions | Alternativen för formaterad textextraktion. |

### Returvärde

En instans avTextReaderklass med den extraherade texten; `null` om formaterad textsidesextraktion inte stöds.

### Anmärkningar

**Läs mer:**

* [Extrahera formaterad text från dokumentsidan](https://docs.groupdocs.com/display/parsernet/Extract+formatted+text+from+document+page)
* Extrahera en dokumenttext som[HTML](https://docs.groupdocs.com/display/parsernet/HTML)
* Extrahera en dokumenttext som[Prissänkning](https://docs.groupdocs.com/display/parsernet/Markdown)
* Extrahera en dokumenttext som[Oformatterad text](https://docs.groupdocs.com/display/parsernet/Plain+text)

### Exempel

Följande exempel visar hur man extraherar en dokumentsidatext som Markdown-text:

```csharp
// Skapa en instans av Parser-klassen
using (Parser parser = new Parser(filePath))
{
    // Kontrollera om dokumentet stöder formaterad textextraktion
    if (!parser.Features.FormattedText)
    {
        Console.WriteLine("Document isn't supports formatted text extraction.");
        return;
    }
    
    // Få dokumentinformationen
    IDocumentInfo documentInfo = parser.GetDocumentInfo();
    // Kontrollera om dokumentet har sidor
    if (documentInfo.PageCount == 0)
    {
        Console.WriteLine("Document hasn't pages.");
        return;
    }
    
    // Iterera över sidor
    for (int p = 0; p<documentInfo.PageCount; p++)
    {
        // Skriv ut ett sidnummer 
        Console.WriteLine(string.Format("Page {0}/{1}", p + 1, documentInfo.PageCount));
        // Extrahera en formaterad text i läsaren
        using (TextReader reader = parser.GetFormattedText(p, new FormattedTextOptions(FormattedTextMode.Markdown)))
        {
            // Skriv ut en formaterad text från dokumentet
            // Vi ignorerar nollkontroll eftersom vi har kontrollerat stöd för formaterad textextraktion tidigare
            Console.WriteLine(reader.ReadToEnd());
        }
    }
}
```

### Se även

* class [FormattedTextOptions](../../../groupdocs.parser.options/formattedtextoptions)
* class [Parser](../../parser)
* namnutrymme [GroupDocs.Parser](../../parser)
* hopsättning [GroupDocs.Parser](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->
