---
title: XmlDataSource
second_title: GroupDocs.Assembly .NET API संदर्भ के लिए
description: कस दस्तवेज़ क असेंबल करते समय उपयग क जने वल XML फ़इल य स्ट्रम के डेट तक पहुँच प्रदन करत है
type: docs
weight: 180
url: /hi/net/groupdocs.assembly.data/xmldatasource/
---
## XmlDataSource class

किसी दस्तावेज़ को असेंबल करते समय उपयोग की जाने वाली XML फ़ाइल या स्ट्रीम के डेटा तक पहुँच प्रदान करता है।

```csharp
public class XmlDataSource
```

## कंस्ट्रक्टर्स

| नाम | विवरण |
| --- | --- |
| [XmlDataSource](xmldatasource#constructor)(Stream) | XML डेटा लोड करने के लिए डिफ़ॉल्ट विकल्पों का उपयोग करके XML स्ट्रीम से डेटा के साथ एक नया डेटा स्रोत बनाता है। |
| [XmlDataSource](xmldatasource#constructor_4)(string) | XML डेटा लोड करने के लिए डिफ़ॉल्ट विकल्पों का उपयोग करके XML फ़ाइल से डेटा के साथ एक नया डेटा स्रोत बनाता है। |
| [XmlDataSource](xmldatasource#constructor_2)(Stream, Stream) | XML स्कीमा डेफिनिशन स्ट्रीम का उपयोग करके XML स्ट्रीम से डेटा के साथ एक नया डेटा स्रोत बनाता है। XML डेटा लोड करने के लिए डिफ़ॉल्ट विकल्प का उपयोग किया जाता है। |
| [XmlDataSource](xmldatasource#constructor_1)(Stream, XmlDataLoadOptions) | XML डेटा लोड करने के लिए निर्दिष्ट विकल्पों का उपयोग करके XML स्ट्रीम से डेटा के साथ एक नया डेटा स्रोत बनाता है। |
| [XmlDataSource](xmldatasource#constructor_6)(string, string) | XML स्कीमा परिभाषा फ़ाइल का उपयोग करके XML फ़ाइल से डेटा के साथ एक नया डेटा स्रोत बनाता है। XML डेटा लोड करने के लिए डिफ़ॉल्ट विकल्प का उपयोग किया जाता है। |
| [XmlDataSource](xmldatasource#constructor_5)(string, XmlDataLoadOptions) | XML डेटा लोड करने के लिए निर्दिष्ट विकल्पों का उपयोग करके XML फ़ाइल से डेटा के साथ एक नया डेटा स्रोत बनाता है। |
| [XmlDataSource](xmldatasource#constructor_3)(Stream, Stream, XmlDataLoadOptions) | XML स्कीमा डेफिनिशन स्ट्रीम का उपयोग करके XML स्ट्रीम से डेटा के साथ एक नया डेटा स्रोत बनाता है। XML डेटा लोड करने के लिए निर्दिष्ट विकल्पों का उपयोग किया जाता है। |
| [XmlDataSource](xmldatasource#constructor_7)(string, string, XmlDataLoadOptions) | XML स्कीमा परिभाषा फ़ाइल का उपयोग करके XML फ़ाइल से डेटा के साथ एक नया डेटा स्रोत बनाता है। XML डेटा लोड करने के लिए निर्दिष्ट विकल्पों का उपयोग किया जाता है। |

### टिप्पणियों

किसी दस्तावेज़ को असेंबल करते समय संबंधित फ़ाइल या स्ट्रीम के डेटा तक पहुँचने के लिए, इस वर्ग के एक उदाहरण को डेटा स्रोत के रूप में पास करें[`DocumentAssembler`](../../groupdocs.assembly/documentassembler) .इकट्ठा दस्तावेज़ ओवरलोड।

टेम्प्लेट दस्तावेज़ों में, यदि एक शीर्ष-स्तरीय XML तत्व में केवल उसी प्रकार के तत्वों की एक सूची है, तो a[`XmlDataSource`](../xmldatasource) उदाहरण के साथ उसी तरह व्यवहार किया जाना चाहिए जैसे कि यह थाDataTable उदाहरण। अन्यथा, ए[`XmlDataSource`](../xmldatasource) उदाहरण को उसी तरह से व्यवहार किया जाना चाहिए जैसे कि यह एक थाDataRowउदाहरण। अधिक जानकारी के लिए, टेम्पलेट सिंटैक्स संदर्भ देखें

जब XML स्कीमा परिभाषा इस वर्ग के एक कंस्ट्रक्टर को पास की जाती है, तो स्कीमा के अनुसार सरल XML तत्वों के डेटा प्रकार और विशेषताएँ निर्धारित की जाती हैं। इसलिए टेम्प्लेट दस्तावेज़ों में, आप केवल स्ट्रिंग्स के बजाय टाइप किए गए मानों के साथ काम कर सकते हैं।

जब एक्सएमएल स्कीमा परिभाषा इस वर्ग के निर्माता को पारित नहीं की जाती है, तो सरल एक्सएमएल तत्वों के डेटा प्रकार और गुण उनके स्ट्रिंग प्रस्तुतियों पर स्वचालित रूप से निर्धारित होते हैं। तो टेम्पलेट दस्तावेज़ों में, आप इस मामले में भी टाइप किए गए मानों के साथ काम कर सकते हैं। इंजन स्वचालित रूप से निम्नलिखित प्रकार के मूल्यों को पहचानने में सक्षम है:

* `लंबा?`
* `दोहरा?`
* `बूल?`
* `दिनांक समय?`
* `डोरी`

ध्यान दें कि कार्य करने के लिए डेटा प्रकारों की स्वत: पहचान के लिए, सरल XML तत्वों के मानों का स्ट्रिंग प्रतिनिधित्व और विशेषताएँ अपरिवर्तनीय संस्कृति सेटिंग्स का उपयोग करके बनाई जानी चाहिए।

एक्सएमएल डेटा लोडिंग के डिफ़ॉल्ट व्यवहार को ओवरराइड करने के लिए, प्रारंभ करें और पास करें[`XmlDataLoadOptions`](../xmldataloadoptions) उदाहरण इस वर्ग के एक निर्माता के लिए।

### यह सभी देखें

* नाम स्थान [GroupDocs.Assembly.Data](../../groupdocs.assembly.data)
* सभा [GroupDocs.Assembly](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Assembly.dll -->
