---
title: JsonDataLoadOptions
second_title: GroupDocs.Assembly .NET API संदर्भ के लिए
description: JSON डेट क पर्स करने के लए वकल्पं क प्रतनधत्व करत है
type: docs
weight: 140
url: /hi/net/groupdocs.assembly.data/jsondataloadoptions/
---
## JsonDataLoadOptions class

JSON डेटा को पार्स करने के लिए विकल्पों का प्रतिनिधित्व करता है।

```csharp
public class JsonDataLoadOptions
```

## कंस्ट्रक्टर्स

| नाम | विवरण |
| --- | --- |
| [JsonDataLoadOptions](jsondataloadoptions)() | डिफ़ॉल्ट विकल्पों के साथ इस वर्ग का एक नया उदाहरण आरंभ करता है। |

## गुण

| नाम | विवरण |
| --- | --- |
| [AlwaysGenerateRootObject](../../groupdocs.assembly.data/jsondataloadoptions/alwaysgeneraterootobject) { get; set; } | एक फ़्लैग प्राप्त करता है या सेट करता है जो दर्शाता है कि जनरेट किए गए डेटा स्रोत में हमेशा JSON root तत्व के लिए कोई ऑब्जेक्ट होगा या नहीं। यदि एक JSON मूल तत्व में एक एकल जटिल गुण है, तो ऐसी वस्तु डिफ़ॉल्ट रूप से नहीं बनाई जाती है। |
| [ExactDateTimeParseFormats](../../groupdocs.assembly.data/jsondataloadoptions/exactdatetimeparseformats) { get; set; } | JSON लोड करते समय JSON दिनांक-समय मानों को पार्स करने के लिए सटीक स्वरूप प्राप्त या सेट करता है। डिफ़ॉल्ट है**व्यर्थ** . |
| [SimpleValueParseMode](../../groupdocs.assembly.data/jsondataloadoptions/simplevalueparsemode) { get; set; } | JSON सरल मानों (शून्य, बूलियन, संख्या, पूर्णांक और स्ट्रिंग) को पार्स करने के लिए एक मोड प्राप्त या सेट करता है JSON लोड करते समय। ऐसा मोड दिनांक-समय मानों के विश्लेषण को प्रभावित नहीं करता है। डिफ़ॉल्ट हैLoose . |

### टिप्पणियों

इस वर्ग का एक उदाहरण के निर्माणकर्ताओं में पारित किया जा सकता है[`JsonDataSource`](../jsondatasource) .

### यह सभी देखें

* नाम स्थान [GroupDocs.Assembly.Data](../../groupdocs.assembly.data)
* सभा [GroupDocs.Assembly](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Assembly.dll -->
