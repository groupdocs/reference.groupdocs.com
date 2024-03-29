---
title: FileLogger
second_title: GroupDocs.NET API संदर्भ के लिए खोजें
description: एक लकड़हरे क प्रतनधत्व करत है ज घटनओं और त्रुटयं क एक स्थनय फ़इल में लग करत है
type: docs
weight: 140
url: /hi/net/groupdocs.search.common/filelogger/
---
## FileLogger class

एक लकड़हारे का प्रतिनिधित्व करता है जो घटनाओं और त्रुटियों को एक स्थानीय फ़ाइल में लॉग करता है।

```csharp
public class FileLogger : ILogger
```

## कंस्ट्रक्टर्स

| नाम | विवरण |
| --- | --- |
| [FileLogger](filelogger)(string, double) | का एक नया उदाहरण प्रारंभ करता है[`FileLogger`](../filelogger) वर्ग. |

## गुण

| नाम | विवरण |
| --- | --- |
| [FilePath](../../groupdocs.search.common/filelogger/filepath) { get; } | लॉग फ़ाइल पथ प्राप्त करता है। |
| [MaxSize](../../groupdocs.search.common/filelogger/maxsize) { get; } | मेगाबाइट्स में लॉग फ़ाइल का अधिकतम आकार प्राप्त करता है। |

## तरीकों

| नाम | विवरण |
| --- | --- |
| [Error](../../groupdocs.search.common/filelogger/error)(string) | इंडेक्स में हुई त्रुटि को लॉग करता है। |
| [Trace](../../groupdocs.search.common/filelogger/trace)(string) | इंडेक्स में हुई एक घटना को लॉग करता है। |

### टिप्पणियों

**और अधिक जानें**

* [लॉगिंग](https://docs.groupdocs.com/display/searchnet/Logging)

### उदाहरण

उदाहरण वर्ग के एक विशिष्ट उपयोग को प्रदर्शित करता है।

```csharp
string indexFolder = @"c:\MyIndex\";
string documentsFolder = @"c:\MyDocuments\";
string query = "Einstein";
string logPath = @"c:\Log.txt";

IndexSettings settings = new IndexSettings();
settings.Logger = new FileLogger(logPath, 4.0); // लॉग फ़ाइल का पथ और अधिकतम 4 एमबी की लंबाई निर्दिष्ट करना

Index index = new Index(indexFolder, settings); // निर्दिष्ट फ़ोल्डर में एक इंडेक्स बनाना

index.Add(documentsFolder); // निर्दिष्ट फ़ोल्डर से दस्तावेज़ अनुक्रमण

SearchResult result = index.Search(query); // इंडेक्स में खोजें
```

### यह सभी देखें

* interface [ILogger](../ilogger)
* नाम स्थान [GroupDocs.Search.Common](../../groupdocs.search.common)
* सभा [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
