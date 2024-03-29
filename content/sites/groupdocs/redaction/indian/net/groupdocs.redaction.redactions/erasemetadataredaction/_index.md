---
title: EraseMetadataRedaction
second_title: .NET API संदर्भ के लिए GroupDocs.Redaction
description: एक मेटडेट रडक्शन क प्रतनधत्व करत है ज दस्तवेज़ से वशष्ट मेटडेट फ़ल्टर से मेल खने वले सभ मेटडेट य मेटडेट क मट देत है
type: docs
weight: 480
url: /hi/net/groupdocs.redaction.redactions/erasemetadataredaction/
---
## EraseMetadataRedaction class

एक मेटाडेटा रिडक्शन का प्रतिनिधित्व करता है जो दस्तावेज़ से विशिष्ट मेटाडेटा फ़िल्टर से मेल खाने वाले सभी मेटाडेटा या मेटाडेटा को मिटा देता है।

```csharp
public class EraseMetadataRedaction : MetadataRedaction
```

## कंस्ट्रक्टर्स

| नाम | विवरण |
| --- | --- |
| [EraseMetadataRedaction](erasemetadataredaction#constructor)() | सभी मेटाडेटा को मिटाते हुए EraseMetadataRedaction वर्ग का एक नया उदाहरण आरंभ करता है। |
| [EraseMetadataRedaction](erasemetadataredaction#constructor_1)(MetadataFilters) | EraseMetadataRedaction वर्ग का एक नया उदाहरण प्रारंभ करता है, मेटाडेटा मिटाता है, विशिष्ट संयोजन से मेल खाता है[`MetadataFilters`](../metadatafilters) . |

## गुण

| नाम | विवरण |
| --- | --- |
| override [Description](../../groupdocs.redaction.redactions/erasemetadataredaction/description) { get; } | एक स्ट्रिंग लौटाता है, जो रिडक्शन और उसके मापदंडों का वर्णन करता है। |
| [Filter](../../groupdocs.redaction.redactions/metadataredaction/filter) { get; set; } | फ़िल्टर प्राप्त या सेट करता है, जिसका उपयोग सभी या विशिष्ट मेटाडेटा का चयन करने के लिए किया जाता है, उदाहरण के लिए लेखक या कंपनी। |

## तरीकों

| नाम | विवरण |
| --- | --- |
| override [ApplyTo](../../groupdocs.redaction.redactions/metadataredaction/applyto)(DocumentFormatInstance) | किसी दिए गए प्रारूप उदाहरण के लिए संपादन लागू करता है। |

### टिप्पणियों

**और अधिक जानें**

* कटौती लागू करने के बारे में अधिक विवरण: [सुधार मूल बातें](https://docs.groupdocs.com/redaction/net/redaction-basics/)
* दस्तावेज़ मेटाडेटा सुधारों के बारे में अधिक विवरण: [मेटाडेटा कटौती](https://docs.groupdocs.com/redaction/net/metadata-redactions/)

### उदाहरण

निम्न उदाहरण प्रदर्शित करता है कि सभी या विशिष्ट मेटाडेटा को कैसे मिटाया जाए (खाली मानों के बराबर सेट)।

```csharp
using (Redactor redactor = new Redactor(@"C:\sample.docx"))
{
   // लेखक, प्रबंधक और कंपनी को मिटा दें
   redactor.Apply(new EraseMetadataRedaction(MetadataFilters.Author | MetadataFilters.Manager | MetadataFilters.Company));
   // सभी मेटाडेटा मिटा दें
   redactor.Apply(new EraseMetadataRedaction(MetadataFilters.All));
   redactor.Save();
}
```

### यह सभी देखें

* class [MetadataRedaction](../metadataredaction)
* नाम स्थान [GroupDocs.Redaction.Redactions](../../groupdocs.redaction.redactions)
* सभा [GroupDocs.Redaction](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Redaction.dll -->
