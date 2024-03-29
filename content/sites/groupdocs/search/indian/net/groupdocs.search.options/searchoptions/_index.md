---
title: SearchOptions
second_title: GroupDocs.NET API संदर्भ के लिए खोजें
description: खज ऑपरेशन के लए वकल्प प्रदन करत है
type: docs
weight: 1040
url: /hi/net/groupdocs.search.options/searchoptions/
---
## SearchOptions class

खोज ऑपरेशन के लिए विकल्प प्रदान करता है।

```csharp
public class SearchOptions
```

## कंस्ट्रक्टर्स

| नाम | विवरण |
| --- | --- |
| [SearchOptions](searchoptions)() | का एक नया उदाहरण प्रारंभ करता है[`SearchOptions`](../searchoptions) वर्ग. |

## गुण

| नाम | विवरण |
| --- | --- |
| [Cancellation](../../groupdocs.search.options/searchoptions/cancellation) { get; set; } | ऑपरेशन कैंसलेशन ऑब्जेक्ट प्राप्त या सेट करता है। डिफ़ॉल्ट मान है`व्यर्थ` . |
| [DateFormats](../../groupdocs.search.options/searchoptions/dateformats) { get; } | दिनांक सीमा खोज के लिए दिनांक स्वरूपों का संग्रह प्राप्त करता है। डिफ़ॉल्ट दिनांक प्रारूप 'dd.MM.yyyy', 'MM/dd/yyyy', और 'yyyy-MM-dd' हैं। |
| [FuzzySearch](../../groupdocs.search.options/searchoptions/fuzzysearch) { get; } | अस्पष्ट खोज विकल्प प्राप्त करता है। |
| [IsChunkSearch](../../groupdocs.search.options/searchoptions/ischunksearch) { get; set; } | चंक्स द्वारा खोज का ध्वज प्राप्त या सेट करता है। डिफ़ॉल्ट मान है`असत्य` . |
| [KeyboardLayoutCorrector](../../groupdocs.search.options/searchoptions/keyboardlayoutcorrector) { get; } | कीबोर्ड लेआउट सुधारक विकल्प प्राप्त करता है। |
| [MaxOccurrenceCountPerTerm](../../groupdocs.search.options/searchoptions/maxoccurrencecountperterm) { get; set; } | खोज क्वेरी में प्रत्येक शब्द की अधिकतम संख्या को प्राप्त या सेट करता है। डिफ़ॉल्ट मान है`100000` . |
| [MaxTotalOccurrenceCount](../../groupdocs.search.options/searchoptions/maxtotaloccurrencecount) { get; set; } | एक खोज क्वेरी में सभी शब्दों की अधिकतम संख्या को प्राप्त या सेट करता है। डिफ़ॉल्ट मान है`500000` . |
| [SearchDocumentFilter](../../groupdocs.search.options/searchoptions/searchdocumentfilter) { get; set; } | खोज दस्तावेज़ फ़िल्टर प्राप्त या सेट करता है। [`SearchDocumentFilter`](./searchdocumentfilter) समावेशन तर्क पर काम करता है। उपयोग करें[`SearchDocumentFilter`](../searchdocumentfilter) एक खोज दस्तावेज़ फ़िल्टर उदाहरण के निर्माण के लिए वर्ग. डिफ़ॉल्ट मान है`व्यर्थ` , जिसका अर्थ है कि सभी पाए गए दस्तावेज़ वापस कर दिए जाएंगे. |
| [SpellingCorrector](../../groupdocs.search.options/searchoptions/spellingcorrector) { get; } | वर्तनी सुधारक विकल्प प्राप्त करता है। |
| [UseCaseSensitiveSearch](../../groupdocs.search.options/searchoptions/usecasesensitivesearch) { get; set; } | केस संवेदी खोज का ध्वज प्राप्त या सेट करता है। डिफ़ॉल्ट मान है`असत्य` . |
| [UseHomophoneSearch](../../groupdocs.search.options/searchoptions/usehomophonesearch) { get; set; } | खोज में उपयोग होमोफ़ोन का ध्वज प्राप्त या सेट करता है। डिफ़ॉल्ट मान है`असत्य` . |
| [UseSynonymSearch](../../groupdocs.search.options/searchoptions/usesynonymsearch) { get; set; } | खोज में समानार्थक शब्द का प्रयोग करता है या सेट करता है। डिफ़ॉल्ट मान है`असत्य` . |
| [UseWordFormsSearch](../../groupdocs.search.options/searchoptions/usewordformssearch) { get; set; } | खोज में विभिन्न शब्द रूपों के उपयोग का ध्वज प्राप्त करता है या सेट करता है। डिफ़ॉल्ट मान है`असत्य` . |

### टिप्पणियों

**और अधिक जानें**

* [खोज विकल्प](https://docs.groupdocs.com/display/searchnet/Search+options)

### यह सभी देखें

* नाम स्थान [GroupDocs.Search.Options](../../groupdocs.search.options)
* सभा [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
