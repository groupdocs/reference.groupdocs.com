---
title: IDocumentInfo
second_title: GroupDocs.Redaction for .NET API 参考
description: 定义获取基本文档信息所需的方法
type: docs
weight: 100
url: /zh/net/groupdocs.redaction/idocumentinfo/
---
## IDocumentInfo interface

定义获取基本文档信息所需的方法。

```csharp
public interface IDocumentInfo
```

## 特性

| 姓名 | 描述 |
| --- | --- |
| [FileType](../../groupdocs.redaction/idocumentinfo/filetype) { get; } | 获取文件格式描述。 |
| [PageCount](../../groupdocs.redaction/idocumentinfo/pagecount) { get; } | 获取总页数。 |
| [Pages](../../groupdocs.redaction/idocumentinfo/pages) { get; } | 获取列表[`PageInfo`](../pageinfo)页面信息. |
| [Size](../../groupdocs.redaction/idocumentinfo/size) { get; } | 以字节为单位获取文档大小。 |

### 评论

**学到更多**

* [获取文件信息](https://docs.groupdocs.com/redaction/net/get-file-info/)

### 例子

以下示例演示如何使用检索一般文档信息[`IDocumentInfo`](../idocumentinfo).

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

### 也可以看看

* 命名空间 [GroupDocs.Redaction](../../groupdocs.redaction)
* 部件 [GroupDocs.Redaction](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Redaction.dll -->