---
title: IRedactionCallback
second_title: .NET API संदर्भ के लिए GroupDocs.Redaction
description: उन वधयं क परभषत करत है ज प्रत्येक संपदन परवर्तन पर जनकर प्रप्त करने के लए आवश्यक हैं और वैकल्पक रूप से इसे रकते हैं
type: docs
weight: 500
url: /hi/net/groupdocs.redaction.redactions/iredactioncallback/
---
## IRedactionCallback interface

उन विधियों को परिभाषित करता है जो प्रत्येक संपादन परिवर्तन पर जानकारी प्राप्त करने के लिए आवश्यक हैं और वैकल्पिक रूप से इसे रोकते हैं।

```csharp
public interface IRedactionCallback
```

## तरीकों

| नाम | विवरण |
| --- | --- |
| [AcceptRedaction](../../groupdocs.redaction.redactions/iredactioncallback/acceptredaction)(RedactionDescription) | यह कॉल दस्तावेज़ में किसी भी सुधार को लागू करने से ठीक पहले ट्रिगर किया गया है और इसे लॉग करने या प्रतिबंधित करने की अनुमति देता है। |

### टिप्पणियों

**और अधिक जानें**

* IRedactionCallback इंटरफ़ेस लागू करने के बारे में अधिक विवरण: [रिडक्शन कॉलबैक का प्रयोग करें](https://docs.groupdocs.com/redaction/net/use-redaction-callback/)

### उदाहरण

निम्न उदाहरण दर्शाता है कि संपादन प्रक्रिया के लिए विस्तृत लॉगिंग को कैसे लागू किया जाए।

```csharp
public class RedactionDump : IRedactionCallback
{
    public RedactionDump()
    {
    }

    public bool AcceptRedaction(RedactionDescription description)
    {
        Console.Write("{0} redaction, {1} action, item {2}. ", description.RedactionType, description.ActionType, description.OriginalText);
        if (description.Replacement != null)
        {
            Console.Write("Text {0} is replaced with {1}. ", description.Replacement.OriginalText, description.Replacement.Replacement);
        }
        Console.WriteLine();
        // आप संपादन प्रक्रिया के दौरान विशेष परिवर्तन को रोकने के लिए यहां "गलत" लौटा सकते हैं
        return true;
    }
}

...

// Redactor का उपयोग करने से पहले एक उदाहरण असाइन करें
Redactor.RedactionCallback = new RedactionDump();
```

### यह सभी देखें

* नाम स्थान [GroupDocs.Redaction.Redactions](../../groupdocs.redaction.redactions)
* सभा [GroupDocs.Redaction](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Redaction.dll -->
