---
title: TemplateField
second_title: .NET API Başvurusu için GroupDocs.Parser
description: Şablon metin alanını sağlar.
type: docs
weight: 670
url: /tr/net/groupdocs.parser.templates/templatefield/
---
## TemplateField class

Şablon metin alanını sağlar.

```csharp
public sealed class TemplateField : TemplateItem
```

## yapıcılar

| İsim | Tanım |
| --- | --- |
| [TemplateField](templatefield#constructor)(TemplatePosition, string) | Yeni bir örneğini başlatır.[`TemplateField`](../templatefield) sınıf. |
| [TemplateField](templatefield#constructor_1)(TemplatePosition, string, int?) | Yeni bir örneğini başlatır.[`TemplateField`](../templatefield) sınıf. |

## Özellikleri

| İsim | Tanım |
| --- | --- |
| [Name](../../groupdocs.parser.templates/templateitem/name) { get; } | Şablon öğesinin adını alır. |
| [PageIndex](../../groupdocs.parser.templates/templateitem/pageindex) { get; } | Şablon öğesinin sayfa dizinini alır. |
| [Position](../../groupdocs.parser.templates/templatefield/position) { get; } | Belge sayfasında şablon alanının nasıl bulunacağını açıklayan değeri alır. |

### Notlar

Metin alanları, sayfadaki konumuna göre tanımlanır. Bir metin alanı tanımlamanın üç yolu vardır:

* [`Dikdörtgen alanı kullanma`](../templatefixedposition)
* [`Normal ifadeyi kullanma`](../templateregexposition)
* [`Bağlantılı alanı kullanma`](../templatelinkedposition)

### Ayrıca bakınız

* class [TemplateItem](../templateitem)
* ad alanı [GroupDocs.Parser.Templates](../../groupdocs.parser.templates)
* toplantı [GroupDocs.Parser](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->
