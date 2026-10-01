---
title: "Belge"
second_title: "GroupDocs.Annotation Java için API Referansı"
description: "Belge özelliklerini temsil eder"
type: docs
weight: 12
url: /tr/java/com.groupdocs.annotation/document/
---
**Inheritance:**
java.lang.Object

**All Implemented Interfaces:**
java.io.Closeable
```
public class Document implements Closeable
```

Belge özelliklerini temsil eder
## Yapıcılar

| Yapıcı | Açıklama |
| --- | --- |
| [Document(InputStream stream)](#Document-java.io.InputStream-) | Yeni bir [Document](../../com.groupdocs.annotation/document) sınıfı örneğini başlatır. |
| [Document(InputStream stream, String password)](#Document-java.io.InputStream-java.lang.String-) | Yeni bir [Document](../../com.groupdocs.annotation/document) sınıfı örneğini başlatır. |
## Metotlar

| Metot | Açıklama |
| --- | --- |
| [setCache(ICache value)](#setCache-com.groupdocs.annotation.cache.ICache-) |  |
| [getName()](#getName--) | Belge adı |
| [setName(String value)](#setName-java.lang.String-) | Belge adı |
| [getStreamSize()](#getStreamSize--) | Belge boyutu |
| [createStream()](#createStream--) | Belge giriş akışı oluşturur |
| [getPassword()](#getPassword--) | Belge şifresi |
| [setPassword(String value)](#setPassword-java.lang.String-) |  |
| [getRotation()](#getRotation--) | Belge Döndürme |
| [setRotation(Byte value)](#setRotation-java.lang.Byte-) | Belge Döndürme |
| [getProcessPages()](#getProcessPages--) | Belge sayfaları |
| [setProcessPages(int value)](#setProcessPages-int-) | Belge sayfaları |
| [generatePreview(PreviewOptions previewOptions)](#generatePreview-com.groupdocs.annotation.options.pagepreview.PreviewOptions-) | Belge sayfalarının önizlemesini oluşturur. |
| [getDocumentInfo()](#getDocumentInfo--) | Belge hakkında bilgi alır - belge türü ve boyutu, sayfa sayısı vb. |
| [close()](#close--) |  |
| [addImageToDocument(String dataDir, String jpgFileName, int pageNumber, int imageQuality)](#addImageToDocument-java.lang.String-java.lang.String-int-int-) | Görüntü kalitesini değiştir ve belgeye görüntü ekle |
### Document(InputStream stream) {#Document-java.io.InputStream-}
```
public Document(InputStream stream)
```


Yeni bir [Document](../../com.groupdocs.annotation/document) sınıfı örneğini başlatır.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| akış | java.io.InputStream | Belge akışı. |

### Document(InputStream stream, String password) {#Document-java.io.InputStream-java.lang.String-}
```
public Document(InputStream stream, String password)
```


Yeni bir [Document](../../com.groupdocs.annotation/document) sınıfı örneğini başlatır.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| akış | java.io.InputStream | Belge akışı. |
| parola | java.lang.String | Belge parolası. |

### setCache(ICache value) {#setCache-com.groupdocs.annotation.cache.ICache-}
```
public final void setCache(ICache value)
```




**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| value | [ICache](../../com.groupdocs.annotation.cache/icache) |  |

### getName() {#getName--}
```
public final String getName()
```


Belge adı

**Returns:**
java.lang.String -
### setName(String value) {#setName-java.lang.String-}
```
public final void setName(String value)
```


Belge adı

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| değer | java.lang.String |  |

### getStreamSize() {#getStreamSize--}
```
public final long getStreamSize()
```


Belge boyutu

**Returns:**
long -
### createStream() {#createStream--}
```
public final InputStream createStream()
```


Belge giriş akışı oluşturur

**Returns:**
java.io.InputStream
### getPassword() {#getPassword--}
```
public final String getPassword()
```


Belge şifresi

**Returns:**
java.lang.String
### setPassword(String value) {#setPassword-java.lang.String-}
```
public final void setPassword(String value)
```




**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| değer | java.lang.String |  |

### getRotation() {#getRotation--}
```
public final Byte getRotation()
```


Belge Döndürme

**Returns:**
java.lang.Byte -
### setRotation(Byte value) {#setRotation-java.lang.Byte-}
```
public final void setRotation(Byte value)
```


Belge Döndürme

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| değer | java.lang.Byte |  |

### getProcessPages() {#getProcessPages--}
```
public final int getProcessPages()
```


Belge sayfaları

**Returns:**
int -
### setProcessPages(int value) {#setProcessPages-int-}
```
public final void setProcessPages(int value)
```


Belge sayfaları

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| değer | int |  |

### generatePreview(PreviewOptions previewOptions) {#generatePreview-com.groupdocs.annotation.options.pagepreview.PreviewOptions-}
```
public final void generatePreview(PreviewOptions previewOptions)
```


Belge sayfalarının önizlemesini oluşturur.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| previewOptions | [PreviewOptions](../../com.groupdocs.annotation.options.pagepreview/previewoptions) | Belge önizleme seçenekleri |

### getDocumentInfo() {#getDocumentInfo--}
```
public final IDocumentInfo getDocumentInfo()
```


Belge hakkında bilgi alır - belge türü ve boyutu, sayfa sayısı vb.

**Returns:**
[IDocumentInfo](../../com.groupdocs.annotation/idocumentinfo) - 
### close() {#close--}
```
public void close()
```




### addImageToDocument(String dataDir, String jpgFileName, int pageNumber, int imageQuality) {#addImageToDocument-java.lang.String-java.lang.String-int-int-}
```
public void addImageToDocument(String dataDir, String jpgFileName, int pageNumber, int imageQuality)
```


Görüntü kalitesini değiştir ve belgeye görüntü ekle

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| dataDir | java.lang.String | Giriş PDF dosyasının yolunu belirtin |
| jpgFileName | java.lang.String | JPG dosyasının yolu |
| pageNumber | int | Görüntünün ekleneceği sayfa |
| imageQuality | int | Görüntü kalitesini 1 ile 100 arasında ayarlayın, "1" - en düşük çözünürlük, "100" - en yüksek çözünürlük |

