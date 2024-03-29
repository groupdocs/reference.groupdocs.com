---
title: GetCssContent
second_title: .NET API संदर्भ के लिए GroupDocs.Editor
description: स्ट्रंग क सूच के रूप में सभ बहर स्टइलशट क समग्र लटत है जहं एक स्ट्रंग एक स्टइलशट क प्रतनधत्व करत है खल सूच लटत है अगर इस दस्तवेज़ के लए कई सएसएस नहं है
type: docs
weight: 140
url: /hi/net/groupdocs.editor/editabledocument/getcsscontent/
---
## GetCssContent() {#getcsscontent}

स्ट्रिंग की सूची के रूप में सभी बाहरी स्टाइलशीट की सामग्री लौटाता है, जहां एक स्ट्रिंग एक स्टाइलशीट का प्रतिनिधित्व करती है। खाली सूची लौटाता है, अगर इस दस्तावेज़ के लिए कोई सीएसएस नहीं है।

```csharp
public List<string> GetCssContent()
```

### प्रतिलाभ की मात्रा

स्ट्रिंग्स की एक सूची, जहां प्रत्येक स्ट्रिंग में एक CSS दस्तावेज़ की सामग्री होती है

### यह सभी देखें

* class [EditableDocument](../../editabledocument)
* नाम स्थान [GroupDocs.Editor](../../editabledocument)
* सभा [GroupDocs.Editor](../../../)

---

## GetCssContent(string, string) {#getcsscontent_1}

स्ट्रिंग की सूची के रूप में सभी बाहरी स्टाइलशीट की सामग्री लौटाता है, जहां एक स्ट्रिंग एक स्टाइलशीट का प्रतिनिधित्व करती है। प्रत्येक परिणामी स्टाइलशीट में बाहरी संसाधन के प्रत्येक लिंक पर निर्दिष्ट उपसर्ग लागू किया जाएगा। खाली सूची देता है, अगर इसके लिए कोई सीएसएस नहीं है दस्तावेज़.

```csharp
public List<string> GetCssContent(string externalImagesPrefix, string externalFontsPrefix)
```

| पैरामीटर | प्रकार | विवरण |
| --- | --- | --- |
| externalImagesPrefix | String | उपयोग किए गए इस पैरामीटर के माध्यम से एक उपसर्ग निर्दिष्ट कर सकते हैं, जो सभी बाहरी छवियों के लिंक में जोड़ा जाएगा, जो परिणामी सीएसएस स्ट्रिंग्स में सीएसएस घोषणाओं में मौजूद होगा। यदि NULL या रिक्त है, तो उपसर्ग नहीं जोड़े जाएँगे। |
| externalFontsPrefix | String | उपयोग किए गए इस पैरामीटर के माध्यम से एक उपसर्ग निर्दिष्ट किया जा सकता है, जो परिणामी CSS स्ट्रिंग्स में @font-face at-rules में सभी बाहरी फोंट के लिए links में जोड़ा जाएगा। यदि NULL या रिक्त है, तो उपसर्ग नहीं जोड़े जाएँगे। |

### प्रतिलाभ की मात्रा

स्ट्रिंग्स की एक सूची, जहां प्रत्येक स्ट्रिंग में एक CSS दस्तावेज़ की सामग्री होती है

### यह सभी देखें

* class [EditableDocument](../../editabledocument)
* नाम स्थान [GroupDocs.Editor](../../editabledocument)
* सभा [GroupDocs.Editor](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
