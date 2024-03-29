---
title: Mp3Audio
second_title: .NET API संदर्भ के लिए GroupDocs.Editor
description: मनमने प्ररूप के एक ऑडय संसधन क प्रतनधत्व करत है
type: docs
weight: 350
url: /hi/net/groupdocs.editor.htmlcss.resources.audio/mp3audio/
---
## Mp3Audio class

मनमाने प्रारूप के एक ऑडियो संसाधन का प्रतिनिधित्व करता है

```csharp
public sealed class Mp3Audio : IEquatable<Mp3Audio>, IHtmlResource
```

## कंस्ट्रक्टर्स

| नाम | विवरण |
| --- | --- |
| [Mp3Audio](mp3audio)(string, Stream) | एमपी3 सामग्री से नई एमपी3ऑडियो कक्षा बनाता है, जिसे बाइट स्ट्रीम के रूप में दर्शाया जाता है, और निर्दिष्ट नाम के साथ |

## गुण

| नाम | विवरण |
| --- | --- |
| [ByteContent](../../groupdocs.editor.htmlcss.resources.audio/mp3audio/bytecontent) { get; } | बाइट स्ट्रीम के रूप में इस फ़ॉन्ट की सामग्री लौटाता है |
| [FilenameWithExtension](../../groupdocs.editor.htmlcss.resources.audio/mp3audio/filenamewithextension) { get; } | इस एमपी3 सामग्री का सही फ़ाइल नाम लौटाता है, जिसमें नाम और एक्सटेंशन शामिल हैं। सैद्धांतिक रूप से नाम से भिन्न हो सकता है. |
| [IsDisposed](../../groupdocs.editor.htmlcss.resources.audio/mp3audio/isdisposed) { get; } | निर्धारित करता है कि यह एमपी3 सामग्री निपटाई गई है या नहीं |
| [Name](../../groupdocs.editor.htmlcss.resources.audio/mp3audio/name) { get; } | इस MP3 सामग्री का नाम लौटाता है। आमतौर पर फ़ाइल नाम एक्सटेंशन नहीं होता है और सैद्धांतिक रूप से फ़ाइल नाम से भिन्न हो सकता है। |
| [TextContent](../../groupdocs.editor.htmlcss.resources.audio/mp3audio/textcontent) { get; } | इस एमपी3 संसाधन की सामग्री को बेस64-एन्कोडेड स्ट्रिंग के रूप में लौटाता है। यह मान पहले आह्वान के बाद कैश किया गया है। |
| [Type](../../groupdocs.editor.htmlcss.resources.audio/mp3audio/type) { get; } | एक ऑडियो प्रकार देता है। Mp3 |

## तरीकों

| नाम | विवरण |
| --- | --- |
| [Dispose](../../groupdocs.editor.htmlcss.resources.audio/mp3audio/dispose)() | इस एमपी3 संसाधन का निपटान करता है, इसकी सामग्री का निपटान करता है और अधिकांश तरीकों और गुणों को गैर-कार्यशील बनाता है |
| [Equals](../../groupdocs.editor.htmlcss.resources.audio/mp3audio/equals#equals_1)(IHtmlResource) | संदर्भ समानता पर निर्दिष्ट HTML संसाधन के साथ इस उदाहरण की जाँच करता है |
| [Equals](../../groupdocs.editor.htmlcss.resources.audio/mp3audio/equals#equals)(Mp3Audio) | संदर्भ समानता पर निर्दिष्ट फ़ॉन्ट संसाधन के साथ इस उदाहरण की जाँच करता है |
| [Save](../../groupdocs.editor.htmlcss.resources.audio/mp3audio/save)(string) | इस MP3 संसाधन को निर्दिष्ट फ़ाइल में सहेजता है |
| static [IsValid](../../groupdocs.editor.htmlcss.resources.audio/mp3audio/isvalid)(Stream) | जांचता है कि निर्दिष्ट स्ट्रीम मान्य एमपी3 सामग्री है |

## आयोजन

| नाम | विवरण |
| --- | --- |
| event [Disposed](../../groupdocs.editor.htmlcss.resources.audio/mp3audio/disposed) | घटना, जो तब होती है जब यह एमपी3 सामग्री निपटा दी जाती है |

### यह सभी देखें

* interface [IHtmlResource](../../groupdocs.editor.htmlcss.resources/ihtmlresource)
* नाम स्थान [GroupDocs.Editor.HtmlCss.Resources.Audio](../../groupdocs.editor.htmlcss.resources.audio)
* सभा [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
