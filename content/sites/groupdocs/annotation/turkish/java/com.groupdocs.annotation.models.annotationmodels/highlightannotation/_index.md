---
title: "HighlightAnnotation"
second_title: "GroupDocs.Annotation Java için API Referansı"
description: "Vurgulama ek açıklama özelliklerini temsil eder"
type: docs
weight: 15
url: /tr/java/com.groupdocs.annotation.models.annotationmodels/highlightannotation/
---
**Inheritance:**
java.lang.Object, [com.groupdocs.annotation.models.annotationmodels.AnnotationBase](../../com.groupdocs.annotation.models.annotationmodels/annotationbase)

**All Implemented Interfaces:**
[com.groupdocs.annotation.models.annotationmodels.interfaces.annotations.IHighlightAnnotation](../../com.groupdocs.annotation.models.annotationmodels.interfaces.annotations/ihighlightannotation)
```
public class HighlightAnnotation extends AnnotationBase implements IHighlightAnnotation
```

Vurgulama ek açıklama özelliklerini temsil eder
## Yapıcılar

| Yapıcı | Açıklama |
| --- | --- |
| [HighlightAnnotation()](#HighlightAnnotation--) | Yeni bir [HighlightAnnotation](../../com.groupdocs.annotation.models.annotationmodels/highlightannotation) sınıfının örneğini başlatır. |
## Metotlar

| Metot | Açıklama |
| --- | --- |
| [getBackgroundColor()](#getBackgroundColor--) | Ek açıklama arka plan rengini alır veya ayarlar |
| [setBackgroundColor(Integer value)](#setBackgroundColor-java.lang.Integer-) | Ek açıklama arka plan rengini alır veya ayarlar |
| [getFontColor()](#getFontColor--) | Ek açıklama metni yazı tipi rengini alır veya ayarlar |
| [setFontColor(Integer value)](#setFontColor-java.lang.Integer-) | Ek açıklama metni yazı tipi rengini alır veya ayarlar |
| [getOpacity()](#getOpacity--) | Açıklama opaklığını alır veya ayarlar |
| [setOpacity(Double value)](#setOpacity-java.lang.Double-) | Açıklama opaklığını alır veya ayarlar |
| [getPoints()](#getPoints--) | Metin içeren dikdörtgenleri tanımlayan noktaların koleksiyonunu alır veya ayarlar |
| [setPoints(List<Point> value)](#setPoints-java.util.List-com.groupdocs.annotation.models.Point--) | Metin içeren dikdörtgenleri tanımlayan noktaların koleksiyonunu alır veya ayarlar |
| [equals(HighlightAnnotation other)](#equals-com.groupdocs.annotation.models.annotationmodels.HighlightAnnotation-) | Highlight Annotations'ı IEquatable Equals yöntemiyle karşılaştırır |
| [equals(Object obj)](#equals-java.lang.Object-) | Highlight Annotations'ı standart nesne Equals yöntemiyle karşılaştırır |
| [hashCode()](#hashCode--) | Highlight Annotation'ın HashCode değerini döndürür |
| [deepClone()](#deepClone--) | Aynı değerlerle yeni bir örnek döndürür |
| [toString()](#toString--) |  |
| [toString(ToStringStyle toStringStyle)](#toString-org.apache.commons.lang3.builder.ToStringStyle-) |  |
### HighlightAnnotation() {#HighlightAnnotation--}
```
public HighlightAnnotation()
```


Yeni bir [HighlightAnnotation](../../com.groupdocs.annotation.models.annotationmodels/highlightannotation) sınıfının örneğini başlatır.

### getBackgroundColor() {#getBackgroundColor--}
```
public final Integer getBackgroundColor()
```


Ek açıklama arka plan rengini alır veya ayarlar

**Returns:**
java.lang.Integer
### setBackgroundColor(Integer value) {#setBackgroundColor-java.lang.Integer-}
```
public final void setBackgroundColor(Integer value)
```


Ek açıklama arka plan rengini alır veya ayarlar

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| değer | java.lang.Integer |  |

### getFontColor() {#getFontColor--}
```
public final Integer getFontColor()
```


Ek açıklama metni yazı tipi rengini alır veya ayarlar

**Returns:**
java.lang.Integer -
### setFontColor(Integer value) {#setFontColor-java.lang.Integer-}
```
public final void setFontColor(Integer value)
```


Ek açıklama metni yazı tipi rengini alır veya ayarlar

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| değer | java.lang.Integer |  |

### getOpacity() {#getOpacity--}
```
public final Double getOpacity()
```


Açıklama opaklığını alır veya ayarlar

**Returns:**
java.lang.Double -
### setOpacity(Double value) {#setOpacity-java.lang.Double-}
```
public final void setOpacity(Double value)
```


Açıklama opaklığını alır veya ayarlar

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| değer | java.lang.Double |  |

### getPoints() {#getPoints--}
```
public final List<Point> getPoints()
```


Metin içeren dikdörtgenleri tanımlayan noktaların koleksiyonunu alır veya ayarlar

**Returns:**
java.util.List<com.groupdocs.annotation.models.Point> -
### setPoints(List<Point> value) {#setPoints-java.util.List-com.groupdocs.annotation.models.Point--}
```
public final void setPoints(List<Point> value)
```


Metin içeren dikdörtgenleri tanımlayan noktaların koleksiyonunu alır veya ayarlar

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| değer | java.util.List<com.groupdocs.annotation.models.Point> |  |

### equals(HighlightAnnotation other) {#equals-com.groupdocs.annotation.models.annotationmodels.HighlightAnnotation-}
```
public final boolean equals(HighlightAnnotation other)
```


Highlight Annotations'ı IEquatable Equals yöntemiyle karşılaştırır

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| other | [HighlightAnnotation](../../com.groupdocs.annotation.models.annotationmodels/highlightannotation) | Mevcut nesneyle karşılaştırmak için HighlightAnnotation nesnesi |

**Returns:**
boolean -
### equals(Object obj) {#equals-java.lang.Object-}
```
public boolean equals(Object obj)
```


Highlight Annotations'ı standart nesne Equals yöntemiyle karşılaştırır

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| obj | java.lang.Object | Mevcut nesneyle karşılaştırılacak nesne |

**Returns:**
boolean
### hashCode() {#hashCode--}
```
public int hashCode()
```


Highlight Annotation'ın HashCode değerini döndürür

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
