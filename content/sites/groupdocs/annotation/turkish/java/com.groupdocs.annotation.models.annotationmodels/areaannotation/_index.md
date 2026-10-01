---
title: "AreaAnnotation"
second_title: "GroupDocs.Annotation Java için API Referansı"
description: "Alan ek açıklama özelliklerini temsil eder"
type: docs
weight: 11
url: /tr/java/com.groupdocs.annotation.models.annotationmodels/areaannotation/
---
**Inheritance:**
java.lang.Object, [com.groupdocs.annotation.models.annotationmodels.AnnotationBase](../../com.groupdocs.annotation.models.annotationmodels/annotationbase), com.groupdocs.annotation.models.annotationmodels.AnnotationBaseProps

**All Implemented Interfaces:**
[com.groupdocs.annotation.models.annotationmodels.interfaces.annotations.IAreaAnnotation](../../com.groupdocs.annotation.models.annotationmodels.interfaces.annotations/iareaannotation)
```
public class AreaAnnotation extends AnnotationBaseProps implements IAreaAnnotation
```

Alan ek açıklama özelliklerini temsil eder
## Yapıcılar

| Yapıcı | Açıklama |
| --- | --- |
| [AreaAnnotation()](#AreaAnnotation--) | Yeni bir [AreaAnnotation](../../com.groupdocs.annotation.models.annotationmodels/areaannotation) sınıfı örneği başlatır. |
## Metotlar

| Metot | Açıklama |
| --- | --- |
| [getPenStyle()](#getPenStyle--) | Açıklama kalem stilini alır veya ayarlar |
| [setPenStyle(Byte value)](#setPenStyle-java.lang.Byte-) | Açıklama kalem stilini alır veya ayarlar |
| [equals(AreaAnnotation other)](#equals-com.groupdocs.annotation.models.annotationmodels.AreaAnnotation-) | Area Annotations'ı IEquatable Equals yöntemiyle karşılaştırır |
| [deepClone()](#deepClone--) | Aynı değerlerle yeni bir örnek döndürür |
| [equals(Object o)](#equals-java.lang.Object-) |  |
| [hashCode()](#hashCode--) |  |
| [toString()](#toString--) |  |
| [toString(ToStringStyle toStringStyle)](#toString-org.apache.commons.lang3.builder.ToStringStyle-) |  |
### AreaAnnotation() {#AreaAnnotation--}
```
public AreaAnnotation()
```


Yeni bir [AreaAnnotation](../../com.groupdocs.annotation.models.annotationmodels/areaannotation) sınıfı örneği başlatır.

### getPenStyle() {#getPenStyle--}
```
public final Byte getPenStyle()
```


Açıklama kalem stilini alır veya ayarlar

**Returns:**
java.lang.Byte -
### setPenStyle(Byte value) {#setPenStyle-java.lang.Byte-}
```
public final void setPenStyle(Byte value)
```


Açıklama kalem stilini alır veya ayarlar

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| değer | java.lang.Byte |  |

### equals(AreaAnnotation other) {#equals-com.groupdocs.annotation.models.annotationmodels.AreaAnnotation-}
```
public final boolean equals(AreaAnnotation other)
```


Area Annotations'ı IEquatable Equals yöntemiyle karşılaştırır

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| other | [AreaAnnotation](../../com.groupdocs.annotation.models.annotationmodels/areaannotation) | Mevcut nesneyle karşılaştırılacak AreaAnnotation nesnesi |

**Returns:**
boolean -
### deepClone() {#deepClone--}
```
public Object deepClone()
```


Aynı değerlerle yeni bir örnek döndürür

**Returns:**
java.lang.Object -
### equals(Object o) {#equals-java.lang.Object-}
```
public boolean equals(Object o)
```


Standart nesne Equals yöntemi kullanarak Base Annotations karşılaştırır

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| o | java.lang.Object |  |

**Returns:**
boolean
### hashCode() {#hashCode--}
```
public int hashCode()
```


AnnotationBase Message, PageNumber ve Type özelliklerinin HashCode'unu döndürür

**Returns:**
int
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
