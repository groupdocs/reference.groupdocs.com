---
title: Edit
second_title: .NET API Başvurusu için GroupDocs.Editor
description:  örneğini oluşturup döndürerek belirtilen biçime özgü seçenekleri kullanarak önceden yüklenmiş bir belgeyi düzenleme için açar.EditableDocumentgroupdocs.editor/editabledocument HTML işaretlemesi ve ilgili kaynakları üretmek için yöntemler içeren sınıf.
type: docs
weight: 50
url: /tr/net/groupdocs.editor/editor/edit/
---
## Edit(IEditOptions) {#edit_1}

' örneğini oluşturup döndürerek belirtilen biçime özgü seçenekleri kullanarak önceden yüklenmiş bir belgeyi düzenleme için açar.[`EditableDocument`](../../editabledocument) HTML işaretlemesi ve ilgili kaynakları üretmek için yöntemler içeren sınıf.

```csharp
public EditableDocument Edit(IEditOptions editOptions)
```

| Parametre | Tip | Tanım |
| --- | --- | --- |
| editOptions | IEditOptions | Dönüştürme sürecini ayarlamanıza izin veren biçime özgü belge seçenekleri. NULL olabilir — bu durumda GroupDocs.Editor önceden yüklenmiş belgenin bir biçimini algılar ve bu biçim için varsayılan olan seçenekleri uygular. Önceden uygulanan yükleme seçenekleriyle çakışmamalıdır. |

### Geri dönüş değeri

' örneği[`EditableDocument`](../../editabledocument) genel girdi belgesini tüm kaynaklarıyla birlikte ara formatta kapsülleyen sınıf. Bu yöntem, başarıyla tamamlanırsa hiçbir zaman NULL döndürmez.

### Notlar

Girilen orijinal belge, yapıcı aracılığıyla 'Editör' örneğine yüklendiğinde, bu yöntem belgeyi 'EditableDocument' sınıfı örneği içinde kapsüllenmiş ara formata dönüştürerek düzenleme için açmaya izin verir. '[`EditableDocument`](../../editabledocument) bu yöntemden döndürülen, daha sonra herhangi bir WYSIWYG HTML düzenleyicisine geçirmek için gerekli tüm yapılandırmalarda HTML işaretlemesi ve karşılık gelen kaynakları (resimler, yazı tipleri ve stil sayfaları gibi) oluşturmak için gerekli tüm yöntemleri ve özellikleri içerir. Bu aşırı yükleme, aile biçimlerine özgü düzenleme seçeneklerini alır. **Daha fazla bilgi edin**

* GroupDocs.Editor: kullanarak belgeleri düzenleme hakkında daha fazla bilgi[GroupDocs.Editor kullanılarak belge nasıl düzenlenir?](https://docs.groupdocs.com/display/editornet/Edit+document)

### Ayrıca bakınız

* class [EditableDocument](../../editabledocument)
* interface [IEditOptions](../../../groupdocs.editor.options/ieditoptions)
* class [Editor](../../editor)
* ad alanı [GroupDocs.Editor](../../editor)
* toplantı [GroupDocs.Editor](../../../)

---

## Edit() {#edit}

' örneğini oluşturup döndürerek varsayılan seçenekleri kullanarak önceden yüklenmiş bir belgeyi düzenleme için açar.[`EditableDocument`](../../editabledocument) HTML işaretlemesi ve ilgili kaynakları üretmek için yöntemler içeren sınıf.

```csharp
public EditableDocument Edit()
```

### Geri dönüş değeri

' örneği[`EditableDocument`](../../editabledocument) genel girdi belgesini tüm kaynaklarıyla birlikte ara formatta kapsülleyen sınıf. Bu yöntem, başarıyla tamamlanırsa hiçbir zaman NULL döndürmez.

### Notlar

Girilen orijinal belge yapıcı aracılığıyla 'Düzenleyici' örneğine yüklendiğinde, bu yöntem belgeyi ' örneği içinde kapsüllenen ara formata dönüştürerek düzenleme için açmaya izin verir.[`EditableDocument`](../../editabledocument) sınıf. '[`EditableDocument`](../../editabledocument) bu yöntemden döndürülen, daha sonra herhangi bir WYSIWYG HTML düzenleyicisine geçirmek için gerekli tüm yapılandırmalarda HTML işaretlemesi ve karşılık gelen kaynakları (resimler, yazı tipleri ve stil sayfaları gibi) oluşturmak için gerekli tüm yöntemleri ve özellikleri içerir. Bu aşırı yükleme, girdi belgesinin ait olduğu biçim için varsayılan olan düzenleme seçeneklerini uygular. **Daha fazla bilgi edin**

* GroupDocs.Editor: kullanarak belgeleri düzenleme hakkında daha fazla bilgi[GroupDocs.Editor kullanılarak belge nasıl düzenlenir?](https://docs.groupdocs.com/display/editornet/Edit+document)

### Ayrıca bakınız

* class [EditableDocument](../../editabledocument)
* class [Editor](../../editor)
* ad alanı [GroupDocs.Editor](../../editor)
* toplantı [GroupDocs.Editor](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
