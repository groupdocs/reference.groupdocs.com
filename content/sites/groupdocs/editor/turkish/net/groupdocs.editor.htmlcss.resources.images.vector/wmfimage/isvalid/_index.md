---
title: IsValid
second_title: .NET API Başvurusu için GroupDocs.Editor
description: Belirtilen akışın geçerli bir WMF image olup olmadığını kontrol eder
type: docs
weight: 90
url: /tr/net/groupdocs.editor.htmlcss.resources.images.vector/wmfimage/isvalid/
---
## IsValid(Stream) {#isvalid}

Belirtilen akışın geçerli bir WMF image olup olmadığını kontrol eder

```csharp
public static bool IsValid(Stream binaryContent)
```

| Parametre | Tip | Tanım |
| --- | --- | --- |
| binaryContent | Stream | Giriş bayt akışı. NULL olamaz, okumayı ve aramayı desteklemelidir. |

### Geri dönüş değeri

Belirtilen akış geçerli bir WMF görüntüsü içeriyorsa doğru, aksi takdirde yanlış

### Ayrıca bakınız

* class [WmfImage](../../wmfimage)
* ad alanı [GroupDocs.Editor.HtmlCss.Resources.Images.Vector](../../wmfimage)
* toplantı [GroupDocs.Editor](../../../)

---

## IsValid(string) {#isvalid_1}

Belirtilen base64 kodlu dizenin geçerli bir WMF image olup olmadığını kontrol eder

```csharp
public static bool IsValid(string contentInBase64)
```

| Parametre | Tip | Tanım |
| --- | --- | --- |
| contentInBase64 | String | WMF görüntüsünün içeriğinin base64 kodlamasında depolandığı giriş dizesi. NULL veya boş olamaz. |

### Geri dönüş değeri

Belirtilen dize geçerli bir WMF görüntüsü içeriyorsa doğrudur, aksi takdirde yanlıştır

### Ayrıca bakınız

* class [WmfImage](../../wmfimage)
* ad alanı [GroupDocs.Editor.HtmlCss.Resources.Images.Vector](../../wmfimage)
* toplantı [GroupDocs.Editor](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
