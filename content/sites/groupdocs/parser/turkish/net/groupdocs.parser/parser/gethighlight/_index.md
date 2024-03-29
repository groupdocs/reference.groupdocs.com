---
title: GetHighlight
second_title: .NET API Başvurusu için GroupDocs.Parser
description: Belgeden bir vurgu çıkarır.
type: docs
weight: 90
url: /tr/net/groupdocs.parser/parser/gethighlight/
---
## Parser.GetHighlight method

Belgeden bir vurgu çıkarır.

```csharp
public HighlightItem GetHighlight(int position, bool isDirect, HighlightOptions options)
```

| Parametre | Tip | Tanım |
| --- | --- | --- |
| position | Int32 | Vurgulamanın başlangıç konumu. |
| isDirect | Boolean | Vurgu çıkarmanın doğrudan olup olmadığını gösteren değer. `doğru` vurgulama sağ tarafından çıkarılırsa*position* ; aksi takdirde,`YANLIŞ` . |
| options | HighlightOptions | Vurgu çıkarma seçenekleri. |

### Geri dönüş değeri

Bir örneği[`HighlightItem`](../../../groupdocs.parser.data/highlightitem) çıkarılan vurguyu temsil eden sınıf; `hükümsüz` vurgu çıkarma desteklenmiyorsa.

### Notlar

**Daha fazla bilgi edin:**

* [Vurguları çıkar](https://docs.groupdocs.com/display/parsernet/Extract+highlights)

### Örnekler

Aşağıdaki örnek, 3 kelime içeren bir vurgunun nasıl çıkarılacağını gösterir:

```csharp
// Parser sınıfının bir örneğini oluşturun
using (Parser parser = new Parser(filePath))
{
    // Bir vurguyu çıkarın:
    HighlightItem hl = parser.GetHighlight(2, true, new HighlightOptions(3));
    
    // Vurgu çıkarmanın desteklenip desteklenmediğini kontrol edin
    if (hl == null)
    {
        Console.WriteLine("Highlight extraction isn't supported");
        return;
    }
    
    // Ayıklanmış bir vurguyu yazdır
    Console.WriteLine(string.Format("At {0}: {1}", hl.Position, hl.Text));
}
```

### Ayrıca bakınız

* class [HighlightItem](../../../groupdocs.parser.data/highlightitem)
* class [HighlightOptions](../../../groupdocs.parser.options/highlightoptions)
* class [Parser](../../parser)
* ad alanı [GroupDocs.Parser](../../parser)
* toplantı [GroupDocs.Parser](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->
