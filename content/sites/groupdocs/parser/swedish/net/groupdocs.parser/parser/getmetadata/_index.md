---
title: GetMetadata
second_title: GroupDocs.Parser för .NET API-referens
description: Extraherar metadata från dokumentet.
type: docs
weight: 120
url: /sv/net/groupdocs.parser/parser/getmetadata/
---
## Parser.GetMetadata method

Extraherar metadata från dokumentet.

```csharp
public IEnumerable<MetadataItem> GetMetadata()
```

### Returvärde

En samling metadataobjekt; `null` om extrahering av metadata inte stöds.

### Anmärkningar

**Läs mer:**

* [Extrahera metadata från dokument](https://docs.groupdocs.com/display/parsernet/Extract+metadata+from+documents)
* [Extrahera metadata från Microsoft Office Word-dokument](https://docs.groupdocs.com/display/parsernet/Extract+metadata+from+Microsoft+Office+Word+documents)
* [Extrahera metadata från Microsoft Office Excel-kalkylblad](https://docs.groupdocs.com/display/parsernet/Extract+metadata+from+Microsoft+Office+Excel+spreadsheets)
* [Extrahera metadata från Microsoft Office PowerPoint-presentationer](https://docs.groupdocs.com/display/parsernet/Extract+metadata+from+Microsoft+Office+PowerPoint+presentations)
* [Extrahera metadata från PDF-dokument](https://docs.groupdocs.com/display/parsernet/Extract+metadata+from+PDF+documents)
* [Extrahera metadata från e-postmeddelanden](https://docs.groupdocs.com/display/parsernet/Extract+metadata+from+Emails)

### Exempel

Följande exempel visar hur man extraherar metadata från ett dokument:

```csharp
// Skapa en instans av Parser-klassen
using(Parser parser = new Parser(filePath))
{
    // Extrahera metadata från dokumentet
    IEnumerable<MetadataItem> metadata = parser.GetMetadata();
    // Kontrollera om extrahering av metadata stöds
    if(metadata == null)
    {
        Console.WriteLine("Metatada extraction isn't supported");
    }
 
    // Iterera över metadataobjekt
    foreach(MetadataItem item in metadata)
    {
        // Skriv ut ett objekts namn och värde
        Console.WriteLine(string.Format("{0}: {1}", item.Name, item.Value));
    }
}
```

### Se även

* class [MetadataItem](../../../groupdocs.parser.data/metadataitem)
* class [Parser](../../parser)
* namnutrymme [GroupDocs.Parser](../../parser)
* hopsättning [GroupDocs.Parser](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->
