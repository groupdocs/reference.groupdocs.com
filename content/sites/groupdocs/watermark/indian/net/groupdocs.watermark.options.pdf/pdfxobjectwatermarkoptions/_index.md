---
title: PdfXObjectWatermarkOptions
second_title: .NET API संदर्भ के लिए GroupDocs.Watermark
description: पडएफ दस्तवेज़ में एक्सऑब्जेक्ट वटरमर्क जड़ते समय वटरमर्क जड़ने के वकल्पं क प्रतनधत्व करत है
type: docs
weight: 1920
url: /hi/net/groupdocs.watermark.options.pdf/pdfxobjectwatermarkoptions/
---
## PdfXObjectWatermarkOptions class

पीडीएफ दस्तावेज़ में एक्सऑब्जेक्ट वॉटरमार्क जोड़ते समय वॉटरमार्क जोड़ने के विकल्पों का प्रतिनिधित्व करता है।

```csharp
public sealed class PdfXObjectWatermarkOptions : PdfWatermarkOptions
```

## कंस्ट्रक्टर्स

| नाम | विवरण |
| --- | --- |
| [PdfXObjectWatermarkOptions](pdfxobjectwatermarkoptions)() | का एक नया उदाहरण प्रारंभ करता है[`PdfXObjectWatermarkOptions`](../pdfxobjectwatermarkoptions) वर्ग. |

## गुण

| नाम | विवरण |
| --- | --- |
| [PageIndex](../../groupdocs.watermark.options.pdf/pdfxobjectwatermarkoptions/pageindex) { get; set; } | वॉटरमार्क जोड़ने के लिए पृष्ठ अनुक्रमणिका प्राप्त या सेट करता है. |

### टिप्पणियों

**और अधिक जानें:**

* [पीडीएफ दस्तावेजों में वॉटरमार्क जोड़ें](https://docs.groupdocs.com/display/watermarknet/Add+watermarks+to+PDF+documents)

### उदाहरण

पीडीएफ दस्तावेज़ के किसी विशेष पृष्ठ पर वॉटरमार्क जोड़ें।

```csharp
PdfLoadOptions loadOptions = new PdfLoadOptions();
using (Watermarker watermarker = new Watermarker(@"C:\doc.pdf", loadOptions))
using (ImageWatermark watermark = new ImageWatermark(@"C:\watermark.png"))
{
    PdfXObjectWatermarkOptions options = new PdfXObjectWatermarkOptions();
    options.PageIndex = 0;

    watermarker.Add(watermark, options);
    watermarker.Save();
}
```

### यह सभी देखें

* class [PdfWatermarkOptions](../pdfwatermarkoptions)
* नाम स्थान [GroupDocs.Watermark.Options.Pdf](../../groupdocs.watermark.options.pdf)
* सभा [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
