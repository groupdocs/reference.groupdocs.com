---
title: SpreadsheetSaveOptions
second_title: .NET API संदर्भ के लिए GroupDocs.Editor
description: स्प्रैडशट एक्सेलअनुरूप दस्तवेज़ बनने और सहेजने के लए कस्टम वकल्प नर्दष्ट करने क अनुमत देत है
type: docs
weight: 1120
url: /hi/net/groupdocs.editor.options/spreadsheetsaveoptions/
---
## SpreadsheetSaveOptions class

स्प्रैडशीट (एक्सेल-अनुरूप) दस्तावेज़ बनाने और सहेजने के लिए कस्टम विकल्प निर्दिष्ट करने की अनुमति देता है

```csharp
public sealed class SpreadsheetSaveOptions : ISaveOptions
```

## कंस्ट्रक्टर्स

| नाम | विवरण |
| --- | --- |
| [SpreadsheetSaveOptions](spreadsheetsaveoptions)(SpreadsheetFormats) | निर्दिष्ट अनिवार्य स्प्रेडशीट आउटपुट स्वरूप के साथ स्प्रेडशीटसेवऑप्शन का एक नया उदाहरण बनाता है, जबकि अन्य सभी पैरामीटर default हैं |

## गुण

| नाम | विवरण |
| --- | --- |
| [InsertAsNewWorksheet](../../groupdocs.editor.options/spreadsheetsaveoptions/insertasnewworksheet) { get; set; } | बूलियन फ़्लैग, जो निर्दिष्ट करता है कि क्या संपादित वर्कशीट को मौजूदा वर्कशीट को मूल स्प्रेडशीट में स्थिति पर प्रतिस्थापित करना चाहिए, द्वारा निर्दिष्ट[`WorksheetNumber`](./worksheetnumber) संपत्ति, या इसकी सामग्री को बदले बिना मौजूदा वर्कशीट और पिछले एक के बीच इंजेक्ट किया जाना चाहिए। डिफ़ॉल्ट रूप से गलत है - मौजूदा वर्कशीट को बदल दिया जाएगा। इस संपत्ति को नजरअंदाज कर दिया जाता है, यदि का मान[`WorksheetNumber`](./worksheetnumber) गुण '0' पर सेट है. |
| [OutputFormat](../../groupdocs.editor.options/spreadsheetsaveoptions/outputformat) { get; set; } | एक स्प्रेडशीट प्रारूप निर्दिष्ट करने की अनुमति देता है, जिसका उपयोग दस्तावेज़ को सहेजने के लिए किया जाएगा |
| [Password](../../groupdocs.editor.options/spreadsheetsaveoptions/password) { get; set; } | एक पासवर्ड निर्दिष्ट करने, संशोधित करने, प्राप्त करने या निकालने की अनुमति देता है, जिसका उपयोग जनरेट किए गए स्प्रेडशीट दस्तावेज़ को एन्कोड करने के लिए किया जाएगा, यदि tis दस्तावेज़ प्रारूप पासवर्ड सुरक्षा का समर्थन करता है। पासवर्ड को हटाने (सफाई) के लिए NULL या खाली स्ट्रिंग निर्दिष्ट करें। |
| [WorksheetNumber](../../groupdocs.editor.options/spreadsheetsaveoptions/worksheetnumber) { get; set; } | एक नई एकल-वर्कशीट स्प्रेडशीट (डिफ़ॉल्ट व्यवहार) बनाने के बजाय संपादित वर्कशीट को मौजूदा स्प्रेडशीट की कॉपी में सम्मिलित करने की अनुमति देता है। वर्कशीट नंबर स्प्रेडशीट में वर्कशीट की 1-आधारित संख्या है, जिसे संपादक वर्ग में लोड किया गया है। यदि यह 0 (डिफ़ॉल्ट मान) है, तो नई स्प्रेडशीट एकल संपादित वर्कशीट के साथ बनाई जाएगी। इनपुट संपादन योग्य दस्तावेज़ उदाहरण, इस स्प्रैडशीट में डाला जाएगा. |
| [WorksheetProtection](../../groupdocs.editor.options/spreadsheetsaveoptions/worksheetprotection) { get; set; } | आउटपुट स्प्रेडशीट दस्तावेज़ के लिए वर्कशीट सुरक्षा को सक्षम करने की अनुमति देता है। डिफ़ॉल्ट रूप से शून्य है - सुरक्षा लागू नहीं होती है। सभी प्रारूप वर्कशीट सुरक्षा का समर्थन नहीं करते हैं। |

### यह सभी देखें

* interface [ISaveOptions](../isaveoptions)
* नाम स्थान [GroupDocs.Editor.Options](../../groupdocs.editor.options)
* सभा [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
