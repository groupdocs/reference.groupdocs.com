---
title: "Annotator"
second_title: "GroupDocs.Annotation Java için API Referansı"
description: "Belge açıklama sürecini kontrol eden ana sınıfı temsil eder."
type: docs
weight: 10
url: /tr/java/com.groupdocs.annotation/annotator/
---
**Inheritance:**
java.lang.Object

**All Implemented Interfaces:**
com.aspose.ms.System.IDisposable, java.io.Closeable
```
public class Annotator implements System.IDisposable, Closeable
```

Belge açıklama sürecini kontrol eden ana sınıfı temsil eder.
## Yapıcılar

| Yapıcı | Açıklama |
| --- | --- |
| [Annotator(String filePath)](#Annotator-java.lang.String-) | Belge yolunu kabul eden annotator sınıfını başlat |
| [Annotator(String filePath, LoadOptions loadOptions)](#Annotator-java.lang.String-com.groupdocs.annotation.options.LoadOptions-) | Belge yolunu kabul eden annotator sınıfını başlat |
| [Annotator(String filePath, AnnotatorSettings settings)](#Annotator-java.lang.String-com.groupdocs.annotation.AnnotatorSettings-) | Belge yolunu kabul eden annotator sınıfını başlat |
| [Annotator(String filePath, LoadOptions loadOptions, AnnotatorSettings settings)](#Annotator-java.lang.String-com.groupdocs.annotation.options.LoadOptions-com.groupdocs.annotation.AnnotatorSettings-) | Belge yolunu kabul eden annotator sınıfını başlat |
| [Annotator(InputStream inputStream)](#Annotator-java.io.InputStream-) | Belge akışını kabul eden annotator sınıfını başlat |
| [Annotator(InputStream inputStream, LoadOptions loadOptions)](#Annotator-java.io.InputStream-com.groupdocs.annotation.options.LoadOptions-) | Belge akışını kabul eden annotator sınıfını başlat |
| [Annotator(InputStream inputStream, AnnotatorSettings settings)](#Annotator-java.io.InputStream-com.groupdocs.annotation.AnnotatorSettings-) | Belge akışını kabul eden annotator sınıfını başlat |
| [Annotator(InputStream inputStream, LoadOptions loadOptions, AnnotatorSettings settings)](#Annotator-java.io.InputStream-com.groupdocs.annotation.options.LoadOptions-com.groupdocs.annotation.AnnotatorSettings-) | inputStream akışını kabul eden annotator sınıfını başlat |
## Metotlar

| Metot | Açıklama |
| --- | --- |
| [getDocument()](#getDocument--) | Belge |
| [getRotation()](#getRotation--) | Belge Döndürme |
| [setRotation(Byte value)](#setRotation-java.lang.Byte-) | Belge Döndürme |
| [getProcessPages()](#getProcessPages--) | Belge sayfaları |
| [setProcessPages(int value)](#setProcessPages-int-) | Belge sayfaları |
| [save()](#save--) | Eklemeler, güncellemeler veya kaldırmalar yapıldıktan sonra belgeyi kaydeder. |
| [save(SaveOptions saveOptions)](#save-com.groupdocs.annotation.options.export.SaveOptions-) | Eklemeler, güncellemeler veya kaldırmalar yapıldıktan sonra belgeyi kaydeder. |
| [save(OutputStream document)](#save-java.io.OutputStream-) | Eklemeler, güncellemeler veya kaldırmalar yapıldıktan sonra belgeyi kaydeder. |
| [save(String filePath)](#save-java.lang.String-) | Eklemeler, güncellemeler veya kaldırmalar yapıldıktan sonra belgeyi kaydeder. |
| [save(OutputStream outputStream, SaveOptions saveOptions)](#save-java.io.OutputStream-com.groupdocs.annotation.options.export.SaveOptions-) | Eklemeler, güncellemeler veya kaldırmalar yapıldıktan sonra outputStream'i kaydeder. |
| [save(String filePath, SaveOptions saveOptions)](#save-java.lang.String-com.groupdocs.annotation.options.export.SaveOptions-) | Eklemeler, güncellemeler veya kaldırmalar yapıldıktan sonra belgeyi kaydeder. |
| [dispose()](#dispose--) | Serbest bırak |
| [add(AnnotationBase annotation)](#add-com.groupdocs.annotation.models.annotationmodels.AnnotationBase-) | Belgeye açıklama ekler |
| [add(List<AnnotationBase> annotations)](#add-java.util.List-com.groupdocs.annotation.models.annotationmodels.AnnotationBase--) | Bir belgeye açıklama koleksiyonu ekler. |
| [update(AnnotationBase newAnnotation)](#update-com.groupdocs.annotation.models.annotationmodels.AnnotationBase-) | Belge açıklamasını günceller. |
| [update(List<AnnotationBase> annotations)](#update-java.util.List-com.groupdocs.annotation.models.annotationmodels.AnnotationBase--) | Belge açıklamaları koleksiyonunu günceller. |
| [remove(int annotationId)](#remove-int-) | Id'ye göre belge üzerinden açıklamayı kaldırır. |
| [remove(AnnotationBase annotation)](#remove-com.groupdocs.annotation.models.annotationmodels.AnnotationBase-) | Belgeden açıklamayı kaldırır. |
| [remove(AnnotationBase[] annotationsToDelete)](#remove-com.groupdocs.annotation.models.annotationmodels.AnnotationBase...-) | Sağlanan açıklama kimlikleriyle belge üzerinden açıklama koleksiyonunu kaldırır. |
| [remove(List<Integer> annotationsIdsToDelete)](#remove-java.util.List-java.lang.Integer--) | Sağlanan açıklama kimlikleriyle belge üzerinden açıklama koleksiyonunu kaldırır. |
| [removeInternal(List<AnnotationBase> annotationsToDelete)](#removeInternal-java.util.List-com.groupdocs.annotation.models.annotationmodels.AnnotationBase--) | Belgeden açıklama koleksiyonunu kaldırır. |
| [get()](#get--) | Belge açıklamaları koleksiyonlarını alır. |
| [getVersionsList()](#getVersionsList--) | Sürümleri al. |
| [getVersion(Object version)](#getVersion-java.lang.Object-) | Sürümlerden açıklamaları al. |
| [get(int type)](#get-int-) | Açıklama türüne göre belge açıklamaları koleksiyonunu alır. |
| [importAnnotationsFromDocument(String outputPath)](#importAnnotationsFromDocument-java.lang.String-) | Açıklamaları belgeden XML dosyasına içe aktar. |
| [exportAnnotationsFromDocument(String filePath)](#exportAnnotationsFromDocument-java.lang.String-) | Açıklamaları XML belgesinden dışa aktar. |
| [close()](#close--) |  |
### Annotator(String filePath) {#Annotator-java.lang.String-}
```
public Annotator(String filePath)
```


Belge yolunu kabul eden annotator sınıfını başlat

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
|  | filePath | java.lang.String | Dosya yolu |

--------------------

 **Learn more** 

 *  
 *   |

### Annotator(String filePath, LoadOptions loadOptions) {#Annotator-java.lang.String-com.groupdocs.annotation.options.LoadOptions-}
```
public Annotator(String filePath, LoadOptions loadOptions)
```


Belge yolunu kabul eden annotator sınıfını başlat

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| filePath | java.lang.String | Dosya yolu |
|  | loadOptions | [LoadOptions](../../com.groupdocs.annotation.options/loadoptions) | Yükleme seçenekleri |

--------------------

 **Learn more** 

 *  
 *  
 *  
 *   |

### Annotator(String filePath, AnnotatorSettings settings) {#Annotator-java.lang.String-com.groupdocs.annotation.AnnotatorSettings-}
```
public Annotator(String filePath, AnnotatorSettings settings)
```


Belge yolunu kabul eden annotator sınıfını başlat

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| filePath | java.lang.String | Dosya yolu |
|  | settings | [AnnotatorSettings](../../com.groupdocs.annotation/annotatorsettings) | Annotator ayarları |

--------------------

 **Learn more** 

 *  
 *   |

### Annotator(String filePath, LoadOptions loadOptions, AnnotatorSettings settings) {#Annotator-java.lang.String-com.groupdocs.annotation.options.LoadOptions-com.groupdocs.annotation.AnnotatorSettings-}
```
public Annotator(String filePath, LoadOptions loadOptions, AnnotatorSettings settings)
```


Belge yolunu kabul eden annotator sınıfını başlat

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| filePath | java.lang.String | Dosya yolu |
| loadOptions | [LoadOptions](../../com.groupdocs.annotation.options/loadoptions) | Yükleme seçenekleri |
|  | settings | [AnnotatorSettings](../../com.groupdocs.annotation/annotatorsettings) | Annotator ayarları |

--------------------

 **Learn more** 

 *  
 *  
 *  
 *   |

### Annotator(InputStream inputStream) {#Annotator-java.io.InputStream-}
```
public Annotator(InputStream inputStream)
```


Belge akışını kabul eden annotator sınıfını başlat

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
|  | inputStream | java.io.InputStream | Belge akışı |

--------------------

 **Learn more** 

 *  
 *   |

### Annotator(InputStream inputStream, LoadOptions loadOptions) {#Annotator-java.io.InputStream-com.groupdocs.annotation.options.LoadOptions-}
```
public Annotator(InputStream inputStream, LoadOptions loadOptions)
```


Belge akışını kabul eden annotator sınıfını başlat

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| inputStream | java.io.InputStream | Belge akışı |
|  | loadOptions | [LoadOptions](../../com.groupdocs.annotation.options/loadoptions) | Yükleme seçenekleri |

--------------------

 **Learn more** 

 *  
 *  
 *  
 *   |

### Annotator(InputStream inputStream, AnnotatorSettings settings) {#Annotator-java.io.InputStream-com.groupdocs.annotation.AnnotatorSettings-}
```
public Annotator(InputStream inputStream, AnnotatorSettings settings)
```


Belge akışını kabul eden annotator sınıfını başlat

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| inputStream | java.io.InputStream | Belge akışı |
|  | settings | [AnnotatorSettings](../../com.groupdocs.annotation/annotatorsettings) | Annotator ayarları |

--------------------

 **Learn more** 

 *  
 *   |

### Annotator(InputStream inputStream, LoadOptions loadOptions, AnnotatorSettings settings) {#Annotator-java.io.InputStream-com.groupdocs.annotation.options.LoadOptions-com.groupdocs.annotation.AnnotatorSettings-}
```
public Annotator(InputStream inputStream, LoadOptions loadOptions, AnnotatorSettings settings)
```


inputStream akışını kabul eden annotator sınıfını başlat

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| inputStream | java.io.InputStream | Belge akışı |
| loadOptions | [LoadOptions](../../com.groupdocs.annotation.options/loadoptions) | Yükleme seçenekleri |
|  | settings | [AnnotatorSettings](../../com.groupdocs.annotation/annotatorsettings) | Annotator ayarları |

--------------------

 **Learn more** 

 *  
 *  
 *  
 *   |

### getDocument() {#getDocument--}
```
public final Document getDocument()
```


Belge

**Returns:**
[Document](../../com.groupdocs.annotation/document) - 
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

### save() {#save--}
```
public final void save()
```


Eklemeler, güncellemeler veya kaldırmalar yapıldıktan sonra belgeyi kaydeder.

--------------------

 **Learn more about saving annotated documents** 

 *  
 *  
 *  

### save(SaveOptions saveOptions) {#save-com.groupdocs.annotation.options.export.SaveOptions-}
```
public final void save(SaveOptions saveOptions)
```


Eklemeler, güncellemeler veya kaldırmalar yapıldıktan sonra belgeyi kaydeder.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
|  | saveOptions | [SaveOptions](../../com.groupdocs.annotation.options.export/saveoptions) | Kaydetme seçenekleri. |

--------------------

 **Learn more about saving annotated documents** 

 *  
 *  
 *   |

### save(OutputStream document) {#save-java.io.OutputStream-}
```
public final void save(OutputStream document)
```


Eklemeler, güncellemeler veya kaldırmalar yapıldıktan sonra belgeyi kaydeder.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
|  | belge | java.io.OutputStream | Çıktı akışı. |

--------------------

 **Learn more about saving annotated documents** 

 *  
 *  
 *   |

### save(String filePath) {#save-java.lang.String-}
```
public final void save(String filePath)
```


Eklemeler, güncellemeler veya kaldırmalar yapıldıktan sonra belgeyi kaydeder.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
|  | filePath | java.lang.String | Çıktı dosya yolu. |

--------------------

 **Learn more about saving annotated documents** 

 *  
 *  
 *   |

### save(OutputStream outputStream, SaveOptions saveOptions) {#save-java.io.OutputStream-com.groupdocs.annotation.options.export.SaveOptions-}
```
public final void save(OutputStream outputStream, SaveOptions saveOptions)
```


Eklemeler, güncellemeler veya kaldırmalar yapıldıktan sonra outputStream'i kaydeder.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| outputStream | java.io.OutputStream | Çıktı akışı. |
|  | saveOptions | [SaveOptions](../../com.groupdocs.annotation.options.export/saveoptions) | Kaydetme seçenekleri. |

--------------------

 **Learn more about saving annotated documents** 

 *  
 *  
 *   |

### save(String filePath, SaveOptions saveOptions) {#save-java.lang.String-com.groupdocs.annotation.options.export.SaveOptions-}
```
public final void save(String filePath, SaveOptions saveOptions)
```


Eklemeler, güncellemeler veya kaldırmalar yapıldıktan sonra belgeyi kaydeder.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| filePath | java.lang.String | Çıktı dosya yolu. |
|  | saveOptions | [SaveOptions](../../com.groupdocs.annotation.options.export/saveoptions) | Kaydetme seçenekleri. |

--------------------

 **Learn more about saving annotated documents** 

 *  
 *  
 *   |

### dispose() {#dispose--}
```
public final void dispose()
```


Serbest bırak

### add(AnnotationBase annotation) {#add-com.groupdocs.annotation.models.annotationmodels.AnnotationBase-}
```
public final void add(AnnotationBase annotation)
```


Belgeye açıklama ekler

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
|  | annotation | [AnnotationBase](../../com.groupdocs.annotation.models.annotationmodels/annotationbase) | Eklenecek açıklama. |

--------------------

 **Learn more** 

 *   |

### add(List<AnnotationBase> annotations) {#add-java.util.List-com.groupdocs.annotation.models.annotationmodels.AnnotationBase--}
```
public final void add(List<AnnotationBase> annotations)
```


Bir belgeye açıklama koleksiyonu ekler.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
|  | açıklamalar | java.util.List<com.groupdocs.annotation.models.annotationmodels.AnnotationBase> | Eklenecek açıklamalar listesi. |

--------------------

 **Learn more** 

 *   |

### update(AnnotationBase newAnnotation) {#update-com.groupdocs.annotation.models.annotationmodels.AnnotationBase-}
```
public final void update(AnnotationBase newAnnotation)
```


Belge açıklamasını günceller.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
|  | newAnnotation | [AnnotationBase](../../com.groupdocs.annotation.models.annotationmodels/annotationbase) | Güncellenecek açıklama (Id sağlanmalıdır). |

--------------------

 **Learn more** 

 *   |

### update(List<AnnotationBase> annotations) {#update-java.util.List-com.groupdocs.annotation.models.annotationmodels.AnnotationBase--}
```
public final void update(List<AnnotationBase> annotations)
```


Belge açıklamaları koleksiyonunu günceller.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
|  | açıklamalar | java.util.List<com.groupdocs.annotation.models.annotationmodels.AnnotationBase> | Ayarlanacak açıklamalar listesi. |

--------------------

 **Learn more** 

 *   |

### remove(int annotationId) {#remove-int-}
```
public final void remove(int annotationId)
```


Id'ye göre belge üzerinden açıklamayı kaldırır.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
|  | annotationId | int | Silinmesi gereken açıklamanın kimliği. |

--------------------

 **Learn more** 

 *   |

### remove(AnnotationBase annotation) {#remove-com.groupdocs.annotation.models.annotationmodels.AnnotationBase-}
```
public final void remove(AnnotationBase annotation)
```


Belgeden açıklamayı kaldırır.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
|  | annotation | [AnnotationBase](../../com.groupdocs.annotation.models.annotationmodels/annotationbase) | Silinmesi gereken açıklama. |

--------------------

 **Learn more** 

 *   |

### remove(AnnotationBase[] annotationsToDelete) {#remove-com.groupdocs.annotation.models.annotationmodels.AnnotationBase...-}
```
public final void remove(AnnotationBase[] annotationsToDelete)
```


Sağlanan açıklama kimlikleriyle belge üzerinden açıklama koleksiyonunu kaldırır.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
|  | annotationsToDelete | [AnnotationBase\[\]](../../com.groupdocs.annotation.models.annotationmodels/annotationbase) | Silinmesi gereken açıklamanın kimliği. |

--------------------

 **Learn more** 

 *   |

### remove(List<Integer> annotationsIdsToDelete) {#remove-java.util.List-java.lang.Integer--}
```
public final void remove(List<Integer> annotationsIdsToDelete)
```


Sağlanan açıklama kimlikleriyle belge üzerinden açıklama koleksiyonunu kaldırır.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
|  | annotationsIdsToDelete | java.util.List<java.lang.Integer> | Silinmesi gereken açıklamanın kimliği. |

--------------------

 **Learn more** 

 *   |

### removeInternal(List<AnnotationBase> annotationsToDelete) {#removeInternal-java.util.List-com.groupdocs.annotation.models.annotationmodels.AnnotationBase--}
```
public final void removeInternal(List<AnnotationBase> annotationsToDelete)
```


Belgeden açıklama koleksiyonunu kaldırır.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
|  | annotationsToDelete | java.util.List<com.groupdocs.annotation.models.annotationmodels.AnnotationBase> | Silinmesi gereken açıklamalar. |

--------------------

 **Learn more** 

 *   |

### get() {#get--}
```
public final List<AnnotationBase> get()
```


Belge açıklamaları koleksiyonlarını alır.

**Returns:**
java.util.List<com.groupdocs.annotation.models.annotationmodels.AnnotationBase> - Açıklamaların listesi.

--------------------

 **Learn more** 

 *  
### getVersionsList() {#getVersionsList--}
```
public final List<Object> getVersionsList()
```


Sürümleri al.

**Returns:**
java.util.List<java.lang.Object> - Sürümlerin listesi.
### getVersion(Object version) {#getVersion-java.lang.Object-}
```
public final List<AnnotationBase> getVersion(Object version)
```


Sürümlerden açıklamaları al.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| sürüm | java.lang.Object | İstediğiniz sürümlerin anahtarı |

**Returns:**
java.util.List<com.groupdocs.annotation.models.annotationmodels.AnnotationBase> - Belirli sürümlere ait açıklamaların listesi. Null ise sonuncusu dönecek.
### get(int type) {#get-int-}
```
public final List<AnnotationBase> get(int type)
```


Açıklama türüne göre belge açıklamaları koleksiyonunu alır.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
|  | tür | int | Döndürülmesi gereken ek açıklama türü. |

--------------------

 **Learn more** 

 *   |

**Returns:**
java.util.List<com.groupdocs.annotation.models.annotationmodels.AnnotationBase> - Türüne göre ek açıklamaların listesi.
### importAnnotationsFromDocument(String outputPath) {#importAnnotationsFromDocument-java.lang.String-}
```
public final void importAnnotationsFromDocument(String outputPath)
```


Açıklamaları belgeden XML dosyasına içe aktar.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
|  | outputPath | java.lang.String | Çıktı dosya yolu. |

--------------------

 **Learn more** 

 *   |

### exportAnnotationsFromDocument(String filePath) {#exportAnnotationsFromDocument-java.lang.String-}
```
public final void exportAnnotationsFromDocument(String filePath)
```


Açıklamaları XML belgesinden dışa aktar.

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
|  | filePath | java.lang.String | Girdi dosya yolu. |

--------------------

 **Learn more** 

 *   |

### close() {#close--}
```
public void close()
```




