---
title: GetIndexingReports
second_title: GroupDocs.NET API संदर्भ के लिए खोजें
description: इंडेक्संग ऑपरेशंस पर रपर्ट प्रप्त करत है
type: docs
weight: 160
url: /hi/net/groupdocs.search/index/getindexingreports/
---
## Index.GetIndexingReports method

इंडेक्सिंग ऑपरेशंस पर रिपोर्ट प्राप्त करता है।

```csharp
public IndexingReport[] GetIndexingReports()
```

### प्रतिलाभ की मात्रा

अनुक्रमण रिपोर्ट करता है।

### उदाहरण

उदाहरण दर्शाता है कि इंडेक्सिंग रिपोर्ट कैसे प्राप्त करें।

```csharp
string indexFolder = @"c:\MyIndex\";
string documentsFolder = @"c:\MyDocuments\";

Index index = new Index(indexFolder); // निर्दिष्ट फ़ोल्डर में इंडेक्स बनाना
index.Add(documentsFolder); // निर्दिष्ट फ़ोल्डर से दस्तावेज़ अनुक्रमण

IndexingReport[] reports = index.GetIndexingReports(); // इंडेक्सिंग रिपोर्ट प्राप्त करना
```

### यह सभी देखें

* class [IndexingReport](../../../groupdocs.search.common/indexingreport)
* class [Index](../../index)
* नाम स्थान [GroupDocs.Search](../../index)
* सभा [GroupDocs.Search](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
