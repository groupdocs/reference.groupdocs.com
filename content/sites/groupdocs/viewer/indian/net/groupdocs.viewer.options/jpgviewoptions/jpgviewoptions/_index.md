---
title: JpgViewOptions
second_title: .NET API संदर्भ के लिए GroupDocs.Viewer
description: क नय उदहरण शुरू करत हैJpgViewOptionsgroupdocs.viewer.options/jpgviewoptions वर्ग.
type: docs
weight: 10
url: /hi/net/groupdocs.viewer.options/jpgviewoptions/jpgviewoptions/
---
## JpgViewOptions(CreatePageStream) {#constructor_1}

का नया उदाहरण शुरू करता है[`JpgViewOptions`](../../jpgviewoptions) वर्ग.

```csharp
public JpgViewOptions(CreatePageStream createPageStream)
```

| पैरामीटर | प्रकार | विवरण |
| --- | --- | --- |
| createPageStream | CreatePageStream | आउटपुट पेज डेटा लिखने के लिए उपयोग की जाने वाली स्ट्रीम को इंस्टेंट करने वाली विधि। |

### अपवाद

| अपवाद | स्थिति |
| --- | --- |
| ArgumentNullException | कब फेंका*createPageStream* शून्य है। |

### यह सभी देखें

* delegate [CreatePageStream](../../../groupdocs.viewer.interfaces/createpagestream)
* class [JpgViewOptions](../../jpgviewoptions)
* नाम स्थान [GroupDocs.Viewer.Options](../../jpgviewoptions)
* सभा [GroupDocs.Viewer](../../../)

---

## JpgViewOptions(CreatePageStream, ReleasePageStream) {#constructor_2}

का नया उदाहरण शुरू करता है[`JpgViewOptions`](../../jpgviewoptions) वर्ग.

```csharp
public JpgViewOptions(CreatePageStream createPageStream, ReleasePageStream releasePageStream)
```

| पैरामीटर | प्रकार | विवरण |
| --- | --- | --- |
| createPageStream | CreatePageStream | आउटपुट पेज डेटा लिखने के लिए उपयोग की जाने वाली स्ट्रीम को इंस्टेंट करने वाली विधि। |
| releasePageStream | ReleasePageStream | वह विधि जो उस विधि द्वारा बनाई गई स्ट्रीम को जारी करती है जिसे पारित करने वाले प्रतिनिधि को सौंपा गया है*createPageStream* पैरामीटर। |

### अपवाद

| अपवाद | स्थिति |
| --- | --- |
| ArgumentNullException | कब फेंका*createPageStream* शून्य है। |
| ArgumentNullException | कब फेंका*releasePageStream* शून्य है। |

### यह सभी देखें

* delegate [CreatePageStream](../../../groupdocs.viewer.interfaces/createpagestream)
* delegate [ReleasePageStream](../../../groupdocs.viewer.interfaces/releasepagestream)
* class [JpgViewOptions](../../jpgviewoptions)
* नाम स्थान [GroupDocs.Viewer.Options](../../jpgviewoptions)
* सभा [GroupDocs.Viewer](../../../)

---

## JpgViewOptions(IPageStreamFactory) {#constructor_3}

का नया उदाहरण शुरू करता है[`JpgViewOptions`](../../jpgviewoptions) वर्ग.

```csharp
public JpgViewOptions(IPageStreamFactory pageStreamFactory)
```

| पैरामीटर | प्रकार | विवरण |
| --- | --- | --- |
| pageStreamFactory | IPageStreamFactory | फैक्ट्री जो आउटपुट पेज स्ट्रीम बनाने और जारी करने के तरीकों को लागू करती है। |

### अपवाद

| अपवाद | स्थिति |
| --- | --- |
| ArgumentNullException | कब फेंका*pageStreamFactory* शून्य है। |

### यह सभी देखें

* interface [IPageStreamFactory](../../../groupdocs.viewer.interfaces/ipagestreamfactory)
* class [JpgViewOptions](../../jpgviewoptions)
* नाम स्थान [GroupDocs.Viewer.Options](../../jpgviewoptions)
* सभा [GroupDocs.Viewer](../../../)

---

## JpgViewOptions() {#constructor}

का नया उदाहरण शुरू करता है[`JpgViewOptions`](../../jpgviewoptions) वर्ग.

```csharp
public JpgViewOptions()
```

### टिप्पणियों

यह कंस्ट्रक्टर नए इंस्टेंस को इनिशियलाइज़ करता है[`JpgViewOptions`](../../jpgviewoptions)आउटपुट फ़ाइलों के लिए फ़ाइल पथ प्रारूप के रूप में "p_{0}.jpg" के साथ . आउटपुट फ़ाइलों को एप्लिकेशन की वर्तमान कार्यशील निर्देशिका में रखा जाएगा।

### यह सभी देखें

* class [JpgViewOptions](../../jpgviewoptions)
* नाम स्थान [GroupDocs.Viewer.Options](../../jpgviewoptions)
* सभा [GroupDocs.Viewer](../../../)

---

## JpgViewOptions(string) {#constructor_4}

का नया उदाहरण शुरू करता है[`JpgViewOptions`](../../jpgviewoptions) वर्ग.

```csharp
public JpgViewOptions(string filePathFormat)
```

| पैरामीटर | प्रकार | विवरण |
| --- | --- | --- |
| filePathFormat | String | फ़ाइल पथ स्वरूप, उदाहरण के लिए 'page_{0}.jpg'। |

### अपवाद

| अपवाद | स्थिति |
| --- | --- |
| ArgumentException | कब फेंका*filePathFormat* शून्य या खाली है। |

### यह सभी देखें

* class [JpgViewOptions](../../jpgviewoptions)
* नाम स्थान [GroupDocs.Viewer.Options](../../jpgviewoptions)
* सभा [GroupDocs.Viewer](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->
