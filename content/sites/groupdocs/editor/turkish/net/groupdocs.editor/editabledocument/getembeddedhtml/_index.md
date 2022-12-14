---
title: GetEmbeddedHtml
second_title: .NET API Başvurusu için GroupDocs.Editor
description: Bu HTML belgesinin tüm içeriğini ilgili tüm kaynaklarla birlikte tek bir dize biçiminde döndürür burada tüm kaynaklar base64 kodlu bir biçimde HTML işaretlemesinin içine gömülüdür.
type: docs
weight: 150
url: /tr/net/groupdocs.editor/editabledocument/getembeddedhtml/
---
## EditableDocument.GetEmbeddedHtml method

Bu HTML belgesinin tüm içeriğini, ilgili tüm kaynaklarla birlikte tek bir dize biçiminde döndürür; burada tüm kaynaklar, base64 kodlu bir biçimde HTML işaretlemesinin içine gömülüdür.

```csharp
public string GetEmbeddedHtml()
```

### Geri dönüş değeri

Her durumda NULL veya boş olmayan dize

### istisnalar

| istisna | şart |
| --- | --- |
| ObjectDisposedException | Bu EditableDocument örneği zaten atılmış |

### Notlar

Bu yöntem, bu EditableDocument'ı HTML'ye dönüştürür ve tüm kaynakların HTML işaretlemesiyle birlikte dizeye gömüldüğü, tek dizesine seri hale getirir:

* HTML-&gt;BODY'deki tüm resimler base64 biçimine dönüştürülür ve IMG 'src' özniteliğinde bulunur
* Tüm stil sayfaları, HTML-&gt;HEAD bölümleri içindeki STYLE öğelerinde saklanır.
* Stil sayfalarındaki tüm resimler base64 biçimine dönüştürülür ve uygun CSS bildirimlerinde bulunur
* Stil sayfalarındaki tüm yazı tipleri base64 formatına dönüştürülür ve uygun @font-face at-rules içinde bulunur.

### Ayrıca bakınız

* class [EditableDocument](../../editabledocument)
* ad alanı [GroupDocs.Editor](../../editabledocument)
* toplantı [GroupDocs.Editor](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
