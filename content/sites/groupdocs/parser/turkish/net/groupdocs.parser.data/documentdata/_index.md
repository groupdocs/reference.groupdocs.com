---
title: DocumentData
second_title: .NET API Başvurusu için GroupDocs.Parser
description: Belgenin verilerini temsil eder. Bu oluşmaktadırFieldData./fielddataDocument. den alan verilerini içeren object
type: docs
weight: 20
url: /tr/net/groupdocs.parser.data/documentdata/
---
## DocumentData class

Belgenin verilerini temsil eder. Bu oluşmaktadır[`FieldData`](../fielddata)Document. 'den alan verilerini içeren object

```csharp
public class DocumentData : IEnumerable<FieldData>
```

## yapıcılar

| İsim | Tanım |
| --- | --- |
| [DocumentData](documentdata)(IEnumerable&lt;FieldData&gt;) | Yeni bir örneğini başlatır.[`FieldData`](../fielddata) sınıf. |

## Özellikleri

| İsim | Tanım |
| --- | --- |
| [Count](../../groupdocs.parser.data/documentdata/count) { get; } | Alan verilerinin toplam sayısını alır. |
| [Item](../../groupdocs.parser.data/documentdata/item) { get; } | Alan verilerini bir dizine göre alır. |

## yöntemler

| İsim | Tanım |
| --- | --- |
| [GetEnumerator](../../groupdocs.parser.data/documentdata/getenumerator)() | Veri alanları için bir numaralandırıcı döndürür. |
| [GetFieldsByName](../../groupdocs.parser.data/documentdata/getfieldsbyname)(string) | Adın şuna eşit olduğu alan verileri koleksiyonunu döndürür:*fieldName* . |

### Notlar

Bir örneği[`DocumentData`](../documentdata) sınıf, dönüş değeri olarak kullanılır[`ParseByTemplate`](../../groupdocs.parser/parser/parsebytemplate) Ve[`ParseForm`](../../groupdocs.parser/parser/parseform) method. Oradaki kullanım örneklerine bakın.

### Ayrıca bakınız

* class [FieldData](../fielddata)
* ad alanı [GroupDocs.Parser.Data](../../groupdocs.parser.data)
* toplantı [GroupDocs.Parser](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->
