---
title: SignatureSettings
second_title: .NET API संदर्भ के लिए GroupDocs.Signature
description: अनुकूलन के लए सेटंग्स क परभषत करत हैSignature./signature व्यवहर.
type: docs
weight: 1890
url: /hi/net/groupdocs.signature/signaturesettings/
---
## SignatureSettings class

अनुकूलन के लिए सेटिंग्स को परिभाषित करता है[`Signature`](../signature) व्यवहार.

```csharp
public class SignatureSettings
```

## कंस्ट्रक्टर्स

| नाम | विवरण |
| --- | --- |
| [SignatureSettings](signaturesettings#constructor)() | डिफ़ॉल्ट मानों के साथ डिफ़ॉल्ट सिग्नेचरसेटिंग इंस्टेंस बनाता है। |
| [SignatureSettings](signaturesettings#constructor_1)(ILogger) | लॉगर कार्यान्वयन के साथ डिफ़ॉल्ट सिग्नेचरसेटिंग इंस्टेंस बनाता है। |

## गुण

| नाम | विवरण |
| --- | --- |
| [DefaultCulture](../../groupdocs.signature/signaturesettings/defaultculture) { get; set; } | दस्तावेज़ प्रसंस्करण के दौरान उपयोग किए जाने वाले डिफ़ॉल्ट संस्कृति को प्राप्त या सेट करता है। डिफ़ॉल्ट मान "en-US" है. |
| [IncludeStandardMetadataSignatures](../../groupdocs.signature/signaturesettings/includestandardmetadatasignatures) { get; set; } | मेटाडेटा सूची में एम्बेड किए गए मानक दस्तावेज़ मेटाडेटा हस्ताक्षरों जैसे लेखक, स्वामी, दस्तावेज़ निर्माण दिनांक, संशोधित दिनांक आदि को शामिल करने के लिए फ़्लैग प्राप्त करता है या सेट करता है. यदि यह फ़्लैग गलत पर सेट है (डिफ़ॉल्ट रूप से) तो GetDocumentInfo में ये मेटाडेटा शामिल नहीं होंगे हस्ताक्षर. जब यह फ़्लैग सही पर सेट होता है, तो दस्तावेज़ की जानकारी में ये मानक मेटाडेटा हस्ताक्षर शामिल होंगे. |
| [Logger](../../groupdocs.signature/signaturesettings/logger) { get; } | लॉगिंग के लिए उपयोग किया जाने वाला लॉगर कार्यान्वयन (त्रुटियां, चेतावनियां, निशान)।[`ILogger`](../../groupdocs.signature.logging/ilogger) . |
| [LogLevel](../../groupdocs.signature/signaturesettings/loglevel) { get; set; } | संदेशों को सीमित करने के लिए लॉगिंग का स्तर (सभी, निशान, चेतावनियां, त्रुटियां)।[`LogLevel`](./loglevel) . डिफ़ॉल्ट रूप से सभी स्तर का प्रकार सेट है। |
| [SaveDocumentOnEmptyDelete](../../groupdocs.signature/signaturesettings/savedocumentonemptydelete) { get; set; } | स्रोत दस्तावेज़ को फिर से सहेजने के लिए फ़्लैग प्राप्त करता है या सेट करता है जब हटाने की विधि में हटाने के लिए कोई प्रभावित हस्ताक्षर नहीं होते हैं। मिटाने की विधि में हटाने के लिए कोई हस्ताक्षर नहीं है। |
| [SaveDocumentOnEmptyUpdate](../../groupdocs.signature/signaturesettings/savedocumentonemptyupdate) { get; set; } | स्रोत दस्तावेज़ को फिर से सहेजने के लिए फ़्लैग करता है या सेट करता है जब अपडेट विधि में अपडेट करने के लिए कोई हस्ताक्षर नहीं होते हैं। विधि में अद्यतन करने के लिए कोई हस्ताक्षर नहीं है। |
| [ShowDeletedSignaturesInfo](../../groupdocs.signature/signaturesettings/showdeletedsignaturesinfo) { get; set; } | फ़्लैग प्राप्त करता है या सेट करता है जिसमें दस्तावेज़ जानकारी परिणाम में हटाए गए हस्ताक्षर शामिल हैं। प्रत्येक हस्ताक्षर[`BaseSignature`](../../groupdocs.signature.domain/basesignature) ध्वज हटा दिया गया है[`Deleted`](../../groupdocs.signature.domain/basesignature/deleted) यह पता लगाने के लिए कि क्या इसे हटा दिया गया था। |

### यह सभी देखें

* नाम स्थान [GroupDocs.Signature](../../groupdocs.signature)
* सभा [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
