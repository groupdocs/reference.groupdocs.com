---
title: QrCodeSearchOptions
second_title: .NET API संदर्भ के लिए GroupDocs.Signature
description: क्यूआरकड हस्तक्षरं के लए खज वकल्पं क प्रतनधत्व करत है
type: docs
weight: 1620
url: /hi/net/groupdocs.signature.options/qrcodesearchoptions/
---
## QrCodeSearchOptions class

क्यूआर-कोड हस्ताक्षरों के लिए खोज विकल्पों का प्रतिनिधित्व करता है।

```csharp
public class QrCodeSearchOptions : SearchOptions
```

## कंस्ट्रक्टर्स

| नाम | विवरण |
| --- | --- |
| [QrCodeSearchOptions](qrcodesearchoptions#constructor)() | डिफ़ॉल्ट मानों के साथ QRCodeSearchOptions वर्ग का एक नया उदाहरण आरंभ करता है। |
| [QrCodeSearchOptions](qrcodesearchoptions#constructor_1)(QrCodeType) | एनकोड प्रकार मान के साथ QRCodeSearchOptions वर्ग का एक नया उदाहरण आरंभ करता है। |
| [QrCodeSearchOptions](qrcodesearchoptions#constructor_2)(QrCodeType, string) | एनकोड प्रकार और पाठ मानों के साथ QRCodeSearchOptions वर्ग का एक नया उदाहरण प्रारंभ करता है। |

## गुण

| नाम | विवरण |
| --- | --- |
| [AllPages](../../groupdocs.signature.options/searchoptions/allpages) { get; set; } | प्रत्येक दस्तावेज़ पृष्ठ पर खोजने के लिए ध्वजांकित करें। डिफ़ॉल्ट रूप से यह मान सत्य पर सेट होता है. |
| [DataEncryption](../../groupdocs.signature.options/qrcodesearchoptions/dataencryption) { get; set; } | के कार्यान्वयन को प्राप्त या सेट करता है[`IDataEncryption`](../../groupdocs.signature.domain.extensions/idataencryption) क्यूआर-कोड सिग्नेचर टेक्स्ट या डेटा गुणों को एनकोड और डिकोड करने के लिए इंटरफ़ेस। |
| [EncodeType](../../groupdocs.signature.options/qrcodesearchoptions/encodetype) { get; set; } | क्यूआर-कोड खोजने के लिए एनकोड प्रकार संपत्ति निर्दिष्ट करता है। यदि यह मान सेट नहीं है, तो सभी समर्थित क्यूआर-कोड प्रकारों के लिए खोज संसाधित की जाती है। |
| [MatchType](../../groupdocs.signature.options/qrcodesearchoptions/matchtype) { get; set; } | क्यूआर-कोड पाठ मिलान प्रकार खोज प्राप्त या सेट करता है। इसका उपयोग केवल तभी किया जाता है जब टेक्स्ट प्रॉपर्टी सेट हो। |
| [PageNumber](../../groupdocs.signature.options/searchoptions/pagenumber) { get; set; } | खोज के लिए दस्तावेज़ पृष्ठ संख्या प्राप्त या सेट करता है। मान वैकल्पिक है। |
| [PagesSetup](../../groupdocs.signature.options/searchoptions/pagessetup) { get; set; } | हस्ताक्षर खोजने के लिए पृष्ठों को निर्दिष्ट करने के विकल्प। |
| [ReturnContent](../../groupdocs.signature.options/qrcodesearchoptions/returncontent) { get; set; } | दस्तावेज़ पृष्ठ पर हस्ताक्षर की क्यूआर-कोड छवि सामग्री को पकड़ने के लिए ध्वज प्राप्त या सेट करता है। यदि यह ध्वज सही है, तो क्यूआर-कोड हस्ताक्षर छवि सामग्री आवश्यक प्रारूप द्वारा अपरिष्कृत छवि डेटा रखेगी[`ReturnContentType`](./returncontenttype) . डिफ़ॉल्ट रूप से यह विकल्प अक्षम है। |
| [ReturnContentType](../../groupdocs.signature.options/qrcodesearchoptions/returncontenttype) { get; set; } | रिटर्नकंटेंट गुण सक्षम होने पर क्यूआर-कोड हस्ताक्षर की लौटाई गई छवि सामग्री के फ़ाइल प्रकार को निर्दिष्ट करता है। डिफ़ॉल्ट रूप से यह शून्य पर सेट होता है। इसका मतलब क्यूआर-कोड छवि सामग्री को मूल स्वरूप में वापस करना है। यह छवि प्रारूप निर्दिष्ट किया गया है[`Format`](../../groupdocs.signature.domain/qrcodesignature/format) संभावित समर्थित मान हैं: FileType.JPEG, FileType.PNG, FileType.BMP। यदि प्रदान किया गया प्रारूप समर्थित नहीं है, तो मूल .png में क्यूआर-कोड छवि सामग्री वापस आ जाएगी। |
| [SkipExternal](../../groupdocs.signature.options/searchoptions/skipexternal) { get; set; } | केवल IsSignature के रूप में चिह्नित हस्ताक्षर वापस करने के लिए फ़्लैग करें। डिफ़ॉल्ट मान असत्य है जो निर्दिष्ट मानदंडों से मेल खाने वाले सभी हस्ताक्षरों को वापस करने का संकेत देता है। |
| [Text](../../groupdocs.signature.options/qrcodesearchoptions/text) { get; set; } | क्यूआर-कोड सिग्नेचर टेक्स्ट निर्दिष्ट करता है यदि इसे खोजा और मिलान किया जाना चाहिए। |

### टिप्पणियों

**और अधिक जानें**

* GroupDocs द्वारा क्यूआर-कोड इलेक्ट्रॉनिक हस्ताक्षर के लिए खोज का मूल उपयोग। हस्ताक्षर: [किसी दस्तावेज़ में क्यूआर-कोड हस्ताक्षरों की ई-खोज कैसे करें](https://docs.groupdocs.com/display/signaturenet/Search+for+QR-Code+e-signatures)
* GroupDocs के साथ क्यूआर-कोड इलेक्ट्रॉनिक हस्ताक्षर के लिए खोज की सेटिंग का उन्नत उपयोग। हस्ताक्षर: [एक दस्तावेज़ और अतिरिक्त सेटिंग्स में ईसर्च क्यूआर-कोड हस्ताक्षरों का उन्नत उपयोग](https://docs.groupdocs.com/display/signaturenet/Advanced+search+for+QR-code+signatures)

### यह सभी देखें

* class [SearchOptions](../searchoptions)
* नाम स्थान [GroupDocs.Signature.Options](../../groupdocs.signature.options)
* सभा [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
