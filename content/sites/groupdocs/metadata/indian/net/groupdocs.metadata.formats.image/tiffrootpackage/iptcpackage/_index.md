---
title: IptcPackage
second_title: .NET API संदर्भ के लिए GroupDocs.Metadata
description: IPTC मेटडेट पैकेज प्रप्त य सेट करत है
type: docs
weight: 20
url: /hi/net/groupdocs.metadata.formats.image/tiffrootpackage/iptcpackage/
---
## TiffRootPackage.IptcPackage property

IPTC मेटाडेटा पैकेज प्राप्त या सेट करता है।

```csharp
public IptcRecordSet IptcPackage { get; set; }
```

### संपत्ति मूल्य

आईपीटीसी मेटाडेटा पैकेज.

### टिप्पणियों

**और अधिक जानें**

* [IPTC IIM मेटाडेटा के साथ कार्य करना](https://docs.groupdocs.com/display/metadatanet/Working+with+IPTC+IIM+metadata)

### उदाहरण

यह उदाहरण दिखाता है कि किसी TIFF छवि से मूल IPTC मेटाडेटा गुण कैसे निकालें।

```csharp
using (Metadata metadata = new Metadata(Constants.TiffWithIptc))
{
    var root = metadata.GetRootPackage<TiffRootPackage>();
    if (root.IptcPackage != null)
    {
        if (root.IptcPackage.EnvelopeRecord != null)
        {
            Console.WriteLine(root.IptcPackage.EnvelopeRecord.DateSent);
            Console.WriteLine(root.IptcPackage.EnvelopeRecord.Destination);
            Console.WriteLine(root.IptcPackage.EnvelopeRecord.FileFormat);
            Console.WriteLine(root.IptcPackage.EnvelopeRecord.FileFormatVersion);

            // ...
        }

        if (root.IptcPackage.ApplicationRecord != null)
        {
            Console.WriteLine(root.IptcPackage.ApplicationRecord.Headline);
            Console.WriteLine(root.IptcPackage.ApplicationRecord.ByLine);
            Console.WriteLine(root.IptcPackage.ApplicationRecord.ByLineTitle);
            Console.WriteLine(root.IptcPackage.ApplicationRecord.CaptionAbstract);
            Console.WriteLine(root.IptcPackage.ApplicationRecord.City);
            Console.WriteLine(root.IptcPackage.ApplicationRecord.DateCreated);
            Console.WriteLine(root.IptcPackage.ApplicationRecord.ReleaseDate);

            // ...
        }
    }
}
```

### यह सभी देखें

* class [IptcRecordSet](../../../groupdocs.metadata.standards.iptc/iptcrecordset)
* class [TiffRootPackage](../../tiffrootpackage)
* नाम स्थान [GroupDocs.Metadata.Formats.Image](../../tiffrootpackage)
* सभा [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
