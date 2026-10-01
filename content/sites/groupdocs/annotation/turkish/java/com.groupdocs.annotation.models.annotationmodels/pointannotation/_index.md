---
title: "PointAnnotation"
second_title: "GroupDocs.Annotation Java için API Referansı"
description: "Nokta ek açıklama özelliklerini temsil eder"
type: docs
weight: 18
url: /tr/java/com.groupdocs.annotation.models.annotationmodels/pointannotation/
---
**Inheritance:**
java.lang.Object, [com.groupdocs.annotation.models.annotationmodels.AnnotationBase](../../com.groupdocs.annotation.models.annotationmodels/annotationbase)

**All Implemented Interfaces:**
[com.groupdocs.annotation.models.annotationmodels.interfaces.annotations.IPointAnnotation](../../com.groupdocs.annotation.models.annotationmodels.interfaces.annotations/ipointannotation)
```
public class PointAnnotation extends AnnotationBase implements IPointAnnotation
```

Nokta ek açıklama özelliklerini temsil eder
## Yapıcılar

| Yapıcı | Açıklama |
| --- | --- |
| [PointAnnotation()](#PointAnnotation--) | Yeni bir [PointAnnotation](../../com.groupdocs.annotation.models.annotationmodels/pointannotation) sınıfı örneği başlatır. |
## Metotlar

| Metot | Açıklama |
| --- | --- |
| [getBox()](#getBox--) | Açıklama konumunu alır veya ayarlar |
| [setBox(Rectangle value)](#setBox-com.groupdocs.annotation.models.Rectangle-) | Açıklama konumunu alır veya ayarlar |
| [equals(PointAnnotation other)](#equals-com.groupdocs.annotation.models.annotationmodels.PointAnnotation-) | Point Annotation'ları IEquatable Equals yöntemiyle karşılaştırır |
| [equals(Object o)](#equals-java.lang.Object-) | Point Annotation'ları standart nesne Equals yöntemiyle karşılaştırır |
| [hashCode()](#hashCode--) | Point Annotation'ın HashCode'unu döndürür |
| [deepClone()](#deepClone--) | Aynı değerlerle yeni bir örnek döndürür |
| [toString()](#toString--) |  |
| [toString(ToStringStyle toStringStyle)](#toString-org.apache.commons.lang3.builder.ToStringStyle-) |  |
### PointAnnotation() {#PointAnnotation--}
```
public PointAnnotation()
```


Yeni bir [PointAnnotation](../../com.groupdocs.annotation.models.annotationmodels/pointannotation) sınıfı örneği başlatır.

### getBox() {#getBox--}
```
public final Rectangle getBox()
```


Açıklama konumunu alır veya ayarlar

**Returns:**
[Rectangle](../../com.groupdocs.annotation.models/rectangle)
### setBox(Rectangle value) {#setBox-com.groupdocs.annotation.models.Rectangle-}
```
public final void setBox(Rectangle value)
```


Açıklama konumunu alır veya ayarlar

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| value | [Rectangle](../../com.groupdocs.annotation.models/rectangle) |  |

### equals(PointAnnotation other) {#equals-com.groupdocs.annotation.models.annotationmodels.PointAnnotation-}
```
public final boolean equals(PointAnnotation other)
```


Point Annotation'ları IEquatable Equals yöntemiyle karşılaştırır

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| other | [PointAnnotation](../../com.groupdocs.annotation.models.annotationmodels/pointannotation) | Mevcut nesneyle karşılaştırılacak PointAnnotation nesnesi |

**Returns:**
boolean -
### equals(Object o) {#equals-java.lang.Object-}
```
public boolean equals(Object o)
```


Point Annotation'ları standart nesne Equals yöntemiyle karşılaştırır

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


Point Annotation'ın HashCode'unu döndürür

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
