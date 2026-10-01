---
title: "ReleasePageStream"
second_title: "GroupDocs.Annotation Java için API Referansı"
description: "Çıktı sayfa önizleme akışını serbest bırakma yöntemini tanımlayan temsilci."
type: docs
weight: 12
url: /tr/java/com.groupdocs.annotation.options.pagepreview/releasepagestream/
---
**Inheritance:**
java.lang.Object, com.aspose.ms.System.Delegate, com.aspose.ms.System.MulticastDelegate
```
public abstract class ReleasePageStream extends System.MulticastDelegate
```

Çıktı sayfa önizleme akışını serbest bırakma yöntemini tanımlayan temsilci.
## Yapıcılar

| Yapıcı | Açıklama |
| --- | --- |
| [ReleasePageStream()](#ReleasePageStream--) |  |
## Metotlar

| Metot | Açıklama |
| --- | --- |
| [invoke(int pageNumber, OutputStream pageStream)](#invoke-int-java.io.OutputStream-) |  |
| [beginInvoke(int pageNumber, OutputStream pageStream, System.AsyncCallback callback, Object state)](#beginInvoke-int-java.io.OutputStream-com.aspose.ms.System.AsyncCallback-java.lang.Object-) |  |
| [endInvoke(System.IAsyncResult result)](#endInvoke-com.aspose.ms.System.IAsyncResult-) |  |
### ReleasePageStream() {#ReleasePageStream--}
```
public ReleasePageStream()
```


### invoke(int pageNumber, OutputStream pageStream) {#invoke-int-java.io.OutputStream-}
```
public abstract void invoke(int pageNumber, OutputStream pageStream)
```




**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| pageNumber | int |  |
| pageStream | java.io.OutputStream |  |

### beginInvoke(int pageNumber, OutputStream pageStream, System.AsyncCallback callback, Object state) {#beginInvoke-int-java.io.OutputStream-com.aspose.ms.System.AsyncCallback-java.lang.Object-}
```
public final System.IAsyncResult beginInvoke(int pageNumber, OutputStream pageStream, System.AsyncCallback callback, Object state)
```




**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| pageNumber | int |  |
| pageStream | java.io.OutputStream |  |
| callback | com.aspose.ms.System.AsyncCallback |  |
| state | java.lang.Object |  |

**Returns:**
com.aspose.ms.System.IAsyncResult
### endInvoke(System.IAsyncResult result) {#endInvoke-com.aspose.ms.System.IAsyncResult-}
```
public final void endInvoke(System.IAsyncResult result)
```




**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| result | com.aspose.ms.System.IAsyncResult |  |

