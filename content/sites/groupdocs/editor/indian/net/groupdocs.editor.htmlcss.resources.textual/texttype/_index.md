---
title: TextType
second_title: .NET API संदर्भ के लिए GroupDocs.Editor
description: एक सहयक पठ्य संसधन प्रकर क प्रतनधत्व करत है
type: docs
weight: 650
url: /hi/net/groupdocs.editor.htmlcss.resources.textual/texttype/
---
## TextType structure

एक सहायक पाठ्य संसाधन प्रकार का प्रतिनिधित्व करता है

```csharp
public struct TextType : IEquatable<TextType>, IResourceType
```

## गुण

| नाम | विवरण |
| --- | --- |
| static [Css](../../groupdocs.editor.htmlcss.resources.textual/texttype/css) { get; } | टेक्स्ट रिसोर्स का CSS प्रकार |
| static [Undefined](../../groupdocs.editor.htmlcss.resources.textual/texttype/undefined) { get; } | विशेष मान, जो अपरिभाषित, अज्ञात या असमर्थित पाठ संसाधन को चिह्नित करता है |
| static [Xml](../../groupdocs.editor.htmlcss.resources.textual/texttype/xml) { get; } | टेक्स्ट संसाधन का XML प्रकार |
| [FileExtension](../../groupdocs.editor.htmlcss.resources.textual/texttype/fileextension) { get; } | किसी विशेष टेक्स्टुअल रिसोर्स का फ़ाइल एक्सटेंशन (बिना डॉट कैरेक्टर के) |
| [FormalName](../../groupdocs.editor.htmlcss.resources.textual/texttype/formalname) { get; } | इस शाब्दिक संसाधन प्रकार का एक औपचारिक नाम लौटाता है |
| [MimeCode](../../groupdocs.editor.htmlcss.resources.textual/texttype/mimecode) { get; } | किसी विशेष पाठ संसाधन प्रकार का MIME कोड |

## तरीकों

| नाम | विवरण |
| --- | --- |
| static [ParseFromFilenameWithExtension](../../groupdocs.editor.htmlcss.resources.textual/texttype/parsefromfilenamewithextension)(string) | टेक्स्टटाइप मान लौटाता है, जो फ़ाइल नाम एक्सटेंशन के समतुल्य है, जिसे एक्सटेंशन या शुद्ध एक्सटेंशन के साथ निर्दिष्ट फ़ाइल नाम से निकाला जाता है |
| override [Equals](../../groupdocs.editor.htmlcss.resources.textual/texttype/equals#equals_1)(object) | निर्धारित करता है कि क्या यह उदाहरण निर्दिष्ट अनकास्टेड ऑब्जेक्ट के बराबर है, जो संभवतः एक और "टेक्स्टटाइप" उदाहरण है |
| [Equals](../../groupdocs.editor.htmlcss.resources.textual/texttype/equals#equals)(TextType) | निर्धारित करता है कि क्या यह उदाहरण निर्दिष्ट "टेक्स्ट टाइप" उदाहरण के बराबर है |
| override [GetHashCode](../../groupdocs.editor.htmlcss.resources.textual/texttype/gethashcode)() | एक हैश-कोड लौटाता है, जो इस विशिष्ट मान प्रकार के लिए एक स्थिर संख्या है |
| [operator ==](../../groupdocs.editor.htmlcss.resources.textual/texttype/op_equality) | परिभाषित करता है कि क्या दो विशिष्ट "टेक्स्ट टाइप" उदाहरण बराबर हैं |
| [operator !=](../../groupdocs.editor.htmlcss.resources.textual/texttype/op_inequality) | परिभाषित करता है कि क्या दो विशिष्ट "टेक्स्ट टाइप" उदाहरण समान नहीं हैं |

### यह सभी देखें

* interface [IResourceType](../../groupdocs.editor.htmlcss.resources/iresourcetype)
* नाम स्थान [GroupDocs.Editor.HtmlCss.Resources.Textual](../../groupdocs.editor.htmlcss.resources.textual)
* सभा [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
