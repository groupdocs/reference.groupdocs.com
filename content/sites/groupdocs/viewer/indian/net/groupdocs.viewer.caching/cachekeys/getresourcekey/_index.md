---
title: GetResourceKey
second_title: .NET API संदर्भ के लिए GroupDocs.Viewer
description: प्रतनधत्व करने वल कैश प्रवष्ट के लए अद्वतय पहचनकर्त देत हैResourcegroupdocs.viewer.results/resource वस्तु.
type: docs
weight: 70
url: /hi/net/groupdocs.viewer.caching/cachekeys/getresourcekey/
---
## CacheKeys.GetResourceKey method

प्रतिनिधित्व करने वाली कैश प्रविष्टि के लिए अद्वितीय पहचानकर्ता देता है[`Resource`](../../../groupdocs.viewer.results/resource) वस्तु.

```csharp
public static string GetResourceKey(int pageNumber, Resource resource)
```

| पैरामीटर | प्रकार | विवरण |
| --- | --- | --- |
| pageNumber | Int32 | पेज की संख्या। |
| resource | Resource | एचटीएमएल संसाधन। |

### प्रतिलाभ की मात्रा

प्रतिनिधित्व करने वाली कैश प्रविष्टि के लिए अद्वितीय पहचानकर्ता[`Resource`](../../../groupdocs.viewer.results/resource) वस्तु।

### अपवाद

| अपवाद | स्थिति |
| --- | --- |
| ArgumentException | कब फेंका*pageNumber* कम या शून्य के बराबर है। |
| ArgumentNullException | कब फेंका*resource* शून्य है। |

### यह सभी देखें

* class [Resource](../../../groupdocs.viewer.results/resource)
* class [CacheKeys](../../cachekeys)
* नाम स्थान [GroupDocs.Viewer.Caching](../../cachekeys)
* सभा [GroupDocs.Viewer](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->
