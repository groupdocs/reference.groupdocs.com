---
title: GetSearchReports
second_title: GroupDocs.NET API संदर्भ के लिए खोजें
description: खज कर्यं पर रपर्ट प्रप्त करत है
type: docs
weight: 170
url: /hi/net/groupdocs.search/index/getsearchreports/
---
## Index.GetSearchReports method

खोज कार्यों पर रिपोर्ट प्राप्त करता है।

```csharp
public SearchReport[] GetSearchReports()
```

### प्रतिलाभ की मात्रा

खोज रिपोर्ट।

### उदाहरण

उदाहरण दर्शाता है कि खोज रिपोर्ट कैसे प्राप्त करें।

```csharp
string indexFolder = @"c:\MyIndex\";
string documentsFolder = @"c:\MyDocuments\";
string query1 = "Einstein";
string query2 = "Newton";

Index index = new Index(indexFolder); // निर्दिष्ट फ़ोल्डर में इंडेक्स बनाना
index.Add(documentsFolder); // निर्दिष्ट फ़ोल्डर से दस्तावेज़ अनुक्रमण

SearchResult result1 = index.Search(query1); // खोज कर
SearchResult result2 = index.Search(query2);
SearchResult result3 = index.Search(query1 + " & " + query2);

SearchReport[] reports = index.GetSearchReports(); // खोज रिपोर्ट प्राप्त करना
```

### यह सभी देखें

* class [SearchReport](../../../groupdocs.search.common/searchreport)
* class [Index](../../index)
* नाम स्थान [GroupDocs.Search](../../index)
* सभा [GroupDocs.Search](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
