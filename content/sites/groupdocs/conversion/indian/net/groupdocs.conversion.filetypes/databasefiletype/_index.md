---
title: DatabaseFileType
second_title: .NET API संदर्भ के लिए GroupDocs.Conversion
description: डेटबेस दस्तवेजं क परभषत करत है नम्न फ़इल प्रकर शमल हैं Nsf./databasefiletype/nsfLog./databasefiletype/logSql./databasefiletype/sql
type: docs
weight: 890
url: /hi/net/groupdocs.conversion.filetypes/databasefiletype/
---
## DatabaseFileType class

डेटाबेस दस्तावेजों को परिभाषित करता है। निम्न फ़ाइल प्रकार शामिल हैं: [`Nsf`](./nsf)[`Log`](./log)[`Sql`](./sql)

```csharp
public sealed class DatabaseFileType : FileType
```

## कंस्ट्रक्टर्स

| नाम | विवरण |
| --- | --- |
| [DatabaseFileType](databasefiletype)() | सीरियलाइज़ेशन कंस्ट्रक्टर |

## गुण

| नाम | विवरण |
| --- | --- |
| [Description](../../groupdocs.conversion.filetypes/filetype/description) { get; } | फ़ाइल प्रकार विवरण |
| [Extension](../../groupdocs.conversion.filetypes/filetype/extension) { get; } | फ़ाइल एक्सटेंशन |
| [Family](../../groupdocs.conversion.filetypes/filetype/family) { get; } | फ़ाइल परिवार |
| [FileFormat](../../groupdocs.conversion.filetypes/filetype/fileformat) { get; } | फ़ाइल स्वरूप |

## तरीकों

| नाम | विवरण |
| --- | --- |
| [CompareTo](../../groupdocs.conversion.contracts/enumeration/compareto)(object) | वर्तमान वस्तु की तुलना अन्य से करता है। |
| override [Equals](../../groupdocs.conversion.filetypes/filetype/equals)(Enumeration) | निर्धारित करता है कि क्या दो वस्तु उदाहरण समान हैं। |
| override [Equals](../../groupdocs.conversion.contracts/enumeration/equals)(object) | निर्धारित करता है कि क्या दो वस्तु उदाहरण समान हैं। |
| override [GetHashCode](../../groupdocs.conversion.contracts/enumeration/gethashcode)() | डिफ़ॉल्ट हैश फ़ंक्शन के रूप में कार्य करता है। |
| override [ToString](../../groupdocs.conversion.filetypes/filetype/tostring)() | स्ट्रिंग प्रतिनिधित्व |

## खेत

| नाम | विवरण |
| --- | --- |
| static readonly [Log](../../groupdocs.conversion.filetypes/databasefiletype/log) | .लॉग एक्सटेंशन वाली फ़ाइल में टाइमस्टैम्प के साथ सादे पाठ की सूची होती है। आमतौर पर, डेवलपर्स या उपयोगकर्ताओं को एक निश्चित समय अवधि में क्या हो रहा था, यह ट्रैक करने में मदद करने के लिए सॉफ़्टवेयर या ऑपरेटिंग सिस्टम द्वारा कुछ गतिविधि विवरण लॉग किया जाता है। इस फ़ाइल प्रारूप के बारे में और जानें[यहाँ](https://docs.fileformat.com/database/log) . |
| static readonly [Nsf](../../groupdocs.conversion.filetypes/databasefiletype/nsf) | .nsf (नोट्स स्टोरेज फैसिलिटी) एक्सटेंशन वाली एक फ़ाइल IBM नोट्स सॉफ़्टवेयर द्वारा उपयोग किया जाने वाला एक डेटाबेस फ़ाइल स्वरूप है, जिसे पहले लोटस नोट्स के रूप में जाना जाता था। यह ईमेल, अपॉइंटमेंट, दस्तावेज़, फ़ॉर्म और व्यू जैसे अलग-अलग तरह के ऑब्जेक्ट स्टोर करने के लिए स्कीमा को परिभाषित करता है. इस फ़ाइल फ़ॉर्मैट के बारे में ज़्यादा जानें[यहाँ](https://docs.fileformat.com/database/nsf) . |
| static readonly [Sql](../../groupdocs.conversion.filetypes/databasefiletype/sql) | .sql एक्सटेंशन वाली फाइल एक स्ट्रक्चर्ड क्वेरी लैंग्वेज (SQL) फाइल है जिसमें रिलेशनल डेटाबेस के साथ काम करने के लिए कोड होता है। इसका उपयोग डेटाबेस पर CRUD (क्रिएट, रीड, अपडेट और डिलीट) ऑपरेशंस के लिए SQL स्टेटमेंट लिखने के लिए किया जाता है। इस फ़ाइल प्रारूप के बारे में और जानें[यहाँ](https://docs.fileformat.com/database/sql) . |

### यह सभी देखें

* class [FileType](../filetype)
* नाम स्थान [GroupDocs.Conversion.FileTypes](../../groupdocs.conversion.filetypes)
* सभा [GroupDocs.Conversion](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Conversion.dll -->
