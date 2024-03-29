---
title: TemplateLinkedPosition
second_title: .NET API Başvurusu için GroupDocs.Parser
description: Bağlantılı alanı kullanan bir şablon alan konumu sağlar.
type: docs
weight: 700
url: /tr/net/groupdocs.parser.templates/templatelinkedposition/
---
## TemplateLinkedPosition class

Bağlantılı alanı kullanan bir şablon alan konumu sağlar.

```csharp
public sealed class TemplateLinkedPosition : TemplatePosition
```

## yapıcılar

| İsim | Tanım |
| --- | --- |
| [TemplateLinkedPosition](templatelinkedposition#constructor)(string, Size, TemplateLinkedPositionEdges) | Yeni bir örneğini başlatır.[`TemplateLinkedPosition`](../templatelinkedposition) sınıf. |
| [TemplateLinkedPosition](templatelinkedposition#constructor_1)(string, Size, TemplateLinkedPositionEdges, bool) | Yeni bir örneğini başlatır.[`TemplateLinkedPosition`](../templatelinkedposition) sınıf. |

## Özellikleri

| İsim | Tanım |
| --- | --- |
| [AutoScale](../../groupdocs.parser.templates/templatelinkedposition/autoscale) { get; } | olup olmadığını gösteren değeri alır.[`SearchArea`](./searcharea) bağlantılı alan boyutuna göre ölçeklenir. |
| [Edges](../../groupdocs.parser.templates/templatelinkedposition/edges) { get; } | Bir alanın arandığı bağlantılı alanın kenarlarını alır. |
| [LinkedFieldName](../../groupdocs.parser.templates/templatelinkedposition/linkedfieldname) { get; } | Bağlantılı alan adını alır. |
| [SearchArea](../../groupdocs.parser.templates/templatelinkedposition/searcharea) { get; } | Bir alanın arandığı alanın boyutunu alır. |

### Örnekler

Aşağıdaki örnek, durum için kodu gösterir, eğer bir fatura numarasına sahip alanın "Fatura numarası" dizisinin sağında yer aldığı biliniyorsa, aşağıdaki kod kullanılır:

```csharp
// "Fatura Numarası" metnini bulmak için bir normal ifade şablonu alanı oluşturun
TemplateField invoice = new TemplateField(new TemplateRegexPosition("Invoice Number"), "Invoice");

// "Fatura" alanıyla ilişkilendirilmiş ilgili bir şablon alanı oluşturun ve sağındaki değeri çıkarın
TemplateField invoiceNumber = new TemplateField(
    new TemplateLinkedPosition("invoice", new Size(100, 15), new TemplateLinkedPositionEdges(false, false, true, false)),
    "InvoiceNumber");
```

### Ayrıca bakınız

* class [TemplatePosition](../templateposition)
* ad alanı [GroupDocs.Parser.Templates](../../groupdocs.parser.templates)
* toplantı [GroupDocs.Parser](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->
