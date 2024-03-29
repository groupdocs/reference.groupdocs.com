---
title: OpenTypeFlags
second_title: .NET API संदर्भ के लिए GroupDocs.Metadata
description: ओपन टइप फ़न्ट हेडर फ्लैग क प्रतनधत्व करत है
type: docs
weight: 1450
url: /hi/net/groupdocs.metadata.formats.font/opentypeflags/
---
## OpenTypeFlags enumeration

ओपन टाइप फ़ॉन्ट हेडर फ्लैग का प्रतिनिधित्व करता है।

```csharp
[Flags]
public enum OpenTypeFlags : ushort
```

### मान

| नाम | कीमत | विवरण |
| --- | --- | --- |
| None | `0` | अपरिभाषित, कोई झंडे नहीं। |
| BaselineAtY0 | `1` | y=0. पर फ़ॉन्ट के लिए आधार रेखा |
| LeftSidebearingAtX0 | `2` | x=0 पर बायां साइडबियरिंग बिंदु (केवल ट्रू टाइप रास्टराइज़र के लिए प्रासंगिक)। |
| DependOnPointSize | `4` | निर्देश बिंदु के आकार पर निर्भर हो सकते हैं। |
| ForceToInteger | `8` | पीपीएम को सभी आंतरिक स्केलर गणित के लिए पूर्णांक मानों पर बल दें; यदि यह बिट स्पष्ट है तो आंशिक पीपीएम आकार का उपयोग कर सकते हैं। |
| AlterAdvanceWidth | `10` | निर्देश अग्रिम चौड़ाई को बदल सकते हैं (अग्रिम चौड़ाई रैखिक रूप से मापी नहीं जा सकती है)। |
| Lossless | `1000` | फ़ॉन्ट डेटा "दोषरहित" है जिसके परिणामस्वरूप रूपांतरण और/या संपीड़न का अनुकूलन किया गया है। |
| Converted | `2000` | फ़ॉन्ट परिवर्तित (संगत मीट्रिक उत्पन्न करें). |
| Optimized | `4000` | फ़ॉन्ट ClearType™. के लिए अनुकूलित |
| Resort | `8000` | अंतिम रिज़ॉर्ट फ़ॉन्ट. |

### यह सभी देखें

* नाम स्थान [GroupDocs.Metadata.Formats.Font](../../groupdocs.metadata.formats.font)
* सभा [GroupDocs.Metadata](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
