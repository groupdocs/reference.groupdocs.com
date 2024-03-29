---
title: PageInfo
second_title: .NET API 참조용 GroupDocs.Redaction
description: 간략한 페이지 정보를 나타냅니다.
type: docs
weight: 390
url: /ko/net/groupdocs.redaction/pageinfo/
---
## PageInfo class

간략한 페이지 정보를 나타냅니다.

```csharp
public class PageInfo
```

## 생성자

| 이름 | 설명 |
| --- | --- |
| [PageInfo](pageinfo)() | 기본 생성자입니다. |

## 속성

| 이름 | 설명 |
| --- | --- |
| [Height](../../groupdocs.redaction/pageinfo/height) { get; set; } | 페이지 높이를 가져오거나 설정합니다. |
| [PageNumber](../../groupdocs.redaction/pageinfo/pagenumber) { get; set; } | 페이지 번호를 가져오거나 설정합니다. |
| [Width](../../groupdocs.redaction/pageinfo/width) { get; set; } | 페이지 너비를 가져오거나 설정합니다. |

### 비고

**더 알아보기**

* [파일 정보 얻기](https://docs.groupdocs.com/redaction/net/get-file-info/)

### 예

다음 예는 다음을 사용하여 일반 문서 정보를 검색하는 방법을 보여줍니다.[`IDocumentInfo`](../idocumentinfo).

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

### 또한보십시오

* 네임스페이스 [GroupDocs.Redaction](../../groupdocs.redaction)
* 집회 [GroupDocs.Redaction](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Redaction.dll -->
