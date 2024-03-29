---
title: PageInfo
second_title: Справочник по API GroupDocs.Redaction для .NET
description: Представляет краткую информацию о странице.
type: docs
weight: 390
url: /ru/net/groupdocs.redaction/pageinfo/
---
## PageInfo class

Представляет краткую информацию о странице.

```csharp
public class PageInfo
```

## Конструкторы

| Имя | Описание |
| --- | --- |
| [PageInfo](pageinfo)() | Конструктор по умолчанию. |

## Характеристики

| Имя | Описание |
| --- | --- |
| [Height](../../groupdocs.redaction/pageinfo/height) { get; set; } | Получает или задает высоту страницы. |
| [PageNumber](../../groupdocs.redaction/pageinfo/pagenumber) { get; set; } | Получает или задает номер страницы. |
| [Width](../../groupdocs.redaction/pageinfo/width) { get; set; } | Получает или задает ширину страницы. |

### Примечания

**Узнать больше**

* [Получить информацию о файле](https://docs.groupdocs.com/redaction/net/get-file-info/)

### Примеры

В следующем примере показано, как получить общую информацию о документе с помощью[`IDocumentInfo`](../idocumentinfo).

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

### Смотрите также

* пространство имен [GroupDocs.Redaction](../../groupdocs.redaction)
* сборка [GroupDocs.Redaction](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Redaction.dll -->
