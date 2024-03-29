---
title: InspectionPackage
second_title: .NET API संदर्भ के लिए GroupDocs.Metadata
description: एक मेटडेट पैकेज प्रप्त करत है जसमें दस्तवेज़ के लए नरक्षण परणम हते हैं पैकेज में दस्तवेज़ के हस्सं के बरे में जनकर हत है जसे कुछ ममलं में मेटडेट मन ज सकत है
type: docs
weight: 30
url: /hi/net/groupdocs.metadata.formats.document/pdfrootpackage/inspectionpackage/
---
## PdfRootPackage.InspectionPackage property

एक मेटाडेटा पैकेज प्राप्त करता है जिसमें दस्तावेज़ के लिए निरीक्षण परिणाम होते हैं। पैकेज में दस्तावेज़ के हिस्सों के बारे में जानकारी होती है जिसे कुछ मामलों में मेटाडेटा माना जा सकता है।

```csharp
public PdfInspectionPackage InspectionPackage { get; }
```

### संपत्ति मूल्य

एक मेटाडेटा पैकेज जिसमें दस्तावेज़ के निरीक्षण के परिणाम हैं।

### टिप्पणियों

**और अधिक जानें**

* [पीडीएफ दस्तावेजों में मेटाडेटा के साथ काम करना](https://docs.groupdocs.com/display/metadatanet/Working+with+metadata+in+PDF+documents)

### उदाहरण

यह उदाहरण दर्शाता है कि पीडीएफ दस्तावेज़ का निरीक्षण कैसे किया जाता है।

```csharp
using (Metadata metadata = new Metadata(Constants.SignedPdf))
{
    var root = metadata.GetRootPackage<PdfRootPackage>();

    if (root.InspectionPackage.Annotations != null)
    {
        foreach (var annotation in root.InspectionPackage.Annotations)
        {
            Console.WriteLine(annotation.Name);
            Console.WriteLine(annotation.Text);
            Console.WriteLine(annotation.PageNumber);
        }
    }

    if (root.InspectionPackage.Attachments != null)
    {
        foreach (var attachment in root.InspectionPackage.Attachments)
        {
            Console.WriteLine(attachment.Name);
            Console.WriteLine(attachment.MimeType);
            Console.WriteLine(attachment.Description);
        }
    }

    if (root.InspectionPackage.Bookmarks != null)
    {
        foreach (var bookmark in root.InspectionPackage.Bookmarks)
        {
            Console.WriteLine(bookmark.Title);
        }
    }

    if (root.InspectionPackage.DigitalSignatures != null)
    {
        foreach (var signature in root.InspectionPackage.DigitalSignatures)
        {
            Console.WriteLine(signature.CertificateSubject);
            Console.WriteLine(signature.Comments);
            Console.WriteLine(signature.SignTime);

            // ...
        }
    }

    if (root.InspectionPackage.Fields != null)
    {
        foreach (var field in root.InspectionPackage.Fields)
        {
            Console.WriteLine(field.Name);
            Console.WriteLine(field.Value);

            // ...
        }
    }
}
```

### यह सभी देखें

* class [PdfInspectionPackage](../../pdfinspectionpackage)
* class [PdfRootPackage](../../pdfrootpackage)
* नाम स्थान [GroupDocs.Metadata.Formats.Document](../../pdfrootpackage)
* सभा [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
