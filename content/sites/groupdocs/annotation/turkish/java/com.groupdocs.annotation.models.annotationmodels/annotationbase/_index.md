---
title: "AnnotationBase"
second_title: "GroupDocs.Annotation Java için API Referansı"
description: "Tüm açıklama türleri için temel sınıf"
type: docs
weight: 10
url: /tr/java/com.groupdocs.annotation.models.annotationmodels/annotationbase/
---
**Inheritance:**
java.lang.Object

**All Implemented Interfaces:**
com.aspose.ms.System.ICloneable, java.lang.Cloneable, com.aspose.ms.System.IEquatable
```
public abstract class AnnotationBase implements System.ICloneable, Cloneable, System.IEquatable<AnnotationBase>
```

Tüm açıklama türleri için temel sınıf
## Yapıcılar

| Yapıcı | Açıklama |
| --- | --- |
| [AnnotationBase()](#AnnotationBase--) |  |
## Metotlar

| Metot | Açıklama |
| --- | --- |
| [getCounter()](#getCounter--) |  |
| [setCounter(int counter)](#setCounter-int-) |  |
| [getId()](#getId--) | annotation benzersiz kimliğini alır veya ayarlar |
| [setId(int value)](#setId-int-) | annotation benzersiz kimliğini alır veya ayarlar |
| [getCreatedOn()](#getCreatedOn--) | annotation oluşturulma tarihini alır veya ayarlar |
| [setCreatedOn(Date value)](#setCreatedOn-java.util.Date-) | annotation oluşturulma tarihini alır veya ayarlar |
| [getMessage()](#getMessage--) | annotation mesajını alır veya ayarlar |
| [setMessage(String value)](#setMessage-java.lang.String-) | annotation mesajını alır veya ayarlar |
| [getPageNumber()](#getPageNumber--) | Ek açıklama yapılacak sayfa numarasını alır veya ayarlar |
| [setPageNumber(Integer value)](#setPageNumber-java.lang.Integer-) | Ek açıklama yapılacak sayfa numarasını alır veya ayarlar |
| [getReplies()](#getReplies--) | Ek açıklama yanıtları koleksiyonunu temsil eder |
| [setReplies(List<Reply> value)](#setReplies-java.util.List-com.groupdocs.annotation.models.Reply--) | Ek açıklama yanıtları koleksiyonunu temsil eder |
| [getStateBeforeAnnotation()](#getStateBeforeAnnotation--) | Ek açıklamadan önceki metin durumu |
| [setStateBeforeAnnotation(Object value)](#setStateBeforeAnnotation-java.lang.Object-) | Ek açıklamadan önceki metin durumu |
| [getType()](#getType--) | Ek açıklama tipini alır veya ayarlar |
| [setType(int value)](#setType-int-) | Ek açıklama tipini alır veya ayarlar |
| [getUser()](#getUser--) | Ek açıklama oluşturucusunu alır veya ayarlar |
| [setUser(User value)](#setUser-com.groupdocs.annotation.models.User-) | Ek açıklama oluşturucusunu alır veya ayarlar |
| [equals(AnnotationBase other)](#equals-com.groupdocs.annotation.models.annotationmodels.AnnotationBase-) | Temel Ek Açıklamaları IEquatable Equals yöntemiyle karşılaştırır |
| [equals(Object obj)](#equals-java.lang.Object-) | Standart nesne Equals yöntemi kullanarak Base Annotations karşılaştırır |
| [hashCode()](#hashCode--) | AnnotationBase Message, PageNumber ve Type özelliklerinin HashCode'unu döndürür |
| [deepClone()](#deepClone--) | Aynı değerlerle yeni bir örnek döndürür |
| [toString()](#toString--) |  |
| [toString(ToStringStyle toStringStyle)](#toString-org.apache.commons.lang3.builder.ToStringStyle-) |  |
### AnnotationBase() {#AnnotationBase--}
```
public AnnotationBase()
```


### getCounter() {#getCounter--}
```
public static int getCounter()
```




**Returns:**
int
### setCounter(int counter) {#setCounter-int-}
```
public static void setCounter(int counter)
```




**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| sayıcı | int |  |

### getId() {#getId--}
```
public final int getId()
```


annotation benzersiz kimliğini alır veya ayarlar

**Returns:**
int -
### setId(int value) {#setId-int-}
```
public final void setId(int value)
```


annotation benzersiz kimliğini alır veya ayarlar

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| değer | int |  |

### getCreatedOn() {#getCreatedOn--}
```
public final Date getCreatedOn()
```


annotation oluşturulma tarihini alır veya ayarlar

**Returns:**
java.util.Date -
### setCreatedOn(Date value) {#setCreatedOn-java.util.Date-}
```
public final void setCreatedOn(Date value)
```


annotation oluşturulma tarihini alır veya ayarlar

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| değer | java.util.Date |  |

### getMessage() {#getMessage--}
```
public final String getMessage()
```


annotation mesajını alır veya ayarlar

**Returns:**
java.lang.String -
### setMessage(String value) {#setMessage-java.lang.String-}
```
public final void setMessage(String value)
```


annotation mesajını alır veya ayarlar

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| değer | java.lang.String |  |

### getPageNumber() {#getPageNumber--}
```
public final Integer getPageNumber()
```


Ek açıklama yapılacak sayfa numarasını alır veya ayarlar

**Returns:**
java.lang.Integer -
### setPageNumber(Integer value) {#setPageNumber-java.lang.Integer-}
```
public final void setPageNumber(Integer value)
```


Ek açıklama yapılacak sayfa numarasını alır veya ayarlar

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| değer | java.lang.Integer |  |

### getReplies() {#getReplies--}
```
public final List<Reply> getReplies()
```


Ek açıklama yanıtları koleksiyonunu temsil eder

**Returns:**
java.util.List<com.groupdocs.annotation.models.Reply> -
### setReplies(List<Reply> value) {#setReplies-java.util.List-com.groupdocs.annotation.models.Reply--}
```
public final void setReplies(List<Reply> value)
```


Ek açıklama yanıtları koleksiyonunu temsil eder

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| değer | java.util.List<com.groupdocs.annotation.models.Reply> |  |

### getStateBeforeAnnotation() {#getStateBeforeAnnotation--}
```
public final Object getStateBeforeAnnotation()
```


Ek açıklamadan önceki metin durumu

**Returns:**
java.lang.Object -
### setStateBeforeAnnotation(Object value) {#setStateBeforeAnnotation-java.lang.Object-}
```
public final void setStateBeforeAnnotation(Object value)
```


Ek açıklamadan önceki metin durumu

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| değer | java.lang.Object |  |

### getType() {#getType--}
```
public final int getType()
```


Ek açıklama tipini alır veya ayarlar

**Returns:**
int -
### setType(int value) {#setType-int-}
```
public final void setType(int value)
```


Ek açıklama tipini alır veya ayarlar

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| değer | int |  |

### getUser() {#getUser--}
```
public final User getUser()
```


Ek açıklama oluşturucusunu alır veya ayarlar

**Returns:**
[User](../../com.groupdocs.annotation.models/user) - 
### setUser(User value) {#setUser-com.groupdocs.annotation.models.User-}
```
public final void setUser(User value)
```


Ek açıklama oluşturucusunu alır veya ayarlar

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| value | [User](../../com.groupdocs.annotation.models/user) |  |

### equals(AnnotationBase other) {#equals-com.groupdocs.annotation.models.annotationmodels.AnnotationBase-}
```
public final boolean equals(AnnotationBase other)
```


Temel Ek Açıklamaları IEquatable Equals yöntemiyle karşılaştırır

**Parameters:**
| Parametre | Tür | Açıklama |
| --- | --- | --- |
| other | [AnnotationBase](../../com.groupdocs.annotation.models.annotationmodels/annotationbase) | Mevcut nesneyle karşılaştırılacak AnnotationBase nesnesi |

**Returns:**
boolean -
### equals(Object obj) {#equals-java.lang.Object-}
```
public boolean equals(Object obj)
```


Standart nesne Equals yöntemi kullanarak Base Annotations karşılaştırır

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


AnnotationBase Message, PageNumber ve Type özelliklerinin HashCode'unu döndürür

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
