---
title: DocumentTableSet
second_title: .NET API Başvurusu için GroupDocs.Assembly
description: Bir belgeyi birleştirirken kullanılmak üzere harici bir belgede bulunan birden çok tablonun veya elektronik tabloların verilerine erişim sağlar. Ayrıca belge tabloları için ebeveynçocuk ilişkilerinin tanımlanmasını sağlar böylece şablon belgelerdeki ilgili verilere erişimi basitleştirir.
type: docs
weight: 120
url: /tr/net/groupdocs.assembly.data/documenttableset/
---
## DocumentTableSet class

Bir belgeyi birleştirirken kullanılmak üzere harici bir belgede bulunan birden çok tablonun (veya elektronik tabloların) verilerine erişim sağlar. Ayrıca, belge tabloları için ebeveyn-çocuk ilişkilerinin tanımlanmasını sağlar, böylece şablon belgelerdeki ilgili verilere erişimi basitleştirir.

```csharp
public class DocumentTableSet
```

## yapıcılar

| İsim | Tanım |
| --- | --- |
| [DocumentTableSet](documenttableset#constructor)(Stream) | Varsayılan kullanan bir belgedeki tüm tabloları yükleyen bu sınıfın yeni bir örneğini oluşturur[`DocumentTableOptions`](../documenttableoptions) . |
| [DocumentTableSet](documenttableset#constructor_2)(string) | Varsayılan kullanan bir belgedeki tüm tabloları yükleyen bu sınıfın yeni bir örneğini oluşturur[`DocumentTableOptions`](../documenttableoptions) . |
| [DocumentTableSet](documenttableset#constructor_1)(Stream, IDocumentTableLoadHandler) | Bu sınıfın yeni bir örneğini oluşturur. |
| [DocumentTableSet](documenttableset#constructor_3)(string, IDocumentTableLoadHandler) | Bu sınıfın yeni bir örneğini oluşturur. |

## Özellikleri

| İsim | Tanım |
| --- | --- |
| [Relations](../../groupdocs.assembly.data/documenttableset/relations) { get; } | Bu kümenin belge tabloları için tanımlanan ebeveyn-çocuk ilişkileri koleksiyonunu alır. |
| [Tables](../../groupdocs.assembly.data/documenttableset/tables) { get; } | Koleksiyonunu alır[`DocumentTable`](../documenttable) bu kümenin tablolarını temsil eden nesneler. |

### Notlar

Elektronik Tablo dosya biçimlerindeki belgeler için, bir[`DocumentTableSet`](../documenttableset) örnek, bir dizi sayfayı temsil eder. Diğer dosya biçimlerindeki belgeler için, bir[`DocumentTableSet`](../documenttableset) örnek, bir dizi tabloyu temsil eder.

Bir belgeyi bir araya getirirken ilgili tabloların verilerine erişmek için, bu sınıfın bir örneğini veri kaynağı olarak aşağıdakilerden birine iletin[`DocumentAssembler`](../../groupdocs.assembly/documentassembler) .AssembleDocument aşırı yüklemeler.

Şablon belgelerinde bir[`DocumentTableSet`](../documenttableset) örnek was a gibi aynı şekilde ele alınmalıdır.DataSet misal. Daha fazla bilgi için şablon sözdizimi referansına bakın.

### Ayrıca bakınız

* ad alanı [GroupDocs.Assembly.Data](../../groupdocs.assembly.data)
* toplantı [GroupDocs.Assembly](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Assembly.dll -->
