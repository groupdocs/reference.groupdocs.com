---
title: DateFormats
second_title: GroupDocs.NET API संदर्भ के लिए खोजें
description: दनंक सम खज के लए दनंक स्वरूपं क संग्रह प्रप्त करत है डफ़ल्ट दनंक प्ररूप dd.MM.yyyy MM/dd/yyyy और yyyyMMdd हैं
type: docs
weight: 30
url: /hi/net/groupdocs.search.options/searchoptions/dateformats/
---
## SearchOptions.DateFormats property

दिनांक सीमा खोज के लिए दिनांक स्वरूपों का संग्रह प्राप्त करता है। डिफ़ॉल्ट दिनांक प्रारूप 'dd.MM.yyyy', 'MM/dd/yyyy', और 'yyyy-MM-dd' हैं।

```csharp
public DateFormatCollection DateFormats { get; }
```

### संपत्ति मूल्य

दिनांक श्रेणी खोज के लिए दिनांक स्वरूपों का संग्रह।

### उदाहरण

उदाहरण दर्शाता है कि खोज के लिए दिनांक प्रारूप कैसे सेट करें।

```csharp
string indexFolder = @"c:\MyIndex\";
string documentsFolder = @"c:\MyDocuments\";
string query = "Einstein";

Index index = new Index(indexFolder); // निर्दिष्ट फ़ोल्डर में एक इंडेक्स बनाना
index.Add(documentsFolder); // निर्दिष्ट फ़ोल्डर से दस्तावेज़ अनुक्रमण

SearchOptions options = new SearchOptions();
options.DateFormats.Clear(); // डिफ़ॉल्ट दिनांक स्वरूपों को हटाना
DateFormatElement[] elements = new DateFormatElement[]
{
    DateFormatElement.MonthTwoDigits,
    DateFormatElement.DayOfMonthTwoDigits,
    DateFormatElement.YearFourDigits,
};
// दिनांक स्वरूप पैटर्न 'MM/dd/yyyy' बनाना
DateFormat dateFormat = new DateFormat(elements, "/");
options.DateFormats.Add(dateFormat);

SearchResult result = index.Search(query, options); // इंडेक्स में खोजें
```

### यह सभी देखें

* class [DateFormatCollection](../../dateformatcollection)
* class [SearchOptions](../../searchoptions)
* नाम स्थान [GroupDocs.Search.Options](../../searchoptions)
* सभा [GroupDocs.Search](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
