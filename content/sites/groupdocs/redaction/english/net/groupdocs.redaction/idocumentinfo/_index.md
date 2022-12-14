---
title: IDocumentInfo
second_title: GroupDocs.Redaction for .NET API Reference
description: Defines methods that are required for getting basic document information.
type: docs
weight: 100
url: /net/groupdocs.redaction/idocumentinfo/
---
## IDocumentInfo interface

Defines methods that are required for getting basic document information.

```csharp
public interface IDocumentInfo
```

## Properties

| Name | Description |
| --- | --- |
| [FileType](../../groupdocs.redaction/idocumentinfo/filetype) { get; } | Gets the file format description. |
| [PageCount](../../groupdocs.redaction/idocumentinfo/pagecount) { get; } | Gets the total page count. |
| [Pages](../../groupdocs.redaction/idocumentinfo/pages) { get; } | Gets the list of [`PageInfo`](../pageinfo) page information. |
| [Size](../../groupdocs.redaction/idocumentinfo/size) { get; } | Gets the document size in bytes. |

### Remarks

**Learn more**

* [Get file info](https://docs.groupdocs.com/redaction/net/get-file-info/)

### Examples

The following example demonstrates how to retrieve the general document information using [`IDocumentInfo`](../idocumentinfo).

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

### See Also

* namespace [GroupDocs.Redaction](../../groupdocs.redaction)
* assembly [GroupDocs.Redaction](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.redaction.dll -->
