---
title: GetToc
second_title: Riferimento API GroupDocs.Parser per .NET
description: Estrae un sommario dal documento.
type: docs
weight: 170
url: /it/net/groupdocs.parser/parser/gettoc/
---
## Parser.GetToc method

Estrae un sommario dal documento.

```csharp
public IEnumerable<TocItem> GetToc()
```

### Valore di ritorno

Una raccolta di elementi del sommario; `nullo` se l'estrazione del sommario non è supportata.

### Osservazioni

**Saperne di più:**

* [Estrai il sommario](https://docs.groupdocs.com/display/parsernet/Extract+table+of+contents)
* [Estrai il testo per voce del sommario](https://docs.groupdocs.com/display/parsernet/Extract+text+by+table+of+contents+item)
* [Estrai il sommario dai documenti di Microsoft Office Word](https://docs.groupdocs.com/display/parsernet/Extract+table+of+contents+from+Microsoft+Office+Word+documents)
* [Estrai il sommario dagli eBook EPUB](https://docs.groupdocs.com/display/parsernet/Extract+table+of+contents+from+EPUB+eBooks)

### Esempi

L'esempio seguente mostra come estrarre il sommario dal file CHM:

```csharp
// Crea un'istanza della classe Parser
using (Parser parser = new Parser(filePath))
{
    // Controlla se l'estrazione del testo è supportata
    if (!parser.Features.Text)
    {
        Console.WriteLine("Text extraction isn't supported.");
        return;
    }

    // Controlla se l'estrazione di toc è supportata
    if (!parser.Features.Toc)
    {
        Console.WriteLine("Toc extraction isn't supported.");
        return;
    }
 
    // Ottieni il sommario
    IEnumerable<TocItem> toc = parser.GetToc();
    
    // Itera sugli elementi
    foreach (TocItem i in toc)
    {
        // Stampa il testo Toc
        Console.WriteLine(i.Text);
        // Controlla se l'indice della pagina ha un valore
        if (i.PageIndex == null)
        {
            continue;
        }
        // Estrai il testo di una pagina
        using (TextReader reader = parser.GetText(i.PageIndex.Value))
        {
            Console.WriteLine(reader.ReadToEnd());
        }
    }
}
```

### Guarda anche

* class [TocItem](../../../groupdocs.parser.data/tocitem)
* class [Parser](../../parser)
* spazio dei nomi [GroupDocs.Parser](../../parser)
* assemblea [GroupDocs.Parser](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->
