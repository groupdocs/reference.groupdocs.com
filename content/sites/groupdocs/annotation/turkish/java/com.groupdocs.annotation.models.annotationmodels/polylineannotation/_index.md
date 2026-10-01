---
title: "PolylineAnnotation"
second_title: "GroupDocs.Annotation Java için API Referansı"
description: "Çoklu çizgi ek açıklama özelliklerini temsil eder"
type: docs
weight: 19
url: /tr/java/com.groupdocs.annotation.models.annotationmodels/polylineannotation/
---
**Inheritance:**
java.lang.Object, [com.groupdocs.annotation.models.annotationmodels.AnnotationBase](../../com.groupdocs.annotation.models.annotationmodels/annotationbase), com.groupdocs.annotation.models.annotationmodels.AnnotationBasePropsV3

**All Implemented Interfaces:**
[com.groupdocs.annotation.models.annotationmodels.interfaces.annotations.IPolylineAnnotation](../../com.groupdocs.annotation.models.annotationmodels.interfaces.annotations/ipolylineannotation)
```
public class PolylineAnnotation extends AnnotationBasePropsV3 implements IPolylineAnnotation
```

Çoklu çizgi ek açıklama özelliklerini temsil eder
## Yapıcılar

| Yapıcı | Açıklama |
| --- | --- |
| [PolylineAnnotation()](#PolylineAnnotation--) | Yeni bir [AreaAnnotation](../../com.groupdocs.annotation.models.annotationmodels/areaannotation) sınıfı örneği başlatır. |
## Metotlar

| Metot | Açıklama |
| --- | --- |
| [getSvgPath()](#getSvgPath--) | Ek açıklama SVG yolunu alır veya ayarlar |
| [setSvgPath(String value)](#setSvgPath-java.lang.String-) | Ek açıklama SVG yolunu alır veya ayarlar |
| [equals(PolylineAnnotation other)](#equals-com.groupdocs.annotation.models.annotationmodels.PolylineAnnotation-) | Polyline Annotation'ları IEquatable Equals yöntemiyle karşılaştırır |
| [equals(Object o)](#equals-java.lang.Object-) | Polyline Annotation'ları standart nesne Equals yöntemiyle karşılaştırır |
| [hashCode()](#hashCode--) | Polyline Annotation'ın HashCode'unu döndürür |
| [deepClone()](#deepClone--) | Aynı değerlerle yeni bir örnek döndürür |
| [toString()](#toString--) |  |
| [toString(ToStringStyle toStringStyle)](#toString-org.apache.commons.lang3.builder.ToStringStyle-) |  |
### PolylineAnnotation() {#PolylineAnnotation--}
```
public PolylineAnnotation()
```


Yeni bir [AreaAnnotation](../../com.groupdocs.annotation.models.annotationmodels/areaannotation) sınıfı örneği başlatır.

### getSvgPath() {#getSvgPath--}
```
public final String getSvgPath()
```


Ek açıklama SVG yolunu alır veya ayarlar

**Returns:**
java.lang.String -
### setSvgPath(String value) {#setSvgPath-java.lang.String-}
```
public final void setSvgPath(String value)
```


Ek açıklama SVG yolunu alır veya ayarlar

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| değer | java.lang.String |  |

### equals(PolylineAnnotation other) {#equals-com.groupdocs.annotation.models.annotationmodels.PolylineAnnotation-}
```
public final boolean equals(PolylineAnnotation other)
```


Polyline Annotation'ları IEquatable Equals yöntemiyle karşılaştırır

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| other | [PolylineAnnotation](../../com.groupdocs.annotation.models.annotationmodels/polylineannotation) | Mevcut nesneyle karşılaştırılacak PolylineAnnotation nesnesi |

**Returns:**
boolean -
### equals(Object o) {#equals-java.lang.Object-}
```
public boolean equals(Object o)
```


Polyline Annotation'ları standart nesne Equals yöntemiyle karşılaştırır

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| o | java.lang.Object | Mevcut nesneyle karşılaştırılacak nesne |

**Returns:**
boolean
### hashCode() {#hashCode--}
```
public int hashCode()
```


Polyline Annotation'ın HashCode'unu döndürür

**Returns:**
int
### deepClone() {#deepClone--}
```
public Object deepClone()
```


Aynı değerlerle yeni bir örnek döndürür

**Returns:**
java.lang.Object -
### toString() {#toString--}
```
public String toString()
```




**Returns:**
java.lang.String
### toString(ToStringStyle toStringStyle) {#toString-org.apache.commons.lang3.builder.ToStringStyle-}
```
public String toString(ToStringStyle toStringStyle)
```




**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| toStringStyle | org.apache.commons.lang3.builder.ToStringStyle |  |

**Returns:**
java.lang.String
