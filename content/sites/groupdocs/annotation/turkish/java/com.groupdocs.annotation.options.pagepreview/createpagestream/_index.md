---
title: "CreatePageStream"
second_title: "GroupDocs.Annotation Java için API Referansı"
description: "Çıktı sayfa önizleme akışını oluşturma yöntemini tanımlayan temsilci."
type: docs
weight: 10
url: /tr/java/com.groupdocs.annotation.options.pagepreview/createpagestream/
---
**Inheritance:**
java.lang.Object, com.aspose.ms.System.Delegate, com.aspose.ms.System.MulticastDelegate
```
public abstract class CreatePageStream extends System.MulticastDelegate
```

Çıktı sayfa önizleme akışını oluşturma yöntemini tanımlayan temsilci.
## Yapıcılar

| Yapıcı | Açıklama |
| --- | --- |
| [CreatePageStream()](#CreatePageStream--) |  |
## Metotlar

| Metot | Açıklama |
| --- | --- |
| [invoke(int pageNumber)](#invoke-int-) |  |
| [beginInvoke(int pageNumber, System.AsyncCallback callback, Object state)](#beginInvoke-int-com.aspose.ms.System.AsyncCallback-java.lang.Object-) |  |
| [endInvoke(System.IAsyncResult result)](#endInvoke-com.aspose.ms.System.IAsyncResult-) |  |
### CreatePageStream() {#CreatePageStream--}
```
public CreatePageStream()
```


### invoke(int pageNumber) {#invoke-int-}
```
public abstract OutputStream invoke(int pageNumber)
```




**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| pageNumber | int |  |

**Returns:**
java.io.OutputStream
### beginInvoke(int pageNumber, System.AsyncCallback callback, Object state) {#beginInvoke-int-com.aspose.ms.System.AsyncCallback-java.lang.Object-}
```
public final System.IAsyncResult beginInvoke(int pageNumber, System.AsyncCallback callback, Object state)
```




**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| pageNumber | int |  |
| callback | com.aspose.ms.System.AsyncCallback |  |
| state | java.lang.Object |  |

**Returns:**
com.aspose.ms.System.IAsyncResult
### endInvoke(System.IAsyncResult result) {#endInvoke-com.aspose.ms.System.IAsyncResult-}
```
public final OutputStream endInvoke(System.IAsyncResult result)
```




**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| result | com.aspose.ms.System.IAsyncResult |  |

**Returns:**
java.io.OutputStream
