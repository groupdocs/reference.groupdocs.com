---
title: "TextRedactionAnnotation"
second_title: "GroupDocs.Annotation Java için API Referansı"
description: "Metin kırpma ek açıklama özelliklerini temsil eder"
type: docs
weight: 26
url: /tr/java/com.groupdocs.annotation.models.annotationmodels/textredactionannotation/
---
**Inheritance:**
java.lang.Object, [com.groupdocs.annotation.models.annotationmodels.AnnotationBase](../../com.groupdocs.annotation.models.annotationmodels/annotationbase)

**All Implemented Interfaces:**
[com.groupdocs.annotation.models.annotationmodels.interfaces.annotations.ITextRedactionAnnotation](../../com.groupdocs.annotation.models.annotationmodels.interfaces.annotations/itextredactionannotation)
```
public class TextRedactionAnnotation extends AnnotationBase implements ITextRedactionAnnotation
```

Metin kırpma ek açıklama özelliklerini temsil eder
## Yapıcılar

| Yapıcı | Açıklama |
| --- | --- |
| [TextRedactionAnnotation()](#TextRedactionAnnotation--) | Yeni bir [TextRedactionAnnotation](../../com.groupdocs.annotation.models.annotationmodels/textredactionannotation) sınıfı örneği başlatır. |
## Metotlar

| Metot | Açıklama |
| --- | --- |
| [getFontColor()](#getFontColor--) | Ek açıklama metni yazı tipi rengini alır veya ayarlar |
| [setFontColor(Integer value)](#setFontColor-java.lang.Integer-) | Ek açıklama metni yazı tipi rengini alır veya ayarlar |
| [getPoints()](#getPoints--) | Metin içeren dikdörtgenleri tanımlayan noktaların koleksiyonunu alır veya ayarlar |
| [setPoints(List<Point> value)](#setPoints-java.util.List-com.groupdocs.annotation.models.Point--) | Metin içeren dikdörtgenleri tanımlayan noktaların koleksiyonunu alır veya ayarlar |
| [equals(TextRedactionAnnotation other)](#equals-com.groupdocs.annotation.models.annotationmodels.TextRedactionAnnotation-) | Text Redaction Annotations'ı IEquatable Equals yöntemiyle karşılaştırır |
| [equals(Object o)](#equals-java.lang.Object-) | Text Redaction Annotations'ı standart nesne Equals yöntemiyle karşılaştırır |
| [hashCode()](#hashCode--) | Text Redaction Annotation'ın HashCode değerini döndürür |
| [deepClone()](#deepClone--) | Aynı değerlerle yeni bir örnek döndürür |
| [toString()](#toString--) |  |
| [toString(ToStringStyle toStringStyle)](#toString-org.apache.commons.lang3.builder.ToStringStyle-) |  |
### TextRedactionAnnotation() {#TextRedactionAnnotation--}
```
public TextRedactionAnnotation()
```


Yeni bir [TextRedactionAnnotation](../../com.groupdocs.annotation.models.annotationmodels/textredactionannotation) sınıfı örneği başlatır.

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

### equals(TextRedactionAnnotation other) {#equals-com.groupdocs.annotation.models.annotationmodels.TextRedactionAnnotation-}
```
public final boolean equals(TextRedactionAnnotation other)
```


Text Redaction Annotations'ı IEquatable Equals yöntemiyle karşılaştırır

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| other | [TextRedactionAnnotation](../../com.groupdocs.annotation.models.annotationmodels/textredactionannotation) | Geçerli nesneyle karşılaştırılacak TextRedactionAnnotation nesnesi |

**Returns:**
boolean
### equals(Object o) {#equals-java.lang.Object-}
```
public boolean equals(Object o)
```


Text Redaction Annotations'ı standart nesne Equals yöntemiyle karşılaştırır

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


Text Redaction Annotation'ın HashCode değerini döndürür

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
