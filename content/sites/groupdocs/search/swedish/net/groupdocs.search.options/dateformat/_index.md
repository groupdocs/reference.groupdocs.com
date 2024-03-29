---
title: DateFormat
second_title: GroupDocs.Search efter .NET API Reference
description: Representerar ett datumformat.
type: docs
weight: 770
url: /sv/net/groupdocs.search.options/dateformat/
---
## DateFormat class

Representerar ett datumformat.

```csharp
public class DateFormat
```

## Konstruktörer

| namn | Beskrivning |
| --- | --- |
| [DateFormat](dateformat#constructor)(DateFormatElement[], string) | Initierar en ny instans av[`DateFormat`](../dateformat) class. |
| [DateFormat](dateformat#constructor_1)(string, DateFormatElement[]) | Initierar en ny instans av[`DateFormat`](../dateformat) class. |

## Egenskaper

| namn | Beskrivning |
| --- | --- |
| [DateSeparator](../../groupdocs.search.options/dateformat/dateseparator) { get; } | Hämtar datumavgränsaren. |

## Metoder

| namn | Beskrivning |
| --- | --- |
| override [ToString](../../groupdocs.search.options/dateformat/tostring)() | Returnerar enString som representerar strömmen[`DateFormat`](../dateformat) . |

### Anmärkningar

**Läs mer**

* [Sök efter datumintervall](https://docs.groupdocs.com/display/searchnet/Date+range+search)

### Exempel

Exemplet visar en typisk användning av klassen.

```csharp
string indexFolder = @"c:\MyIndex\";
string documentsFolder = @"c:\MyDocuments\";
string query = "daterange(2017-01-01 ~~ 2019-12-31)";

Index index = new Index(indexFolder); // Skapar ett index i den angivna mappen
index.Add(documentsFolder); // Indexering av dokument från den angivna mappen

SearchOptions options = new SearchOptions();
options.DateFormats.Clear(); // Tar bort standard datumformat
DateFormatElement[] elements = new DateFormatElement[]
{
    DateFormatElement.MonthTwoDigits,
    DateFormatElement.DateSeparator,
    DateFormatElement.DayOfMonthTwoDigits,
    DateFormatElement.DateSeparator,
    DateFormatElement.YearFourDigits,
};
// Skapa ett datumformatmönster 'MM/dd/åååå'
DateFormat dateFormat = new DateFormat(elements, "/");
options.DateFormats.Add(dateFormat);

SearchResult result = index.Search(query, options); // Sök i index
```

### Se även

* namnutrymme [GroupDocs.Search.Options](../../groupdocs.search.options)
* hopsättning [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
