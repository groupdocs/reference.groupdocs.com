---
title: MoveTo
second_title: GroupDocs.Parser .NET API संदर्भ के लिए
description: में समन आकर वभजक और स्थत के सथ एक नय लेआउट बनत हैpoint .
type: docs
weight: 50
url: /hi/net/groupdocs.parser.templates/templatetablelayout/moveto/
---
## TemplateTableLayout.MoveTo method

में समान आकार, विभाजक और स्थिति के साथ एक नया लेआउट बनाता है*point* .

```csharp
public TemplateTableLayout MoveTo(Point point)
```

| पैरामीटर | प्रकार | विवरण |
| --- | --- | --- |
| point | Point | नए लेआउट की स्थिति। |

### प्रतिलाभ की मात्रा

समान आकार, विभाजक और स्थिति के साथ एक नया लेआउट*point*.

### उदाहरण

यह कार्यक्षमता तालिका लेआउट को स्थानांतरित करने की अनुमति देती है।

उदाहरण के लिए, एक दस्तावेज़ में प्रत्येक पृष्ठ पर तालिकाएँ होती हैं (या पृष्ठ पर तालिका वाले दस्तावेज़ों का एक सेट)। ये तालिकाएँ स्थिति और सामग्री के अनुसार भिन्न हैं, लेकिन इनमें समान स्तंभ और पंक्तियाँ हैं। इस मामले में एक उपयोगकर्ता को परिभाषित कर सकता है[`TemplateTableLayout`](../../templatetablelayout) पर वस्तु`(0, 0)` एक बार और फिर इसे निश्चित तालिका के स्थान पर ले जाएँ।

यदि तालिका की स्थिति पृष्ठ के अन्य ऑब्जेक्ट पर निर्भर करती है, तो उपयोगकर्ता परिभाषित कर सकता है[`TemplateTableLayout`](../../templatetablelayout) ऑब्जेक्ट आधारित टेम्पलेट दस्तावेज़ पर और फिर इसे एंकर ऑब्जेक्ट के अनुसार स्थानांतरित करें। उदाहरण के लिए, यदि यह सारांश तालिका है और इसके बाद विवरण तालिका है (जिसमें पंक्तियों की एक अलग संख्या हो सकती है)। इस मामले में एक उपयोगकर्ता को परिभाषित कर सकता है[`TemplateTableLayout`](../../templatetablelayout)टेम्पलेट दस्तावेज़ पर वस्तु (ज्ञात विवरण तालिका आयत के साथ) और फिर को स्थानांतरित करें[`TemplateTableLayout`](../../templatetablelayout) टेम्पलेट और वास्तविक दस्तावेज़ के विवरण तालिका आयत के अंतर के अनुसार वस्तु।

`MoveTo` विधि वर्तमान वस्तु की एक प्रति लौटाती है। एक उपयोगकर्ता कोई भी निर्देशांक पास कर सकता है (नकारात्मक भी - फिर लेआउट बाईं/शीर्ष पर ले जाया जाएगा).

```csharp
// टेबल लेआउट बनाएं
TemplateTableLayout layout = new TemplateTableLayout(
    new double[] { 0, 25, 150, 180, 230 },
    new double[] { 0, 15, 30, 45, 60, 75 });

// एक आयत प्रिंट करें
Rectangle rect = layout.Rectangle;

// प्रिंट: स्थिति: (0, 0) आकार: (230, 75)
Console.WriteLine(string.Format("pos: ({0}, {1}) size: ({2}, {3})", rect.Left, rect.Top, rect.Size.Width, rect.Size.Height));

// लेआउट को निश्चित तालिका स्थान पर ले जाएं
TemplateTableLayout movedLayout = layout.MoveTo(new Point(315, 250));

// सुनिश्चित करें कि पहले विभाजक स्थानांतरित हो गए हैं:
Console.WriteLine(movedLayout.VerticalSeparators[0]); // प्रिंट: 315
Console.WriteLine(movedLayout.HorizontalSeparators[0]); // प्रिंट: 250

Rectangle movedRect = movedLayout.Rectangle;

// प्रिंट: स्थिति: (315, 250) आकार: (230, 75)
Console.WriteLine(string.Format("pos: ({0}, {1}) size: ({2}, {3})", movedRect.Left, movedRect.Top, movedRect.Size.Width, movedRect.Size.Height));

// स्थानांतरित लेआउट ऑब्जेक्ट लेआउट ऑब्जेक्ट की एक प्रति है, इस प्रकार हम विभाजकों को मूल लेआउट पर प्रभाव के बिना ट्यून कर सकते हैं:
movedLayout.HorizontalSeparators.Add(90);

Console.WriteLine(movedLayout.HorizontalSeparators.Count); // प्रिंट: 7
Console.WriteLine(layout.HorizontalSeparators.Count); // प्रिंट: 6
```

### यह सभी देखें

* class [Point](../../../groupdocs.parser.data/point)
* class [TemplateTableLayout](../../templatetablelayout)
* नाम स्थान [GroupDocs.Parser.Templates](../../templatetablelayout)
* सभा [GroupDocs.Parser](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->
