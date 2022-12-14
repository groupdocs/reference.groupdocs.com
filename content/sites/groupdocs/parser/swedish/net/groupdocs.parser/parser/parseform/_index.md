---
title: ParseForm
second_title: GroupDocs.Parser för .NET API-referens
description: Analyserar dokumentformuläret.
type: docs
weight: 190
url: /sv/net/groupdocs.parser/parser/parseform/
---
## Parser.ParseForm method

Analyserar dokumentformuläret.

```csharp
public DocumentData ParseForm()
```

### Returvärde

En instans av[`DocumentData`](../../../groupdocs.parser.data/documentdata) klass som innehåller extraherade data; `null` om analys efter mall inte stöds.

### Anmärkningar

**Läs mer:**

* [Extrahera data från PDF-formulär](https://docs.groupdocs.com/display/parsernet/Extract+data+from+PDF+forms)
* [Arbeta med extraherade data](https://docs.groupdocs.com/display/parsernet/Working+with+data+extracted+by+template)
* [Analysera data från PDF-dokument](https://docs.groupdocs.com/display/parsernet/Parse+data+from+PDF+documents)

### Exempel

Följande exempel visar hur man analyserar en form av dokumentet:

```csharp
// Skapa en instans av Parser-klassen
using (Parser parser = new Parser(filePath))
{
    // Extrahera data från PDF-dokument
    DocumentData data = parser.ParseForm();
    // Iterera över extraherade data
    for (int i = 0; i<data.Count; i++)
    {
        Console.Write(data[i].Name + ": ");
        PageTextArea area = data[i].PageArea as PageTextArea;
        Console.WriteLine(area == null ? "Not a template field" : area.Text);
    }
}
```

### Se även

* class [DocumentData](../../../groupdocs.parser.data/documentdata)
* class [Parser](../../parser)
* namnutrymme [GroupDocs.Parser](../../parser)
* hopsättning [GroupDocs.Parser](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->
