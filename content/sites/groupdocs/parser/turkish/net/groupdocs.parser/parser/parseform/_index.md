---
title: ParseForm
second_title: .NET API Başvurusu için GroupDocs.Parser
description: Belge formunu ayrıştırır.
type: docs
weight: 190
url: /tr/net/groupdocs.parser/parser/parseform/
---
## Parser.ParseForm method

Belge formunu ayrıştırır.

```csharp
public DocumentData ParseForm()
```

### Geri dönüş değeri

Bir örneği[`DocumentData`](../../../groupdocs.parser.data/documentdata) çıkarılan verileri içeren sınıf; `hükümsüz` şablona göre ayrıştırma desteklenmiyorsa.

### Notlar

**Daha fazla bilgi edin:**

* [PDF formlarından veri ayıklayın](https://docs.groupdocs.com/display/parsernet/Extract+data+from+PDF+forms)
* [Ayıklanan verilerle çalışma](https://docs.groupdocs.com/display/parsernet/Working+with+data+extracted+by+template)
* [PDF belgelerinden verileri ayrıştırın](https://docs.groupdocs.com/display/parsernet/Parse+data+from+PDF+documents)

### Örnekler

Aşağıdaki örnek, bir belge formunun nasıl ayrıştırılacağını gösterir:

```csharp
// Parser sınıfının bir örneğini oluşturun
using (Parser parser = new Parser(filePath))
{
    // PDF belgesinden veri çıkar
    DocumentData data = parser.ParseForm();
    // Ayıklanan veriler üzerinde yineleme yapın
    for (int i = 0; i<data.Count; i++)
    {
        Console.Write(data[i].Name + ": ");
        PageTextArea area = data[i].PageArea as PageTextArea;
        Console.WriteLine(area == null ? "Not a template field" : area.Text);
    }
}
```

### Ayrıca bakınız

* class [DocumentData](../../../groupdocs.parser.data/documentdata)
* class [Parser](../../parser)
* ad alanı [GroupDocs.Parser](../../parser)
* toplantı [GroupDocs.Parser](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->
