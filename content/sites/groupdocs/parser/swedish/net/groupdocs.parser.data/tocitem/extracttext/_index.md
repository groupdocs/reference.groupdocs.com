---
title: ExtractText
second_title: GroupDocs.Parser för .NET API-referens
description: Extraherar en text från dokumentet somTocItemgroupdocs.parser.data/tocitem objekt refererar.
type: docs
weight: 50
url: /sv/net/groupdocs.parser.data/tocitem/extracttext/
---
## TocItem.ExtractText method

Extraherar en text från dokumentet som[`TocItem`](../../tocitem) objekt refererar.

```csharp
public virtual TextReader ExtractText()
```

### Returvärde

Ett exempel påTextReader klass med den extraherade texten.

### Exempel

Följande exempel hur man extraherar en text med en innehållsförteckning:

```csharp
// Skapa en instans av Parser-klassen
using (Parser parser = new Parser(Constants.SampleDocxWithToc))
{
    // Få innehållsförteckning
    IEnumerable<TocItem> tocItems = parser.GetToc();
    // Kontrollera om toc-extraktion stöds
    if (tocItems == null)
    {
        Console.WriteLine("Table of contents extraction isn't supported");
    }
    // Iterera över objekt
    foreach (TocItem tocItem in tocItems)
    {
        // Skriv ut kapitlets text
        using (TextReader reader = tocItem.ExtractText())
        {
            Console.WriteLine("----");
            Console.WriteLine(reader.ReadToEnd());
        }
    }
}
```

### Se även

* class [TocItem](../../tocitem)
* namnutrymme [GroupDocs.Parser.Data](../../tocitem)
* hopsättning [GroupDocs.Parser](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->
