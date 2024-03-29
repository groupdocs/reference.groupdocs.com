---
title: XmlText
second_title: .NET API Başvurusu için GroupDocs.Editor
description: XML olan bir metin kaynağını temsil eder.
type: docs
weight: 660
url: /tr/net/groupdocs.editor.htmlcss.resources.textual/xmltext/
---
## XmlText class

XML olan bir metin kaynağını temsil eder.

```csharp
public sealed class XmlText : TextResourceBase
```

## Özellikleri

| İsim | Tanım |
| --- | --- |
| [ByteContent](../../groupdocs.editor.htmlcss.resources.textual/textresourcebase/bytecontent) { get; } | Bu metin kaynağının içeriğini orijinal kodlamayla bayt akışı olarak döndürür |
| [Encoding](../../groupdocs.editor.htmlcss.resources.textual/textresourcebase/encoding) { get; } | Bu metin kaynağının kodlamasını döndürür. Genellikle UTF-8. döndürür |
| [FilenameWithExtension](../../groupdocs.editor.htmlcss.resources.textual/textresourcebase/filenamewithextension) { get; } | Bu metin kaynağının ad ve uzantıdan oluşan doğru dosya adını döndürür |
| [IsDisposed](../../groupdocs.editor.htmlcss.resources.textual/textresourcebase/isdisposed) { get; } | Bu metin kaynağının atılıp atılmadığını belirler |
| [Name](../../groupdocs.editor.htmlcss.resources.textual/textresourcebase/name) { get; } | Dosya uzantısı olmadan bu metin kaynağının adını döndürür |
| [ParsedDocument](../../groupdocs.editor.htmlcss.resources.textual/xmltext/parseddocument) { get; } | Bu XML kaynağından bir "XmlDocument" döndürür |
| [TextContent](../../groupdocs.editor.htmlcss.resources.textual/textresourcebase/textcontent) { get; } | Bu metin kaynağının içeriğini standart bir string olarak döndürür |
| override [Type](../../groupdocs.editor.htmlcss.resources.textual/xmltext/type) { get; } | TextType.Xml döndürür |

## yöntemler

| İsim | Tanım |
| --- | --- |
| [Dispose](../../groupdocs.editor.htmlcss.resources.textual/textresourcebase/dispose)() | İçeriğini düzenleyerek ve çoğu yöntem ve özelliği çalışmaz hale getirerek bu metin kaynağını ortadan kaldırır. Birden fazla aramaya toleranslıdır. |
| [Equals](../../groupdocs.editor.htmlcss.resources.textual/textresourcebase/equals)(IHtmlResource) | Bu örneği eşitlikte belirtilen şekilde kontrol eder. |
| [Save](../../groupdocs.editor.htmlcss.resources.textual/textresourcebase/save)(string) | Bu metin kaynağını belirtilen dosyaya kaydeder |

## Olaylar

| İsim | Tanım |
| --- | --- |
| event [Disposed](../../groupdocs.editor.htmlcss.resources.textual/textresourcebase/disposed) | Bu metin kaynağı atıldığında meydana gelen olay |

### Ayrıca bakınız

* class [TextResourceBase](../textresourcebase)
* ad alanı [GroupDocs.Editor.HtmlCss.Resources.Textual](../../groupdocs.editor.htmlcss.resources.textual)
* toplantı [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
