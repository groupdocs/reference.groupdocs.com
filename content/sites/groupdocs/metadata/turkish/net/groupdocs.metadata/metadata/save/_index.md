---
title: Save
second_title: .NET API Başvurusu için GroupDocs.Metadata
description: Yüklenen belgede yapılan tüm değişiklikleri kaydeder.
type: docs
weight: 110
url: /tr/net/groupdocs.metadata/metadata/save/
---
## Save() {#save}

Yüklenen belgede yapılan tüm değişiklikleri kaydeder.

```csharp
public void Save()
```

### Notlar

**Daha fazla bilgi edin**

* [Değiştirilmiş bir dosyayı orijinal kaynağa kaydetme](https://docs.groupdocs.com/display/metadatanet/Save+a+modified+file+to+the+original+source)
* [Değiştirilmiş bir dosyayı belirtilen bir konuma kaydedin](https://docs.groupdocs.com/display/metadatanet/Save+a+modified+file+to+a+specified+location)
* [Değiştirilmiş bir dosyayı bir akışa kaydetme](https://docs.groupdocs.com/display/metadatanet/Save+a+modified+file+to+a+stream)

### Örnekler

Bu örnek, değiştirilen içeriğin temel alınan kaynağa nasıl kaydedileceğini gösterir.

```csharp
using (Metadata metadata = new Metadata(Constants.OutputPpt))
{
    // Meta verileri burada düzenleyin veya kaldırın

    // Belgeyi temel alınan kaynağa (akış veya dosya) kaydeder
    metadata.Save();
}
```

### Ayrıca bakınız

* class [Metadata](../../metadata)
* ad alanı [GroupDocs.Metadata](../../metadata)
* toplantı [GroupDocs.Metadata](../../../)

---

## Save(Stream) {#save_1}

Belge içeriğini bir akışa kaydeder.

```csharp
public void Save(Stream document)
```

| Parametre | Tip | Tanım |
| --- | --- | --- |
| document | Stream | Belge için bir çıktı akışı. |

### Notlar

**Daha fazla bilgi edin**

* [Değiştirilmiş bir dosyayı orijinal kaynağa kaydetme](https://docs.groupdocs.com/display/metadatanet/Save+a+modified+file+to+the+original+source)
* [Değiştirilmiş bir dosyayı belirtilen bir konuma kaydedin](https://docs.groupdocs.com/display/metadatanet/Save+a+modified+file+to+a+specified+location)
* [Değiştirilmiş bir dosyayı bir akışa kaydetme](https://docs.groupdocs.com/display/metadatanet/Save+a+modified+file+to+a+stream)

### Örnekler

Bu örnek, bir belgenin belirtilen akışa nasıl kaydedileceğini gösterir.

```csharp
using (MemoryStream stream = new MemoryStream())
{
    using (Metadata metadata = new Metadata(Constants.InputPng))
    {
        // Meta verileri burada düzenleyin veya kaldırın

        metadata.Save(stream);
    }
}
```

### Ayrıca bakınız

* class [Metadata](../../metadata)
* ad alanı [GroupDocs.Metadata](../../metadata)
* toplantı [GroupDocs.Metadata](../../../)

---

## Save(string) {#save_2}

Belge içeriğini belirtilen dosyaya kaydeder.

```csharp
public void Save(string filePath)
```

| Parametre | Tip | Tanım |
| --- | --- | --- |
| filePath | String | Çıktı dosyasının tam adı. |

### Notlar

**Daha fazla bilgi edin**

* [Değiştirilmiş bir dosyayı orijinal kaynağa kaydetme](https://docs.groupdocs.com/display/metadatanet/Save+a+modified+file+to+the+original+source)
* [Değiştirilmiş bir dosyayı belirtilen bir konuma kaydedin](https://docs.groupdocs.com/display/metadatanet/Save+a+modified+file+to+a+specified+location)
* [Değiştirilmiş bir dosyayı bir akışa kaydetme](https://docs.groupdocs.com/display/metadatanet/Save+a+modified+file+to+a+stream)

### Örnekler

Bu örnek, bir belgenin belirtilen konuma nasıl kaydedileceğini gösterir.

```csharp
using (Metadata metadata = new Metadata(Constants.InputJpeg))
{
    // Meta verileri burada düzenleyin veya kaldırın

    metadata.Save(Constants.OutputJpeg);
}
```

### Ayrıca bakınız

* class [Metadata](../../metadata)
* ad alanı [GroupDocs.Metadata](../../metadata)
* toplantı [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
