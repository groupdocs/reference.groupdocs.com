---
title: IDocumentInfo
second_title: GroupDocs.Redaction för .NET API-referens
description: Definierar metoder som krävs för att få grundläggande dokumentinformation.
type: docs
weight: 100
url: /sv/net/groupdocs.redaction/idocumentinfo/
---
## IDocumentInfo interface

Definierar metoder som krävs för att få grundläggande dokumentinformation.

```csharp
public interface IDocumentInfo
```

## Egenskaper

| namn | Beskrivning |
| --- | --- |
| [FileType](../../groupdocs.redaction/idocumentinfo/filetype) { get; } | Hämtar filformatsbeskrivningen. |
| [PageCount](../../groupdocs.redaction/idocumentinfo/pagecount) { get; } | Får det totala antalet sidor. |
| [Pages](../../groupdocs.redaction/idocumentinfo/pages) { get; } | Hämtar listan över[`PageInfo`](../pageinfo) sidinformation. |
| [Size](../../groupdocs.redaction/idocumentinfo/size) { get; } | Hämtar dokumentstorleken i byte. |

### Anmärkningar

**Läs mer**

* [Få filinformation](https://docs.groupdocs.com/redaction/net/get-file-info/)

### Exempel

Följande exempel visar hur man hämtar den allmänna dokumentinformationen med hjälp av[`IDocumentInfo`](../idocumentinfo).

```csharp
    try
    {
        using (Redactor red = new Redactor(@"C:\Temp\testfile.doc"))
        {
            IDocumentInfo docInfo = red.GetDocumentInfo();
            Console.WriteLine("Document size: {0}", docInfo.Size);
            Console.WriteLine("Document format: {0}", docInfo.FileType.FileFormat);
            Console.WriteLine("Document contains {0} pages", docInfo.PageCount);
            foreach (PageInfo page in docInfo.Pages)
            {
                Console.WriteLine("Page {0} size is {1}x{2}", page.PageNumber, page.Width, page.Height);
            }
        }
    }
    catch (GroupDocs.Redaction.Exceptions.PasswordRequiredException)
    {
        Console.WriteLine("You are trying to access document which is password protected. Please, set the password.");
    }
    catch (GroupDocs.Redaction.Exceptions.IncorrectPasswordException)
    {
        Console.WriteLine("The provided password is not valid.");
    }
```

### Se även

* namnutrymme [GroupDocs.Redaction](../../groupdocs.redaction)
* hopsättning [GroupDocs.Redaction](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Redaction.dll -->
