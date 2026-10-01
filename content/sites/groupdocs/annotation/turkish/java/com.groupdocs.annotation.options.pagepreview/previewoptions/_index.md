---
title: "PreviewOptions"
second_title: "GroupDocs.Annotation Java için API Referansı"
description: "Belge önizleme seçeneklerini temsil eder."
type: docs
weight: 11
url: /tr/java/com.groupdocs.annotation.options.pagepreview/previewoptions/
---
**Inheritance:**
java.lang.Object
```
public class PreviewOptions
```

Belge önizleme seçeneklerini temsil eder.
## Yapıcılar

| Yapıcı | Açıklama |
| --- | --- |
| [PreviewOptions(CreatePageStream createPageStream)](#PreviewOptions-com.groupdocs.annotation.options.pagepreview.CreatePageStream-) | Yeni bir [PreviewOptions](../../com.groupdocs.annotation.options.pagepreview/previewoptions) sınıfının bir örneğini başlatır. |
| [PreviewOptions(CreatePageStream createPageStream, ReleasePageStream releasePageStream)](#PreviewOptions-com.groupdocs.annotation.options.pagepreview.CreatePageStream-com.groupdocs.annotation.options.pagepreview.ReleasePageStream-) | Yeni bir [PreviewOptions](../../com.groupdocs.annotation.options.pagepreview/previewoptions) sınıfının bir örneğini başlatır. |
## Metotlar

| Metot | Açıklama |
| --- | --- |
| [getCreatePageStream()](#getCreatePageStream--) | Çıktı sayfa önizleme akışını oluşturmak için yöntemi tanımlayan temsilci. |
| [setCreatePageStream(CreatePageStream value)](#setCreatePageStream-com.groupdocs.annotation.options.pagepreview.CreatePageStream-) | Çıktı sayfa önizleme akışını oluşturmak için yöntemi tanımlayan temsilci. |
| [getReleasePageStream()](#getReleasePageStream--) | Çıktı sayfa önizleme akışını kaldırmak için yöntemi tanımlayan temsilci |
| [setReleasePageStream(ReleasePageStream value)](#setReleasePageStream-com.groupdocs.annotation.options.pagepreview.ReleasePageStream-) | Çıktı sayfa önizleme akışını kaldırmak için yöntemi tanımlayan temsilci |
| [getWidth()](#getWidth--) | Sayfa önizleme genişliği. |
| [setWidth(int value)](#setWidth-int-) | Sayfa önizleme genişliği. |
| [getHeight()](#getHeight--) | Sayfa önizleme yüksekliği. |
| [setHeight(int value)](#setHeight-int-) | Sayfa önizleme yüksekliği. |
| [getPageNumbers()](#getPageNumbers--) | Önizlenecek sayfa numaraları. |
| [setPageNumbers(int[] value)](#setPageNumbers-int---) | Önizlenecek sayfa numaraları. |
| [getPreviewFormat()](#getPreviewFormat--) | Önizleme görüntü formatı. |
| [setPreviewFormat(int value)](#setPreviewFormat-int-) | Önizleme görüntü formatı. |
| [getResolution()](#getResolution--) |  |
| [setResolution(int value)](#setResolution-int-) |  |
| [getRenderComments()](#getRenderComments--) | Önizleme üzerinde yorumların oluşturulup oluşturulmayacağını kontrol eden özellik. |
| [setRenderComments(boolean value)](#setRenderComments-boolean-) | Önizleme üzerinde yorumların oluşturulup oluşturulmayacağını kontrol eden özellik. |
| [getRenderAnnotations()](#getRenderAnnotations--) | Önizleme üzerinde açıklamaların oluşturulup oluşturulmayacağını kontrol eden özellik. |
| [setRenderAnnotations(boolean value)](#setRenderAnnotations-boolean-) | Önizleme üzerinde açıklamaların oluşturulup oluşturulmayacağını kontrol eden özellik. |
| [getWorksheetColumns()](#getWorksheetColumns--) | Oluşturulacak çalışma sayfası sütunları. |
| [getWorksheetColumnsInternal()](#getWorksheetColumnsInternal--) |  |
| [setWorksheetColumns(List<WorksheetColumnsRange> value)](#setWorksheetColumns-java.util.List-com.groupdocs.annotation.options.pagepreview.WorksheetColumnsRange--) | Oluşturulacak çalışma sayfası sütunları. |
| [setWorksheetColumnsInternal(System.Collections.Generic.List<WorksheetColumnsRange> value)](#setWorksheetColumnsInternal-com.aspose.ms.System.Collections.Generic.List-com.groupdocs.annotation.options.pagepreview.WorksheetColumnsRange--) |  |
### PreviewOptions(CreatePageStream createPageStream) {#PreviewOptions-com.groupdocs.annotation.options.pagepreview.CreatePageStream-}
```
public PreviewOptions(CreatePageStream createPageStream)
```


Yeni bir [PreviewOptions](../../com.groupdocs.annotation.options.pagepreview/previewoptions) sınıfının bir örneğini başlatır.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| createPageStream | [CreatePageStream](../../com.groupdocs.annotation.options.pagepreview/createpagestream) | Çıktı sayfa önizleme akışını oluşturmak için yöntemi tanımlayan temsilci. |

### PreviewOptions(CreatePageStream createPageStream, ReleasePageStream releasePageStream) {#PreviewOptions-com.groupdocs.annotation.options.pagepreview.CreatePageStream-com.groupdocs.annotation.options.pagepreview.ReleasePageStream-}
```
public PreviewOptions(CreatePageStream createPageStream, ReleasePageStream releasePageStream)
```


Yeni bir [PreviewOptions](../../com.groupdocs.annotation.options.pagepreview/previewoptions) sınıfının bir örneğini başlatır.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| createPageStream | [CreatePageStream](../../com.groupdocs.annotation.options.pagepreview/createpagestream) | Çıktı sayfa önizleme akışını oluşturmak için yöntemi tanımlayan temsilci. |
| releasePageStream | [ReleasePageStream](../../com.groupdocs.annotation.options.pagepreview/releasepagestream) | Çıktı sayfa önizleme akışını serbest bırakmak için yöntemi tanımlayan temsilci. |

### getCreatePageStream() {#getCreatePageStream--}
```
public final CreatePageStream getCreatePageStream()
```


Çıktı sayfa önizleme akışını oluşturmak için yöntemi tanımlayan temsilci.

**Returns:**
[CreatePageStream](../../com.groupdocs.annotation.options.pagepreview/createpagestream) - 
### setCreatePageStream(CreatePageStream value) {#setCreatePageStream-com.groupdocs.annotation.options.pagepreview.CreatePageStream-}
```
public final void setCreatePageStream(CreatePageStream value)
```


Çıktı sayfa önizleme akışını oluşturmak için yöntemi tanımlayan temsilci.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| value | [CreatePageStream](../../com.groupdocs.annotation.options.pagepreview/createpagestream) |  |

### getReleasePageStream() {#getReleasePageStream--}
```
public final ReleasePageStream getReleasePageStream()
```


Çıktı sayfa önizleme akışını kaldırmak için yöntemi tanımlayan temsilci

**Returns:**
[ReleasePageStream](../../com.groupdocs.annotation.options.pagepreview/releasepagestream) - 
### setReleasePageStream(ReleasePageStream value) {#setReleasePageStream-com.groupdocs.annotation.options.pagepreview.ReleasePageStream-}
```
public final void setReleasePageStream(ReleasePageStream value)
```


Çıktı sayfa önizleme akışını kaldırmak için yöntemi tanımlayan temsilci

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| value | [ReleasePageStream](../../com.groupdocs.annotation.options.pagepreview/releasepagestream) |  |

### getWidth() {#getWidth--}
```
public final int getWidth()
```


Sayfa önizleme genişliği.

**Returns:**
int -
### setWidth(int value) {#setWidth-int-}
```
public final void setWidth(int value)
```


Sayfa önizleme genişliği.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| değer | int |  |

### getHeight() {#getHeight--}
```
public final int getHeight()
```


Sayfa önizleme yüksekliği.

**Returns:**
int -
### setHeight(int value) {#setHeight-int-}
```
public final void setHeight(int value)
```


Sayfa önizleme yüksekliği.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| değer | int |  |

### getPageNumbers() {#getPageNumbers--}
```
public final int[] getPageNumbers()
```


Önizlenecek sayfa numaraları.

**Returns:**
int[] -
### setPageNumbers(int[] value) {#setPageNumbers-int---}
```
public final void setPageNumbers(int[] value)
```


Önizlenecek sayfa numaraları.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| değer | int[] |  |

### getPreviewFormat() {#getPreviewFormat--}
```
public final int getPreviewFormat()
```


Önizleme görüntü formatı.

**Returns:**
int -
### setPreviewFormat(int value) {#setPreviewFormat-int-}
```
public final void setPreviewFormat(int value)
```


Önizleme görüntü formatı.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| değer | int |  |

### getResolution() {#getResolution--}
```
public int getResolution()
```




**Returns:**
int
### setResolution(int value) {#setResolution-int-}
```
public void setResolution(int value)
```




**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| değer | int |  |

### getRenderComments() {#getRenderComments--}
```
public final boolean getRenderComments()
```


Önizleme üzerinde yorumların oluşturulup oluşturulmayacağını kontrol eden özellik. Varsayılan Durum - true. Şu anda yalnızca MS Word belgesinde desteklenir

**Returns:**
boolean -
### setRenderComments(boolean value) {#setRenderComments-boolean-}
```
public final void setRenderComments(boolean value)
```


Önizleme üzerinde yorumların oluşturulup oluşturulmayacağını kontrol eden özellik. Varsayılan Durum - true. Şu anda yalnızca MS Word belgesinde desteklenir

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| değer | boolean |  |

### getRenderAnnotations() {#getRenderAnnotations--}
```
public final boolean getRenderAnnotations()
```


Önizleme üzerinde açıklamaların oluşturulup oluşturulmayacağını kontrol eden özellik. Varsayılan Durum - true.

**Returns:**
boolean -
### setRenderAnnotations(boolean value) {#setRenderAnnotations-boolean-}
```
public final void setRenderAnnotations(boolean value)
```


Önizleme üzerinde açıklamaların oluşturulup oluşturulmayacağını kontrol eden özellik. Varsayılan Durum - true.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| değer | boolean |  |

### getWorksheetColumns() {#getWorksheetColumns--}
```
public final List<WorksheetColumnsRange> getWorksheetColumns()
```


Oluşturulacak çalışma sayfası sütunları. Oluşturma belirtilen sırada ilerler.

**Returns:**
java.util.List<com.groupdocs.annotation.options.pagepreview.WorksheetColumnsRange> -
### getWorksheetColumnsInternal() {#getWorksheetColumnsInternal--}
```
public System.Collections.Generic.List<WorksheetColumnsRange> getWorksheetColumnsInternal()
```




**Returns:**
com.aspose.ms.System.Collections.Generic.List<com.groupdocs.annotation.options.pagepreview.WorksheetColumnsRange>
### setWorksheetColumns(List<WorksheetColumnsRange> value) {#setWorksheetColumns-java.util.List-com.groupdocs.annotation.options.pagepreview.WorksheetColumnsRange--}
```
public final void setWorksheetColumns(List<WorksheetColumnsRange> value)
```


Oluşturulacak çalışma sayfası sütunları. Oluşturma belirtilen sırada ilerler.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| değer | java.util.List<com.groupdocs.annotation.options.pagepreview.WorksheetColumnsRange> |  |

### setWorksheetColumnsInternal(System.Collections.Generic.List<WorksheetColumnsRange> value) {#setWorksheetColumnsInternal-com.aspose.ms.System.Collections.Generic.List-com.groupdocs.annotation.options.pagepreview.WorksheetColumnsRange--}
```
public void setWorksheetColumnsInternal(System.Collections.Generic.List<WorksheetColumnsRange> value)
```




**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| değer | com.aspose.ms.System.Collections.Generic.List<com.groupdocs.annotation.options.pagepreview.WorksheetColumnsRange> |  |

