---
title: Error
second_title: .NET API संदर्भ के लिए GroupDocs.Viewer
description: एक त्रुट संदेश लखत है त्रुट लग संदेश एप्लकेशन प्रवह में पुनर्प्रप्त न करने यग्य घटनओं के बरे में जनकर प्रदन करते हैं
type: docs
weight: 10
url: /hi/net/groupdocs.viewer.logging/ilogger/error/
---
## ILogger.Error method

एक त्रुटि संदेश लिखता है। त्रुटि लॉग संदेश एप्लिकेशन प्रवाह में पुनर्प्राप्त न करने योग्य घटनाओं के बारे में जानकारी प्रदान करते हैं।

```csharp
public void Error(string message, Exception exception)
```

| पैरामीटर | प्रकार | विवरण |
| --- | --- | --- |
| message | String | त्रुटि संदेश। |
| exception | Exception | अपवाद। |

### अपवाद

| अपवाद | स्थिति |
| --- | --- |
| ArgumentNullException | कब फेंका*message* शून्य है। |
| ArgumentNullException | कब फेंका*exception* शून्य है। |

### यह सभी देखें

* interface [ILogger](../../ilogger)
* नाम स्थान [GroupDocs.Viewer.Logging](../../ilogger)
* सभा [GroupDocs.Viewer](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->
