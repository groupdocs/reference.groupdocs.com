---
title: TableDiscreteFunction
second_title: GroupDocs.NET API संदर्भ के लिए खोजें
description: अस्पष्ट खज एल्गरदम क प्रतनधत्व करत है जसमें शब्द क लंबई और अनुमत गलतयं क संख्य के बच पत्रचर हत है यह एल्गरदम आउटपुट मनं क तलक य चरण फ़ंक्शन द्वर नर्दष्ट कय ज सकत है
type: docs
weight: 1090
url: /hi/net/groupdocs.search.options/tablediscretefunction/
---
## TableDiscreteFunction class

अस्पष्ट खोज एल्गोरिदम का प्रतिनिधित्व करता है जिसमें शब्द की लंबाई और अनुमत गलतियों की संख्या के बीच पत्राचार होता है। यह एल्गोरिदम आउटपुट मानों की तालिका या चरण फ़ंक्शन द्वारा निर्दिष्ट किया जा सकता है।

```csharp
public class TableDiscreteFunction : FuzzyAlgorithm
```

## कंस्ट्रक्टर्स

| नाम | विवरण |
| --- | --- |
| [TableDiscreteFunction](tablediscretefunction#constructor_1)(int, int[]) | का एक नया उदाहरण प्रारंभ करता है[`TableDiscreteFunction`](../tablediscretefunction) वर्ग. |
| [TableDiscreteFunction](tablediscretefunction#constructor)(int, params Step[]) | का एक नया उदाहरण प्रारंभ करता है[`TableDiscreteFunction`](../tablediscretefunction) वर्ग. |

## तरीकों

| नाम | विवरण |
| --- | --- |
| override [GetMaxMistakeCount](../../groupdocs.search.options/tablediscretefunction/getmaxmistakecount)(int) | निर्दिष्ट अवधि की लंबाई के लिए गलतियों की अधिकतम अनुमत संख्या प्राप्त करता है। |
| override [GetSimilarityLevel](../../groupdocs.search.options/tablediscretefunction/getsimilaritylevel)(int) | निर्दिष्ट अवधि लंबाई के लिए एक समानता स्तर प्राप्त करता है। |

### टिप्पणियों

**और अधिक जानें**

* [अस्पष्ट खोज](https://docs.groupdocs.com/display/searchnet/Fuzzy+search)

### उदाहरण

उदाहरण वर्ग के एक विशिष्ट उपयोग को प्रदर्शित करता है।

```csharp
string indexFolder = @"c:\MyIndex\";
string documentsFolder = @"c:\MyDocuments\";
string query = "Einstein";

Index index = new Index(indexFolder); // निर्दिष्ट फ़ोल्डर में एक इंडेक्स बनाना
index.Add(documentsFolder); // निर्दिष्ट फ़ोल्डर से दस्तावेज़ अनुक्रमण

SearchOptions options = new SearchOptions();
options.FuzzySearch.Enabled = true; // फ़ज़ी खोज को सक्षम करना
options.FuzzySearch.FuzzyAlgorithm = new TableDiscreteFunction(1, new Step(5, 2), new Step(8, 3)); // फ़ज़ी सर्च एल्गोरिथम बनाना
// यह फ़ंक्शन 1 को 1 से 4 वर्णों के शब्दों के लिए गलतियों की अधिकतम संख्या के रूप में निर्दिष्ट करता है।
// यह 2 को 5 से 7 वर्णों के शब्दों के लिए अधिकतम गलतियों के रूप में निर्दिष्ट करता है।
// यह 3 को 8 और अधिक वर्णों के शब्दों के लिए अधिकतम गलतियों के रूप में निर्दिष्ट करता है।

SearchResult result = index.Search(query, options); // इंडेक्स में खोजें
```

### यह सभी देखें

* class [FuzzyAlgorithm](../fuzzyalgorithm)
* नाम स्थान [GroupDocs.Search.Options](../../groupdocs.search.options)
* सभा [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
