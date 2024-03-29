---
title: EbookEditOptions
second_title: .NET API संदर्भ के लिए GroupDocs.Editor
description: सभ समर्थत स्वरूपं में ईपुस्तक दस्तवेज़ं के संपदन के लए कस्टम वकल्पं क नर्दष्ट और समयजत करने क अनुमत देत है ePub MOBI और AZW3.
type: docs
weight: 840
url: /hi/net/groupdocs.editor.options/ebookeditoptions/
---
## EbookEditOptions class

सभी समर्थित स्वरूपों में ई-पुस्तक दस्तावेज़ों के संपादन के लिए कस्टम विकल्पों को निर्दिष्ट और समायोजित करने की अनुमति देता है: ePub, MOBI, और AZW3.

```csharp
public sealed class EbookEditOptions : IEditOptions
```

## कंस्ट्रक्टर्स

| नाम | विवरण |
| --- | --- |
| [EbookEditOptions](ebookeditoptions#constructor)() | का एक नया उदाहरण प्रारंभ करता है[`EbookEditOptions`](../ebookeditoptions) वर्ग, जहां सभी विकल्प उनके डिफ़ॉल्ट मान पर सेट होते हैं |
| [EbookEditOptions](ebookeditoptions#constructor_1)(bool) | का एक नया उदाहरण प्रारंभ करता है[`EbookEditOptions`](../ebookeditoptions) निर्दिष्ट पेजिनेशन मोड के साथ वर्ग |

## गुण

| नाम | विवरण |
| --- | --- |
| [EnableLanguageInformation](../../groupdocs.editor.options/ebookeditoptions/enablelanguageinformation) { get; set; } | निर्दिष्ट करता है कि भाषा की जानकारी HTML मार्कअप को 'लैंग' HTML विशेषताओं के रूप में निर्यात की जाती है या नहीं। यह विकल्प बहु-भाषा दस्तावेज़ों के राउंडट्रिप रूपांतरण के लिए उपयोगी हो सकता है। डिफ़ॉल्ट रूप से यह अक्षम है (`असत्य`. |
| [EnablePagination](../../groupdocs.editor.options/ebookeditoptions/enablepagination) { get; set; } | परिणामी HTML दस्तावेज़ में पेजिनेशन को सक्षम या अक्षम करने की अनुमति देता है। डिफ़ॉल्ट रूप से अक्षम है (`असत्य`. |

### टिप्पणियों

समर्थित ई-पुस्तक प्रारूप:

1. [को ePub](https://docs.fileformat.com/ebook/epub/) (इलेक्ट्रॉनिक प्रकाशन)
2. [मोबी](https://docs.fileformat.com/ebook/mobi/) (मोबीपॉकेट)
3. [AZW3](https://docs.fileformat.com/ebook/azw3/) (किंडल फॉर्मेट 8टी)

### यह सभी देखें

* interface [IEditOptions](../ieditoptions)
* नाम स्थान [GroupDocs.Editor.Options](../../groupdocs.editor.options)
* सभा [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
