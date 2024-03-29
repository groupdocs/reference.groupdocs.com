---
title: GetDocumentInfo
second_title: .NET API संदर्भ के लिए GroupDocs.Redaction
description: दस्तवेज़ के बरे में समन्य जनकर प्रप्त करत है  आकर पृष्ठ संख्य आद.
type: docs
weight: 50
url: /hi/net/groupdocs.redaction/redactor/getdocumentinfo/
---
## Redactor.GetDocumentInfo method

दस्तावेज़ के बारे में सामान्य जानकारी प्राप्त करता है - आकार, पृष्ठ संख्या, आदि.

```csharp
public IDocumentInfo GetDocumentInfo()
```

### प्रतिलाभ की मात्रा

IDocumentInfo का एक उदाहरण

### उदाहरण

निम्न उदाहरण दर्शाता है कि सामान्य दस्तावेज़ जानकारी का उपयोग करके कैसे पुनर्प्राप्त किया जाए[`IDocumentInfo`](../../idocumentinfo).

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

### यह सभी देखें

* interface [IDocumentInfo](../../idocumentinfo)
* class [Redactor](../../redactor)
* नाम स्थान [GroupDocs.Redaction](../../redactor)
* सभा [GroupDocs.Redaction](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Redaction.dll -->
